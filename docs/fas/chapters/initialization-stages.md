[← 9. openSFI Execution Model and Boot Flow](opensfi-execution-model-and-boot-flow.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#10-initialization-stages) | [11. Platform Input Configuration Semantics →](platform-input-configuration-semantics.md)

# 10. Initialization Stages

Each of the following stages represent a discrete steps in silicon
bring-up:

```c
typedef enum {
  SFI_INIT_STAGE_LIB_INIT = 0,       ///> Library initialization (Optional)
  SFI_STAGE_GET_SYS_RSC_MAP,         ///> System resource map query
  SFI_STAGE_SI_RECONFIG,             ///> PCIe, USB, SATA, and other IO
  SFI_STAGE_RESET_REQUEST,           ///>
  SFI_STAGE_FINAL_SYS_RSC_MAP,       ///> Finalized resource map
  SFI_STAGE_PREPARE_FOR_OS_HANDOFF,  ///> Final handoff to OS loader
  SFI_STAGE_EXIT_HOST_FW,            ///> Tear Down
} INIT_STAGES;
```

The stage identifiers listed above are illustrative placeholders only,
and are not intended to represent a finalized or ratified list of
silicon lifecycle stages for this revision of the spec. Please refer to
an aligned list of InitStages in [Appendix C - Unified Enumerated Stages
List](appendix-c-unified-enumerated-stages-list.md#appendix-c---unified-enumerated-stages-list), which is expected to be defined in v0.5.

These examples are included to facilitate architectural discussions and
clarify the role of InitializeSilicon() & ExecuteSiliconRuntimeOps()
across different lifecycle transitions.

A formally ratified, vendor-inclusive superset of initialization stages
will be defined in openSFI v0.5, starting with alignment across x86
vendors (AMD, Intel) and extending to additional architectures (e.g.,
ARM) in future revisions (v1.0+).

## 10.1. SFI_INIT_STAGE_LIB_INIT - Library Initialization Metadata Query Stage

This ***optional*** stage enables host firmware to query metadata about
the VAL implementation, including memory sizing recommendations for
stage-specific \*Output structures, before invoking any silicon-specific
initialization stages.

**Stage ID:** SFI_INIT_STAGE_LIB_INIT

**Use Case:**

- Enables host firmware to adapt its memory allocation strategies
  based on the size requirements reported by the silicon vendor’s VAL
  implementation.

- Especially useful in pre-DRAM boot stages where memory is highly
  constrained.

- Avoids the need for a separate API by reusing the existing
  InitializeSilicon() interface.

**Expected Behavior:**

- The VAL will populate the provided Output structure with one or more
  fields describing:

  - Recommended Output buffer sizes for known stages.

  - Maximum buffer size required across all supported stages.

  - Optional implementation metadata (VAL version, supported SoCIDs,
    etc.).

**Input/Output:**

- The host firmware shall pass:

  - An empty Input structure (or a vendor-defined structure for
    future extensibility)

  - A valid Output buffer

- If successful, the VAL returns status SUCCESS and fills Output.

- If unsupported, the VAL returns UNSUPPORTED_STAGE.

**Notes:**

- Host firmware must not invoke other initialization stages until
  after this call (if used).

- This stage is optional and may be deprecated in v0.5+ if proven
  unnecessary.

## 10.2. Stage Execution Order Manifest (Normative)

The numeric values of INIT_STAGES are identifiers, not an execution
sequence. The host firmware determines execution order per SoC by
consulting a const, compile-time manifest. This keeps enums append-only
(for forward compatibility) while making the call order explicit and
vendor-specific.

Requirements

1.  **Order defined by manifest**: For each supported SoC, the host
    firmware SHALL reference a constant, read-only manifest, implemented
    as a const array of INIT_STAGES, that explicitly encodes the
    required initialization sequence for that SoC. This manifest is
    SoC-specific, immutable at runtime, and serves as the sole
    authoritative definition of execution order. The manifest MUST be
    included in the platform build and selected based on the SoCID of
    the target

    e.g.,

    ```c
    const INIT_STAGES SocInitSequence[] = {
      SFI_INIT_STAGE_LIB_INIT = 0,
      SFI_STAGE_GET_SYS_RSC_MAP,
      SFI_STAGE_SI_RECONFIG,
      SFI_STAGE_RESET_REQUEST,
      SFI_STAGE_FINAL_SYS_RSC_MAP,
      SFI_STAGE_PREPARE_FOR_OS_HANDOFF,
      SFI_STAGE_EXIT_HOST_FW,
    };
    ```

2.  **No inference from enum values**: The host and VAL MUST NOT infer
    order from the numeric values of INIT_STAGES.

3.  **Per-SoC selection**: The host SHALL select the appropriate
    manifest using the SoCID it is targeting.

4.  **Idempotence / skip model**: If a listed stage is not supported for
    a given SoC revision, the VAL SHALL return
    SFI_STATUS_UNSUPPORTED_STAGE; the host SHALL skip that stage and
    continue.

5.  **Mutability**: Manifests are static (const) and shipped with the
    platform build; runtime modification is out of scope.

---

[← 9. openSFI Execution Model and Boot Flow](opensfi-execution-model-and-boot-flow.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#10-initialization-stages) | [11. Platform Input Configuration Semantics →](platform-input-configuration-semantics.md)
