# clear-expiration

## Overview

You can use the `"clear-expiration"` trigger action to remove an existing due date from a workflow state.

![Comala visual editor clearexpiration trigger action configuration](/cms_trial/assets/da1ae92d-e9c6-4023-8979-6257ddcbc353.png)

The expiration is cleared from the workflow state specified in the workflow trigger condition. If no condition is set, it is cleared from the workflow state at the time when the event occurred.

When the workflow trigger event occurs, the trigger checks that any required conditions are met, and if they are, the `"clear-expiration"` action clears the expiration date.

## clear-expiration

The `"clear-expiration"` action removes an existing workflow state expiration period.

- **action (*****clear-expiration*** **)**

There are no parameters for this action.

### Example trigger code

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"final":true}
	],
	"actions":
	[
		{"action": "clear-expiration"}
	]}
]
```

In the above example, the expiration due date on the workflow final state is cleared when the transition to this state occurs.

You can add a new expiration date using the [set-expiration trigger action](/cms_trial/space/CDMC/2193950357/set-expiration/).