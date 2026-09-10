# final

## Overview

You can define one or more **conditions** for a specific workflow event to control when a trigger is activated. Conditions help ensure that the trigger responds only to targeted occurrences of the event.

For example, adding the **Is Final State** as **True** condition ensures the trigger only activates when the event occurs **while the document is in the final state** of the workflow.

![Comala visual editor trigger with final state condition and clean messages](/cms_trial/assets/b9f29021-5221-4018-ac88-c812a0ed983f.png)

The condition is a **Boolean** value—either **true** or **false**.

When the specified workflow event occurs, the trigger checks whether the condition is met and executes the defined action or actions.

JSON Condition

`"final": (boolean true/false)`

JSON code

```json
"conditions":
[
	{"final":true}
],
```

The trigger action occurs if the state for the event is the `final` state.

For example,

- `"event":"on-change-state", "conditions":[{"final":true}],`

This `"on-change-state"` event condition is met when the workflow transitions to its **final** state.

The `final` parameter value is a Boolean condition

- `"final":true`
- `"final":false`

## Example `on-change-state` event

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

The trigger action clears any existing messages in the content

- `"actions":[{ "action":"clean-messages"}],`

The messages are only cleared on the change of state to the final state in the workflow

- `"conditions": [{"final": true}],`