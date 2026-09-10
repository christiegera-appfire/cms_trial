# sendEmail() template throws error "Variable >>issue<< is already defined in the same context!"

## Problem

When referencing the `issue` variable in a template referenced when using `sendEmail()`, an error is thrown: `Variable >>issue<< is already defined in the same context!`

The `issue` variable is a reserved keyword when using `sendmail()` with a template. Consider the following `sendEmail()` script that references `template.tpl`:

```text
string issue = "DEMO-1";
sendEmail("name@example.com", "subject goes here, "path/to/template.tpl");
```

For template.tpl:

```text
Current issue key: $issue$.
```

## Solution

Consider using a variable besides `issue`. For example, `issueKey`:

```text
string issueKey = "DEMO-1";
sendEmail("name@example.com", "subject goes here, "path/to/template.tpl");
```

For `template.tpl`:

```text
Current issue key: $issueKey$.
```

In this instance, `issueKey` will not throw an error.