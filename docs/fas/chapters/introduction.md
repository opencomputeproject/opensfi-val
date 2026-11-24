[← 5. Problem Statement](problem-statement.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#6-introduction) | [7. Architecture Overview →](architecture-overview.md)

# 6. Introduction

The Open Silicon Firmware Interface (openSFI) is a specification that
defines a common, architecture-neutral interface for host firmware to
interact with silicon initialization firmware. Its goal is to enable
modular, scalable, and vendor-agnostic integration of silicon into host
firmware environments.

**openSFI Specification is the Foundational Contract**. Host firmware
doesn’t care how the silicon initialization is implemented. It just
needs a clean, stable API contract to call the right function, with the
right inputs, and get deterministic outputs.

## 6.1. Description

openSFI aims to address the fragmentation and fragility in firmware
systems by defining a common silicon firmware interface. This design
specification focuses on creating a scalable and flexible framework that
enhances interoperability across various silicon platforms. Key features
include:

- **Unified Interface Definition:** openSFI will standardize
  interactions between host firmware and silicon vendors, simplifying
  integration and interaction.

- **Platform Integration:** Streamlined methods to integrate diverse
  silicon, aligning with Open Compute Project (OCP) principles.

- **Resource Efficiency:** Promoting sustainability by optimizing
  firmware processes and reducing redundant engineering work across
  multi-generational platforms.

- **Industry Collaboration:** Encourages collaboration among industry
  participants to bridge ecosystem gaps while maintaining backward
  compatibility.

## 6.2. Scope

openSFI defines a standard interface between host firmware and silicon
lifecycle management components, supporting both initialization and
post-boot operations.

The openSFI specification defines a C-based interface between host
firmware and silicon initialization components (e.g., AMD openSIL, Intel
FSP). It is targeted at x86 SoCs for the initial release but designed to
be ISA-neutral. openSFI standardizes early boot silicon initialization
during the SEC, PEI, and early DXE phases (in UEFI terminology), or
equivalent early stages in other firmware frameworks like coreboot.

## 6.3. Goals

The primary goals of the openSFI are to:

- **Unify** silicon initialization interfaces across vendors.

- **Simplify** host firmware integration.

- **Enable** reuse of host firmware across platforms and vendors.

- **Reduce** engineering cost, duplication, and validation overhead.

- **Promote** sustainability through efficient resource usage and
  common tooling.

## 6.4. Interface Compatibility Testing

Interface compatibility testing for openSFI ensures predictable
interoperability across diverse silicon platforms while maintaining
adherence to established interface definitions.

- **Compatibility Procedures:**

  - Validate API implementation against defined specification,
    data-types and encoding format of input and output parameters,
    and return values.

  - Define and execute test cases that confirm cross-platform
    interoperability, leveraging existing platforms or a
    vendor-neutral simulated reference implementation to validate
    integration behavior and performance. This enables consistent
    benchmarking, helps detect regressions, and ensures that
    openSFI-compliant integrations meet the intended abstraction
    guarantees.

  - Execute test cases to ensure no output buffer overflows occur
    across API calls, alignment requirements are met and APIs can
    handle malformed or incorrect input parameters and return
    appropriate error codes.

- **Success Criteria:**

  - Implementation conforms to API contract in terms of data-types
    of input and output parameters, required encoding formats are
    strictly met(such as UPCI specified encoding), and return values
    are compliant with the specification.

  - Host firmware can successfully interface with silicon from
    multiple vendors without requiring vendor-specific changes in
    the host firmware.

  - Any non-functional requirements are met like execution
    performance(E.g.: time-bounded return of API calls) and
    robustness of implementation ensuring no unwanted side effects
    such as data corruption occurs.

## 6.5. Standards Interoperability (Non-Normative) Compliance

openSFI does not establish or replace external industry standards (e.g.,
ACPI, SMBIOS, UEFI). However, implementations must not preclude standard
host firmware behavior or break assumptions made by standards compliant
firmware frameworks and operating systems.

In practice, this means:

- **Interoperable Outputs:** Data produced via openSFI (e.g. hardware
  description, discovery, or telemetry) MUST be emitted in a form that
  host firmware can reliably translate into standards compliant
  artifacts without ambiguity or loss of fidelity.

- **No Contract Violations:** openSFI MUST NOT introduce ordering,
  timing, or data dependencies that conflict with normative behavior
  required by ACPI/UEFI/SMBIOS (or other applicable standards) in the
  platform’s boot flow.

- **Forward Compatibility:** Where a vendor returns “fragments” or
  partial descriptors, those fragments MUST be “standard-ready”, i.e.
  structurally sufficient and unambiguous so the host can
  deterministically assemble fully compliant tables/records.

Here's a succinct example (ACPI): A VAL may return ACPI ready fragments
(e.g. CPU topology, memory map deltas, device resources) that are not
complete ACPI tables by themselves. These fragments MUST be formatted
and annotated such that the host firmware can compose fully compliant
ACPI structures (e.g. MADT, SRAT, SLIT, HEST) without guessing or vendor
specific heuristics. Failure to meet this requirement risks breaking OS
expectations and is non-conformant with openSFI’s interoperability
rules.

---

[← 5. Problem Statement](problem-statement.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#6-introduction) | [7. Architecture Overview →](architecture-overview.md)
