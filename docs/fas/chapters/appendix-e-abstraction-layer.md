[← Appendix D - Supporting Documentation & Guidance](appendix-d-supporting-documentation.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-e---abstraction-layer-defined-interface-spec) | [Appendix F →](appendix-f-sc-approval-checklist.md)

# Appendix E - Abstraction Layer (Defined Interface Spec)

To achieve the goal of silicon-agnostic host firmware integration,
openSFI introduces two closely related architectural constructs:

- Abstraction Layer (defined by the spec)

- Vendor Adaptation Layer (VAL) (implementation-specific shim layer)

These components work together to isolate host firmware from
vendor-specific silicon initialization implementations while enabling
extensibility and maintainability.

## Abstraction Layer (Defined Interface Spec)

<mark>The abstraction layer is</mark> formally defined by this
specification<mark>. It describes a common C-based API for invoking silicon
lifecycle operations (initialization and runtime). These interfaces are
stable and documented, and include:</mark>

```c
int InitializeSilicon(...)
int ExecuteSiliconRuntimeOp(...)
```

The abstraction layer standardizes the interface surface, enabling
consistent API calls from the host firmware (the consumer), regardless
of the silicon vendor behind the implementation (the producer).

Example:

```c
// Defined by openSFI Spec - implemented by the silicon vendor
int InitializeSilicon(void *Input, void *Output, uint32_t Stage);
```

This function is the contract between host firmware and the silicon
initialization backend.

## Vendor Adaptation Layer (VAL / Shim Layer)

The VAL Library is an implementation construct, a thin translation layer
developed by silicon vendors (or debatably by platform integrators and /
or IFVs). **It adapts the openSFI abstraction to vendor-specific
initialization or runtime mechanisms** (e.g., AMD’s
InitializeAMDSilicon() or Intel’s FspSiliconInit()).

The VAL can be delivered as either a binary or source code library that
encapsulates silicon specific behavior for initialization and runtime
services, while conforming to the unified interface defined by the
openSFI specification. In doing so, it ensures consistency and
compatibility both across vendors and across that vendor’s own
generations of silicon, allowing host firmware to interact in a
canonical, vendor neutral manner regardless of underlying hardware
differences. This canonical model enables predictable integration
behavior, minimizes porting complexity, and fosters long term
interoperability within the openSFI ecosystem.

The VAL Library is not part of the openSFI specification, but its
presence is instrumental during early adoption phases or
proof-of-concept (POC) efforts, and may eventually be optimized away as
vendors integrate the abstraction directly into their native flows.

Example Platform Integrator Implementation:

```c
// openSFIShim.c
int InitializeSilicon(void *Input, void *Output, uint32_t InitStageID) {
  if (IsAMDSoC(SoCID)) {
    return InitializeAmdSilicon(Input, Output, InitStageID, SoCID);
  } else if (IsIntelSoC(SoCID)) {
    return FSPSiliconInit(Input, Output, Stage, SoCID);
  }
  return UNSUPPORTED_SOC; // Unsupported SoC
}
```

In this model:

- The abstraction layer is spec-defined, universal, and fixed.

- The VAL Library is implementation-defined, flexible, and SoC
  vendor-specific that can be integrated by a Platform Integrator or
  an IFV to serve platform designs based on more than one silicon
  vendor SoC.

## Lifecycle of the VAL Library

The VAL Library is expected to evolve:

- **Initial POC Phase:** Serves as a translation layer to map openSFI
  APIs to vendor-specific APIs.

- **Mid-Adoption:** Some common logic may migrate into host firmware
  or silicon packages.

- **Mature Stage:** The VAL may disappear entirely as silicon vendors
  embed native support for openSFI directly into their firmware
  packages (e.g., openSIL or Intel FSP implementing
  InitializeSilicon() natively)

While the VAL Library is expected to evolve, <mark>a vendor may well choose
to jump directly to native integration or remain in the shim model
indefinitely if it suits their business and / or architecture
needs.</mark>

## Design Goals and Benefits

- **Encapsulation:** Host firmware is completely decoupled from
  vendor-specific APIs (unless the silicon vendor has migrated to the
  aforementioned ‘Mature Stage’ natively supporting the openSFI
  interfaces).

- **Portability:** The same host firmware can support different SoCs
  with minimal changes.

- **Debug Efficiency:** The VAL enables traceability and diagnostics
  mapping across vendors.

- **Security:** A standardized interface simplifies security auditing
  and validation of firmware interactions.

## Illustration – Conceptual Mapping

| **Layer** | **Purpose** | **Ownership** |
|:---|:---|:---|
| Abstraction (API) | Defined contract (e.g., InitializeSilicon) | Spec (openSFI WG) |
| Vendor Adaptation Layer (VAL) | Translation to SoC-specific API | Silicon Vendor / IFV / Integrator |
| Vendor Silicon Code | Actual init logic (e.g., FSP/openSIL) | Silicon Vendor |

> **Note**: Vendor-specific integration details, including mapping
> openSFI to native silicon initialization flows (e.g., openSIL, Intel
> FSP), will be documented in SiP-maintained guides separate from this
> specification. These include the Silicon-Specific Implementer’s Guide
> (SSImG) and Silicon-Specific Integrator’s Guide (SSInG) integration
> guides for specific host firmware environments such as UEFI or
> coreboot. This separation allows the openSFI specification to remain
> stable and vendor-neutral, while enabling each SiP to update their
> integration guidance as their silicon and firmware stacks evolve.
> Please see [**Appendix D - Supporting Documentation &
> Guidance**](https://docs.google.com/document/d/18ZuWfUk6WxZuTpbloAt2fBGFQZSZqLfV/edit?pli=1#heading=h.chkoeiwupkwf)
> for details.

---

[← Appendix D - Supporting Documentation & Guidance](appendix-d-supporting-documentation.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-e---abstraction-layer-defined-interface-spec) | [Appendix F →](appendix-f-sc-approval-checklist.md)
