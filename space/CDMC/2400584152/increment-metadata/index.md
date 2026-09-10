# increment-metadata

## Overview

The increment-metadata trigger action lets you automatically increase numeric metadata values, making it easier to manage custom versioning and other automated numbering needs.

The metadata can be defined as:

- **Simple integer**  
  A single numeric value (for example, `1`).
- **Composite number**  
  A value with up to three numeric elements, separated by dots (`.`).

  - Examples: `1.0`, `1.0.0`
- **Composite number with a suffix**  
  A value with up to three numeric elements followed by an optional suffix, separated by a hyphen (`-`).

  - Example: `1.0.0-BETA`
- The increment can be:

  - Explicitly specified, or
  - Defaulted to a simple increase of the last element in the value.

![Comala incrementmetadata trigger action configuration](/cms_trial/assets/23cc17fd-f984-4e71-bbbe-55807e1cd9a3.png)

- Only the dot (`.`) and hyphen (`-`) characters are supported as non-numeric separators.
- Composite numbers are limited to three numeric elements (e.g., `1.2.3.4` is not supported).
- Non-numeric elements (other than hyphenated suffixes) are not supported.

### **Example use cases:**

- Incrementing a metadata field for a **simple version number** (for example, `VERSIONNUMBER`)
- Managing **composite versioning schemes** (for example, `MAJOR.MINOR` or `MAJOR.MINOR.PATCH`)
- When a higher-order element is incremented, all lower-order elements are reset to `0`.

  - For example, incrementing `1.1.4` with the expression `1.0.0` results in `2.0.0`.

### **Limitations**

- Metadata values cannot contain more than three numeric elements (e.g., `1.2.3.4` is not supported).
- Non-numeric elements cannot be incremented.

**Example:**

```none
  "actions": [
      {
        "action": "increment-metadata",
        "name": "my-version"
      },
      {
        "action": "increment-metadata",
        "name": "semver",
        "increment": "1.0.0-BETA"
      }
    ]
```

## Parameters

| **Parameter** | **Required** | **Default** | **Notes** |
| --- | --- | --- | --- |
| metadata name | ✅ | *none* | The metadata item. The metadata item value is numeric and can be:   - simple (for example, whole number) - composite (for example, 2.1 or 2.1.1)   A suffix may be used after the last numeric element, e.g., 2.1.1-BETA. This can be any set of characters (including letters, symbols, and numbers). |
| `increment` |  | *increment last numeric element by 1* | The increment expression, if specified, is a numeric expression to increment element(s) of the numeric value.  If no increment value is specified, the last numeric element of the current metadata value is incremented by 1.  The expression can be:   - a simple integer number (for example, `2`) - composite number (for example, `1.2`  or `1.2.3`)   A composite number cannot have more than 3 numeric elements; for example, 1.2.3.4 is not supported.  When defining the increment expression, the format **MUST** match the metadata item value format, including any separators and suffix identifiers.   - Increment or a change for non-numeric elements is not supported. - Incrementing a single higher-order element of a composite numeric value will reset any lower-order elements to zero. For example, a metadata value of 1.2.3 with an increment expression of 1.0.0 will update the value to 2.0.0. |

## Increment Expression examples

- **Higher-order increments**  
  If the expression increments only a higher-order element of a composite numeric value, all lower-order elements are reset to `0`.

  - Example: Incrementing `1.1.4` with `1.0.0` results in `2.0.0`.
- **Format requirements**  
  The format of the increment expression, including separators and any suffix identifier, must exactly match the format of the metadata value being incremented.

| Metadata Value | Increment Expression | Resulting Value |
| --- | --- | --- |
| `1` | *(empty)* | `2` |
| `1.0` | *(empty)* | `1.1` |
| `3.5.1` | *(empty)* | `3.5.2` |
| `3.5.1` | `0.0.1` | `3.5.2` |
| `3.5.1` | `0.2.0` | `3.7.0` |
| `3.5.1` | `1.0.0` | `4.0.0` |
| `3.5.1-BETA` | `1.0.0-BETA` | `4.0.0-BETA` |
| `1-2-3` | `0-0-1` | `1-2-4` |
| `1-2-3` | `0.0.1` | **Invalid** |
| `1.2.3-BETA` | `0.0.1` | **Invalid** |
| `1.2.3.4` | *(any)* | **Invalid** |