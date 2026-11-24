[← 6. Architecture Overview](architecture-overview.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#7-soc-support-determination-and-enforcement) | [8. API Definition →](api-definition.md)

# 7. SoC Support Determination and Enforcement

The following requirements are mandatory for any silicon firmware
implementation claiming compliance with the current revision of the
specification.

## 7.1. Hardware-Derived SoC Identification

- The silicon firmware **MUST** derive the executing SoC identity exclusively from hardware-resident identification mechanisms.

   *Meaning: SoC identity must come from on-silicon sources such as ID registers, fuses, or architecturally defined identification instructions.*

- The silicon firmware **MUST NOT** rely on host-provided parameters, configuration data, or API arguments to determine SoC identity.

   *Meaning: Host firmware cannot assert, override, or influence the identity of the executing silicon.*

## 7.2. Supported SoC Determination

- The silicon firmware MUST determine whether the executing SoC is within its supported set before performing any functional work for an openSFI API invocation.

   *Meaning: Support must be checked up-front, not after partial initialization or runtime activity.*

- The supported set MUST include all constraints required for correct operation, including SoC family, revision or stepping, and required feature or SKU characteristics.

   *Meaning: “Supported” is not limited to a marketing name, but includes all hardware*

## 7.3. Mandatory Error Signaling

- If the executing SoC is not supported, the silicon firmware **MUST** return SFI_STATUS_UNSUPPORTED_SOC for the invoked API.

   *Meaning: Unsupported silicon must fail explicitly and predictably, not silently or with a generic error.*

- When returning SFI_STATUS_UNSUPPORTED_SOC, the silicon firmware **MUST NOT** perform any externally visible initialization or runtime side effects beyond what is required to determine SoC identity.

   *Meaning: No registers, memory, clocks, or fabrics may be partially initialized before reporting unsupported silicon.*

## 7.4. Support Determination Invariance

- Support determination **MUST** be invariant for the lifetime of the Boot Session.

   *Meaning: A given boot cannot transition from “supported” to “unsupported” or vice versa.*

- If any openSFI API invocation returns a status other than SFI_STATUS_UNSUPPORTED_SOC, then all subsequent openSFI API invocations in the same Boot Session **MUST NOT** return SFI_STATUS_UNSUPPORTED_SOC.

   *Meaning: Once support is established, it cannot later be revoked during the same boot.*

- If the executing SoC is unsupported, then **all** openSFI API invocations in the same Boot Session **MUST** return SFI_STATUS_UNSUPPORTED_SOC.

   *Meaning: Unsupported silicon must fail consistently across all APIs and call sequences.*

## 7.5. Uniform Application Across APIs

- The requirements in this section **MUST** apply uniformly to all openSFI APIs, including initialization and runtime operations.

   *Meaning: There are no “special” APIs that bypass SoC support enforcement.*

- Silicon firmware **MUST NOT** vary SoC support behavior based on API call ordering, invocation history, or partial initialization state.

   *Meaning: Support determination cannot depend on whether Init or RuntimeOps was called first.*

## 7.6. Conformance Claim Integrity

- A silicon firmware implementation claiming compliance with **the current revision of the specification** **MUST**implement all behavior described in this section.

   *Meaning: Partial or selective implementation does not qualify as compliant.*

- Claiming compliance with **the current revision of the specification** **MUST NOT** be interpreted as a claim of support for all SoCs, but only as adherence to the openSFI interface and behavioral requirements.

   *Meaning: Compliance describes correct behavior, not breadth of silicon coverage.*

## 7.7. Host Firmware Expectations (Non-Normative)

*Host firmware is expected to treat openSFI silicon firmware as the
authoritative source of SoC support determination. Host firmware
SHOULD NOT attempt to identify, classify, or validate the executing
SoC on behalf of the silicon firmware, and SHOULD NOT infer support
based on platform configuration or prior knowledge of silicon
variants. Silicon FW provider must return SFI_STATUS_UNSUPPORTED_SOC
if openSFI is not supported on the active, installed SoC.*

---

[← 6. Architecture Overview](architecture-overview.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#7-soc-support-determination-and-enforcement) | [8. API Definition →](api-definition.md)
