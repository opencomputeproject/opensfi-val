[← 7. SoC Support Determination and Enforcement](soc-support-determination-and-enforcement.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#8-api-definition) | [9. openSFI Execution Model and Boot Flow →](opensfi-execution-model-and-boot-flow.md)

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

This API is the entry point for silicon initialization during platform
boot stages.

**Prototype:**

```c
SFIStatus
InitializeSilicon (
  void      *SFIInput,
  void      *SFIOutput,
  uint32_t  InitStageID
  );
```

**Arguments:**

|  |  |
|:---|:---|
| SFIInput | Pointer to a contiguous InitStageID specific silicon configuration input structure |
| SFIOutput | Pointer to a contiguous InitStageID specific structure with return data, diagnostics data or handoff buffer |
| InitStageID | Enum indicating the silicon initialization phase |

**Return Value(s):**

- SFIStatus

|          |                             |
|:---------|:----------------------------|
| zero     | Success                     |
| non-zero | Error (error codes **TBD**) |

## 8.2. ExecutePostSiliconInitOp()

This API is used for executing operations on silicon
post-initialization.

**Prototype:**

```c
SFIStatus
ExecutePostSiliconInitOp (
  void      *SFIInput,
  void      *SFIOutput,
  uint32_t  PostInitOpsID
  );
```

**Arguments:**

|  |  |
|:---|:---|
| SFIInput | Pointer to a contiguous PostInitOpsID specific input structure |
| SFIOutput | Pointer to a contiguous PostInitOpsID specific output structure with return status, diags data or handoff buffer |
| RuntimeOpsID | Enum defining the type of lifecycle action (e.g. telemetry, reconfiguration) |

**Returns Value(s):**

- SFIStatus

|          |                             |
|:---------|:----------------------------|
| 0        | Success                     |
| non-zero | Error (error codes **TBD**) |

The separation of initialization and runtime APIs improves clarity,
composability, and vendor adoption. Implementations may expose both or a
subset based on silicon capabilities.

Notes:

- **Scope Clarification for ExecutePostSiliconInitOp()**

The definition and intended scope of ExecutePostSiliconInitOp() are
not yet finalized in v0.5. It remains under discussion whether this
operation is meant to service silicon bound runtime services during OS
runtime, or to target a transitional phase after silicon
initialization completes but before OS handoff, or both. This
ambiguity is expected to be resolved in v0.5+, along with a more
definitive API contract.

## 8.3. HostFWMain()

This API defines the signature for the host firmware main entry point
to be called following the Vendor-Owned Early
Initialization stage. This API is
defined by openSFI, but implementation is left to host firmware.

**Prototype:**

```c
void
HostFWMain (
  void  *SFIMemData
  );
```

**Arguments:**

|  |  |
|:---|----|
| SFIMemData | Pointer to a structure containing a description of the early (temporary) memory map. |

**Return Value(s):**

- None

## 8.4. Library Model, State, and Ownership

openSFI APIs are intended to be consumed as statically linked libraries
integrated into the host firmware image. From the perspective of the
host firmware, the openSFI API surface is defined to be stateless.

Silicon implementations shall not rely on persistent internal state
across API invocations, unless such state is explicitly represented in
openSFI-defined data structures exchanged with the host firmware.

All openSFI-defined input and output data structures are caller-owned:

- The host firmware is responsible for allocating, owning, and
  maintaining the lifetime of all openSFI data structures.

- Silicon firmware may read and update structures passed by reference
  during an invocation.

- Silicon firmware shall not assume ownership of these structures and
  shall not retain hidden state across invocations.

All openSFI APIs use pointer-based calling conventions. Unless
explicitly stated otherwise, structure arguments passed to openSFI APIs
shall be pointers, and callers shall pass the address of the structure
(e.g., using the & operator in C).

This model ensures that platform state is explicit, inspectable, and
portable, and prevents the introduction of implicit or opaque state
within silicon implementations.

### 8.4.1. XFERLIST_SMBIOS_RECORD

### 8.4.2. XFERLIST_BOOT_MODE

---

[← 7. SoC Support Determination and Enforcement](soc-support-determination-and-enforcement.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#8-api-definition) | [9. openSFI Execution Model and Boot Flow →](opensfi-execution-model-and-boot-flow.md)
