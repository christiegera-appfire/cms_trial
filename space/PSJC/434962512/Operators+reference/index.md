# Operators reference

Simple Issue Language (SIL) provides several categories of operators for performing various operations on different data types. This page covers the main operator types, their usage, and type compatibility.

## Arithmetic operators

These are operators that perform mathematical calculations and manipulations.

| **Operator** | **Description** | **Example** |
| --- | --- | --- |
| `+` | Addition, concatenation | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `%` | Modulo (remainder) | `a % b` |

### Table 1: Basic Arithmetic Operators

| **Operator** | **LHS type** | **Valid RHS types (in order)** | **Result type** | **Description** |
| --- | --- | --- | --- | --- |
| `+` | number | number, integer | number | Standard addition of numbers |
| integer | integer, number | integer | Standard addition of integers |
| string | string | string | Adds the string representation of the RHS operand at the end of the LHS string (string concatenation) |
| boolean | Unsupported |
| date | interval | date | Adds interval to date |
| interval | interval, date | interval/date | Adds intervals or dates |
| byte | byte | byte | Standard addition of bytes |
| <type> [] | <type> | <type> [] | Adds the RHS value to the LHS array, where <type> can be any type |
| `-` | number | number, integer | number | Standard subtraction of numbers |
| integer | integer, number | integer | Standard subtraction of integers |
| string | string | string | Removes all occurrences of the RHS string in the LHS value |
| boolean | Unsupported |
| date | date, interval | interval/date | Returns the interval difference between two dates or subtracts the RHS interval from the date and returns the value. |
| interval | interval | interval | Standard interval subtraction. |
| byte | byte | byte | Standard subtraction of bytes. |
| <type>[] | <type> | <type>[] | Removes the first occurrence of the RHS value from the array; where <type> can be any type. |
| n/a | number, integer | number, integer | Returns number \* -1 |
| `*` | number | number, integer | number | Standard multiplication of numbers |
| interval | interval | Multiplies the interval by the number of times specified by the LHS operand and returns the result |
| number [] | number, integer | number [] | Multiplies each value in the LHS array with the number in the RHS operand and returns the result |
| integer | integer, number | integer | Standard multiplication of integers |
| interval | interval | Multiplies the interval by the integer of times specified by the LHS operand and returns the result |
| integer [] | integer, number | integer [] | Multiplies each value in the LHS array with the integer in the RHS operand and returns the result |
| string | Unsupported |
| boolean | Unsupported |
| date | Unsupported |
| interval | number | interval | Multiplies the interval by the number of times specified by the RHS operand and returns the result |
| byte | byte | byte | Standard multiplication of bytes |
| <type>[]  (except number) | Unsupported |
| `/` | number | number, integer | number | Standard division of numbers. |
| number [] | number, integer | number [] | Divides each value in the LHS array by the number in the RHS operand and returns the result |
| integer | integer, number | integer | Standard division of integers |
| integer [] | integer, number | integer [] | Divides each value in the LHS array by the integer in the RHS operand and returns the result |
| string | Unsupported |
| boolean | Unsupported |
| date | Unsupported |
| interval | number | interval | Divides the interval by the number specified in the RHS operand |
| byte | byte | byte | Standard division of bytes |
| <type>[] | Unsupported (except number) |
| `%` | number | number, integer | number | Standard modulo division of numbers |
| number [] | number, integer | number [] | Applies the modulo operator on each number in the LHS array with the number in the RHS operand and returns the results |
| integer | integer, number | integer | Standard modulo division of integers |
| integer [] | integer, number | integer [] | Applies the modulo operator on each number in the LHS array with the integer in the RHS operand and returns the results |
| byte | byte | byte | Standard modulo division of bytes |
| string | Unsupported |
| boolean | Unsupported |
| date | Unsupported |
| interval | Unsupported |
| <type>[] | Unsupported (except number) |
| ! | n/a | number | number | Returns number \* -1 |

---

## Combined Assignment Operators

These operators combine an arithmetic operation with the assignment operator in a single step:

- `+=` Add and assign
- `-=` Subtract and assign
- `*=` Multiply and assign
- `/=` Divide and assign

As illustrated by this example, combined assignment operators make code shorter and often clearer:

```text
// Basic Combined Assignment Operators
number x = 10;
number y = 5;
x += y    // Same as: x = x + y  (Addition) result is 15
x -= y    // Same as: x = x - y  (Subtraction) result is 5
x *= y    // Same as: x = x * y  (Multiplication) resuult is 50
x /= y    // Same as: x = x / y  (Division) result is 2

// Examples
number score = 10;
score += 5;        // score is now 15
score -= 3;        // score is now 12
score *= 2;        // score is now 24
score /= 4;        // score is now 6

// Works with strings too
string name = "Hello";
name += " World";  // name is now "Hello World"
```

---

## Increment/Decrement Operators

These operators add or subtract 1 from a numeric valuе.

- `++` Increment by 1
- `--` Decrement by 1

They come in two forms: prefix (pre) and postfix (post).

```text
// Increment (++)
++i    // Pre-increment: Adds 1 to i BEFORE using the value
i++    // Post-increment: Adds 1 to i AFTER using the value

// Decrement (--)
--i    // Pre-decrement: Subtracts 1 from i BEFORE using the value
i--    // Post-decrement: Subtracts 1 from i AFTER using the value

// Example showing the difference
integer x = 5;
integer y = ++x;   // x is 6, y is 6 (increment happens first)
integer z = x++;   // x is 7, z is 6 (increment happens after assignment)
```

---

## Comparison operators

These operators compare values and return boolean results (true/false).

### Table 2: Comparison operators reference

| **Operator** | **Alias** | **LHS Type** | **Valid RHS types** | **Explanation and usage** |
| --- | --- | --- | --- | --- |
| `==` | eq | any | same as LHS\* | Equal comparison: returns true if the values are equal and false otherwise |
| `!=` | neq | any | same as LHS\* | Not equal comparison: returns false if the values are equal and true otherwise |
| `<` | It | number/integer/string/date | same as LHS\* | Less than comparison: returns true if the first value is lower than the second one and false otherwise |
| `>` | gt | number/integer/string/date | same as LHS\* | Greater than comparison: returns true if the first value is greater than the second one and false otherwise |
| `<=` | le | number/integer/string/date | same as LHS\* | Less than or equal: returns true if the first value is lower than or equal to the second one and false otherwise |
| `>=` | ge | number/integer/string/date | same as LHS\* | Greater than or equal: returns true if the first value is greater than or equal to the second one and false otherwise |

\*RHS type will be converted to LHS type if different but compatible.

---

## Logical Operators

These are operators that perform boolean logic operations:

- `&&` (AND): Both conditions must be true
- `||` (OR): At least one condition must be true
- `!` (NOT):

  - With booleans: Inverts true/false
  - With numbers: Multiplies by -1

This example illustrates how each logical operator is used in a SIL program:

```text
// Logical AND (&&) or 'and'
boolean hasPassword = true;
boolean isAdmin = true;
if (hasPassword && isAdmin) {
    // Both conditions must be true
    // This code runs because both are true
}

// Logical OR (||) or 'or'
boolean hasCreditCard = false;
boolean hasPayPal = true;
if (hasCreditCard || hasPayPal) {
    // At least one condition must be true
    // This code runs because hasPayPal is true
}

// Logical NOT (!) or 'not'
boolean isLocked = true;
if (!isLocked) {
    // Inverts the boolean value
    // This code won't run because !true is false
}

// Combining operators
boolean hasPermission = true;
boolean isLoggedIn = true;
boolean isBanned = false;
if (hasPermission && isLoggedIn && !isBanned) {
    // All conditions must be true:
    // - hasPermission is true
    // - isLoggedIn is true
    // - !isBanned is true (because isBanned is false)
    // This code will run
}

// NOT with numbers
number x = 5;
number y = !x;    // y becomes -5 (multiplies by -1)
```

### Table 3: Logical operators reference

| **Operator** | **Alias** | **Operand Types** | **Result Type** | **Description** |
| --- | --- | --- | --- | --- |
| `&&` | and | boolean `&&` boolean | boolean | Returns true only if both operands are true. |
| `||` | or | boolean `||` boolean | boolean | Returns true if either operand is true. |
| `!` | not | boolean | boolean | Inverts boolean value. |

---

## The Ternary Operator

The ternary operator is a conditional operator that takes three operands and provides a way to write simple if-else conditions in a more concise form. It uses the following general syntax:

```text
<condition> ? <ifTrueValue> : <ifFalseValue>
```

### Table 4: The Ternary operator reference

| **Operator** | **Operand types** | **Result type** | **Description** |
| --- | --- | --- | --- |
| `?:` | Takes three operands:   - A condition which must evaluate to boolean. - <type> A value if true. - <type> A value if false.   Both return values must be of the same type. | <type>  Returns a single value based on the condition. | If <condition> is true, returns <ifTrueValue>, otherwise returns <ifFalseValue>.  Note that <ifTrueValue> and <ifFalseValue> must have the same type.  **Example:**  ```text // Basic usage boolean isValid = true; string result = isValid ? "Valid" : "Invalid"; // If isValid is true, result = "Valid" // If isValid is false, result = "Invalid" ``` |

---

## The Indexing Operator

The indexing operator in SIL provides flexible access to elements in arrays, maps, structures, and special types. It supports numeric indexing and string-based key access.

### Table 5: Indexing operator basic usage patterns

| **Usage Type** | **Syntax** | **Return Type** | **Description** |
| --- | --- | --- | --- |
| Array access | `array[integer]`  `array[number]` | element type | Gets or sets element at numeric index. Similar to the `arrayGetElement` function. If index is out of bounds, it will return an empty value. |
| Map access | `array[string]` | element type | Gets or sets element using string key. Lets you create key-value lists (maps) and retrieve values from them using a string inside the operator (instead of a number). |
| String indexing | `string[integer]`  `string[number]` | string | Gets or sets individual characters in a string. |
| Date field access | date[string] | depends on the element | See [Table 6: Indexing operator reference for date and interval](/cms_trial/space/PSJC/434962512/Operators+reference/) section below. |
| Interval field access | interval[string] | integer | See [Table 6: Indexing operator reference for date and interval](/cms_trial/space/PSJC/434962512/Operators+reference/) section below. |
| Structure field access | struct\_instance[integer]  struct\_instance[number] | depends on the field | See [Using the indexing operator on a structure](/cms_trial/space/PSJC/434962512/Operators+reference/) section below |

### Array Access

#### Example

```text
//Basic array operations
string[] arr = {"a", "b", "c"};     // Create array with three elements
string contents = arr[0] + arr[1] + arr[2] + arr[3];
string first = arr[0];              // Gets "a" (first element)
arr[3] = "d";                       // Adds "d" as a new fourth element
arr[1] = "x";                       // Changes second element to "x"
string empty = arr[5];              // Returns empty (safe out-of-bounds)
```

### Map Access

#### Examples

```text
// Key-value operations
number [] map;          // Declare an array 'map' that will hold numbers
map["one"] = 1;         // Associate the number 1 with the key "one". First element added to array.
map["two"] = 2;         // Associate the number 2 with the key "two". Second element added to array.
runnerLog(map["one"]);      // Retrieve the value associated with key "one", will print 1

// When printing the entire array or using it in a for-loop, 
// only the values (1 and 2) are accessible, not the keys ("one" and "two").
runnerLog(map);             // Will print 1|2
```

When accessing a map as a list, the contents are retrieved in the order they were added. You can access any value in two ways:

- Using the string key you assigned.
- Using the numeric position based on the order it was added.

As illustrated in this example, you can use the indexing operator with an integer value, even on maps.

```text
date [] days;                              // Declare an array 'days' that will hold dates

// Store yesterday's date using the key "yesterday". 
days["yesterday"] = currentDate() - "1d";  // Now this is position [0] (first element in array) 

// Store today's date using the key "today"
days["today"] = currentDate();             // Now this is position [1] (second element in array)

// Store tomorrow's date using the key "tomorrow"
days["tomorrow"] = currentDate() + "1d";   // Now this is position [2] (third element in array)


// Both return the same value because "today" was added second (position element 1)

if(days["today"] == days[1]){
    runnerLog("Today is the second element in the array"); // This will print, both ways access the same value
}

if(days["today"] == days[0]){                          // This won't print, string ["today"] is position [1]
    runnerLog("This won't print");
}
```

### Indexing in special types

The indexing operator can be used with certain simple types (not arrays) to access specific components or parts of the value. For strings, it lets you get or modify individual characters at a specific position, while for dates and intervals, it provides access to various time-related components using predefined string keys.

#### String indexing

String indexing supports both reading and writing operations. It can get and set individual characters using numeric values. The return type is always string.

```text
string text = "Hello";
string firstChar = text[0];    // Gets "H"
text[4] = "a";                 // Changes "Hello" to "Hella"
```

#### Date and interval component access

Date and interval indexing are read-only operations. This means that you cannot modify (set) components using the indexing operator; you can only read (get) values.

### Table 6: Indexing operator reference for date and interval

| **SIL type** | **Index Value** | **Example** | **Description** | **Return Type** |
| --- | --- | --- | --- | --- |
| **date** | "DAY" | `date["DAY"]` | Gets the day of the month (1-31) from the date. | integer |
| "MONTH" | `date["MONTH"]` | Gets the month number (1-12) from the date. | integer |
| "YEAR" | `date["YEAR"]` | Gets the full year from the date. | integer |
| "HOUR" | `date["HOUR"]` | Gets the hour (0-23) from the date. | integer |
| "MINUTE" | `date["MINUTE"]` | Gets the minute (0-59) from the date. | integer |
| "SECOND" | `date["SECOND"]` | Gets the seconds (0-59) from the date. | integer |
| "MILLISECOND" | `date["MILLISECOND"]` | Gets the milliseconds (0-999) from the date. | integer |
| "WEEK" | `date["WEEK"]` | Gets the week number within the current year. | integer |
| "WEEKINMONTH" | `date["WEEKINMONTH"]` | Gets the week number within the current month. | integer |
| "TOMILLIS" | `date["TOMILLIS"]` | Gets the current time as UTC milliseconds from the epoch. | integer |
| "DAYOFWEEK" | `date["DAYOFWEEK"]` | Gets the three-letter format for the day of the week (e.g. "Mon", "Tue", "Wed", etc.) | string |
| "MONTHNAME" | `date["MONTHNAME"]` | Gets the three-letter format for the name of the month (e.g. "Jan", "Feb", "Mar", etc.) | string |
| **interval** | "WEEK" | `"1w 14d"["WEEK"]` | Gets the number of whole weeks inside the interval. Example returns 3, because 1 week + 14 days = 21 days = 3 complete weeks. | integer |
| "DAY" | `"1d 48h"["DAY"]` | Gets the number of whole days inside the interval. Interval example returns 3, because 1 day + 48 hours = 1 day + 2 days = 3 complete days. | integer |
| "HOUR" | `"1h 120m"["HOUR"]` | Gets the number of whole hours inside the interval. Interval example returns 3, because 1 hour + 120 minutes = 1 hour + 2 hours = 3 complete hours. | integer |
| "MINUTE" | `"1m 120s"["MINUTE"]` | Gets the number of whole minutes inside the interval. Interval example returns 3, because 1 minute + 120 seconds = 1 minute + 2 minutes = 3 complete minutes. | integer |
| "SECOND" | `"1h 1m 3s"["SECOND"]` | Gets the number of seconds inside the interval. Interval example returns 3, because it’s looking only at the seconds component, which is 3. | integer |
| "TOMILLIS" | `"1s"["TOMILLIS"]` | Gets the number of milliseconds inside the interval. Interval example returns 1000, because it converts seconds to milliseconds (1 second = 1000 milliseconds). | integer |

---

## Using the indexing operator on a structure

It is possible to use the indexing operator on a structure. In this case, it acts by returning the value, with its type, found in the position you specify.

The indexing operator `[]` can be used on structures to access fields by their position number, starting from 0. While using the dot notation (e.g., `structure.fieldName`) is the preferred approach, you can also access each field by its position using `[]`, which returns both the value and its type.

```text
struct Person {
    string name;      // position 0
    int age;         // position 1
    string address;  // position 2
}

Person p = {"Alice Smith", 25, "123 Main Street"};

// While p.name and p.address are preferred, you can use indexing:
string name = p[0];    // returns: "Alice Smith"
string addr = p[2];    // returns: "123 Main Street"

// Multiple values can be accessed:
return p[1], p[2];   // returns: 25, "123 Main Street"See also
```

---

## Learn more

- [Syntax and types introduction](/cms_trial/space/PSJC/435028043/Syntax+and+types+introduction/)
- [Variable types and reference methods](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/)
- [Statements](/cms_trial/space/PSJC/434472559/Statements/)