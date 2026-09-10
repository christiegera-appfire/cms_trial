# Statements

This page covers syntax, usage patterns, and practical examples for each statement type used in Simple Issue Language (SIL™).

Statements in SIL provide a convenient method to create conditional logic (if-else, switch) and repetitive operations (for, while, do-while) with a syntax similar to C, C++, and Java.

For each statement, you’ll find a description of its usage in SIL, syntax, and examples

## If-else statement

The **if-else** statement enables conditional execution of code blocks, allowing you to create branching logic based on specific conditions.

### Syntax

```text
if (condition) {
    Instruction1;
    ...          //Instructions when condition is true
    InstructionN;
} else if {
    Instruction1:
    ...          //Instructions when condition is true
    InstructionN;
} else {
    Instruction1:
    ...          //Instructions when both condition are false
    InstructionN;
}
```

The `else` branch can be omitted.

### Basic if-else example

```text
if(issueType == "Bug" && environment == "Production") {
    priority = "Highest";
} else if {issueType == "Bug" && environment == "Development") {
    priority = "Medium";
} else {
    priority = "Low";
}
```

#### Example description

This example checks the following conditions in a Jira issue:

- If the issue type is a *Bug* and the environment is *Production*, the issue receives *Highest* priority.
- If the conditions are not met (else), the check continues with the second set of conditions.
- If the issue type is a *Bug* and the environment is *Development*, the issue receives *Medium* priority.
- If this second condition is not met either (else), issues for all other combinations are set to *Low* priority.

### Complex if-else example

```text
if (issueType == "Bug" && severity == "Critical" && impactedUsers > 100) {
    priority = "Highest";
    assignToTeam = "ProductionSupport";
    notifyStakeholders = true;
} else if ((issueType == "Bug" && severity == "Major") || 
           (issueType == "Security" && environment == "Production")) {
    priority = "High";
    assignToTeam = "DevelopmentTeam";
    notifyStakeholders = impactedUsers > 50;
} else if (issueType == "Enhancement" && businessValue == "High" && 
           implementationEffort == "Low") {
    priority = "Medium";
    assignToTeam = "DevelopmentTeam";
    notifyStakeholders = false;
} else {
    priority = "Low";
    assignToTeam = "Backlog";
    notifyStakeholders = false;
}
```

#### **Example description**

This example code implements a comprehensive issue triage system that:

- Sets *Highest* priority for critical bugs affecting many users.
- Assigns *High* priority to major bugs and production security issues.
- Prioritizes high-value, low-effort enhancements as *Medium*.
- Routes issues to appropriate teams and manages stakeholder notifications.
- Defaults all other cases to *Low* priority in the backlog.

---

## For statement

The **for** statement provides a compact way to iterate over a range of values. It is often referred to as the **for loop** statement,because it repeatedly loops until a particular condition is satisfied.

In SIL, the **for** statement provides two primary iteration methods:

- standard form: simply **for**
- **foreach** form

### Standard form

#### Syntax

```text
for(<init>; <condition>; <increment>){
   Instruction1;
   ...
   InstructionN;
}
```

For the standard form, the `<init>` can be an attribution of an already defined variable or a definition for a new variable.

#### Example

```text
// Prints numbers from 0 to 9 in console
for (number i = 0; i < 10; i++) {
    runnerLog(i);
}
```

#### **Example description**

This example demonstrates a basic iteration:

- Initializes a counter `i` to 0.
- Continues looping while `i` is less than 10.
- Increments `i` by 1 in each iteration.
- Prints each number from 0 to 9 (total 10 numbers) in the SIL Manager output console.

### Foreach form

#### Syntax

```text
for(<variable_definition> in <array>){
   Instruction1;
   ...
   InstructionN;
}
```

#### Example

```text
for(string user in watchers){
   runnerLog(user);
}
```

#### Example description

This **foreach** loop iterates through a collection of watchers of a specific issue and prints the list of the watchers:

- Automatically iterates through each element in the `watchers` array.
- Assigns each element to the `user` variable in each iteration.
- Prints the name of each watcher in the SIL Manager output console.

---

## While statement

The **while** statement provides support for conditional repetitive execution of a code block. It evaluates the condition first:

- If the condition is true, the instructions in the body (the loop) is executed.
- If the condition is false from the start, the loop body is never executed.

When using the **while** statement in your scripts, make sure to include safeguards against infinite loops. Infinite loops can freeze your program, consume system resources, and potentially crash your application.

### Syntax

```text
while(condition) {
    Instruction1;
    ...                // Instructions when condition is true
    InstructionN;
}
```

### Example

```text
string [] multisel;
number i = 1;
while(i <= 3) {
    multisel += "value" + i;
    i++;
}
```

#### **Example description**

This while loop in this example demonstrates how to build a collection incrementally:

- Starts with `i` as 1.
- Continues looping while `i` is less than or equal to 3.
- In each iteration, adds a new element to `multisel` array
- Element is created by concatenating `"value"` with the current value of `i`.
- After completion, `multisel` will contain [`"value1"`, `"value2"`, `"value"`].

---

## Do-while statement

The **do-while** statement is similar to the while statement except that it guarantees at least one execution of its code block before evaluating the termination condition. Even if the condition is false, the instructions will still be evaluated once.

When using the **while** statement in your scripts, make sure the condition can be met within the loop body.

### Syntax

```text
do {
    Instruction1;
    ...
    InstructionN;
} while(condition);
```

### Example

```text
number i = 1;
string [] people;
do {
    people += watchers[i];
    i++;
} while(i < 5);
```

#### Example description

This example do-while loop populates a `people` array, ensuring at least one processing of the loop body:

- Starts with `i` as 1.
- Adds watchers to the `people` array from index 1.
- Increments `i` after each iteration.
- Continues until `i` is no longer less than 5.

---

## Switch statement

The **switch** statement provides a structured mechanism for conditional execution based on the value of a specific variable.

- It accepts both number and string variables.
- Evaluates the input variable against multiple predefined case values.
- Executes the first matching case's code block.
- Continues executing subsequent cases unless a `break` statement is used.
- Supports specific handling for unmatched cases through the `default` branch.

### Syntax

```text
switch(variable) {
    case value1:
		Instruction11;
		...
		Instruction1N;	
	[break;] 
    case value2:
		Instruction21;
		...
		Instruction2N;
	[break;]
	...
	case valueN:
		InstructionM1;
		...
		InstructionMN;
	[break;]
	[default:
		InstructionDef1;
		...
		InstructionDefN;]
}
```

The **break** statements and the **default** branch can be omitted, which changes the script behavior.

### Example 1: Switch with numbers (with break statements and default branch)

```text
switch (priority) {    // priority is a number variable
    case 1:
        // Executes only when priority equals 1
        escalateImmediately();
        break;         // Prevents fallthrough to case 2
    case 2:
        // Executes only when priority equals 2
        scheduleReview();
        break;         // Prevents fallthrough to case 3
    case 3:
        // Executes only when priority equals 3
        addToBacklog();
        break;         // Prevents fallthrough to default
    default:
        // Executes when priority doesn't match 1, 2, or 3
        logInvalidPriority();
}
```

### Example 2: Switch with string matching

```text
switch (status) {      // status is a string variable
    case "ERROR":
        logError();    // No break - falls through to "WARN"
    case "WARN":
        sendAlert();
        break;         // Stops here for both "ERROR" and "WARN"
    case "INFO":
        logMessage();
        break;
    default:
        // Handles any status value not matching above cases
        logUnknownStatus();
}
```

#### Examples description

In both examples, cases are evaluated from top to bottom. Only equal values trigger case execution.

- The **break** statement terminates the switch block's execution after a case is handled, preventing unintended fallthrough to subsequent cases. The second example demonstrates an intentional fallthrough. For additional information about the **break** statement, refer to the [Break statement](/cms_trial/space/PSJC/434472559/Statements/) section.
- The **default** branch functions as an essential catch-all mechanism within the switch statement. It executes when the input value doesn't match any of the defined case values, providing a way to handle unexpected or unspecified inputs. While optional, including a default branch is considered best practice as it ensures comprehensive handling of all possible input values and helps prevent undefined behavior.

---

## Break statement

The **break** statement serves two distinct control flow purposes:

- Loop termination: When used within loops (**for**, **while**, **do-while**), the **break** statement provides immediate termination of the entire loop execution, transferring control to the first statement following the loop block. This enables early exit from loops based on specific conditions.
- Switch exit: Within switch statements, break statements terminate the switch block execution, preventing fallthrough to subsequent cases and transferring control to the code following the switch structure.

### Example

```text
// Prints numbers 0-4 in the console, then exits loop early
for (number i = 0; i < 10; i++) {
   if (i >= 5) {
      break;  // Terminates loop when i reaches 5
   }
   runnerLog(i);  // Only prints 0,1,2,3,4
}
// Execution continues here after break
```

---

## Continue statement

The **continue** statement is used inside a loop (**for**, **while**). It provides a mechanism to skip the remaining code within the current loop iteration, immediately jumping to the loop’s next iteration.

### Example

```text
number i = 1;
while (i <= 10) {
    if (i % 3 == 0) {
        i++;        // Update counter before continue
        continue;         // Skip printing multiples of 3
    }
    runnerLog(i);            // Prints: 1,2,4,5,7,8,10
    i++;
}
```

---

## Best practices for using statements in SIL

Following some simple best practices can prevent common pitfalls and ensure your code is maintainable, reliable, and efficient.

### General

- Keep statement blocks concise and focused.
- Avoid mixing too many different control structures.
- Use meaningful variable names that indicate purpose.
- Add comments for complex logic or business rules.
- Test thoroughly.
- Include appropriate error-handling mechanisms. For example, validate inputs before processing, log or report errors.
- Keep your code well-organized by grouping related control structures.
- Maintain consistent indentation and formatting.
- Document complex control flow patterns.

### **If-else statements**

- Keep conditions simple and readable.
- For multiple conditions, consider using **switch** statements instead.
- Avoid deeply-nested **if** statements (maximum 3-4 levels).
- Consider extracting complex conditions into separate boolean functions.

### **Switch statements**

- Always include a **default** case for error handling.
- Use **break** statements consistently to prevent unintended fallthrough.
- Document intentional fallthrough cases with comments.
- Consider **switch** instead of **if-else** when comparing a single variable against multiple values.

### **For loops**

- When the iteration count is known, use the **standard form** for loops.
- When processing arrays, preferably use **for each** loops.
- Initialize variables properly before the loop.
- Avoid modifying loop variables inside the loop body.

### **While loops**

- Include safeguards against infinite loops.
- Ensure loop conditions can eventually become false.
- Initialize all variables before the loop.
- Validate loop variables have been properly updated.
- Use while when iteration count is unknown.
- Add timeout conditions for time-sensitive operations.

### **Do-while loops**

- Use when code must execute at least once. Best suited for validation scenarios.
- Keep the loop body focused on a single task.
- Ensure the condition can be met within the loop body.

### **Break statements**

- Use to exit loops early when a condition is met.
- Avoid using multiple breaks in a single loop.
- Document the exit condition clearly.
- Consider extracting complex logic into separate functions.

### **Continue statement**

- Use to skip iterations based on specific conditions.
- Place **continue** statements early in the loop body.
- Avoid multiple **continue** statements in a single loop.
- Ensure all necessary variables are updated before **continue**.

---

## See also

- [Syntax and types introduction](/cms_trial/space/PSJC/435028043/Syntax+and+types+introduction/)
- [Operators reference](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488430)
- [Variable types and reference methods](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15485601)