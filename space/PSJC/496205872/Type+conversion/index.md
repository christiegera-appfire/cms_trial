# Type conversion

This page covers automatic type conversion rules and behavior in Simple Issue Language (SIL™), distinct from [explicit type casting](/cms_trial/space/PSJC/435028043/Syntax+and+types+introduction/).

## Type conversion rules

Type conversion in SIL allows variables of different types to be automatically converted when using the assignment (=) operator. Type conversion occurs when you assign a value of one type to a variable of another type. The system tries to convert the source value into a format that matches the target type while preserving the semantic meaning of the data.

To ensure correct conversion, improve code clarity and prevent unexpected behavior, make sure to:

- Use appropriate types from the start.
- Use the SIL manager to verify conversion behavior with different input types.
- For complex cases, use explicit conversions instead of relying on the automatic conversion functionality.
- Implement proper error handling for conversion failures. This includes providing meaningful error messages.
- Use consistent formatting in all your scripts.

## Basic type conversion matrix

The table below shows all possible conversions between types:

| **Target type ↓** | **Source type →** | **Notes and examples** |
| --- | --- | --- |
| `string`**\*** | `number` | `integer` | `boolean` | `byte` | `date` | `interval` |
| `string` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Universal conversion target. |
| `number` | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | - `"1" → 1.0` - `1 → 1.0` - Strings must contain valid numeric values. |
| `integer` | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | - `"2" → 2` - `2.5 → 2` - Numbers are truncated, not rounded. |
| `byte` | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | - `"123" → 123` - `123.7 → 123` - `-200 → 56` |
| `boolean` | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | - `"true" → true` - `1 → true` - `0 → false` - Non-zero numbers convert to `true`. |
| `date` | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | - `"2024-01-01" → 2024-01-01` - `1704067200000 → 2024-01-01` - When converting a number to a date, the number is interpreted as milliseconds passed since the Unix epoch. |
| `interval` | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | - `"1h" → interval` - `3600000 → "1h"` - `"60m" → "1h"` - When converting a number to an interval, the number is interpreted as a duration in milliseconds. This represents a time span rather than a specific point in time. |

\*The conversion from a string to a target type is done by parsing the string as a text representation of the target type.

### Conversion examples

```text
// Number conversion examples
number n1 = "42";     // String to number: 42.0
number n2 = 42;       // Integer to number: 42.0

// Integer conversion examples
integer i1 = "123";   // String to integer: 123
integer i2 = 123.7;   // Number to integer: 123 (truncated)

// Boolean conversion examples
boolean b1 = "true";  // String to boolean: true
boolean b2 = 1;       // Number to boolean: true
boolean b3 = 0;       // Number to boolean: false

//Byte conversion examples
byte b1 = (byte) "123";    // String to byte: 123 (if within byte range -128 to 127)
byte b2 = (byte) "-128";   // String to byte: 56 (minimum byte value)
byte b3 = (byte) 123.7;    // Number to byte: 123 (decimal part truncated)
byte b4 = (byte) -5.9;     // Number to byte: -5 (decimal part truncated)
byte b5 = (byte) 200;      // Integer to byte: -56 (wraps around from 200 to -56)
byte b6 = (byte) -200;     // Integer to byte: 56 (wraps around from -200 to 56)

// Date conversion examples
date d1 = "2024-01-01";        // String to date
date d2 = 1704067200000;       // Milliseconds to date

// Interval conversion examples
interval iv1 = "1h 30m";       // String to interval
interval iv2 = 5400000;        // Milliseconds to interval
```

Casting a `string` to an `array` is a two-step process:

- First, the `string`s transformed to a `string[]` by splitting it at every character with a `|`.
- The conversion is done from string[] to the target `array` type.

---

## Advanced type conversions

### Array conversion rules

Array conversion is possible if the following conditions are met:

- The element types (inner type of the array) are convertible.
- The conversion rules for array elements follow the same rules as single-value conversions explained earlier on this page.
- All elements in the source array must be convertible to the target type.

#### Examples

You can cast a `number[]` to a `string[]` because `number` is convertible to `string` (Example 1). However, you cannot convert a `date[]` to an `interval[]` because `date` cannot be converted to `interval` (Example 2).

```text
// Example 1: Number Array to String Array (Valid)
number[] numbers = [1, 2.5, 3.7, -4.2];
string[] stringNumbers = numbers;    // Valid conversion
// Result: ["1", "2.5", "3.7", "-4.2"]

// Example 2: Date Array to Interval Array (Invalid)
date[] dates = [
    "2024-01-01",
    "2024-01-02",
    "2024-01-03"
];
// interval[] periods = dates;    // This would cause a conversion error
                                 // Error: Cannot convert date to interval
```

### String-to-array type conversion rules

When converting a string to an array, the process happens in two steps:

|  |  |  |
| --- | --- | --- |
| **Step 1:** | `string → string[]` and split on "|" | The string is first transformed to a `string[]` by splitting it at every "|" character. |
| **Step 2:** | `string[] → target_type[]` | The conversion is done from `string[]` to the target type array. |

#### Examples

```text
// Step 1: "1|2|3" → ["1", "2", "3"]
// Step 2: ["1", "2", "3"] → [1, 2, 3]

// Basic number array conversion
string numericString = "1|2|3|4|5";
number[] numbers = numericString;
// Result: [1.0, 2.0, 3.0, 4.0, 5.0]

// Basic boolean array conversion
string boolString = "true|false|true|true";
boolean[] flags = boolString;
// Result: [true, false, true, true]
```

---

## Structure conversion rules

Structures can only be converted directly to string or arraytypes. It can be possible for certain structures to be convertible to other types by using one or more intermediate types.

### Structure-to-string conversion

Conversions of this type follow these rules:

- All fields are first converted to strings.
- Fields are joined with commas.

Casting a `structure` to a `string` is equivalent to casting to a `string[]`, and then the resulting `array` to `string`.

```text
// Define a simple structure
struct Person {
    string name;
    integer age;
    boolean isActive;
}

// Create and convert instance
Person person = { "John Smith", 30, true};

// Direct conversion to string
string personString = person;
return personString;
// Result: John Smith|30|true
```

### Structure-to-array conversion

Conversions of this type follow these rules:

- All structure fields must be convertible to the array's element type.
- Fields are converted in order of declaration.

```text
// Structure with all number fields
struct Point3D {
    number x;
    number y;
    number z;
}

Point3D point = { 1.5, 2.0, 3.5 };

// Convert to number array (valid because all fields are numbers)
number[] coordinates = point;
// Result: [1.5, 2.0, 3.5]

// Convert to string array (always valid as all types can convert to string)
string[] stringCoords = point;
return stringCoords;
// Result: 1.5|2|3.5
```

---

## Complex conversions

Complex conversions (to types other than string/array) require:

- Explicit intermediate steps
- Manual casting between types
- Fields that can ultimately convert to target type

Common complex conversion patterns include:

- Structure → string → target type
- Structure → array → target type

In this example, a structure containing a single number field can be converted to a number by first casting it to a string and then the resulting string to a number.

```text
// Simple structure with a single numeric value
struct Temperature {
    number value;
}

// Create instance
Temperature temp = { 25.5 };

// GOAL: Convert the structure to a number

// Invalid: Direct conversion
// number n = temp;    // Error: Cannot convert structure to number

// Valid: Multi-step conversion
string tempStr = temp;           // Step 1: Structure to string ("25.5")
number tempValue = tempStr;      // Step 2: String to number (25.5)

// Alternative using array
string[] tempArray = temp;       // Step 1: Structure to string array (["25.5"])
number tempValue2 = tempArray[0];// Step 2: First array element to number (25.5)

// Using explicit casts (more verbose but clearer)
number explicitValue = (number)((string)temp);
```

---

## Parameter type conversion

When calling functions (functions or UDFs), parameters are automatically converted to match the function’s expected parameter types, following the standard type conversion rules.

```text
function f(string s){
    print(s);
}
f(2); //number automatically converted to string
f(true); // boolean automatically converted to string
```