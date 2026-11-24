[← 9. Initialization Stages](initialization-stages.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#10-platform-input-configuration-semantics) | [11. Standards Alignment →](standards-alignment.md)

# 10. Platform Input Configuration Semantics

The openSFI interface defines a standardized contract between platform
firmware and silicon-specific initialization logic. As part of this
contract, the Input and Output parameters passed to InitializeSilicon()
and ExecuteSiliconRuntimeOp() are critical structures through which
initialization commands, parameters, and resulting metadata are
exchanged.

This chapter outlines the principles for defining, documenting, and
handling these structures.

## 10.1. Purpose and Scope

Each stage of silicon initialization or runtime operation may require
a distinct set of input arguments and may produce unique output
metadata. Rather than mandate a universal schema across all silicon
vendors or stage types, openSFI leaves the structure and
interpretation of these Input and Output arguments to the silicon
vendor’s implementation.

This allows for maximum flexibility while maintaining standardization
at the API boundary.

## 10.2. Vendor Responsibility for Schema Definition

- Each silicon vendor is responsible for defining the per-stage
  structures used for input and output.

- These structures are documented and published in vendor-provided
  headers such as:

  - AMDSoCStageSpecificInputStructs.h

  - AMDSoCStageSpecificOutputStructs.h

- These definitions must remain stable for any given SoCID and StageID
  to preserve interoperability.

## 10.3. Format of Input and Output Structures

- The Input and Output pointers passed to openSFI APIs are expected to
  reference native binary structures, laid out per the vendor-defined
  headers.

- There is no requirement for serialization, self-description, or
  encoding into interpretable binary formats like CBOR or JSON.

- This minimizes complexity and avoids unnecessary processing overhead
  in constrained pre-DRAM environments.

> **Note**: Vendors may choose to internally encode or decode binary
> data for secondary consumers (e.g., µCs, test harnesses etc.), but
> this is outside the scope of the openSFI interface.

## 10.4. Relationship to UPCI

The Unified Platform Configuration Interface (UPCI) may eventually
serve as a governing mechanism for schema compatibility across layers
and tools. However, for the purposes of openSFI v0.3:

- There is no runtime introspection of schemas.

- The layout and interpretation of input/output arguments is assumed
  to be statically known by both producer (host firmware) and consumer
  (VAL implementation).

Future versions (v0.5+) may define optional annotations or UPCI
linkages, but these are not part of the current release.

## 10.5. Error Handling for Memory Allocation

Given the lack of dynamic schema introspection, it is the host
firmware’s responsibility to allocate appropriate memory for the
Output structure. If insufficient memory is allocated, the openSFI
implementation will return an appropriate status code (e.g.,
INSUFFICIENT_MEMORY_ALLOCATED).

To optionally accommodate cases where pre-sizing the structure is
beneficial, a special initialization stage (e.g.,
SFI_INIT_STAGE_LIB_INIT) has been introduced, allowing the host to
query memory requirements in a vendor-defined way. This provision
remains provisional and may be deprecated in a future revision of the
specification should it prove unnecessary.

## 10.6. Post DRAM Initialization Memory Availability

It is expected that once the host firmware reaches the stage *after*
DRAM initialization (e.g., SFI_STAGE_MEM_INIT and beyond), it has
access to significantly more system memory. In such scenarios, the
host firmware is encouraged to allocate a generously sized output
buffer (e.g., 10MB or more) to cover even the most complex
vendor-specific output data requirements, such as detailed memory
maps, firmware resource descriptors, or ACPI table fragments. This
proactive allocation strategy avoids introducing unnecessary API
complexity or memory query calls. The burden of managing memory
efficiency still lies with the vendor provided silicon library, which
should only populate the portion of the output structure relevant to
the current hardware configuration.

---

[← 9. Initialization Stages](initialization-stages.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#10-platform-input-configuration-semantics) | [11. Standards Alignment →](standards-alignment.md)
