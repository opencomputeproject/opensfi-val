[← 2. Terminology](terminology.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#3-scope) | [4. Problem Statement →](problem-statement.md)

# 3. Scope

The specification addresses the lack of common firmware interfaces
across silicon vendors and platform firmware for host platform
initialization, leading to fragmented host firmware and increased costs.

The openSFI specification defines a unified interface between host
firmware and silicon initialization components. It targets x86 SoCs (AMD
and Intel) in its initial release but is designed to be ISA-neutral and
extensible.

The openSFI interface definition considers the bootflow from reset
through OS handoff and runtime services. The interface definition may be
phased in its approach and release to only define common firmware
interfaces for sections of the boot. (for example, from memory
initialization through bootloader exit)

The scope includes:

- API definition for calling silicon initialization routine

- Runtime or post-boot API services

- Platform configuration integration (UPCI) if required

- Support for bootloader integration (UEFI, coreboot, etc.)

Out of Scope:

- Merging of vendor-specific silicon firmware implementations

---

[← 2. Terminology](terminology.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#3-scope) | [4. Problem Statement →](problem-statement.md)
