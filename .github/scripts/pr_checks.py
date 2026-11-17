#!/usr/bin/env python3
"""Check a pull request against the conventions in .github/docs/CONTRIBUTING.md.

Checks that:
  - the branch is named <type>/<issue>-<short-description>
  - the title is "<issue>: <title>"
  - the description links an open issue (Closes/Fixes/Resolves #N)
  - the issue numbers in the branch, title, and description all match

Then labels the pull request by its branch prefix.

Run by .github/workflows/pr-checks.yml. It reads the pull request from the
event payload and calls the GitHub REST API, using only the standard
library. It needs these environment variables, which GitHub Actions sets:
GITHUB_EVENT_PATH, GITHUB_REPOSITORY, GITHUB_TOKEN, and optionally
GITHUB_API_URL and GITHUB_STEP_SUMMARY.

Exits with status 1 if any check fails.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

# Branch prefix -> label applied to the pull request.
LABELS = {
    "feat": "enhancement",
    "fix": "bug",
    "docs": "documentation",
    "refactor": "refactor",
    "ci": "ci",
    "test": "test",
    "style": "style",
}

BRANCH_RE = re.compile(
    r"^(?P<type>" + "|".join(LABELS) + r")/(?P<issue>[0-9]+)-[a-z0-9]+(?:-[a-z0-9]+)*$"
)
TITLE_RE = re.compile(r"^(?P<issue>[0-9]+): \S")
LINK_RE = re.compile(
    r"\b(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\s*:?\s+#(\d+)\b", re.IGNORECASE
)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


class GitHub:
    """Minimal GitHub REST API client."""

    def __init__(self, token, repo, api_url="https://api.github.com"):
        self.token = token
        self.base = f"{api_url}/repos/{repo}"

    def request(self, method, path, body=None):
        """Send a request and return the decoded JSON, or None on 404."""
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(
            self.base + path,
            data=data,
            method=method,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        try:
            with urllib.request.urlopen(req) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            raise

    def get_issue(self, number):
        return self.request("GET", f"/issues/{number}")

    def ensure_label(self, name):
        if self.request("GET", f"/labels/{urllib.parse.quote(name)}") is None:
            self.request("POST", "/labels", {"name": name})

    def add_label(self, number, name):
        self.request("POST", f"/issues/{number}/labels", {"labels": [name]})


def linked_issues(body):
    """Return the issue numbers linked with Closes/Fixes/Resolves, in order."""
    body = HTML_COMMENT_RE.sub("", body or "")
    return list(dict.fromkeys(int(n) for n in LINK_RE.findall(body)))


def check(pr, get_issue):
    """Check a pull request.

    pr is the pull_request object from the event payload. get_issue(number)
    returns the issue as a dict, or None if it does not exist.

    Returns (errors, label), where label is None if the branch name is invalid.
    """
    errors = []

    branch = pr["head"]["ref"]
    branch_match = BRANCH_RE.match(branch)
    if not branch_match:
        errors.append(
            f'Branch "{branch}" does not match <type>/<issue>-<short-description>, '
            f"where <type> is one of: {', '.join(LABELS)} "
            "(e.g. feat/42-add-soc-detection)."
        )

    title = pr["title"]
    title_match = TITLE_RE.match(title)
    if not title_match:
        errors.append(
            f'Title "{title}" does not match "<issue>: <title>" '
            '(e.g. "42: Add SoC detection").'
        )

    linked = linked_issues(pr.get("body"))
    if not linked:
        errors.append('The description does not link an issue. Add "Closes #<issue>".')
    for number in linked:
        issue = get_issue(number)
        if issue is None:
            errors.append(f"Issue #{number} does not exist.")
        elif "pull_request" in issue:
            errors.append(f"#{number} is a pull request, not an issue.")
        elif issue["state"] != "open":
            errors.append(f"Issue #{number} is closed.")

    branch_issue = int(branch_match["issue"]) if branch_match else None
    title_issue = int(title_match["issue"]) if title_match else None
    if branch_issue is not None and title_issue is not None and branch_issue != title_issue:
        errors.append(
            f"The branch names issue #{branch_issue}, but the title names #{title_issue}."
        )
    expected = branch_issue if branch_issue is not None else title_issue
    if expected is not None and linked and expected not in linked:
        errors.append(
            f"Expected the description to link #{expected}, but it links "
            f"{', '.join(f'#{n}' for n in linked)}."
        )

    label = LABELS[branch_match["type"]] if branch_match else None
    return errors, label


def write_summary(errors):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write("## Pull request conventions\n\n")
        if errors:
            f.writelines(f"- {e}\n" for e in errors)
            f.write("\nSee `.github/docs/CONTRIBUTING.md`.\n")
        else:
            f.write("Branch name, title, and linked issue look good.\n")


def main():
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as f:
        pr = json.load(f)["pull_request"]

    # Bots such as Dependabot use their own branch names.
    if pr["user"]["type"] == "Bot":
        print(f"Skipping checks for bot pull request by {pr['user']['login']}.")
        return 0

    gh = GitHub(
        os.environ["GITHUB_TOKEN"],
        os.environ["GITHUB_REPOSITORY"],
        os.environ.get("GITHUB_API_URL", "https://api.github.com"),
    )

    errors, label = check(pr, gh.get_issue)

    if label:
        gh.ensure_label(label)
        gh.add_label(pr["number"], label)
        print(f"Labelled the pull request {label!r}.")

    write_summary(errors)
    for e in errors:
        print(f"::error::{e}")
    if errors:
        return 1
    print("Branch name, title, and linked issue look good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
