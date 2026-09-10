# on-page-updated

## Overview

Use the `on-page-updated` event in a workflow trigger to detect when a page with an active workflow is updated. This event lets you configure actions that run automatically after the update.

## Requirements

- The trigger is activated whenever a page with an active workflow is edited.
- The trigger can be configured with or without conditions.

## Example `"on-page-updated"` event

```text
"triggers":
[
    {"event": "on-page-updated",
    "conditions":
    [
        {"state":"Approved"}
    ],
    "actions":
    [
        {"action": "clean-messages"}
    ]}
]
```

In this example, when a page in the **Approved** state is updated, the trigger runs the [clean-messages](/cms_trial/space/CDMC/2193852928/clean-messages/) action to clear existing messages.