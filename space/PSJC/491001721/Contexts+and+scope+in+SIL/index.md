# Contexts and scope in SIL

It's important to understand that SIL™ involves different types of scope that serve distinct purposes:

- *Jira scope*(or Jira-level scope) refers to the runtime environment that provides access to SIL-defined functions, structs, and variables. This is about what capabilities and resources are available to your script when it runs.
- *Variable scope* refers to the visibility and lifetime of variables declared in your script. This determines where in your code a particular variable can be accessed based on where it was declared.

These scopes operate independently but simultaneously - your script always runs within the Jira scope, while the variable scope controls access to data within your code's structure.

## Understanding contexts

A fundamental concept in creating scripts for Jira is understanding how SIL operates within different contexts. These contexts determine what resources and variables are available to your scripts.

Whenever you run a SIL script, the runtime environment provides both a *Jira scope* and an *Issue context*. The *Issue context* functions as an optional layer that provides direct access to field values from a specific issue, automatic mapping of issue fields to accessible variables, and the ability to read and modify issue data without explicit reference to the issue.

All scripts used by Jira apps run within *Jira scope* and can exist in two primary states:

|  |  |
| --- | --- |
| **With Issue context** | The script has full access to issue-specific fields like summary, assignee, and custom fields. |
| **Without Issue context** | The script is limited to core SIL functionality, unable to directly access or manipulate issue-specific variables. |

This means that while all Jira app scripts operate within the broader Jira context, they may not always have direct access to the specific details of an individual issue. When an *Issue context* is not present, you'll need to use explicit methods to interact with issue-related data.

---

## Working with issue context

Issue context refers to the environment that provides access to a specific Jira issue's fields and values. There are two ways this context can be established: implicitly or explicitly.

### Implicit context

Implicit context refers to when the issue context is automatically provided without requiring any special code. This happens whenever a script runs from an automated context, such as a workflow or listener. The system automatically establishes the issue context based on which issue triggered the automation.

With implicit context, you can directly reference issue fields without specifying which issue they belong to.

#### **Example**

|  |
| --- |
| ```text string value = #{custom field name}; ``` |

### Explicit context references

Explicit context refers to when you manually specify which issue's context to use in your code. Unlike implicit context, explicit context requires you to specifically indicate which issue fields you're accessing, making the code more verbose but also more precise. You can explicitly reference an issue context by using the `key` prefix before a field name.

#### **Example**

|  |
| --- |
| ```text string value = key.#{custom field name}; ``` |

This approach is necessary in scenarios where:

- Your script is not running in an automation that provides implicit context.
- You need to access fields from a specific issue even when another issue's context is implicitly available.
- You want to make it clear in your code which issue fields you're referencing.

---

## Setting default issue context for testing

When running scripts from the SIL Manager, you can use the **Default Script Context** setting. This lets you set the context of your script so that it runs exactly as it would in an automated setting. To set the *Default Script Context*, follow these steps:

1. Open a SIL script in the SIL Manager.
2. Select **Run** > **Default Script Context**.

![Power Scripts for Jira Cloud default script context configuration](/cms_trial/assets/b9851e93-c120-4598-99fd-65c7c4d499a0.png)

1. In the *Script context configuration* window that opens, enter the issue key of the issue you want to use for testing.

![Power Scripts for Jira Cloud issue context settings panel](/cms_trial/assets/bf9b0178-d6a4-427c-be2a-fc4a748bd5f6.png)

1. Click **OK**.

Once set, your script will behave as if it had an implicit context from that issue. You can access issue fields directly without using the `key` prefix, just as your script would in a workflow or listener.

**Note:** If you don't want to run the script in an issue context, leave the **Issue Key** field empty.

---

## Variable scope in SIL

In addition to contexts, SIL also follows specific scoping rules that determine where variables are accessible.

### Understanding the variable resolution process

When your script references a variable, SIL follows a specific resolution process:

1. First, it looks in the current code block.
2. If not found, it checks parent code blocks in sequence.
3. If still not found and the script has an issue context, it checks the issue fields.

This resolution process allows you to override issue field values with local variables when needed while still providing convenient access to issue data.

### Block scope

One specific implementation of *Variable scope* in SIL is *Block scope*, which limits a variable’s accessibility to the block `{}` (set of curly braces) in which it is declared.

```text
{
  string value = "hello"; //Block-scoped variable
  // value is accessible here
}
// value is NOT accessible here
```

This means that variables declared within functions, loops, and conditional statements are limited to the specific block where they are defined.

If you try to access a variable outside its declared block, you’ll get an error:

```text
{
  string value = "hello";
}
runnerLog(value);  // Error: Field >>value<< cannot be matched against a standard field, a custom field or an alias. What is it?
```

This error message indicates that SIL has exhausted its variable resolution process — it couldn't find `value` as a variable in any accessible scope, nor as a field on the current issue.

### Strategies for extended variable access

If you need to access a variable outside its declaration block, you can do one of the following:

1. Define it in an outer scope, as shown in the example below:

```text
string value;  // Declared in outer scope
{
  value = "hello";  // Assigned in inner scope
}
// value is accessible here
runnerLog(value);  // Outputs: "hello"
```

1. Use return values from SIL functions to pass data between blocks, as shown in the example below:

```text
// In a broader scope
string issueKey = "DEMO-123";
number commentId;

// Using a block to isolate some processing
{
   string commentText = "Update required for this issue";
   // The addComment function returns a comment ID we can capture
   commentId = addComment(issueKey, "admin", commentText);
}

// commentText is no longer accessible here, but commentId is
runnerLog("Created comment with ID: " + commentId);
```

This script demonstrates how to isolate variables in a block while still capturing return values for use outside that block. The `commentText` variable is scoped only to the inner block, while the `commentId` variable is available throughout the broader scope.

### Using the minimal scope principle

A best practice in programming, including SIL™, is to declare variables in the narrowest scope possible. This approach:

- Prevents accidental modifications to variables
- Avoids naming conflicts between variables
- Makes code more readable by clarifying where variables are used
- Simplifies maintenance by localizing variable usage

For example, if a variable is only needed within a specific condition, declare it inside that condition's block rather than at the function level.

---

## Examples

### Context and variable scope interaction

This example requires an issue context to run properly. Make sure to set a **Default Script Context** in SIL Manager when testing.

This example demonstrates how contexts and scope interact:

```text
// Accessing an issue field through implicit context
string summary = summary;  // Gets the issue's summary field

// Creating a local variable that shadows the field
{
  string summary = "New summary";  // Local variable takes precedence
  runnerLog(summary);  // Outputs: "New summary"
}

// Outside the block, we get the issue field again
runnerLog(summary);  // Outputs the issue's original summary
```

This example shows how variable resolution works in SIL™:

First, we assign the issue's summary field to a variable with the same name. Inside the block, we create a new variable that "shadows" the outer one. When accessing `summary` inside the block, we get the local variable ("New summary"). When accessing `summary` outside the block, we get the original value from the issue field.

---

## Best practices

- Be mindful of variable names: avoid using names that match issue fields unless you intentionally want to override them.
- Declare variables at appropriate scope: define variables at the narrowest scope needed to avoid confusion.
- Use explicit context references when working with issue fields outside of automatic contexts.
- Set a **Default Script Context**when testing scripts in the SIL Manager to simulate production behavior.
- Be aware of block scope limitations when structuring your scripts.

---

## Related information

- [How SIL works](/cms_trial/space/PSJC/15732008/How+SIL+works/)
- [Standard variables reference](/cms_trial/space/PSJC/1938391090/Standard+variables+reference/)
- [Syntax and types introduction](/cms_trial/space/PSJC/435028043/Syntax+and+types+introduction/)