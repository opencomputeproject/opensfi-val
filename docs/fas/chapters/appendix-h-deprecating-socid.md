[← Appendix G - Example Structures and Enumerations from Normative Specifications](appendix-g-example-structures-and-enumerations.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-h--deprecating-socid-from-the-opensfi-api)

# Appendix H- Deprecating SoCID from the openSFI API

An earlier version of openSFI exposed SoC identity (SoCID) as an
explicit input argument to the silicon firmware interfaces. While this
approach appeared convenient, experience showed that it introduced
ambiguity, unnecessary coupling, and avoidable failure modes between
host firmware and silicon firmware.

In an openSFI system, the silicon firmware is executing *on the silicon
itself*. As such, it is the only software component that can
authoritatively determine which SoC, revision, and feature configuration
is present, using hardware-resident identification mechanisms. Passing
SoCID from host firmware created a redundant and potentially
inconsistent view of identity, where the caller could accidentally or
incorrectly assert an identity that did not match the executing
hardware. This undermined the reliability and security of the interface,
and forced silicon firmware implementations to treat SoCID as untrusted
input.

Starting v0.5 of this specification, openSFI intentionally removes SoCID
from the API surface and instead requires silicon firmware
implementations to derive SoC identity directly from hardware. The role
of the host firmware is not to identify the silicon, but simply to
determine whether the silicon firmware instance it is interacting with
supports the executing SoC. This is expressed through a well defined and
mandatory error status response, SFI_STATUS_UNSUPPORTED_SOC.

With this model, host firmware no longer needs to understand SoC
identity, revision schemes, or vendor specific encodings. It only needs
to know whether the silicon firmware supports the platform it is running
on, and can react accordingly if it does not. This significantly
simplifies host firmware logic, improves portability across silicon
vendors, and eliminates an entire class of misconfiguration and spoofing
risks.

This design also aligns with the expected stateless nature of openSFI
APIs. Support determination is invariant for the lifetime of a boot
session, and is enforced uniformly across all API invocations. Once
silicon firmware indicates that the executing SoC is supported, that
determination remains stable for the duration of the boot. Conversely,
if the SoC is unsupported, all openSFI API invocations will consistently
report this condition, allowing host firmware to treat it as a terminal
outcome and select an alternate boot path or recovery mechanism.

By removing SoCID from the interface and making SoC support an internal
responsibility of the silicon firmware, openSFI v0.5 establishes a
clearer separation of concerns, a more robust security posture, and a
cleaner, more future-proof contract between host firmware and silicon
firmware.

---

[← Appendix G - Example Structures and Enumerations from Normative Specifications](appendix-g-example-structures-and-enumerations.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-h--deprecating-socid-from-the-opensfi-api)
