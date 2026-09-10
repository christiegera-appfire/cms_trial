# clean-messages

## Overview

Use the `clean-messages` action in a workflow trigger to remove all custom on-screen workflow message notifications and tidy up your page for visitors. It can be useful after multiple reviewer actions when you move to the next stage in your process or when moving your workflow to the final published state.

When the workflow trigger event occurs, it checks that any required conditions are met, and if they are, the `"clean-messages"` action removes all set messages.

## `"clean-messages"`

The `"clean-messages"` action removes all messages (set by a `“set-message"` trigger action) on the content.

- **action (*****clean-messages*****)**

There are no parameters for this trigger action.

## Example trigger code

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
		{"action": "clean-messages"}
	]}
]
```

A message can be set using the `"set-message"` trigger action.