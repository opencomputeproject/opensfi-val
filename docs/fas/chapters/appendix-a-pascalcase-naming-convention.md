[← 12. Governance](governance.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-a-pascalcase-naming-convention-with-capitalized-acronyms) | [Appendix B - Clarifying Notes →](appendix-b-clarifying-notes.md)

# Appendix A PascalCase Naming Convention (with Capitalized Acronyms)

PascalCase is a naming convention where the first letter of every word
is capitalized and no underscores or separators are used. In this
document, we adopt an extended PascalCase style that **fully capitalizes
acronyms** to maintain clarity and consistency across hardware-related
identifiers.

**Purpose**:

To ensure clear, concise, and readable naming for types, structures,
classes, and modules across the openSFI and UPCI specifications and
codebase. These conventions collectively support readable, maintainable,
and scalable code design across the openSFI and UPCI ecosystems.

**Guidelines**:

- Each word begins with a capital letter (e.g., ConfigSchema,
  BootManager).

- Acronyms (e.g., CPU, USB, PCIe, IFST) are capitalized in their
  entirety (e.g., CPUTargets, USBDevice).

- Avoid underscores (\_) or hyphens (-).

**Examples**:

- IFSTCPUTargets

- Stage1CPUTargets

- InitializeUSBDevice

- ConfigurePCIeTopology

- ReadECCStatus

## Naming Convention for Constants

Constants (macros, defines, enum values) should be written in **ALL_CAPS
with underscores** separating words. This helps them stand out clearly
in source code and align with long-standing firmware and C-language
traditions.

**Purpose**:

To distinguish constants and macro definitions from other symbols,
ensuring visibility in low-level firmware environments.

**Guidelines**:

- Use uppercase letters with underscores: MAX_CPU_COUNT,
  DEFAULT_TIMEOUT_MS

- Prefix with component or module where necessary: IFST_STAGE1_MASK,
  UPCI_FIELD_VERSION

**Examples**:

- MAX_NUM_OF_SOCKETS

- IFST_STAGE1_BITMASK

- DEFAULT_BIOS_BOOT_MODE

- UPCI_CONFIG_VERSION

**Enumerated Literals (e.g., true, false) – Style Guidance**

For **boolean literals** such as true, false, null, and other
language-level keywords or enumerated constants:

**Do Not PascalCase or CamelCase.** These values **should always remain
in lowercase**, as per **language conventions**, even if the rest of
your codebase uses PascalCase or CamelCase.

#### Example:

```c
bool EnableIFST = true; // correct
bool EnableIFST = True; // incorrect (not defined)
```

#### Why?

- true and false are **language-defined keywords** in C/C++, and their
  casing is standardized by the language and the compiler.

- Changing their casing will **break compilation**, as the compiler
  will not recognize True or False unless you explicitly redefine them
  (which is discouraged and confusing).

- This applies even when adopting strict PascalCase naming for
  variables, functions, structs, etc.

### Additional Tip:

If our project uses custom enumerated types (e.g., typedef enum { Off =
0, On = 1 } State;), those enumerated constants **should follow our
naming convention**, i.e., **PascalCase**

## Naming Convention for Functions, Variables, and Parameters

In alignment with openSFI’s coding style and readability goals, all
**functions, variables, and parameters** shall adopt **PascalCase**,
including **fully capitalized acronyms** (e.g., CPU, IO, IFST). This
provides a uniform and visually distinct naming style, making it easier
to recognize semantic boundaries and maintain clarity in a multi-vendor
codebase.

#### Rules for Naming

- Use **PascalCase** for all identifiers (no underscores).

- Capitalize **every word**, including **acronyms** (e.g., CPU, IO).

- Avoid abbreviations unless they are widely accepted acronyms.

- Names should be descriptive and unambiguous.

#### Examples

| **Category** | **Bad Example** | **Good Example** |
|:---|:---|:---|
| Function | init_cpu_config() | InitCPUConfig() |
| Variable | cpu_status_flag | CPUStatusFlag |
| Parameter | target_io_channel | TargetIOChannel |
| Struct Field | enable_ifst_iod0 | EnableIFSTForIOD0 |
| Constant Ref | MAX_CORES | MaxCores (or kMaxCores if using prefix convention) |

#### Special Notes

- Anonymous union or struct members should also follow PascalCase for
  clarity.

- Arrays should be pluralized meaningfully, e.g., CPUList, IOModules.

---

[← 12. Governance](governance.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-a-pascalcase-naming-convention-with-capitalized-acronyms) | [Appendix B - Clarifying Notes →](appendix-b-clarifying-notes.md)
