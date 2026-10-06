# on approval assigned

## Overview

Use the **on approval assigned** (`on-assign`) event in a workflow trigger to listen for a reviewer assignment event and execute one or more trigger actions.

By adding a trigger condition, you can constrain the assignment event in a workflow trigger to listen for the approval event in a named state within the workflow, such as the workflow's final or initial state.

## Example `“on-assign"` event

```text
"triggers":
[
	{"event": "on-assign",
	"conditions":
	[
		{"state":"Review"}
	],
	"actions":
	[   
			{"action": "send-email",
            "recipients":
            [
                "@creator",
                "@watchers",
                "@lastUpdatedBy",
            ],
            "notification": {"subject": "${content.title} has been assigned in the Review state",
                "title": "${content.title} is assigned",
                "body": "Hello, ${content.link} in the ${content.space} space is
                in approval state Review and has been assigned"}}
    ]}
]
```

The trigger action causes an email to be sent to the page author, page watchers, and the user who last updated the page.

- `"actions":[{ "action":"send-email", ......}],`

The trigger action occurs on the `"on-assign"` event, but ONLY if the current state is the **Review** state

- `"conditions":[{"state":"Review"}],`