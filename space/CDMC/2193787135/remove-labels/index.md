# remove-labels

## Overview

You can use the **remove-labels action** in a workflow trigger to automate the removal of one or more specified labels from a page or blog post. This workflow trigger action can help reduce inconsistencies in document labeling and reduce the manual workload for your team.

![Comala removelabels trigger action for page only with two labels](/cms_trial/assets/138d1385-83ab-4808-b244-fb3938e2329d.png)

Additionally, you can configure this action to only remove labels from **direct child pages** of a document with the applied workflow.

When the **Remove only from child pages** configuration is **True**, the specified labels are removed from the **immediate children** of the page, but not from the parent page itself or any further level of child pages.

![Comala removelabels trigger action for immediate child pages only](/cms_trial/assets/36cf0bd7-9f92-444a-b121-51c283281586.png)

When a workflow trigger event occurs, the system checks if all required conditions are met. If they are, the **remove-labels** action deletes one or more specified labels from the document or its immediate child pages.

The workflow trigger label actions are part of a gradual rollout of new features and are not immediately available to all our customers.

## `"remove-labels"`

The trigger action `"remove-labels"` removes one or more specified labels from

- a document (page or blog post) with the applied workflow
- the immediate direct child pages of the document with the applied workflow (but not the parent page itself or any further levels of child pages)
- **action (*****remove-labels*****)**

  - **labels ❗️** At least one label (as a text string) must be added

    - labels removed are included as an array inside square brackets [ ], for example, `"labels": ["public"]`
    - add a comma-separated list to remove multiple labels, for example, `"labels": ["public", "approved"]`
  - **children** remove the specified labels from the child pages, but not from the parent page itself or any further level of child pages

    - boolean `true` or `false`

      - the default value is `"children": false`: specified labels are removed from the current page only
      - when the value is `"children": true`: specified labels are removed from the direct child pages. Labels are removed from the **immediate children** of the page - not from the parent page itself or any further level of child pages

If the `"children"` parameter is not included in the workflow trigger code, the default value is `false,` and the specified labels are only removed from the page with the applied workflow.

### **❗️**Mandatory parameters

**labels**

At least one label value must be included.

### Trigger example

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"state":"Expired"}
	],
	"actions":
	[
		{"action": "remove-labels",
		"labels": ["public","approved"]
		}
	]}
]
```

The above `trigger` listens for a state change event to the **Expired** state and removes the labels **public** and **approved** from the document.

The trigger below uses the `"remove-labels"` action with `"children": true`, to remove the specified labels from the direct immediate child pages of the page on the transition to the **Draft** state.

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"state":"Draft"}
	],
	"actions":
	[
		{"action": "remove-labels",
		"children": true,
		"labels": ["draft"]
		}
	]
	}
]
```

The **policy** label is removed from the immediate direct child pages of the page with the applied workflow

- However, it is **not** removed from:

  - the **parent** page
  - any subsequent children in the page tree

Specific labels can be added using the `"add-labels"` trigger action. All labels can be removed using the `"clean-labels"` trigger action.