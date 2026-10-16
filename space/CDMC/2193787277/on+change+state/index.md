# on change state

## Overview

Use the **on change state** (`on-change-state`) event in a workflow trigger to detect when a document transitions from one workflow state to another. When this event occurs, the trigger can perform one or more actions.

You can add a condition to the trigger to limit it to specific transitions—for example, only when the document enters a **named state**, such as the workflow's **initial** or **final** state.

## Example `“on-change-state"` event

```text
"triggers":
[
    {"event": "on-change-state",
    "conditions":
    [
        {"final":true}
    ],
    "actions":
    [
        {"action": "clean-messages"}
    ]}
]
```

The trigger action clears any existing messages on the content

- `"actions":[{ "action":"clean-messages"}],`

The messages are only cleared on the change of state to the final state in the workflow

- `"conditions": [{"final": true}],`