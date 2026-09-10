# on-state-expired

## Overview

Use the on-state-expired event in a workflow trigger to listen for a state-expired event and execute one or more trigger actions.

By including a trigger condition, the expiration event in a workflow trigger can be constrained to listen for the state expiration event in a named state, the workflow's final state, or the initial state.

## Example `“on-state-expired"` event

```text
"triggers":
[
	{"event": "on-state-expired",
  	"actions":
	[
		{"action": "change-state",
			"state": "Review"},
		{"action": "set-message",
        	"type": "warning",
            "title": "Stale content",
            "body": "Content has passed its set life and may be out of date"
        }
    ]}
]
```

The on-state-expired event only listens for a workflow expiry event.

Each `event` can include conditions and one or more actions

The trigger event must include at least one trigger action.

There are two actions in the above example

- the `"change-state"` action to transition the workflow to the **Review** state, and
- `"set-message"` notification action

![Comala onexpire event warning notification message](/cms_trial/assets/1d02b077-dbc6-4f53-a7c8-fa7e5abb320b.png)

If a trigger action is present, it can include one or more conditions. If no conditions are added, the trigger listens for an expiration event for any state.