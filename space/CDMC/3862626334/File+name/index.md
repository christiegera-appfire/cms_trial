# File name

## Overview

The **File Name** condition checks whether an attachment's file name matches one or more specified names. Use this condition with attachment-related trigger events to restrict when workflow actions run.

### Configure the condition

Choose an operator and enter one or more file names, including their extensions.

File name matching is case-insensitive and includes the file extension.

- **Equals**: The condition is met when the attachment's file name matches one of the specified names.
- **Not Equals**: The condition is met when the attachment's file name does not match any of the specified names.

## Example: Using `file-name` with the `on-attachment-added` event

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

In this example, the `on-attachment-added` trigger runs the `add-labels` action when an attachment named `review.pdf` is uploaded or restored to a page.

The `file-name` condition restricts the trigger to the specified attachment name, and the `needs-review` label is added to the current page.