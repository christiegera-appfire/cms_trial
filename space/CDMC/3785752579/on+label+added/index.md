# on label added

## Overview

The `on-label-added` trigger event runs when a label is added to a page. Use this event to execute workflow actions when a page label is added.

You can add the **Added Label** condition to restrict the trigger to a specific label.

## Example `"on-label-added"` event

```json
"triggers": [
  {
    "event": "on-label-added",
    "conditions": [
      {
        "added-label": {
          "operator": "equals",
          "value": [
            "editor"
          ]
        }
      }
    ],
    "actions": [
      {
        "action": "add-labels",
        "labels": [
          "needs-review"
        ],
        "children": false
      }
    ]
  }
]
```

The `on-label-added` event fires when a label is added to a page. The `added-label` condition restricts the trigger to cases where the added label is `editor`.

When the condition is met, the `add-labels` action adds the `needs-review` label to the current page.