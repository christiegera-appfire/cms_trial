# Simple Issue Language

## What is SIL

Simple Issue Language™ (SIL™) is an easy-to-learn scripting language used by [Power Scripts for Jira Cloud](https://appfire.atlassian.net/wiki/spaces/PSJC) and other apps. It lets you customize Jira deeply without needing to understand Jira's internal complexity.

## Why choose SIL

|  |  |
| --- | --- |
| **Fast implementation** | You can quickly create custom workflows and automations. |
| **Shields you from Jira internals** | There’s no need to understand Jira's complex API. |
| **Version consistency** | Scripts work reliably across Jira updates. |
| **Extensibility** | Create reusable functions and handle numerous custom fields. |
| **Cost-effective** | Provides a single scripting solution that can replace multiple specialized apps. |
| **Environment portability** | Easily move workflows from test to production environments. |
| **Flexibility** | Scripts can be quickly adapted and modified on the fly. |

---

## Key SIL components

### Jira standard variables

SIL provides a list of standard variables that you can use to change issues fields.

For example, to change the issue description, you can use the standard variable description:

```text
description = "Issue description";
```

Learn more about standard variables [here](/cms_trial/space/PSJC/491001773/Variable+Substitution+and+Jira+Context/).

### Functions

SIL comes with a library of standard functions to use in scripts. There are functions for handling arrays, strings, and dates, and there are specific app functions.

Learn more about SIL functions [here](/cms_trial/space/PSJC/434374166/SIL+Functions+library/).

---

## SIL example script

To get a taste of what a SIL script looks like and does, here's an example that assigns an administrator as both assignee and reporter, sets various issue fields including description and due date, handles custom fields with conditional logic, creates a new issue, and automatically transitions the original issue to a new workflow state.

```text
string k;
assignee = "admin"; 
reporter = assignee;
description = "some description";
dueDate = currentDate() + "1d";

// Custom fields
if(isNull(cfnumber)){
    cfnumber = 1;
} else {
    cfnumber = cfnumber + 1;
}

// Create issue routine
k = createIssue("TSTP", "", issueType, "auto-created issue");
%k%.votes = %k%.votes + 1;

// Autotransition
autotransition(721, key);
```

Let's [explore SIL](/cms_trial/space/PSJC/15731951/Getting+started+with+SIL/) together, building your knowledge step by step through practical examples and clear explanations.

---