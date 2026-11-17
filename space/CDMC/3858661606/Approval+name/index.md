# Approval name

## Overview

The **Approval Name** condition checks whether an approval matches a specified name. Use this condition with approval-related trigger events to restrict when workflow actions run.

### Configure the condition

Choose an operator and select one or more approval names from the dropdown list.

The dropdown displays the approval names configured in the workflow.

- **Equals**: The condition is met when the approval name matches one of the selected names.
- **Not Equals**: The condition is met when the approval name does not match any of the selected names.

## Example: Using `approval-name` with the `on-approve-completed` event

```json
"triggers": [
  {
    "event": "on-approve-completed",
    "conditions": [
      {
        "approval-name": {
          "operator": "equals",
          "value": [
            "Approval"
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

In this example, the `on-approve-completed` trigger runs the `send-email` action when the approval named `Approval` reaches its final approved outcome.

The `approval-name` condition restricts the trigger to the specified approval, and an email notification is sent to the specified recipient.