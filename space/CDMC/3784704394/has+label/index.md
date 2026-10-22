# has label

## Overview

The **has label** condition checks whether a page has one or more specified labels. You can use it with any trigger event.

### Configure the condition

Choose an operator and enter one or more labels:

- **Equals**: the condition is met if the page has **at least one** of the specified labels. When you enter multiple labels, they are evaluated as **OR**.
- **Not equals**: the condition is met only if the page has **none** of the specified labels.

## Example: Using `has-label` with `on-page-updated` event

```json
"triggers":
[
    {
        "event": "on-page-updated",
        "conditions":
        [
            {
                "has-label":
                {
                    "operator": "equals",
                    "value":
                    [
                        "test_1",
                        "test_2"
                    ]
                }
            }
        ],
        "actions":
        [
            {
                "action": "clean-messages"
            }
        ]
    }
]
```

In this example, the `on-page-updated` trigger runs the `clean-messages` action when the page has either the `test_1` label or the `test_2` label.