# Syntax and types introduction

This page provides an overview of the basic elements of the Simple Issue Language (SIL™) scripting syntax.

SIL is a scripting language specifically designed for Jira. It follows common programming language conventions but is tailored to work with Jira issues and workflows. SIL is the underlying scripting language of Power Scripts, Power Actions, and other apps. It is easy to learn and work with.

## Basic syntax rules

- Every instruction must end with a semicolon `;`
- Comments can be written in two ways:

  ```text
  // For single line comments
  /* For multi-line 
     comments */
  ```

## Data types

Data types are templates or definitions that tell the system what kind of data can be stored. SIL uses several categories of data types.

### Basic data types

| **Type** | **Use for** |
| --- | --- |
| `string` | text values like `hello` |
| `boolean` | true/false values |
| `number` | any numeric value |
| `integer` | whole numbers without decimals |
| `byte` | for byte values |
| `date` | for dates like `2024-10-24` |
| `interval` | for time periods like `2d 3h` (two days and three hours) |

### Complex data types

#### Arrays

Arrays are created by adding `[]` after any basic type. The following list represents valid arrays:

- `string[]` one-dimensional array of strings
- `boolean[` one-dimensional array of booleans
- `number[][]` two-dimensional array of numbers
- `integer[]` one-dimensional array of integers
- `date[][][]` three-dimensional array of dates
- `interval[]` one-dimensional array of intervals

You can also create arrays for a user-defined structure:

- `Person[][]` two-dimensional array of (Person) structures

#### Key-value arrays

Arrays in SIL act as maps where list positions serve as keys. Key-value arrays (or maps) are declared like regular arrays.

Learn more about using the [indexing operator](/cms_trial/space/PSJC/434962512/Operators+reference/) to create key-value maps and retrieve values from them.

### Structures

Structures are user-defined data types. A structure in SIL is like a container that can hold different types of data together. The syntax for defining a structure is:

```text
struct StructureName {
    type1 field1;
    type2 field2;
    // ... more fields
}
```

The type of each field can be a basic data type, a user-defined structure, a self-referential structure, or arrays of these types. The following examples show how to define a structure with each type:

```text
struct Address {
    string street;
    string city;
    string zipCode;         //Basic data types in structure
}

struct Employee {
    string id;
    string name;
    Address workAddress;    // Structure inside structure
    Address homeAddress;    // Can use same type multiple times
}
struct Department {
    string name;
    Department parent;            // A Department can reference itself
    Department[] subDepartments;  // Can have array of same type
}
```

**Best practices when creating structures:**

- Use meaningful field names.
- Group related fields together.
- Consider the logical hierarchy of your data.

Once you've defined a structure, you can create variables of that structure type and work with them in two ways:

- You can create a structure variable and set each field individually. Here is an example of field-by-field initialization:

```text
Employee emp;                           // Create structure variable
emp.id = "E123";                        // Set individual fields
emp.name = "John Doe";
emp.workAddress.street = "123 Work St"; // Access nested structure fields
emp.workAddress.city = "Work City";
```

- Alternatively, you can do a one-line initialization, including nested initialization. Here’s an example of one-line initialization:

```text
struct Point {
    integer x;
    integer y;
}

Point p = {10, 20};  // Initialize all fields at once

struct PersonInfo {
    string name;
    number salary;
    Point location;
}

PersonInfo person = {"John Doe", 50000.00, {10, 20}};  // Nested initialization
```

To access the value of a field from a variable in a structure, use the following syntax:

```text
<varName>.<fieldName>

//Example:
print(emp.name);                    // Access name field
```

---

## Literals

Literals are fixed values that appear directly in the code. In SIL, literals are used to represent constant values of different data types.

Literals refer to the constant values used in scripts, NOT [the use of a constant](/cms_trial/space/PSJC/435028043/Syntax+and+types+introduction/), which is the read-only attribute of variables.

| **Type** | **Example** |
| --- | --- |
| **Basic type literals** | ```text // Integer literals integer a = 42; integer b = -17;  // Number (floating point) literals number pi = 3.14; number temperature = -40.5;  // Boolean literals boolean isTrue = true; boolean isFalse = false;  // Bytes require explicit casting byte b1 = (byte) 20; byte b2 = (byte) 255;  // maximum byte value ``` |
| **String, date, and interval literals** | These types require double quotes (" ").  ```text // String literals string name = "John Doe"; string empty = "";  // empty string  // Date literals // Full format: "yyyy-MM-ddTHH:mm:ss.SSSZ" date fullDate = "2010-12-31T24:59:59.999Z";  // with milliseconds and UTC date withZone = "2010-12-31T22:59:59+0200";  // with timezone (UTC+2) date simpleDate = "2010-12-31";              // just date  // Interval literals // Format: combines w(weeks) d(days) h(hours) m(minutes) interval oneDay = "1d"; interval complex = "1w 2d 3h 4m";  // 1 week, 2 days, 3 hours, 4 minutes interval justHours = "8h"; ``` |
| **Array literals** | Arrays use curly braces and commas:  ```text {<value1>, <value2>, ..., <value3>} ```  ```text // One-dimensional arrays string[] names = {"this", "is", "a", "string", "array"};    number[] scores = {95.5, 87.0, 91.5};                                                                              boolean[] flags = {true, false, true};  // Multi-dimensional arrays number[][] matrix = {     {1, 2, 3},     {4, 5, 6},     {7, 8, 9} };  // Array of intervals interval[] durations = {"1d", "2h", "30m"}; ```  Constant representation of key-value arrays is not supported. You can build one using the [indexing operator](/cms_trial/space/PSJC/434962512/Operators+reference/). |
| **Special literals** | You can use `null` or `nil` to unset variables.  The `null` and `nil` values were introduced in SIL version 5.8.0.0.  ```text number n = 0; ..... n = uninitialized; // not recommended n = null;          // or:   n = nil;           // alternative syntax ``` |

---

## Variables

Variables are named containers that use the data types. They are like labeled boxes that can hold specific values.

```text
// Variable format: <data type> <variable name>

// Variable declaration:
string name;    // A container that can hold text
number pi;         // A container that can hold decimal numbers

//You can also have an array of the type of variable#
{ variable1, variable2, variable3 }.    // where variable# can also be an array
```

You can create an array from variables as illustrated in the following example:

```text
// First, declare some variables
string name1 = "John";
string name2 = "Jane";
string name3 = "Bob";

// Create an array from these variables
string[] names = {name1, name2, name3};
// Result: names = {"John", "Jane", "Bob"}
```

You can also create array variables:

```text
// First, declare some array variables
string[] teamA = {"John", "Jane"};
string[] teamB = {"Bob", "Alice"};
string[] teamC = {"Charlie", "David"};

// Create an array of arrays from these variables
string[][] allTeams = {teamA, teamB, teamC};
// Result: allTeams = {
//     {"John", "Jane"},
//     {"Bob", "Alice"},
//     {"Charlie", "David"}
// }
```

### Variable declaration and initialization

To give a value to your variables, you initialize them either when you declare them or later.

```text
string employeeName;               // Just declaring
employeeName = "John";             // Initializing after declaration

string employeeAge = 25;           // Declare and initialize at once

// More examples of variable declaration
integer random = 2;
number pi = 3.14;
boolean valid;
date today = currentDate();
interval spent = "1h 30m";
interval estimate = "2d" - spent;
number [][] matrix = {{0,1}, {2,3}, {4,5}};
```

### Constants

Variables can be made read-only by adding the keyword `const` before the data type when the variable is first defined.

```text
const string COMMA = ",";
const number PI = 3.14;
```

If set to an array or structure, the read-only attribute is applied to all the elements of the array or all fields of the structure.

---

## Explicit type casting

When types are compatible, SIL [automatically converts](/cms_trial/space/PSJC/496205872/Type+conversion/) one type to another. Automatic conversion can lead to ambiguous results. If you want to tell SIL how to convert a type, use explicit type casting with the following syntax:

```text
(<target_type>)varname
```

 The following example illustrates how explicit type casting returns accurate results:

```text
integer n = 1;
number x = 3.14;
string s = "2";

//Ambiguous - could mean different things:
return n + s; // SIL doesn't know if you want "12" or 3

//Explicit - clearn intentions:
return (string)n + s; // Forces n to be treated as string "1" - clearly wants a string "12"
return n + (number)s; // Forces s to be treated as number 2 - clearly wants a number (3)
```

Not all type casts are valid. Converting an interval to a date or a date to a string is an example of invalid type casting.

---

## User-defined functions

SIL comes with many built-in functions. In addition, you can define local functions, referred to as user-defined functions (UFRs). To define and declare a function, use this general syntax:

```text
function <name>(<type> param1, <type> param2, ...) {
   Instruction1;
   ...
   InstructionN;
   return <value>;
}
```

For additional details, see the [User-defined functions (UDFs)](/cms_trial/space/PSJC/433000514/User-defined+functions+(UDRs)/) topic.