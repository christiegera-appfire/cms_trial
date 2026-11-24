# on attachment updated

## Overview

The `on-attachment-updated` trigger event runs when a new version of an existing attachment is uploaded to a page. Use this event to automate workflow actions when an attachment is updated.

You can add the **File Name** condition to restrict the trigger to specific attachments.

![image-20261124-122431.png](/cms_trial/assets/393e578b-72e4-4a8e-b682-9e33ad008232.png)

## Example: `on-attachment-updated` event

In this example, a workflow trigger adds the `needs-review` label to a page when a new version of an attachment named `review.pdf` is uploaded.

```json
 "triggers": [
    {
      "event": "on-attachment-updated",
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

The **File Name** condition restricts the trigger to `review.pdf`. When the condition is met, the **Add Labels** action adds the `needs-review` label to the current page.