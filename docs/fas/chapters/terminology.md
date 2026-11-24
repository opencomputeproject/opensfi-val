[← 1. Compliance with OCP Tenets](../open_silicon_firmware_interface_openSFI_specification.md#1-compliance-with-ocp-tenets) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#2-terminology) | [3. Scope →](scope.md)

# 2. Terminology

- **openSFI**: **O**pen-Source **S**ilicon **F**irmware **I**nterface.
  An unified interface between the Host Firmware and the Silicon
  Initialization firmware

- **UPCI**: **U**nified **P**latform **C**onfiguration **I**nterface.
  A spec to define various interpretable binary formats between data
  producers and consumers.

- **VAL**: **V**endor **A**daptation **L**ayer Library - An
  implementation of this openSFI Specification.

> Note: The VAL chapter has been relocated to the [Appendix
> E](appendix-e-abstraction-layer.md#appendix-e---abstraction-layer-defined-interface-spec)
> in v0.3 of this specification. This is a transitional measure,
> intended to provide reference context while the community calibrates
> to the scope and boundaries of the main openSFI specification. The VAL
> content is currently non-normative, and the long-term plan is to
> gradually externalize this content, potentially into a separate
> standalone document by v0.8. All references to VAL within this
> specification will be reviewed and updated accordingly in future
> revisions.

- **Host Firmware**: Bootloader Firmware executing on a platform host
  processor (aka application processor) such as x86 CPUs based on AMD
  & Intel, or other ISAs such as an ARM SoC. Examples include coreboot
  (Dasharo and Libreboot etc.) and UEFI (EDK2, Aptio, H2O, etc). In
  the context of openSFI, this includes all bootloader firmware
  excluding SiP specific firmware and openSFI.

- **SoC**: System on a Chip, including the CPU (Central Processing
  Unit).

- **API**: **A**pplication **P**rogramming **I**nterface.

- **SiP**: **Si**licon **P**rovider, aka Silicon Vendor

- **Factory Design Pattern**: A creational design pattern that
  provides an interface for creating objects in a superclass, but
  allows subclasses to alter the type of objects that will be created
  (Reference -
  <https://refactoring.guru/design-patterns/factory-method>)

- **Firmware Handoff Transfer List** - Extensible data structure
  consisting of a fixed-length header and a list of self-describing
  Transfer Entries. See
  <https://firmwarehandoff.github.io/firmware_handoff/main/transfer_list.html>

- **Firmware Handoff Transfer Entries (or “Transfer Entries”)** -
  Variable length self-describing data structure consisting of a
  fixed-length header and the body. The format of the body is
  determined by the tag_id field in the header. See
  <https://firmwarehandoff.github.io/firmware_handoff/main/transfer_list.html#tl-entry-header>

---

[← 1. Compliance with OCP Tenets](../open_silicon_firmware_interface_openSFI_specification.md#1-compliance-with-ocp-tenets) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#2-terminology) | [3. Scope →](scope.md)
