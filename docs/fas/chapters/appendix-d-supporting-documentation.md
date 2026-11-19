[← Appendix C - Unified Enumerated Stages List](appendix-c-unified-enumerated-stages-list.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-d---supporting-documentation--guidance) | [Appendix E - Abstraction Layer (Defined Interface Spec) →](appendix-e-abstraction-layer.md)

# Appendix D - Supporting Documentation & Guidance

In addition to the openSFI specification, a complete integration
ecosystem includes the following complementary documents, each owned and
governed appropriately:

## openSFI FAS (openSFI Firmware Architecture Specification)

This Firmware Architecture Specification (FAS) is the authoritative,
version-controlled definition of the openSFI abstraction layer.
Maintained by the OCP SPF openSFI Working Group, this document
describes the stable API contract, its function prototypes, parameter
semantics, expected return codes, and lifecycle rules for invocation.
It is intended to remain consistent across silicon vendors and
platform firmware environments, ensuring that host firmware developers
can rely on a common interface surface. Changes to the FAS follow a
governed change-control process to maintain backward compatibility
wherever possible. This specification is normative, meaning that any
implementation claiming openSFI conformance must adhere fully to its
API definitions and behavioral requirements. The FAS defines this
contract and serves as the foundation for all other integration and
implementation guidance.

- ***Purpose***: Defines the authoritative, versioned contract between
  host firmware and silicon initialization backends. Specifies all
  data structures, enumerations, calling conventions, and error codes
  for InitializeSilicon() and ExecuteSiliconRuntimeOp().

- ***Scope***: Normative and ratified by the OCP OPF openSFI Project
  Working Group. Changes follow the specification governance process.

- ***Audience***: Host firmware developers, silicon vendors, and
  platform integrators requiring a stable, silicon-agnostic API.

## openSFI SSImG (openSFI Silicon Specific Implementer’s Guide)

The Silicon-Specific Implementer’s Guide (SSImG) is an
engineering-focused reference maintained by the Silicon Provider
(SiP). This document explains how to implement the VAL for a given SoC
family in a way that is compliant with the openSFI FAS. It details how
the abstraction layer maps to the SiP’s internal silicon
initialization sequences and platform control flows, including
stage-specific behavior, error handling expectations, and any
optimizations possible within the vendor’s firmware architecture
(e.g., openSIL, FSP).

While the SSImG may be released into the open-source domain at the
SiP’s discretion, it is primarily an internal development document,
written for firmware engineers implementing or modifying the VAL.
Because silicon architecture and firmware internals evolve more
rapidly than the openSFI spec itself, the SSImG is governed
independently by the SiP, allowing it to track product-specific
changes without requiring updates to the normative openSFI
specification.

- ***Purpose***: Internal developer guide owned by the Silicon
  Provider (SiP). Describes how the vendor’s firmware architecture
  (e.g., openSIL for AMD, FSP for Intel) implements the openSFI
  interface. May include build instructions, code flow diagrams, and
  silicon-specific constraints.

- ***Scope***: Non-normative and changeable at the SiP’s discretion to
  reflect ongoing silicon or firmware evolution.

- ***Audience***: Primarily internal engineering teams at the SiP;
  optional release to the open-source community at the vendor’s
  discretion.

## openSFI SSInG UEFI (openSFI SoC-Specific Integrator’s Guide for UEFI Host Firmware)

The SoC-Specific UEFI Integrator’s Guide describes how to integrate a
given silicon vendor’s VAL into a UEFI-based platform firmware
environment (e.g., EDK2). Maintained by the Silicon Provider, this
guide is intended for platform integrators, independent firmware
vendors (IFVs), and OEM/ODM engineering teams who need to consume the
VAL in UEFI-compliant firmware stacks.

The document covers build integration steps, platform configuration
requirements, firmware volume placement, dependency resolution, and
debug hooks specific to UEFI. It may also detail interactions with the
UEFI DXE, PEI, and SMM phases, along with platform policy settings
relevant to silicon bring-up via openSFI. This guide is expected to be
public and could be contributed to the Open Compute Project (OCP) to
encourage multi-vendor alignment and reuse across the UEFI ecosystem.

- ***Purpose***: Public-facing document maintained by the SiP,
  describing how UEFI-based host firmware (e.g., EDK2) integrates with
  the vendor’s openSFI-compliant VAL.

- ***Scope***: May be contributed to OCP for transparency and reuse.
  Updated as needed to reflect changes in UEFI integration flows or
  silicon lifecycle stages.

- ***Audience***: IFVs, OEMs, and platform integrators building UEFI
  firmware for systems using the vendor’s silicon.

## openSFI SSInG coreboot (openSFI SoC-Specific Integrator’s Guide for coreboot Host Firmware)

The SoC-Specific coreboot Integrator’s Guide serves the same role as
the UEFI variant but is tailored for integrating a given SiP’s VAL
into a coreboot-based platform firmware stack. Maintained by the
Silicon Provider, it addresses the unique build system, initialization
sequencing, and payload hand-off mechanics of coreboot.

The guide describes how to integrate the VAL into coreboot stages
(e.g., romstage, ramstage), manage stage-specific buffer allocations,
and align with coreboot’s device tree and Kconfig structures. It may
also cover integration with common payloads (e.g., SeaBIOS, Tianocore)
and provide debugging and logging recommendations consistent with both
coreboot and the silicon vendor’s diagnostics framework. Like the UEFI
guide, it is expected to be public and may be contributed to OCP to
foster broader ecosystem adoption and cross-platform interoperability.

- ***Purpose***: Public-facing document maintained by the SiP,
  describing how coreboot-based host firmware integrates with the
  vendor’s openSFI-compliant VAL.

- ***Scope***: May be contributed to OCP for community benefit.
  Updated in alignment with changes in coreboot or silicon integration
  flows.

- ***Audience***: Open-source firmware developers, community
  maintainers, and integrators building coreboot firmware for systems
  using the vendor’s silicon.

---

[← Appendix C - Unified Enumerated Stages List](appendix-c-unified-enumerated-stages-list.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-d---supporting-documentation--guidance) | [Appendix E - Abstraction Layer (Defined Interface Spec) →](appendix-e-abstraction-layer.md)
