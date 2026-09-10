# clean-labels

## Overview

Use the **clean labels action** in a workflow trigger to remove all the Confluence labels from the page or blog post with the applied workflow.

![Comala cleanlabels trigger action applied to page only](/cms_trial/assets/e1c50349-284d-41c9-863a-55d730f59033.png)

Additionally, you can configure this action to remove all labels only from **direct child pages** of a document with the applied workflow.

When the **Clean only from child pages** configuration is **True**, all labels are removed from the **immediate children** of the page, but not from the parent page itself or any further level of child pages.

![Comala cleanlabels trigger action applied to immediate child pages only](/cms_trial/assets/e99f06d9-b6a9-4522-b335-4cd7d59b57c5.png)

When the workflow trigger event occurs, it checks that any required conditions are met, and if they are, the `"clean-labels"` action removes all Confluence labels.

The workflow trigger label actions are part of a gradual rollout of new features and are not immediately available to all our customers.

## `"clean-labels"`

The `"clean-labels"` action removes all the labels on the document.

- **action (*****clean-labels*****)**

  - **Children** remove all labels from the direct child pages, but not from the parent page itself or any further level of children

    - boolean `true` or `false`

      - the default value is `"children": false`. All labels are removed from the current page
      - when the value is `"children": true`. All labels are removed from the direct child pages. All labels are removed only from the **immediate children** of the page - not from the parent page itself or any further level of child pages

If the `"children"` parameter is not included in the workflow trigger code, the default value `false` is used, and labels are only removed from the page with the applied workflow.

### Example trigger code

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"final":true}
	],
	"actions":
	[
		{"action": "clean-labels"}
	]
	}
]
```

The above `trigger` listens for a state change event to the **final** state in the workflow and removes all the labels from the document. The trigger action is ignored if there are no labels on a page.

The workflow trigger below uses the `"clean-labels"` action with `"children": true` to remove all the labels from the direct child pages on the transition to the **final** state.

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"final": true}
	],
	"actions":
	[
		{"action": "clean-labels",
		"children": true
		}
	]}
]
```

All the labels are removed from the immediate direct child pages of the page with the applied workflow.

However, no labels are removed from

- the page with the applied workflow or
- any subsequent children in the page tree

One or more specified labels can be removed using the `"remove-labels"` trigger action.