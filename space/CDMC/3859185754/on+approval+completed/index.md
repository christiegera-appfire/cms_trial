# on approval completed

## Overview

Use the **On approval completed** (`on-approve-completed`) trigger event to execute one or more workflow actions when an approval reaches its final approved outcome.

The event fires once, after all required reviewers have made their decisions and the approval is approved according to its configured rules.

You can add conditions to restrict when the trigger runs.

## Example: Send an email when an approval is completed

In this example, a workflow trigger sends an email notification when an approval reaches its final approved outcome in the **Approved** state.

```json
"triggers": [
  {
    "event": "on-approve-completed",
    "conditions": [
      {
        "state": {
          "operator": "equals",
          "value": [
            "Approved"
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
          "subject": "Approval completed",
          "body": "The approval has been completed successfully."
        }
      }
    ]
  }
]
```

The trigger sends an email notification to the specified recipient when the approval reaches its final approved outcome.

The **State** condition restricts the trigger to approvals in the **Approved** state.