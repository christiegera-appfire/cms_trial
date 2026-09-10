# add-labels

## Overview

You can use the **Add Labels** action in a workflow trigger to automate adding one or more labels to a page or blog post. This can help reduce inconsistencies in document labeling and reduce your team's manual workload.

![Comala addlabels trigger action with two labels applied to page only](/cms_trial/assets/881e7441-6ab7-44f3-9a20-339c1fd5e823.png)

When you set the **Add only to child pages** configuration to **True**, labels are applied to the page's **immediate children** but not to the parent page itself or any further level of child pages.

![Comala addlabels trigger action with two labels applied to immediate child pages only](/cms_trial/assets/663497f0-adfc-4ccc-ba7c-c0d35ad08d35.png)

## Add Labels action parameters

| **Action Parameters** | **Value** | **Notes** |
| --- | --- | --- |
| **Labels** MANDATORY | One or more Confluence labels | At least one label must be added. |
| **Add only to child pages** | Dropdown option:   - **False** (default) - **True** | When set to **True**, label(s) are added to the immediate child pages of the current page. |

When the workflow Event occurs, the trigger checks that any required Conditions are met, and if they are, the **Add Labels** action adds one or more specified labels to a document or its immediate child pages.

This Add Label trigger action is part of a gradual rollout of new features and is not immediately available to all our customers.

## “add-labels” JSON code

An **Add Restrictions** workflow trigger action added using the visual editor is automatically displayed as an `“add-restrictions”` trigger action code editor.

![Comala code editor showing addrestrictions trigger configuration](/cms_trial/assets/0e6739ab-ad0f-44a5-ae44-e8de54118a8e.png)

You can also use the code editor to add the workflow trigger and the `“add-restrictions”` action.

## "add-labels" parameters and workflow

### `"add-labels"`

The trigger action `"add-labels"` adds one or more specified labels to either

- a document (page or blog post) with the applied workflow
- the immediate direct child pages of the document with the applied workflow (but not the parent page itself or any further levels of child pages)
- **action (*****add-labels*****)**

  - **labels ❗️** At least one label (as a text string) must be added

    - labels added as an array inside square brackets [ ], for example, `"labels": ["stale"]`
    - add a comma-separated list to add multiple labels, for example, `"labels": ["stale", "in_review"]`
  - **Children** add specified labels to direct child pages, but not to the parent page itself or any further level of children

    - boolean `true` or `false`
    - default value is `"children": false`, specified labels are added to the current page only
    - when the value is `"children": true`, specified labels are added to the direct child pages. Labels are applied only to the **immediate children** of the page - not to the parent page itself or any further level of child pages

If the `"children"` parameter is not included in the workflow trigger code, the default value `false` is used, and the specified labels are only added to the page with the applied workflow.

---

### **❗️**Mandatory parameters

**labels**

You must include at least one label value.

---

### Workflow trigger example

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
		{"action": "add-labels",
		"labels": ["stale","in_review"]
		}
	]}
]
```

The above `trigger` listens for a state change event to the **Expired** state and adds the labels **stale** and **in\_review** to the document.

The workflow trigger below uses the `"add-labels"` action with `"children": true` to add the specified labels to the page's immediate child pages on the transition to the **Policy** state.

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"state":"Policy"}
	],
	"actions":
	[
		{"action": "add-labels",
		"children": true,
		"labels": ["policy"]
		}
	]}
]
```

For example, applying the workflow to the page, **HR policies** with the following child page tree:

![Comala Confluence page tree structure](/cms_trial/assets/70481919-f9aa-4cba-bb72-eecc5409ed8e.png)

- only adds the **policy** label to the immediate direct child pages, **Wellness policy**, **Staff support policy**, and **Leave policy**

![Comala page tree with labels added to immediate child pages](/cms_trial/assets/74a28a7c-d023-4bfe-927c-419f2ee2bfdf.png)

The workflow trigger does not apply the **policy** label to the **HR policies** page or any subsequent children in the page tree, such as the **Wellness survey** **page**.

You can remove specific labels using the [remove-labels trigger action](/cms_trial/space/CDMC/2193787135/remove-labels/), or all labels on a page can be removed using the [clean-labels trigger action.](/cms_trial/space/CDMC/2193491914/clean-labels/)