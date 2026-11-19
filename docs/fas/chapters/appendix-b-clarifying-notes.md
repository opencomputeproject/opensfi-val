[← Appendix A PascalCase Naming Convention (with Capitalized Acronyms)](appendix-a-pascalcase-naming-convention.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-b---clarifying-notes) | [Appendix C - Unified Enumerated Stages List →](appendix-c-unified-enumerated-stages-list.md)

# Appendix B - Clarifying Notes

1.  **Stack and Heap Usage** – The openSFI VAL library does not require
    any explicit memory allocations beyond the buffers allocated for the
    \*Input and \*Output arguments. It operates within the same memory
    and runtime context as the host firmware, using the existing stack
    and heap organically.

2.  **Variable Output Buffer Size** – While the VAL library is not
    required to know the allocated size of the \*Output structure at
    runtime, and must assume the buffer provided by the host firmware is
    sufficient for its operation, there is a finite possibility that
    silicon initialization firmware could inadvertently write beyond the
    bounds of the allocated buffer. This concern was raised during the
    v0.30 specification review.

    1.  To mitigate this potential risk, we propose adding an explicit
        indication of the output buffer size to the API interface. To
        maintain efficiency and preserve the four-argument API limit,
        this size will be included as an element within the \*Input
        structure rather than as a separate API argument.

    2.  The intended usage is as follows: if the VAL detects that the
        allocated output buffer is insufficient, it must terminate
        further processing and return control to the caller with the
        SFI_STATUS_OUT_OF_MEMORY status code.

    3.  This requirement will be implemented provisionally. If, by the
        v1.0 release of the specification, no implementation has
        triggered this condition during unit testing or validation, the
        requirement will be removed from the specification.

    4.  If the \*Output structure is known and fixed in size (e.g., a
        compile-time constant determined by using the sizeof operator on
        the associated StageID-specific output structure from the
        openSFIOutputStructures.h file), this concern does not apply, as
        the host firmware can deterministically allocate the exact
        required memory. Such a scenario is expected to cover all
        fixed-format output structures.

3.  **StageIDs** – When defined as an enumerated list, StageIDs must be
    universal and represent a superset across all SoCIDs and all SoC
    vendors.

4.  **Input Structure Definitions** – These must be StageID specific
    and universal across all SoC vendors. Metadata can indicate if a
    given structure element is not applicable to a particular SoC
    vendor.

5.  **Output Structure Definitions** –

    1.  If known at build time, these must be universal to all SoC
        vendors, with non-applicable elements indicated via metadata.

    2.  If not known at build time, the host firmware may not be able to
        interpret the returned data without additional mechanisms. In
        such cases, we need to identify the scope of these scenarios
        (e.g., standard hardware descriptor fragments such as e820,
        ACPI, SMBIOS) and determine whether serialization is warranted,
        unless we can unify the structure definitions across vendors.
        This requires further discussion - **Post v0.3 Spec release,
        expected in v0.5.**

6.  **Precedent for Stateless Static Libraries** – When a custom
    library is statically linked to a C program, its code and data
    become part of the final executable, sharing the same address space
    and heap as the host. In common practice, stateless, statically
    linked libraries, such as c runtime libraries (even the most complex
    ones), do not require special memory allocation for their internal
    operation. Temporary buffers are typically handled in processor
    registers or existing stack space. Only in rare cases requiring
    large working memory should special allocation be considered, and
    such exceptions should be addressed case by case. We should avoid
    introducing such complexity prematurely, to maintain a simple,
    predictable, and vendor-agnostic model.

---

[← Appendix A PascalCase Naming Convention (with Capitalized Acronyms)](appendix-a-pascalcase-naming-convention.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-b---clarifying-notes) | [Appendix C - Unified Enumerated Stages List →](appendix-c-unified-enumerated-stages-list.md)
