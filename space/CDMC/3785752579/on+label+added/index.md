# on label added

## Overview

The `on-label-added` trigger event runs when a label is added to a page. Use this event to execute workflow actions when a page label is added.

You can add the **Added Label** condition to restrict the trigger to a specific label.

## Example `"on-label-added"` event

In this example, a workflow trigger automatically moves a page from the **Draft** state to the **Brand Review** state when the `brandcheck` label is added.

```json
"triggers": [
  {
    "event": "on-label-added",
    "conditions": [
      {
        "added-label": {
          "operator": "equals",
          "value": [
            "brandcheck"
          ]
        }
      },
      {
        "state": {
          "operator": "equals",
          "value": [
            "Draft"
          ]
        }
      }
    ],
    "actions": [
      {
        "action": "change-state",
        "state": "Brand Review"
      }
    ]
  }
]
```

The `on-label-added` event fires when a label is added to a page. The `added-label` condition checks whether the added label is `brandcheck`, while the `state` condition restricts the trigger to pages in the **Draft** state.

When both conditions are met, the **Change State** action moves the page to the **Brand Review** state.