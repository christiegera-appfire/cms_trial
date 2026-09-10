# Exception handling

This page explains Simple Issue Language (SIL™ ) exception handling mechanisms, showing how to create and throw custom errors and catch them using try-catch blocks with different patterns. It provides guidance on handling both SIL and Java exceptions, from basic usage to nested error handling, along with some best practices for implementing error management in your SIL scripts.

Explains SIL exception handling mechanisms, showing how to create and throw custom errors and catch them using try-catch blocks with different patterns.

SIL provides a practical approach to error handling that balances ease of use with error management capabilities. While the language is designed to handle minor issues by returning empty values where appropriate, there are situations where proper exception handling is necessary to ensure your scripts work reliably.

The language also lets you catch system-generated errors and create custom error handling logic. This flexibility allows you to manage errors in a way that makes sense for your particular use case, whether that's displaying user-friendly messages, logging issues for later review, or implementing recovery procedures.

There are two types of exceptions in SIL:

- Java Exceptions that come from the underlying Java system that runs the SIL code.
- SIL objects which are custom errors that you can create and throw in your own code using the `throw` keyword. This page focuses on this type of exception handling.

## Throwing SIL objects

Any SIL value can be thrown as exception. Values can be constants, variables, or expressions.

The general syntax for throwing an exception from SIL is:

```text
throw <value>;
```

**Examples**

```text
// Example 1: Throwing a variable containing an error code
number errorCode = 404;
throw errorCode;  // Throws the numeric value 404

// Example 2: Throwing a literal number
throw 2;  // Throws the number 2 directly

// Example 3: Throwing a value from an array
struct ErrorInfo {
    string fieldName;
    string message;
}
ErrorInfo[] array = {
    {"username", "Username is required"},
    {"email", "Invalid email format"},
    {"password", "Password too short"}
};
throw array[0].fieldName;  // Throws "username"

// Example 4: Throwing a constructed error message using a structure
struct UserData {
    string email;
    string field;
}
UserData structure;
structure.email = "invalid@email";
structure.field = "email";
throw ("Field value invalid: " + structure.field);  // Throws "Field value invalid: email"

// Example 5: Throwing a simple string message
throw "Generic error!";  // Throws the literal string "Generic error!"
```

---

## Try-catch block

The `try`-`catch` block is SIL's main mechanism for handling errors. It lets you:

- Write code that might produce errors in a `try` block
- Handle any errors that occur in one or more `catch` blocks
- Continue program execution gracefully instead of crashing

### Syntax and components

The general syntax for a `try`-`catch` block is the following:

```text
try {                                   // try block component
	<// Code that might cause an error          
} catch <type> <variableName> {         // typed catch block component
	// Handle specific type of error
} catch {                               // general catch block component
	// Code to handle any error
}
```

A `try`-`catch` block can have three possible parts:

| **Component** | **Required** | **Description** | **How it works** |
| --- | --- | --- | --- |
| Try block | ✅ | - You can have one `try` block per `try`-`catch` structure. - It contains the code that might produce an error. | - Code in the `try` block executes normally until an error occurs, or the block completes successfully. - If an error occurs, execution immediately jumps to the `catch` blocks. Any remaining code in the `try` block is skipped. |
| Typed catch block | ❌ | - You can have multiple typed `catch` blocks. - It looks for a `catch` clause that matches the type of the error that was trown (for example, `string` or `number`). - The variable name gives you access to the thrown value. | If you have nested `try`-`catch` blocks , they work like a series of safety nets, where an error that isn't caught by an inner `catch` block "falls through" until caught by an outer `catch` block. Here’s how it works:   - The `catch` blocks are checked in the order they were declared. - First matching `catch` block handles the error. - If no match is found, error “falls through” to the outer `catch`. - This continues until a matching `catch` is found or the program crashes. |
| General catch block (catch-all) | ❌ | - Catches any type of error (SIL objects or Java exceptions). - It is usually placed last. - You can use the following functions to get error details:    - `lastExceptionClass()` : gets the Java exception class name   - `lastExceptionMessage()` :gets the error message |

---

## Common patterns

### Basic example

This example illustrates how the `try`-`catch` mechanism works:

```text
try {
    runnerLog("Starting...");                   // This executes first, outputs "Starting..."
    throw "Error occurred";                     // This executes second, creates an error
    runnerLog("Never reaches this line");       // This never executes because of the error above
} catch string msg {                            // This executes third because we threw a string error
    runnerLog("Caught string error: " + msg);   // This executes fourth, outputs "Caught string error: Error occurred"
} catch number code {                           // This never executes because the string catch already handled the error
    runnerLog("Never reaches this line");
}
runnerLog("Continues here");                    // This executes last, outputs "Continues here"
```

If you run the script in SIL Manager, the output can be:

```text
Starting...
Caught string error: Error occurred
Continues here
```

Think of it like a play script:

1. Actor says "Starting...".
2. Actor sees "Error occurred" and immediately exits stage.
3. String error handler comes on stage and announces the error.
4. Number error handler never appears (not needed).
5. Play continues with next line, "Continues here".

### Type matching and catch all examples

This example illustrates how these two `catch` components work:

```text
// EXAMPLE 1: TYPE MATCHING
try {
    number errorCode = 2;          // Create a number variable
    throw errorCode;               // Throw the number (2)
} catch string s {                 // First catch: looks for string errors
    // Not executed because we threw a number, not a string
} catch number err {               // Second catch: looks for number errors
    // Executes because we threw a number
    // err now contains the value 2 that we threw
    // We can use err in this block
}

// EXAMPLE 2: CATCH-ALL
try {
    number errorCode = 2;          // Create a number variable
    throw errorCode;               // Throw the number (2)
} catch string s {                 // First catch: looks for string errors
    // Not executed because we threw a number, not a string
} catch {                          // Second catch: catches ANY type of error
    // Executes because catch-all handles any error type
    // The thrown value (2) is not accessible here
    // Use lastExceptionMessage() if you need error details
}
```

The first example uses  `catch number err` which:

- Only catches errors of the `number` type.
- Gives you access to the thrown value through `err`.
- Lets you work with the actual error value (2).

The second example uses `catch` which:

- Catches any type of error.
- Doesn't provide access to the thrown value.
- More general but less specific handling.

### Nested try-catch example

In this example, the `processUserData` function handles user information (name, age, email) with three layers of error checking:

```text
// First declare the structure we'll use
struct UserData {
    string name;
    number age;
    string email;
}

function processUserData(UserData userData) {
    try {                                             // Outer try - handles all errors
        runnerLog("Starting data processing");
        
        try {                                         // Inner try - handles validation
            if (userData.age < 0) {
                throw "Invalid age";                  // Throws string error
            }
            
            try {                                     // Inner-inner try - handles DB ops
                // Simulating database operation
                if (userData.name == null) {
                    throw "Database error: null name"; // Simulate DB error
                }
                runnerLog("Saving user: " + userData.name); // Simulated save
            } catch {                                 // Catches DB errors
                // Convert DB error to number code
                runnerLog("DB Error: " + lastExceptionMessage());
                throw 500;                           // Throws number error
            }
            
        } catch string validationError {              // Catches validation errors
            // Handle validation errors specially
            runnerLog("Validation error: " + validationError);
            throw 400;                                // Throws number error
        }
        
    } catch number errorCode {                        // Catches all error codes
        // Handle all error codes in one place
        switch(errorCode) {
            case 400:
                runnerLog("Validation failed");
                break;
            case 500:
                runnerLog("Database error");
                break;
        }
        return false;
    }
    
    return true;
}

// Example usage:
UserData user;
user.name = "John Doe";
user.age = -5;  // This will trigger validation error
user.email = "john@example.com";

boolean result = processUserData(user);
```

Here’s what happens if you test with `user.age = -5;`:

1. The middle layer catches the invalid age.
2. It converts it to error code 400.
3. The outer layer sees error code 400 and logs "Validation failed".
4. As shown in the screenshot below, the function returns false.

   ![This screenshot shows the validation error message and the thrown exception in SIL Manager Editor console.](/cms_trial/assets/82ea4047-f75c-46a2-a208-50a5d2bc14e9.png)

Think of it like checking your ID:

- Inner layer: checks your ID details
- Middle layer: verifies your age
- Outer layer: makes final decision to let you in or not

### Java exceptions

This example shows how to handle Java exceptions in SIL:

```text
try {
    // This line attempts to run code as a different user
    // Since the user doesn't exist, it will throw a Java exception (not a SIL error)
    runAs("user_that_does_not_exist");
    
    // Any code here would be skipped when the exception occurs
    runnerLog("This line never executes");
    
} catch string err {
    // This catch block looks for SIL string errors
    // It won't match because runAs() throws a Java exception, not a SIL string
    runnerLog("This won't execute");
    
} catch {
    // This catch-all block handles any type of error, including Java exceptions
    // It will match and execute in this case
    
    // Get the Java exception class name (e.g., "java.lang.IllegalArgumentException")
    runnerLog("Class:" + lastExceptionClass());
    
    // Get the actual error message (e.g., "User 'user_that_does_not_exist' not found")
    runnerLog("Message:" + lastExceptionMessage());
}
```

Output for this example might look like:

```text
Class:com.keplerrominfo.sil.lang.SILInfoException
Message:[SIL Error on line: 4, column: 5] User user_that_does_not_exist does not exist.
```

Here are some key points about this example:

- `runAs()` is a SIL function that interacts with Java code.
- When Java code throws an exception, it can only be caught by a catch-all block.
- Use `lastExceptionClass()` and `lastExceptionMessage()` to get error details.
- Typed catch blocks (like `catch string`) won't handle Java exceptions.

---

## Best practices

While `try`-`catch` blocks are powerful, carefully consider how to use them. Not every operation needs error handling, but when you do need it, make sure to apply some best practices to your code.

To enhance error specificity:

- Catch specific errors before general ones.
- Use typed `catch` blocks when you need the error value.
- Use general `catch` blocks for unexpected errors.

To improve error handling:

- Log error details for debugging.
- Clean up resources in all error paths.
- Provide meaningful error messages.
- Don't catch errors you can't handle properly.

To streamline code organization:

- Keep `try` blocks focused on specific operations.
- Don't use `try`-`catch` for normal flow control.
- Consider extracting complex error handling into separate functions.