[← 3. Terminology](terminology.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#4-scope) | [5. Problem Statement →](problem-statement.md)

# 4. Scope

The specification addresses the lack of common firmware interfaces for
host firmware initialization, leading to fragmented host firmware and
increased costs.

The openSFI specification defines a unified interface between host
firmware and silicon initialization components. It targets x86 SoCs (AMD
and Intel) in its initial release but is designed to be ISA-neutral and
extensible.

The scope includes:

- API definition for calling silicon initialization routine

- Runtime or post-boot API services

- Platform configuration integration (UPCI) if required

- Support for bootloader integration (UEFI, coreboot, etc.)

Out of Scope:

- Merging of vendor-specific silicon firmware implementations

- Non-x86 architectures (for this initial release)

---

[← 3. Terminology](terminology.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#4-scope) | [5. Problem Statement →](problem-statement.md)
