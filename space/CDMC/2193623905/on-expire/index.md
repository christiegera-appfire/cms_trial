# on-expire

## Overview

Use the on-expire event in a workflow trigger to listen for a state-expired event and execute one or more trigger actions.

By adding a trigger condition, you can constrain the expiration event to a named state, the workflow's final state, or the initial state.

## Example `“on-expire"` event

```text
"triggers":
[
	{"event": "on-expire",
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

The on-expire event only listens for a workflow expiry event.

Each `event` can include conditions and one or more actions

The trigger event must include at least one trigger action.

There are two actions in the above example

- the `"change-state"` action to transition the workflow to the **Review** state, and
- `"set-message"` notification action

![Comala onexpire event warning notification message](/cms_trial/assets/9c3e5e87-1262-4222-bb23-c81accf0a0e0.png)

If a trigger action is present, it can include one or more conditions. If no conditions are added, the trigger listens for an expiration event for any state.