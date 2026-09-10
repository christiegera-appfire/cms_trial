# remove-restrictions

## Overview

You can use the remove-restrictions action in a workflow trigger to remove page-level permissions from your document, for example, when an approval occurs or when transitioning to a different state in your workflow. This can be used to ensure that page-level restrictions do not block your documentation process.

![Comala visual editor removerestrictions trigger action configuration](/cms_trial/assets/68238cf3-c005-4fbf-be02-88304d5c52f3.png)

When the workflow trigger event occurs, the trigger checks that any required conditions are met, and if met, the `"remove-restrictions"` action removes page-level content view and edit restrictions from the current page, or a page specified using the **contentId**.

## `"remove-restrictions"`

The trigger action  `"remove-restrictions"` removes content view and edit restrictions for all users and groups.

- **action (*****remove-restrictions*****)**

  - **contentId** - the Confluence contentId of the page to remove page-level restrictions (optional)

    - If no contentId is added, the contentId of the current page is used.

### Example trigger code

A typical use of this trigger action is to remove all **view** and **edit** restrictions from the **final state** in a workflow.

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
		{"action": "remove-restrictions"}
	]}
]
```

In the app space settings, an administrator can configure the space to remove all page-level restrictions on transitioning to the **final state** of the active workflow.

Only '[Confluence Cloud Standard, Premium, and Enterprise Plans](https://support.atlassian.com/confluence-cloud/docs/learn-about-confluence-cloud-plans/) enable Atlassian Confluence users to edit [permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluence-cloud-permissions-and-restrictions/), including global, space, and page permissions.