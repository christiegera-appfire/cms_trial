# assign

## Overview

You can use the **Assign** workflow trigger action to assign reviewers to an approval. You can use the action to assign a Confluence user and the members of a Confluence user group as reviewers.

![Comala visual editor assign trigger action with user and group values added](/cms_trial/assets/8e6d02e6-f55a-49f0-a4f8-cbba7e1d7a53.png)

Approval assignees can be either a single Confluence user or all members of a Confluence group.

By default, assignees are added as reviewers to the first approval in the workflow state specified in the trigger condition (the **default approval**). However, you can choose to assign reviewers to a specific approval within a particular workflow state.

You can also specify a Confluence user as the assigner. If no assigner is defined, the assigner defaults to the **Comala Document Management app** add-on user.

## Assign action parameters

| **Action Parameter** | **Value** | **Notes** |
| --- | --- | --- |
| **User** MANDATORY | Confluence username   - can be empty if a **Group** value is added   Only one user can be added. | Assign a selected Confluence user as a reviewer.  You must add a user if a **Group** value is empty. |
| **Group** MANDATORY | Confluence user group name.   - can be empty if a **User** value is added   Only one user group can be added. | Assign members of a selected Confluence user group as reviewers.  You must add a user group if the **User** value is empty. |
| **Assigner** | The user who is added as the assigner   - if no value is added, the app add-on user is added as the assigner |  |
| **Approval** | Approval to assign the reviewers,   - if no approval is specified, users are assigned to the **default approval** | Any approval in any state in the workflow can be selected.  The **default approval** is the approval in the state named in the trigger event condition.  Ifthe state has**multiple approvals**, the **default approval** is the first approval listed in the state. |
| **Comment** | Text comment for the assignee. | Text comments are included with the assignment activity entry in the document activity report. |

When the workflow event occurs, the trigger checks that any required conditions are met, and if met, the **Assign** action assigns the specified user and members of a specified user group as reviewers to an approval.

## “assign” JSON code

An **Assign** workflow trigger action added using the visual editor is automatically displayed in the workflow code editor as an `“assign”` trigger action.

![Comala code editor assign trigger action with user and group](/cms_trial/assets/c820d378-b286-4543-8e62-a7830af0e9e0.png)

You can also use the code editor to add the workflow trigger and the `“assign”` action.

## "assign" parameters and workflow trigger code example

### `"assign"`

The trigger action `"assign"` assigns a user to a named approval.

- **action (*****assign*****)**

  - **approval** - the name of the approval to assign. If not specified, the **default approval**† is used
  - **assigner -** Atlassian  `userID` for the assigner (if no value is added, the app add-on user is the assigner for the action)
  - **user ❗️**Atlassian `userID` for the assignee (accepts one value only)
  - **group❗️** Atlassian `groupID` or `groupName` for assignees (accepts one value only)
  - **comment** - comment for the assignment operation

Only one user and one group can be assigned in a single `"assign"` action. You cannot add multiple values for the **user** or **group** parameters.

### ❗️ **Mandatory parameters**

**user and group parameters for assignees**

At least one value must be added for an assignee (using either a **user** or a **group**).

The **user** parameter value must be specified unless a group is specified using the **group** parameter.

### **† Default approval**

If **no approval name is specified** in the trigger action, the **default approval** is the approval in the state named in the trigger event condition.

Ifthe state has**multiple approvals**, the **default approval** is the first approval listed in the state's JSON code.

---

### Example trigger code

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"state":"Review"}
	],
	"actions":
	[
		{"action": "assign",
			"approval": "Triagereview",
			"user": "5d52a37ef0f22a0da2d6f070",
			"group": "qa_reviewers"}
	]}
]
```

When assigning a reviewer, the **user** parameter only accepts one **userID** value.

The Atlassian User Identification Number (userId) is visible in the URL when viewing the **User Profile.**

![Comala assign trigger action code example](/cms_trial/assets/f8c0187e-ec3b-4ee6-9da9-90d907f8d854.png)

To assign multiple users as reviewers, use a Confluence group instead of specifying individual users by using the **group** parameter. You can reference the group using either its **group ID** or **group name**, for example:

`"group": "qa_reviewers"`

Here, `"qa_reviewers"` is the name of a Confluence group.

You can use the [“unassign” trigger action](/cms_trial/space/CDMC/2193659043/unassign/) to remove a Confluence user as an assignee for an approval.