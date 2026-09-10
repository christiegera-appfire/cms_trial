# Variable types and reference methods

This page explains how Simple Issue Language (SIL™) identifies and accesses different types of variables in scripts. It covers standard Jira fields, custom fields, and user-defined variables while providing detailed guidance on various referencing methods and pre-declared variables.

## Basic concepts

Variable resolution is how SIL identifies and accesses different types of variables in your scripts - whether they're standard Jira fields, custom fields, or your own variables. Understanding variable resolution is crucial for writing effective SIL scripts, as it determines how you can reference and manipulate issue data.

- Variables in SIL can be standard Jira fields, custom fields, or user-defined variables.
- Resolution refers to how SIL finds and accesses these variables.
- Context determines how you can reference variables:

  - Implicit reference (in issue context) is used when your script runs in the context of a specific issue.
  - Explicit reference (any context) is used when you need to reference specific issues or related issues.

To learn more about context, see the [Issue context](/cms_trial/space/PSJC/491001721/Contexts+and+scope+in+SIL/) page.

---

## Issue reference in SIL

Pre-declared variables are automatically available in SIL scripts, letting you access information about issues using either direct field names or through specialized issue reference syntax patterns.

### Standard (pre-declared) variables

SIL automatically pre-declares all standard issue variables and their synonyms. For example:

- `key` represents the issue key
- `id` represents the issue ID
- `summary` represents the issue summary

Don’t redeclare these pre-declared variables; this will cause errors in your code.

Use all pre-defined variables directly. When creating your own variables, add a descriptive prefix to their names to distinguish them from Jira's built-in field names. For example, use `myVar_summary` instead of just `summary`, which is already pre-declared.

- Incorrect use example: `string key = "PROJ-123";`
- Correct use example: `runnerLog(key);`

For a full list of pre-declared variables and their usage, see the [Standard variables reference](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/1828290641).

### Specialized issue reference syntax patterns

SIL provides three ways to reference and access issue data through specialized syntax patterns.

| **Reference** | **Syntax pattern** | **Description** |
| --- | --- | --- |
| Parent issue reference | `parent.fieldName` | - Refers to the parent ID - Only valid for subtasks  Example ```text parent.id        // Parent issue's ID parent.summary   // Parent issue's summary parent.status    // Parent issue's status  // Example usage if (parent.status == "Done") {     summary = "Parent is completed: " + parent.summary; } ```  Don’t use on regular issues; this will cause errors in your code. |
| Direct issue reference | `issueKey.fieldName` | - Refers to the specific issue in the project - The issue must exist and you must have appropriate permissions  Example ```text PROJ-123.id          // Specific issue's ID PROJ-123.summary     // Specific issue's summary PROJ-123.assignee    // Specific issue's assignee  // Example usage PROJ-123.assignee = currentUser(); PROJ-123.labels += "needs-review"; ``` |
| Substitution | `%issueKey%.fieldName` | - Used for dynamic issue access when issue keys are stored in variables - Best suited for accessing issues in loops (for, while, do-while) or when creating an issue from the SIL Manager  Example ```text string k = "PROJ-123"; %k%.reporter = currentUser();    // Sets reporter on PROJ-123 %k%.summary = "Updated Summary"; // Sets summary on PROJ-123 ```  Here’s how it works:   - Variable `k` contains an issue key, such as `string k = "PROJ-123";` - The substitution `%k%` uses the value of the variable to access a specific issue - The `.fieldName` accesses that that specific issue's field (like reporter or summary) |

---

## Field reference in SIL

SIL provides flexible ways to access both standard and custom Jira fields through different reference methods.

### Variable substitution

Variable substitution is a mechanism in SIL that lets you dynamically access fields using variables. Instead of directly referencing a field name, you can store the field name in a variable and use that variable to access the field. It uses the basic syntax `%variableName%`.

When SIL encounters `%variableName%`, it performs two steps:

- Step 1: SIL reads the value stored in the variable.
- Step 2: SIL uses the retrieved value as the field name to access.

#### Examples

This basic example illustrates the variable substitution mechanism:

```text
// Step 1: Store field name in a local variable
string fieldName = "customfield_10000";

// Step 2: Use substitution to access field
%fieldName% = "new value";    // Updates the field identified by customfield_10100

// This is equivalent to writing:
customfield_10000 = "new value";
```

These examples illustrate the two common use cases for variable substitution:

- Custom field access

  ```text
  // Store custom field IDs in descriptive variables
  string storyPoints = "customfield_10001";
  string epicLink = "customfield_10002";

  // Use variables to access fields
  %storyPoints% = 5;
  %epicLink% = "EPIC-123";
  ```
- Dynamic field updates

  ```text
  // Update multiple related fields
  string[] fieldsToUpdate = {
      "customfield_10001",
      "customfield_10002",
      "customfield_10003"
  };

  for (string field in fieldsToUpdate) {
      %field% = "Updated Value";
  }
  ```

Using uninitialized or empty variables in substitution patterns can cause errors that are difficult to debug.

- Always validate your variables before using them in substitutions.
- Check field existence before using variable substitution.
- Use descriptive variable names.

This example shows how to validate variables and check if a field exists:

```text
// Bad practice - no validation
string emptyField;
%emptyField% = "value";  // This will cause errors

// Good practice - with validation
string fieldName = "customfield_10000";
if (fieldName != null && fieldName != "") {
    %fieldName% = "New Value";
}
// Check field existence
if (fieldExists(fieldName)) {
    %fieldName% = "New Value";
}
```

### Custom fields

In addition to standard issue fields, SIL provides three ways to access custom fields:

- By field ID
- By field name
- By field alias (if configured)

For information about using aliases, see the [Custom fields aliases](/cms_trial/space/PSJC/496206057/Custom+fields+aliases/) page.

#### Examples

This example shows three ways of accessing a custom field:

The field IDs and names shown are examples. Your actual Jira instance will have different IDs and field names.

```text
// 1. By Field ID - Story Points field
customfield_10024 = 5;             // Uses the customfield_fieldID syntax

// 2. By Field Name
StoryPoints = 5;                   // Field name without spaces
#{Story Points} = 5;               // Uses the #{fieldName} syntax for field names with spaces

// 3. By Field Alias (if configured)
points = 5;                        // Alias for Story Points custom field

// Complex example showing multiple fields
customfield_10025 = "High";        // Priority score
#{Technical Debt} = "Medium";      // Technical debt rating
complexity = "Complex";            // Alias for implementation complexity
```

When multiple custom fields share the same name, Jira API returns the first match. To prevent errors, reference the intended field by its ID by using the `customfield_fieldID` syntax.

See [Supported custom field types](/cms_trial/space/PSJC/434962565/Supported+custom+field+types/) for a complete reference.