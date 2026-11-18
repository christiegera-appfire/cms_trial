# on attachment added

## Overview

The `on-attachment-added` trigger event runs when an attachment is uploaded or restored to a page. Use this event to execute workflow actions when an attachment is added.

You can add the **File Name** condition to restrict the trigger to specific attachments.

![image-20261117-151804.png](/cms_trial/assets/a00cfefd-8ad4-4c9d-bde6-94d26413d2fd.png)

## Example: `on-attachment-added` event

In this example, a workflow trigger adds the `needs-review` label to a page when an attachment named `review.pdf` is uploaded or restored.

```json
"triggers": [
  {
    "event": "on-attachment-added",
    "conditions": [
      {
        "file-name": {
          "operator": "equals",
          "value": [
            "review.pdf"
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

The `on-attachment-added` event fires when an attachment is uploaded or restored to a page. The `file-name` condition restricts the trigger to attachments named `review.pdf`.

When the condition is met, the `add-labels` action adds the `needs-review` label to the current page.