# set-message

## Overview

A trigger action that displays a custom screen notification. The message can be customized with a title, message content, and notification style.

![Comala visual editor setmessage trigger action with info message type](/cms_trial/assets/ccf107bb-283e-4ab8-9c89-8d25b2030582.png)

This trigger displays the following notification:

![Comala setmessage info notification displayed on a page](/cms_trial/assets/457dbc9e-0b7a-430e-910e-5bb479bf36f0.png)

When the workflow trigger event occurs, the trigger checks that any required conditions are met, and if they are, the `"set-message"` action displays an on-screen notification message.

## `"set-message"`

The trigger action `"set-message"` creates a message notification and can include a message title and a body.

It can be set as **info**, **warning,** or **error**, and set to auto-close after a specified period or require user acknowledgment.

- **action (*****set-message*****)**

  - **type ❗️** Indicator of the level of the message

    - info
    - warning
    - error
  - **title**  **❗️** For adding a title to the message
  - **body❗️** For adding the content for the body of the message

---

### ❗️ Mandatory parameters

**type**

The `"type"` parameter value must be included.

**title**

You must add a title for the message

**body**

The `"body"` parameter value must be included.

---

### Trigger example

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"state":"Expired"}
	],
	"actions":
	[
		{"action": "set-message",
			"type": "info",
			"title": "Stale content",
			"body": "Content may be out of date"}
	]}
]
```

The above `trigger` listens for a state change event to the **Expired** state and displays an on-screen message notification on the change of state.

![Comala setmessage info notification displayed on a page](/cms_trial/assets/457dbc9e-0b7a-430e-910e-5bb479bf36f0.png)

The message **Type** can be changed in the visual editor.

![Comala setmessage trigger message type dropdown options](/cms_trial/assets/53b4addb-5fb9-4a9f-87dd-f6c5958c7861.png)

- **Warning** message

![Comala setmessage warning notification displayed on a page](/cms_trial/assets/c8494474-5ec9-4434-ac49-4c4fdd9b2b53.png)

- **Error** message

![Comala setmessage error notification displayed on a page](/cms_trial/assets/b60249f7-ae3d-4aee-b061-8510aaf841a1.png)

All messages can be removed using the `"clean-messages"` trigger action.

Custom email notifications can be sent using the `"send-email"` trigger action.