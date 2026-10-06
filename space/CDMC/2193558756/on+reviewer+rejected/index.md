# on reviewer rejected

## Overview

Use the **on reviewer rejected** (`on-reject`) event in a workflow trigger to listen for an approval reject event and execute one or more trigger actions.

By including a trigger condition, the reject event in a workflow trigger can be constrained to listen for the approval reject event in a named state, the workflow's final state, or the initial state.

## Example `" on-reject"` event

```text
"triggers":
[
	{"event": "on-reject",
	"conditions":
	[
		{"state":"Review"}
	],
	"actions":
	[
		{"action":"change-state",
			"state":"Rejected"}
	]}
]
```

The [trigger action](/cms_trial/space/CDMC/2192870598/Trigger+actions/) causes a change of state

- `"actions":[{ "action":"change-state", "state": "Rejected"}],`

The trigger action occurs on the `"reject"` event, but the added condition means this is ONLY if the current state is the **Review** state

- `"conditions":[{"state":"Review"}],`

This example fast-tracks a state change when a single reviewer rejects the approval in the **Review** state.