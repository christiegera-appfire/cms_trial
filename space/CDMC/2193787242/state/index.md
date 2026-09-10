# state

## Overview

One or more **conditions** can be set to trigger a named event in the workflow. Adding a condition is optional.

Adding a **state** condition to a trigger listens for the trigger event when the document is in the specified state. Only one state is set for the condition.

![Comala visual editor trigger with onapprove event and review state condition](/cms_trial/assets/5d266433-3a5e-4ed7-b523-150fb60c8a24.png)

The state name used in the condition must be a state in the workflow.

When the named workflow event occurs, the trigger checks that the state condition is met and sets one or more actions in the trigger.

**Condition**

`"state": "(string value)"`

**JSON code**

```json
"conditions":
[
	{"state": "Review"}
],
```

The trigger action occurs if the condition matches the provided `"state"`.

- specified state name must exist in the current workflow
- The state name is case-sensitive
- only accepts one state value
- only one `"state": "<statename>"` condition for an event

## Example `on-approve` event

```text
"triggers":
[
	{"event": "on-approve",
	"conditions":
	[
		{"state":"Review"}
	],
	"actions":
	[
		{"action":"change-state",
			"state":"Published"}
	]}
]
```

This example demonstrates how to fast-track a change in workflow state based on a single approval decision.

The trigger listens for the **approve** event and includes a condition that checks if the current state is **Review**.

`"conditions": [{ "state": "Review" }]`

If the condition is met, the following **action** will be executed to change the workflow state to **Published**.

`"actions": [{ "action": "change-state", "state": "Published" }]`

This setup allows the page to automatically move to the **Published** state when a single reviewer approves it in the **Review** state.