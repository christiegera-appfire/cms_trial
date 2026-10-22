# on label added

## Overview

The `on-label-added` trigger event runs when you add a label to a page. Use it to start workflow logic when to apply a label.

In the workflow editor, add the `on-label-added` trigger event. Add the workflow actions that should run when you add a label.

![image-20261022-103427.png](/cms_trial/assets/370a4a07-68ad-45a6-aa49-c9a469641c74.png)

You can pair this event with the **Added Label** condition so the workflow responds only to that label.

## Example `"on-label-added"` event

```json
"triggers":
[
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
            "editor"
          ],
          "children": false
            }
        ]
    }
]
```

The `on-label-added` event fires when a label is added to a page. The `added-label` condition limits this trigger to cases where the added label is `editor`. When the condition matches, the `add-labels` action adds the `editor` label to the page.