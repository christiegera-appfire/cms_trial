# on-reviewer-approved

## Overview

Use the **on-reviewer-approved** event in a workflow trigger to listen for an approval event and execute one or more trigger actions.

By including a trigger condition, the approve event in a workflow trigger can be constrained to listen for the approval event in a named state, such as the workflow's final or initial state.

## Example `“on-reviewer-approved"`

```text
"triggers":
[
	{"event": "on-reviewer-approved",
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

The trigger action causes a change of state to the **Published** state.

- `"actions":[{ "action":"change-state", "state": "Published"}],`

The trigger action occurs on the `approve` event, but ONLY if the current state is the **Review** state

- `"conditions":[{"state":"Review"}],`

This example fast-tracks a change of workflow state when a single reviewer approves a decision made in the **Review** state.