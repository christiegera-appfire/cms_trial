# User-defined functions (UDRs)

This page explains how to create and use user-defined functions (UDFs) in Simple Issue Language (SIL) programs to organize code into reusable components.

You can create and use user-defined functions in your SIL programs to encapsulate reusable logic. They help improve code organization, readability, and maintainability by breaking complex operations into smaller, manageable pieces.

## Syntax and basic usage

A function is defined using the following syntax:

```java
function <name>(<type> param1, <type> param2, ...) {
    Instruction1;
    ...
    InstructionN;
    return <value>;
}
```

When creating a function, keep in mind the following key points:

- The `<name>` of the function cannot contain spaces, and it cannot start with a number.
- Parameters can be any valid SIL type.
- The `return` statement is optional.

### Example

This example function calculates issue priority based on severity and environment. It uses conditional logic to demonstrate parameter passing.

```text
function calculatePriority(string severity, string environment) {
    if (severity == "Critical" && environment == "Production") {
        return "Highest";
    } else if (severity == "Critical" && environment == "Development") {
        return "High";
    } else if (severity == "Major" && environment == "Production") {
        return "High";
    } else {
        return "Medium";
    }
}

// Usage examples:
string newPriority = calculatePriority("Critical", "Production");  // Returns "Highest"
```

#### Description

The function `calculatePriority("Critical", "Production")` receives `"Critical"` and `"Production"` as inputs and checks the first condition against an actual Jira issue. If the condition is met, it changes the priority of the Jira issue to **Highest**. If the condition is not met, the function continues by checking the next condition and so on.

This function can be reused throughout your SIL program whenever you need to calculate priority based on severity and environment; for example, when issues are created, when priority or environment fields are updated, as part of validation rules, or in bulk update operations.

---

## Function definition

SIL has a strict rule about where function definitions can appear in your code. This rule helps ensure that all functions are available when needed and prevents potential issues with code organization and variable scoping.

All functions must be defined before any executable code.

The correct order must be:

1. Global variable declarations (with initialization if needed) and any constant declarations.
2. Function definitions
3. Executable code

#### Invalid definition example

```text
// This is INVALID:
number i;                 // Variable declaration
const number pi = 3.14;   // Constant declaration
i = 0;                    // Error line, this is code execution - NOT ALLOWED HERE
function circleArea(number r) {
    return r * r * pi;
}
```

The error occurs because you can't have executable code (like `i = 0;` where `i` is initialized to a constant) before function definitions.

#### Valid definition example

```text
// This is VALID:
number i = 0;            // Global variable declaration with initialization
const number pi = 3.14;  // Constant declaration

// Functions must be defined after declarations but before executable code
function circleArea(number r) {
    return (i + r) * (i + r) * pi;
}

// Executable code comes after all function definitions
number r = 10;
runnerLog("Area of radius " + r + " is " + circleArea(r));       //returns Area of radius 10 is 314
i++;
runnerLog("Area of radius " + (r + i) + " is " + circleArea(r));  // returns Area of radius 11 is 379.94
```

Running the above code in SIL Manager returns the following (in the Editor console):

![The screenshot shows the results in the Editor console after the code is executed.](/cms_trial/assets/b6c765c2-5cec-45a9-888a-2e9b1de56442.png)

---

## Parameters definition

Here’s what you need to know about parameters definition in a function:

- Parameters can be of any valid SIL type (string, number, boolean, etc.)
- Parameters are passed by value; changes inside the function don't affect the original variables.
- The parameter list can be of any length; it can be empty.

#### Examples

This example illustrates how different parameter types are defined and used in a function.

```text
// Function with no parameters
function zero() {
    return 0;
}

// Function showing different parameter types
function processData(
    string name,           // Single string parameter
    number age,            // Single number parameter
    number[] scores,       // Array of numbers
    boolean isActive,      // Boolean parameter
    string[] comments      // Array of strings
) {
    // Using the parameters
    runnerLog("Processing data for: " + name);
    runnerLog("Age: " + age);
    runnerLog("First score: " + scores[0]);
    runnerLog("Status: " + isActive);
    runnerLog("First comment: " + comments[0]);
}

// Example usage:
string studentName = "John";
number studentAge = 20;
number[] testScores = {95, 87, 92};
boolean active = true;
string[] feedback = {"Good work", "Needs improvement"};

processData(studentName, studentAge, testScores, active, feedback);
```

Running the example usage code in the SIL Manager returns the following result:

Processing data for: John  
Age: 20  
First score: 95  
Status: true  
First comment: Good work  
DONE!

### Pass-by-value behavior

Parameters in UDFs are passed by value in the following way:

- A copy of the value is passed to the function.
- Changes to the parameter inside the function don't affect the original variable.
- The original variable keeps its value after the function exits.
- Pass-by-value behavior is the same for all SIL basic types, arrays, and structs.

#### Example

This example demonstrates pass-by-value behavior for a UDF that takes a number parameter and adds 10 to it.

```text
function updateScore(number score) {
    // Because of pass-by-value, 'score' is a local copy
    score = score + 10;                // Any changes to score parameter won't affect the original value
    runnerLog("Inside function, score is: " + score);
    return score;
}

// Test the function
number testScore = 75;       //testScore variable created and set to 75
runnerLog("Before function call: " + testScore); //shows 75

number newScore = updateScore(testScore);

runnerLog("After function call:");
runnerLog("Original score: " + testScore);   // Still 75 - unchanged
runnerLog("New score: " + newScore);         // 85 - returned value
```

If run in the SIL Manager, the function returns the following result:

Before function call: 75  
Inside function, score is: 85  
After function call:  
Original score: 75  
New score: 85  
DONE!

#### Example description

- First, the function gets a copy of the `testScore = 75` value to work with.
- Inside the function, it adds 10 to that copy, making it 85. The function prints this value: "Inside function, score is: 85"
- After the function exits, both the original score (75) and the modified score (85) are printed.

### Constant parameters

Parameters of UDFs can be made read-only by using the `const` keyword within the function.

#### Example

```text
function f(const string s) {
	...
}
```

### Default parameters

Parameters can have default values. The default value is used only when you don't provide a value for that parameter when calling the function. When you provide a value, it overrides the default.

Parameters with default values must appear after parameters without defaults.

#### Example

```text
// Function with a default parameter - 'name' will use "Guest" if no value is provided
function greet(string name = "Guest") {
    runnerLog("Hello, " + name);
}

// You can call this function two ways:

// 1. Without providing a parameter - will use the default "Guest"
greet();                  // Outputs: "Hello, Guest"

// 2. Providing a value - will use your provided value instead of default
greet("John");           // Outputs: "Hello, John"
```

---

## Variable visibility in UDFs

When writing UDFs, you can work with three different categories of variables:

- Local variables that you create inside the function
- Parameter variables that you pass into the function
- Global variables that are available throughout your program

Understanding how and when you can use each category of variable helps you write more effective and maintainable code.

| **Variable category** | **Definition** | **Example** |
| --- | --- | --- |
| Local | These are variables you create inside your UDF. They:   - Only exist inside that specific UDF. - Are created when the UDF starts running. - Can only be used within that UDF. - Are removed when the UDF finishes running. | ```text function calculateTotal() {     number price = 100;        // Local variable     number tax = price * 0.1;  // Another local variable     return price + tax; } // price and tax no longer exist after this point ``` |
| Parameter | These are variables that get passed into your UDF in the list of parameters. Important characteristics:   - Use the "pass-by-value" policy. - Changes to parameters inside the body of the UDF don’t affect the original value. - Original values are preserved after the UDF exits. | ```text function adjustPrice(number price) {     price = price + 10;    // Only changes the copy inside the UDF     return price; }  number itemPrice = 50; number newPrice = adjustPrice(itemPrice); print(itemPrice);    // Still shows 50 print(newPrice);     // Shows 60 ``` |
| Global | Variables that are already defined and can be used immediately (including in the UDF body); they are accessible throughout the entire program and you don’t have to declare them. These include:   - Variables defined outside any UDF. - Standard issue fields (e.g., `key`, `summary`, `description`) - Custom fields | ```text number totalItems = 0;    // Global variable  function updateInventory() {     totalItems = totalItems + 1;     // Uses global variable     print("Issue: " + key);          // Uses standard issue field } ```  The `key` variable is a standard issue field that you can use anywhere in your SIL program without having to declare it. |

### Best practices for using variables in UDFs

- Keep in mind that local variables have the most limited access (just within the `{` and `}` of your UDF, while global variables have the widest access.
- Minimize the use of global variables to reduce code complexity.
- Use meaningful parameter names to improve code readability.
- Document any global variables used within UDFs.
- Consider passing needed values as parameters rather than relying on their global state.

## Return value

When a UDF finishes running, it can send a value back to where it was called from. You can also use `return` to stop the UDF from running further. This way, return values serve two purposes:

- They provide a way to send results back to the code that called the UDF (like returning a calculation result).
- They allow you to exit the UDF at any point (for example, stop early if an error is found).

#### Examples

This example returns a boolean result:

```text
function isEven(number value) {
    return (value % 2 == 0);    // Returns true or false
}
```

This example returns a calculated value:

```text
function increment(number value) {
    return value + 1;    // Returns the input plus 1
}

number result = increment(2);    // result becomes 3
```

### Important notes about returns

Return types are dynamic.

- SIL determines the return type at runtime, so there is no need to declare it in the UDF definition.
- You cannot return two different types; this represents an error.
- Be careful with type compatibility when using the returned value. In the example below, the value of `myDate` will not be modified because there is an incompatibility between `number` (right-hand side, returned from the function) and `date` (left-hand side, the variable type). See the [Type handling](/cms_trial/space/PSJC/1939538077/Type+handling/) page for details.

  ```text
  function increment(number value) {
      return value + 1;    // Returns a number
  }

  date myDate = increment(2);    // WARNING: This will fail at runtime
                                // Cannot convert number to date
  ```
- A UDF can return only one value.

To return multiple values, consider using an array for multiple values of the same type or a structure for multiple values of different types.

- You can use `return;` without a value. UDFs always return a value, even if `return` is undefined. The result of empty returns is an undefined value.

#### Examples

These are examples of empty returns behavior:

```text
function processStatus(number value) {
    // Case 1: value < 0
    if(value < 0) {
        print("Invalid: negative value");
        return;    // Exits here for negative numbers
    }
    
    // Case 2: value > 100
    if(value > 100) {
        print("Invalid: exceeds maximum");
        return;    // Exits here for numbers over 100
    }
    
    // Case 3: value between 1-100
    if(value > 0) {
        print("Processing: " + value);
        return;    // Exits here for positive numbers up to 100
    }
    
    // Case 4: value equals 0
    if(value == 0) { 
        print("Status: inactive"); 
        // No explicit return - function still exits after this
    }
}

// Let's see what happens in each case:
string result1 = processStatus(150);    
// Prints: "Invalid: exceeds maximum"
// result1 is undefined because of empty return

string result2 = processStatus(-5);     
// Prints: "Invalid: negative value"
// result2 is undefined because of empty return

string result3 = processStatus(50);     
// Prints: "Processing: 50"
// result3 is undefined because of empty return

string result4 = processStatus(0);      
// Prints: "Status: inactive"
// result4 is undefined because function ends without return

// All results are undefined, so all these will print:
print("Result 1 is null");  // Prints for value 150
print("Result 2 is null");  // Prints for value -5
print("Result 3 is null");  // Prints for value 50
print("Result 4 is null");  // Prints for value 0
```

### Best practices for return values

- Always consider what value your UDF should return.
- Be consistent with return types within a single UDF.
- Check for null/undefined values when using returned values.
- Use meaningful return values that help explain the UDF's outcome.