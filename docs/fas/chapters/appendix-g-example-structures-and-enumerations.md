[← Appendix F](appendix-f-sc-approval-checklist.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-g---example-structures-and-enumerations-from-normative-specifications) | [Appendix H- Deprecating SoCID from the openSFI API →](appendix-h-deprecating-socid.md)

# Appendix G - Example Structures and Enumerations from Normative Specifications

This section contains text describing structures and enumerations from
other specifications that are used within openSFI. These are intended to
be informative, to give readers of this specification an idea of the
intent of their usage within openSFI. They are not normative and readers
should consult the original specification for details.

## G.1 SMBIOS Records

The structures which describe SMBIOS records are described normatively
in the DMTF System Management BIOS (SMBIOS) (DSP134) specification. The
structures in this section are for informative purposes only.

Each SMBIOS record begins with a fixed header (see SMBIOS Record Header,
below) and a variable length body. The format of the body is specified
by the Type. Some records may have text strings after the record. The
format of the SMBIOS records is specified in the DMTF SMBIOS
specification. These values are listed here for reference only. Please
consult the specification for the normative definition.

Text strings associated with a given SMBIOS structure are appended
directly after the formatted portion of the structure. This method of
returning string information eliminates the need for application
software to deal with pointers embedded in the SMBIOS structure. Each
string is terminated with a null (0x00) BYTE and the set of strings is
terminated with an additional null (0x00) BYTE. When the formatted
portion of an SMBIOS structure references a string, it does so by
specifying a non-zero string number within the structure’s string-set.
For example, if a string field contains 0x02, it references the second
string following the formatted portion of the SMBIOS structure. If a
string field references no string, a null (0) is placed in that string
field. If the formatted portion of the structure contains
string-reference fields and all the string fields are set to 0 (no
string references), the formatted section of the structure is followed
by two null (0x00) BYTES.

Strings must be encoded as UTF-8 with no byte order mark (BOM). For
compatibility with older SMBIOS

parsers, US-ASCII characters should be used.

### G.1.1 SMBIOS Record Header

The SMBIOS Record Header is a fixed size header which identifies the
SMBIOS Record type, length and handle. This structure is listed here for
reference only.

| **Field** | **Size (bytes)** | **Offset (bytes)** | **Description** |
|----|----|----|----|
| Type | 0x01 | 0x00 | Specifies the type of structure. Types 0 through 127 (7Fh) are reserved for and defined by this specification. Types 128 through 256 (80h to FFh) are available for system- and OEM-specific information. |
| Length | 0x01 | 0x01 | Specifies the length of the formatted area of the structure, starting at the Type field. The length of the structure’s string-set is not included. |
| Handle | 0x02 | 0x02 | Specifies the structure’s handle, a unique 16-bit number in the range 0 to 0xFFFE (for version 2.0) or 0 to 0xFEFF (for version 2.1 and later). The handle numbers are not required to be contiguous. For version 2.1 and later, handle values in the range 0xFF00 to 0xFFFF are reserved for use by this specification.<br>If the system configuration changes, a previously assigned handle might no longer exist. However, after a handle has been assigned by the BIOS, the BIOS cannot reassign that handle number to another structure.<br>Unless otherwise specified, when referring to another structure’s handle, the value 0xFFFF is used to indicate that the referenced handle is not applicable or does not exist. |

## Appendix G.2 Boot Modes

The enumerated values which describe the boot modes are described
normatively in the UEFI\* Platform Initialization specification. The
enumerated values in this section are for informative purposes only.

**BOOT_WITH_FULL_CONFIGURATION** (0x00) - Boot platform with full
configuration.

**BOOT_WITH_MINIMAL_CONFIGURATION** (0x01) - Boot platform with as
little configuration as possible.

**BOOT_ASSUMING_NO_CONFIGURATION_CHANGES** (0x02) - Boot the platform
while assuming that no configuration changes have been made since the
last boot.

**BOOT_WITH_FULL_CONFIGURATION_PLUS_DIAGNOSTICS** (0x03) - Fully
configure the platform and validate the platform devices using
on-board diagnostic capabilities.

**BOOT_WITH_DEFAULT_SETTINGS** (0x04) - Boot using default settings
rather than user-updated settings.

**BOOT_ON_S4_RESUME** (0x05) - Boot on resume from the ACPI S4 power
state. Save-to-disk resume. The entire system must be reinitialized
but the PEIMs may assume that the previous configuration is still
valid **and** the memory map must be maintained.

**BOOT_ON_S5_RESUME** (0x06) - Boot on resume from the ACPI S5 power
state. Soft-off. The entire system must be reinitialized but the PEIMs
may assume that the previous configuration is still valid.

**BOOT_WITH_MFG_MODE_SETTINGS** (0x07) - Boot with actions that should
only occur in the factory or a manufacturer approved setting

**BOOT_ON_S2_RESUME** (0x10) - Boot on resume from the ACPI S2 power
state.

**BOOT_ON_S3_RESUME** (0x11) - Boot on resume from the ACPI S3 power
state. The previously stored configuration data is valid and RAM is
valid. RAM configuration must be restored from nonvolatile storage
(NVS) before RAM may be used. The firmware may only modify previously
reserved RAM.

**BOOT_ON_FLASH_UPDATE** (0x12) - Update the system firmware flash
contents with a flash image that has been placed in an available
non-volatile storage.

**BOOT_IN_RECOVERY_MODE** (0x20) - Recovery is the process of
reconstituting a system’s firmware devices when they have become
corrupted. The corruption can be caused by various mechanisms.

## Appendix G.3 PCI Extended Configuration Access Mechanism (ECAM)

The structures which describe the MMIO address space used for access to
PCI configuration space for the devices on a range of buses are
described normatively in the ACPI MCFG table. The structures and
enumerated values in this section are for informative purposes only.

| **Field** | **Size (bytes)** | **Offset (bytes)** | **Description** |
|----|----|----|----|
| Base Address | 0x08 | 0x00 | The MMIO address for the first device in the bus specified by StartBusNumber in the PCI segment specified by PciSegmentGroupNumber.<br>The address of the first byte of configuration space is calculated as: Base Address + ((Bus - StartBus) \<\< 20) \| (Device \<\< 15) \| (Function \<\< 12).<br>The address space used for PCI configuration space is ((End Bus Number - Start Bus Number) + 1) \* 1MiB. |
| PCI Segment Group Number | 0x02 | 0x08 | The PCI segment on which the buses reside. |
| Start Bus Number | 0x01 | 0x0a | First bus number on the PCI segment. |
| End Bus Number | 0x01 | 0x0b | Last bus number on the PCI bus. Must be greater than or equal to Start Bus Number. |
| Reserved | 0x04 | 0x0c | Reserved Must be initialized to zero. |

### G.3.1 XFERLIST_RESOURCE_DESCRIPTOR

The resource descriptor transfer entry describes the resource properties
of zero or more fixed, nonrelocatable resource ranges found on the
processor host bus. This does not describe how memory is used but
instead describes the attributes of the physical memory present. These
entries mimic the body of the EFI_HOB_RESOURCE_DESCRIPTOR structure in
the UEFI specification.

| **Field** | **Size (bytes)** | **Offset (bytes)** | **Description** |
|:---|:---|----|:---|
| Resources | 0x18\* | 0x00 | Array of resource descriptors. See Resource Descriptors, below. The number of descriptors is the data_size / 0x18. If the remainder is not zero then this resource descriptor Transfer Entry is ignored. |

#### G.3.1.1. Resource Descriptor Entry

This entry describes one resource range. This matches the
EFI_RESOURCE_DESCRIPTOR structure in the UEFI Platform Initialization
specification. This structure is listed here for reference only. Please
consult the specification for the normative definition.

| **Field** | **Size (bytes)** | **Offset (bytes)** | **Description** |
|:---|:---|:---|:---|
| Resource Type | 0x01 | 0x00 | Enumerated value that specifies the platform resource type. |
| Reserved | 0x03 | 0x01 | Reserved. Must be set to zero. |
| Resource Attribute | 0x04 | 0x04 | Bitmask that specifies the attributes of the resource entry. |
| Physical Start | 0x08 | 0x08 | Physical start address of the resource region. |
| Resource Length | 0x08 | 0x10 | Number of bytes in the resource region. |

#### G.3.1.2. Resource Types

The resource type is an enumerated value that specifies the resource
region type as specified EFI_RESOURCE_TYPE_x in the UEFI Platform
Initialization specification. These values are listed here for reference
only. Please consult the specification for the normative definition.

**RESOURCE_TYPE_SYSTEM_MEMORY** (0x0000) - Memory that persists out of
the current firmware execution phase.

**RESOURCE_MEMORY_MAPPED_IO** (0x0001) - Memory-mapped I/O.

**RESOURCE_IO** (0x0002) - Processor I/O space.

**RESOURCE_FIRMWARE_DEVICE** (0x0003) - Memory-mapped firmware devices.

**RESOURCE_MEMORY_MAPPED_IO_PORT** (0x0004) - Memory that is decoded to
produce I/O cycles.

**RESOURCE_MEMORY_RESERVED** (0x0005) - Reserved memory address space.

**RESOURCE_IO_RESERVED** (0x0006) - Reserved I/O address space.

#### G.3.1.3. Resource Attributes

Bitmask that specifies the attribute of the resource region as specified
by EFI_RESOURCE_ATTRIBUTE_x in the UEFI Platform Initialization
specification. These values are listed here for reference only. Please
consult the specification for the normative definition.

The following bits may be OR’d together.

**RESOURCE_ATTRIBUTE_PRESENT** (0x00000001) - Physical memory
attribute: The memory region exists.

**RESOURCE_ATTRIBUTE_INITIALIZED** (0x00000002) - Physical memory
attribute: The memory region has been initialized.

**RESOURCE_ATTRIBUTE_TESTED** (0x00000004) - Physical memory
attribute: The memory region has been tested.

**RESOURCE_ATTRIBUTE_SINGLE_BIT_ECC** (0x00000008) - Physical memory
attribute: The memory region supports single-bit ECC.

**RESOURCE_ATTRIBUTE_MULTIPLE_BIT_ECC** (0x00000010) - Physical memory
attribute: The memory region supports multibit ECC.

**RESOURCE_ATTRIBUTE_READ_PROTECTED** (0x00000080) - Physical memory
protection attribute: The memory region is read protected.

**RESOURCE_ATTRIBUTE_WRITE_PROTECTED** (0x00000100) - Physical memory
protection attribute: The memory region is write protected.This is
typically used as memory cacheability attribute today. NOTE: Please
use **RESOURCE_ATTRIBUTE_READ_ONLY_PROTECTED** as Physical write
protected attribute, and **RESOURCE_ATTRIBUTE_WRITE_PROTECTED** means
Memory cacheability attribute: The memory supports being programmed
with a write-protected cacheable attribute.

**RESOURCE_ATTRIBUTE_EXECUTION_PROTECTED** (0x00000200) - Physical
memory protection attribute: The memory region is execution protected.

**RESOURCE_ATTRIBUTE_READ_ONLY_PROTECTED** (0x00040000) - Physical
memory protection attribute: The memory region is write protected.

**RESOURCE_ATTRIBUTE_PERSISTENT** (0x00800000) - Physical memory
persistence attribute. This memory is configured for byte-addressable
non-volatility.

**RESOURCE_ATTRIBUTE_MORE_RELIABLE** (0x02000000) - Physical memory
relative reliability attribute. This memory provides higher
reliability relative to other memory in the system. If all memory has
the same reliability, then this bit is not used.

**RESOURCE_ATTRIBUTE_UNCACHEABLE** (0x00000400) - Memory cacheability
attribute: The memory does not support caching.

**RESOURCE_ATTRIBUTE_READ_PROTECTABLE** (0x0100000) - Memory
capability attribute: The memory supports being protected from
processor reads.

**RESOURCE_ATTRIBUTE_WRITE_PROTECTABLE** (0x02000000) - Memory
capability attribute: The memory supports being protected from
processor writes.

**RESOURCE_ATTRIBUTE_EXECUTION_PROTECTABLE** (0x00400000) - Memory
capability attribute: The memory supports being protected from
processor execution.

**RESOURCE_ATTRIBUTE_READ_ONLY_PROTECTABLE** (0x00100000) - Memory
capability attribute: The memory supports being protected from
processor writes.

**RESOURCE_ATTRIBUTE_PERSISTABLE** (0x01000000) - Memory capability
attribute. This memory supports byte-addressable non-volatility.

**RESOURCE_ATTRIBUTE_WRITE_THROUGH_CACHEABLE** (0x000010000) - Memory
cacheability attribute: The memory supports being programmed with a
write-through cacheable attribute.

**RESOURCE_ATTRIBUTE_WRITE_COMBINEABLE** (0x00000800) - Memory
cacheability attribute: The memory supports a write-combining
attribute.

**RESOURCE_ATTRIBUTE_WRITE_BACK_CACHEABLE** (0x00002000) - Memory
cacheability attribute: The memory region supports being configured as
cacheable with a write-back policy. Reads and writes that hit in the
cache do not propagate to main memory. Dirty data is written back to
main memory when a new cache line is allocated.

**RESOURCE_ATTRIBUTE_16_BIT_IO** (0x00004000) - Memory physical
attribute: The memory supports 16-bit I/O.

**RESOURCE_ATTRIBUTE_32_BIT_IO** (0x00008000) - Memory physical
attribute: The memory supports 32-bit I/O.

**RESOURCE_ATTRIBUTE_64_BIT_IO** (0x00010000) - Memory physical
attribute: The memory supports 64-bit I/O.

**RESOURCE_ATTRIBUTE_UNCACHED_EXPORTED** (0x00020000) - Memory
cacheability attribute: The memory region is uncacheable and exported
and supports the fetch and add semaphore mechanism.

---

[← Appendix F](appendix-f-sc-approval-checklist.md) | [↑ Back to the specification](../open_silicon_firmware_interface_openSFI_specification.md#appendix-g---example-structures-and-enumerations-from-normative-specifications) | [Appendix H- Deprecating SoCID from the openSFI API →](appendix-h-deprecating-socid.md)
