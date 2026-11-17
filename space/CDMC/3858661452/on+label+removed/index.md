# on label removed

## Overview

The `on-label-removed` trigger event runs when a label is removed from a page. Use this event to execute workflow actions when a page label is removed.

You can add the **Removed Label** condition to restrict the trigger to a specific label.

## Example: `on-label-removed` event

In this example, the **Removed Label** condition restricts the trigger to the `editor` label. When this label is removed, the trigger adds the `needs-review` label to the page.

```json
"triggers": [
  {
    "event": "on-label-removed",
    "conditions": [
      {
        "removed-label": {
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

The `on-label-removed` event fires when the `editor` label is removed from a page. The `removed-label` condition restricts the trigger to this label.

When the condition is met, the `add-labels` action adds the `needs-review` label to the current page.