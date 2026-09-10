# on-approval-unassigned

## Overview

Use the **on-approval-unassigned** event in a workflow trigger to listen for a reviewer unassignment event and execute one or more trigger actions.

By including a trigger condition, the unassign event in a workflow trigger can be constrained to listen for unassignment of an approval reviewer in a named state, such as the workflow’s final or initial state.

## Example `“on-approval-unassigned"`

```text
"triggers":
[
	{"event": "on-approval-unassigned",
	"conditions":
	[
		{"state":"Review"}
	],
	"actions":[       
	       {"action": "set-message",
            "type": "warning",
            "title": "Reviewer has been unassigned",
            "body": "A new reviewer may need to be assigned"
           }]
     }
]
```

The trigger action sets a message notification on the content for users

- `"actions":[{ "action":"set-message", ....}],`

The trigger action occurs on the `"on-unassign"` event, but ONLY if the current state is the **Review** state

- `"conditions":[{"state":"Review"}],`