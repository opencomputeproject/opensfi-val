[← 7. Architecture Overview](architecture-overview.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#8-api-definition) | [9. Initialization Stages →](initialization-stages.md)

# 8. API Definition

The openSFI interface defines two core APIs to separate early boot-time
silicon initialization from post-boot lifecycle operations.

The openSFI interface implementation is a responsibility of the silicon
vendors via a **Vendor Adaptation Layer (VAL) Library** (or simply
**VAL** or **VAL Library**), a Library conforming to this API contract.
For a detailed explanation of the VAL concept, and implementation
formats, see **[Appendix E - Abstraction Layer (Defined Interface
Spec)](appendix-e-abstraction-layer.md#appendix-e---abstraction-layer-defined-interface-spec).**

## 8.1. InitializeSilicon()

This API is the common / unified (across the SoC vendors) entry point
for silicon initialization during platform boot stages.

**Prototype:**

```c
int
InitializeSilicon (
  void      *Input,
  void      *Output,
  uint32_t  Stage,
  uint32_t  SoCID
  );
```

**Arguments:**

|  |  |
|:---|:---|
| Input | Pointer to InitStageID specific silicon configuration input structure |
| Output | Pointer to InitStageID specific structure with return status, diagnostics data or handoff buffer |
| InitStageID | Enum indicating the silicon init phase (e.g., PRE_MEM, MEM_INIT, IO_INIT) |
| SoCID | Vendor-specific identifier for target SoC configuration |

**Return Value(s):**

|          |                             |
|:---------|:----------------------------|
| zero     | Success                     |
| non-zero | Error (error codes **TBD**) |

Notes:

- **SoCID Usage – Forward-Looking Clarification**

The definition and role of SoCID, particularly whether it should be
explicitly included as part of input/output structures, is currently
under review. A clearer position will be established and reflected in
the specification starting with v0.5+, in alignment with design goals
for scalability and abstraction.

## 8.2. ExecuteSiliconRuntimeOp()

This API is used for executing runtime lifecycle operations on silicon
post-initialization.

**Prototype:**

```c
int
ExecuteSiliconRuntimeOp (
  void      *Input,
  void      *Output,
  uint32_t  RuntimeStageID,
  uint32_t  SoCID
  );
```

**Arguments:**

|  |  |
|:---|:---|
| Input | Pointer to RuntimeStageID specific input structure |
| Output | Pointer to RuntimeStageID specific output structure with return status, diags data or handoff buffer |
| RuntimeStageID | Enum defining the type of lifecycle action (e.g. telemetry, reconfiguration) |
| SoCID | Vendor-specific identifier for target SoC or board configuration |

**Returns Value(s):**

|          |                             |
|:---------|:----------------------------|
| 0        | Success                     |
| non-zero | Error (error codes **TBD**) |

The separation of initialization and runtime APIs improves clarity,
composability, and vendor adoption. Implementations may expose both or a
subset based on silicon capabilities.

Notes:

- **Scope Clarification for ExecuteSiliconRuntimeOp()**

The definition and intended scope of ExecuteSiliconRuntimeOp() are not
yet finalized in v0.3. It remains under discussion whether this
operation is meant to service silicon bound runtime services during OS
runtime, or to target a transitional phase after silicon
initialization completes but before OS handoff, or both. This
ambiguity is expected to be resolved in v0.5+, along with a more
definitive API contract.

---

[← 7. Architecture Overview](architecture-overview.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#8-api-definition) | [9. Initialization Stages →](initialization-stages.md)
