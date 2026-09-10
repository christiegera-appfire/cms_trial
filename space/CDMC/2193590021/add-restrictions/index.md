# add-restrictions

## Overview

You can use the **Add Restrictions** action to add Confluence page-level permissions for the users who you want to view or edit your document.

![Comala visual editor add view restrictions trigger with recipient examples](/cms_trial/assets/bcf4b0cd-2462-4b84-9ff3-c73eda6738b0.png)

This **Add Restrictions** trigger action can be used to ensure that users have view or edit permissions for a document at various stages in your documentation process, such as when an approval decision is made or the workflow advances to the next state.

To add both **view** and **edit** restrictions, you must include a separate **Add Restrictions** action in a workflow trigger for each restriction type.

Any existing page-level restrictions remain on the document. The action adds the specified permission to the users and groups included in the action.

## Add Restrictions action parameters

| **Action Parameter** | **Value** | **Notes** |
| --- | --- | --- |
| **Type** MANDATORY | Confluence page-level permissions to be added:   - **view** - **edit**   You must add a separate action for each. | Restricts the **view** or **edit** permission to the specified users   - does not remove any existing page-level permissions |
| **Restrictions** MANDATORY | Restrictions must be applied to at least one user. | At least one value must be added for one of the fields:   - **User** - **Confluence Smart Values** - **Workflow user type parameters** - **Group** - **Workflow group type parameters** |
| **User** | One or more Confluence users. | List of Confluence users   - type to search and select each user |
| **Confluence Smart Values** | One or more Confluence value references. | List of Confluence value references (Smart Values).  Only the following are supported:   - **@watchers** - **@creator** - **@lastUpdatedBy** |
| **Workflow user type parameters** | One or more workflow group type parameters. | List of workflow user type parameters   - add each workflow parameter as **@workflowuserparameter\_name@** |
| **Group** | One or more Confluence user groups. | List of Confluence user groups   - type to search and select each group |
| **Workflow group type parameters** | One or more workflow group type parameters. | List of workflow user type parameters   - add each workflow parameter as **@workflowgroupparameter\_name@** |

When the workflow trigger Event occurs, the trigger checks that any required Conditions are met, and if met, the **Add Restrictions** action adds Confluence page-level content view or edit restrictions to the current page.

## “add-restrictions” JSON code

An **Add Restrictions** workflow trigger action added using the visual editor is automatically displayed in the workflow code editor as an `“add-restrictions”` trigger action.

![Comala code editor addrestrictions trigger on state change event](/cms_trial/assets/0cd4c5d3-3eff-47f8-b472-51ceb6d46a4d.png)

You can also use the code editor to add the workflow trigger and the `“add-restrictions”` action.

## "add-restrictions" workflow parameters and workflow trigger code example

### `"add-restrictions"`

The trigger action  `"add-restrictions"` adds content view or edit restrictions for specified users.

- **action (*****add-restrictions*****)**

  - **type** **!** Type of permission to apply. Only one permission type can be added to each action.

    - **view** - assign view restrictions to one or more users or user groups
    - **edit** - assign edit restrictions to one or more users or user groups
  - **restrictions** **!** List of users and groups with the specified type of permission. At least one user or one user group value must be specified

    - **user** - comma-separated list of user IDs, user type workflow parameters, Confluence value references\*, or metadata

      - `{“user”: [ “userID”, @user_parameter@, @creator, @lastUpdatedBy, @watchers ]}`
    - **group** - comma-separated list of group IDs, group name, group type workflow parameters, or metadata

      - `{“group”: [ “groupID”, "groupName", @group_parameter@ ]}`

\*The following value references in Confluence Cloud are supported: **@creator**, **@watchers**, and **@lastUpdatedBy**.

---

### ❗️ Mandatory parameters

**type**

The `"type"` parameter value must be included. The **view** or **edit** value must be added

**restrictions**

The `"restrictions"` parameter value must be included. At least one value must be added for either the **user** or **group** parameter

Invalid values for the **user** or **group** parameter are ignored.

---

### \*Supported Confluence value references

- **@watchers**
- **@creator**
- **@lastUpdatedBy**

---

### Example trigger code

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
		{"action": "add-restrictions",
            "type": "view",
              "restrictions":
              [
                {"user": [ "5d52a37ef0f22a0da2d6f070", @creator, @lastUpdatedBy ]}
              ]
        },
        {"action": "add-restrictions",
              "type": "edit",
              "restrictions":
            [
              {"user": [ "c54d23a37ff0e11b0da2c6f160s", "@qa_editor@" ]},
              {"group": [ "confluence-developers", @qa_teamgroup@ ]}
    ]}
]
```

Each `“add-restrictions”` trigger action is typically used to add restrictions for a specified type of Confluence permission (**view** or **edit**) when a state change occurs. If you need to add both **view** and **edit** restrictions to a page, two separate `“add-restrictions”` actions are required.

The action adds additional page-level restrictions of the specified type to any page-level restrictions already on the document.

Only '[Confluence Cloud Standard, Premium, and Enterprise Plans](https://support.atlassian.com/confluence-cloud/docs/learn-about-confluence-cloud-plans/) enable Atlassian Confluence users to edit [permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluence-cloud-permissions-and-restrictions/), including global, space, and page permissions.