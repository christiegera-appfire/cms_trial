# on rejection completed

## Overview

Use the **On rejection completed** (`on-reject-completed`) trigger event to execute one or more workflow actions when an approval reaches its final rejected outcome.

The event fires once, after all required reviewers have made their decisions and the approval is rejected according to its configured rules.

You can add conditions to restrict when the trigger runs.

## Example: Send an email when an approval is rejected

In this example, a workflow trigger sends an email notification when an approval is finally rejected in the **Draft** state.

```json
"triggers": [
  {
    "event": "on-reject-completed",
    "conditions": [
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
        "action": "send-email",
        "recipients": [
          "reviewer@example.com"
        ],
        "notification": {
          "subject": "Approval rejected",
          "body": "The approval has been rejected. Review the page and make the necessary changes."
        }
      }
    ]
  }
]
```

The trigger sends an email notification to the specified recipient when the approval reaches its final rejected outcome.

The **State** condition restricts the trigger to approvals in the **Draft** state.