# first-loop

## Overview

`first-loop` is a new condition for the `on-change-state` event

When the specified workflow event occurs, the trigger evaluates the condition. If the condition is met, it executes one or more defined actions.

- `first-loop=true` filters the trigger so it runs only once per piece of content that enters the specified state.
- `first-loop=false` allows the trigger to run whenever the workflow transitions into the state defined by the **state** parameter.

![Comala firstloop condition trigger configuration](/cms_trial/assets/05f65ee5-329b-4084-93be-2747bff283d8.png)

### **JSON Condition**

`"first-loop":(boolean true/false)`

The `first-loop` parameter value is a boolean

- `"first-loop":true`
- `"first-loop":false`

`first-loop` is used as a parameter within the **trigger** macro.

Its primary purpose is to support one-time initialization actions for a given document. For example, during the first review of a document, you may want to send an additional email notification or set specific metadata.

## Example trigger code

```text
"triggers":
[
    {"event": "on-change-state",
    "conditions":
    [
        {"first-loop":"True"}
        {"state":"Draft"}
    ],
    "actions":
    [
        {"action": "set-metadata"}
    ]}
```

A trigger action displays a custom screen notification.

- `"actions":[{ "action":"set-metadata"}],`

`first-loop=true` – this means the trigger listens ONLY for the first occurrence of a transition to a specified state for the content

`first-loop=false` – this means the filter listens for all occurrences of transitions to the specified state