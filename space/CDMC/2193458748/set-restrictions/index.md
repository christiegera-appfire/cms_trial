# set-restrictions

## Overview

You can use the **Set Restrictions** action in a workflow trigger to remove existing Confluence page-level restrictions before applying new ones. This can be useful when an approval occurs or when a document transitions to a different workflow state.

![Comala visual editor set view restrictions trigger with recipient examples](/cms_trial/assets/169659b3-6a6f-461f-b40a-2e5d49ac6437.png)

The **Set Restrictions** trigger action lets you remove all existing page-level restrictions for a specific Confluence permission type and apply new restrictions in a single action.

A separate **Set Restrictions** action is required for each of the following:

- Removing existing **view** permissions and defining who can view the document
- Removing existing **edit** permissions and specifying who can edit the document

To remove and add both view and edit restrictions in a workflow trigger, include a **Set Restrictions** action for each restriction type.

## Set Restrictions action parameters

| **Action Parameter** | **Value** | **Notes** |
| --- | --- | --- |
| **Type** MANDATORY | Existing type of Confluence page-level permissions to be removed and added:   - **view** - **edit**   You must add a separate action for each type of permission. | Removes the existing specified type of permission restrictions and then restricts thepermission to the specified users.  Only one type of permission can be specified in each action:   - **view** - removes view permissions and adds **view** permissions for users specified in **Restrictions** - **edit** - removes edit permissions and adds **edit** permission for users specified in **Restrictions** |
| **Restrictions** MANDATORY | One or more users added using one or more of the following fields   - **User** - **Confluence Smart Values** - **Workflow user type parameters** - **Group** - **Workflow group type parameters**   At least one value must be added to one of these fields. | Restrictions must be applied to at least one user. |
| **User** | One or more Confluence users. | List of Confluence users   - type to search and select each user |
| **Confluence Smart Values** | One or more of the following:   - **@watchers** - **@creator** - **@lastUpdatedBy** | List of Confluence Smart values. |
| **Workflow user type parameters** | One or more workflow group type parameters. | List of workflow user type parameters   - add each workflow parameter as **@workflowuserparameter\_name@** |
| **Group** | One or more Confluence user groups. | List of Confluence user groups   - type to search and select each group |
| **Workflow group type parameters** | One or more workflow group type parameters. | List of workflow user type parameters   - add each workflow parameter as **@workflowgroupparameter\_name@** |

When the workflow trigger Event occurs, the trigger checks that any required Conditions are met, and if met, the **Set Restrictions** action removes existing Confluence page-level view or edit restrictions and adds page-level content view or edit restrictions specified in the action to the current page.

## “set-restrictions” JSON code

A **Set Restrictions** workflow trigger action added using the visual editor is automatically displayed in the workflow code editor as a `“set-restrictions”` trigger action.

![Comala setrestrictions trigger action with restriction type options](/cms_trial/assets/1c08837c-253e-4de0-87b6-594e4264a60d.png)

You can also use the code editor to add the workflow trigger and the `“set-restrictions”` action.

## "set-restrictions" parameters and workflow trigger code example

### `"set-restrictions"`

The trigger action  `"set-restrictions"` removes document view or edit restrictions for all users and adds view or edit restrictions for specified users.

- **action (*****set-restrictions*****)**

  - **type** **!** Type of permission to apply. Only one permission type can be added in each action.

    - **view** - remove all existing view restrictions and then assign view restrictions to one or more users or user groups
    - **edit** - remove all existing edit restrictions and then assign edit restrictions to one or more users or user groups
  - **restrictions** **!** List of users and groups with the specified type of permission. At least one user or one user group must be specified

    - **user** - comma-separated list of Confluence userIds, Confluence ser type workflow parameters, Confluence value references\*, or metadata

      - `{“user”: [ “userID”, @user_parameter@, @creator, @lastUpdatedBy, @watchers ]}`
    - **group** - comma-separated list of Confluence groupIds, Confluence group name, group type workflow parameters, or metadata

      - `{“group”: [ “groupID”, "groupName", @group_parameter@ ]}`

---

### ❗️ Mandatory parameters

**type**

The `"type"` parameter value must be included. The **view** or **edit** value must be added

**restrictions**

The `"restrictions"` parameter value must be included. At least one value must be added for either the **user** or **group** parameter

Invalid values for the **user** or **group** parameter are ignored.

---

### \*Supported Confluence value references

Only the following value references are supported in Confluence Cloud:

- **@creator**
- **@watchers**
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
		{"action": "set-restrictions",
            "type": "view",
              "restrictions":
              [
                {"user": [ "5d52a37ef0f22a0da2d6f070", @creator ]}
              ]
        },
        {"action": "set-restrictions",
              "type": "edit",
              "restrictions":
            [
              {"user": [ "confluence-editors", "@qa_editors@" ]}
    ]}
]
```

This trigger action is typically used when a state change occurs to remove all existing page-level restrictions for a specific Confluence permission type and apply new restrictions in a single action. You must use a separate `"set-restrictions"` action for each type of permission:

- remove **view** permissions and define new **view** restrictions
- remove **edit** permissions and define new **edit** restrictions

Only '[Confluence Cloud Standard, Premium, and Enterprise Plans](https://support.atlassian.com/confluence-cloud/docs/learn-about-confluence-cloud-plans/) enable Atlassian Confluence users to edit [permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluence-cloud-permissions-and-restrictions/), including global, space, and page permissions.