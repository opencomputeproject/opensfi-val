# Contributing to openSFI VAL

This document describes how to contribute changes to this repository.

Every change follows the same path:

1. Open an issue that describes the change.
2. Make the change on a branch named after the issue.
3. Open a pull request that closes the issue.

## Issues

Every change starts with a GitHub issue, so each change in the history can
be traced back to why it was made.

- Before opening a new issue, search the existing ones to avoid duplicates.
- Open the issue with one of the templates:
  - **Bug report**: something is broken or behaves incorrectly.
  - **Feature request**: a new capability or an improvement.
  - **Documentation change**: a change to the specification, READMEs,
    guides, or comments.
- To claim an issue, assign it to yourself, or comment on it if you can't
  assign it. This lets others know that someone is working on it.
- Discuss the approach in the issue before writing a large change.
- An issue is closed when the pull request that resolves it is merged. If
  an issue is closed without a change (for example, as a duplicate or
  because it won't be fixed), leave a comment explaining why.

## Branches

Do not commit directly to `main`. Make each change on its own branch and
open a pull request against `main`.

### Branch naming

Name each branch `<type>/<issue>-<short-description>`:

- `<type>` is one of the prefixes below.
- `<issue>` is the number of the issue the branch resolves.
- `<short-description>` is a few lowercase words separated by hyphens that
  say what the branch does.

For example, the branch for issue #42 that adds SoC detection is
`feat/42-add-soc-detection`.

| Prefix      | Use for                                                                | Example                           |
|-------------|------------------------------------------------------------------------|-----------------------------------|
| `feat/`     | Adds a new feature or capability                                       | `feat/42-add-soc-detection`       |
| `fix/`      | Fixes a bug or broken behavior                                         | `fix/57-broken-auth-redirect`     |
| `docs/`     | Documentation-only changes (specifications, READMEs, guides, comments) | `docs/12-add-api-examples`        |
| `refactor/` | Code restructuring without changing external behavior                  | `refactor/63-simplify-user-query` |
| `ci/`       | Updates to GitHub Actions, Dockerfiles, or build scripts               | `ci/8-add-linting-workflow`       |
| `test/`     | Adding or updating unit and integration tests                          | `test/71-add-checkout-coverage`   |
| `style/`    | Formatting, linting, or whitespace fixes                               | `style/30-run-prettier-format`    |

If a change fits more than one prefix, use the one for its main purpose.
For example, a bug fix that also adds a test uses `fix/`.

## Commits

- Keep each commit focused on one logical change.
- Write the subject line in the imperative mood, in 72 characters or fewer
  (for example, "Add bounds check to config parser").
- Leave a blank line after the subject. In the body, explain what changed
  and why.
- Sign off every commit to certify that you have the right to submit it
  (see [Developer Certificate of Origin](https://developercertificate.org/)).
  Use `git commit -s` to add the `Signed-off-by:` line.

## Pull requests

- Open the pull request against `main`. Its description is pre-filled
  from the [pull request template](../pull_request_template.md).
  Fill in each section that applies.
- Title the pull request `<issue>: <title>`, where `<issue>` is the number
  of the issue it resolves and `<title>` is a short summary in the
  imperative mood. For example, `42: Add SoC detection`. Keep the whole
  title to 72 characters or fewer.
- Link the issue the pull request resolves by writing `Closes #<issue>` in
  the description. GitHub closes the issue when the pull request is merged.
- Keep each pull request to one topic. Split unrelated changes into
  separate pull requests.
- Rebase on the latest `main` before asking for review, and resolve any
  conflicts.
- Respond to review comments by pushing new commits or replying in the
  thread.

### Automated checks

A GitHub Actions workflow
([`pr-checks.yml`](../workflows/pr-checks.yml)) runs on every pull request.
It calls [`pr_checks.py`](../scripts/pr_checks.py), which:

- checks that the branch name follows the naming convention above
- checks that the title is `<issue>: <title>`
- checks that the description links an open issue with `Closes`, `Fixes`,
  or `Resolves`
- checks that the issue numbers in the branch name, the title, and the
  description all match
- labels the pull request by its branch prefix

Fix any failure by renaming the branch or editing the title or
description. The check runs again automatically when you edit the title or
description. After
renaming a branch, open a new pull request from it.
