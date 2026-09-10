# unassign

## Overview

You can use the **Unassign** workflow trigger action to unassign a reviewer from an approval, for example, when the reviewer’s decision is no longer required.

![Comala visual editor unassign trigger action with parameter values](/cms_trial/assets/ebcf850d-fd59-4318-bf60-2600810af9ae.png)

The **Unassign** action is used to unassign a single Confluence **User**. It occurs regardless of the reviewer’s current approval decision status.

By default, the user is unassigned from the first approval in the state named in the trigger condition (the **default approval**). Alternatively, you can choose a specific approval in one of the workflow states. Unless specified, the **Comala Document Management** app add-on user is added as the **Assigner** who unassigns the reviewer.

## Unassign action parameters

| **Action Parameter** | **Value** | **Notes** |
| --- | --- | --- |
| **User** MANDATORY | Confluence user   - one Confluence user | Confluence user to unassign |
| **Approval** | Approval to unassign the reviewer from   - if no approval is specified, the user is unassigned from the **default approval** | Any approval in any state in the workflow can be selected.  The **default approval** is the approval in the state named in the trigger event condition.  Ifthe state has**multiple approvals**, the **default approval** is the first approval listed in the state. |
| **Assigner** | The user who is added as an unassigned reviewer   - If no value is added, the app add-on user is added |  |
| **Comment** | Text comment for the unassign action | Text comments are included with the unassigned activity entry in the document activity report. |

When the workflow event occurs, the trigger checks that any required conditions are met, and if met, the **Unassign** action unassigns a single user as a reviewer from an approval.

## “unassign” JSON code

**Unassign** workflow trigger action added using the visual editor is automatically displayed in the workflow code editor as an `“unassign”` trigger action.

![Comala code editor unassign trigger action configuration](/cms_trial/assets/5c25896e-515f-467a-9b2f-a23cef917346.png)

You can also use the code editor to add the workflow trigger and the `“unassign”` action.

## "unassign" parameters and workflow trigger code example

### `"unassign"`

The trigger action `"unassign"` unassigns a user to a named approval.

- **action (un*****assign*****)**

  - **approval** - the name of the approval to assign. If not specified, the **default approval**† is used
  - **assigner** -Atlassian  `userID` for the un-assigner (if no value is added, the app add-on user is the un-assigner for the action)
  - **user ❗️**Atlassian  `userID` to unassign
  - **comment** - comment for the assignment operation

---

### ❗️ Mandatory parameter

**user parameter for the user to be unassigned**

The **user** paramet*er* value must be specified with the`"unassign"`action parameter.

---

### **† Default approval**

If **no approval name is specified** in the trigger action, the **default approval** is the approval in the state named in the trigger event condition.

Ifthe state has**multiple approvals**, the **default approval** is the first approval listed in the state's JSON markup.

---

### Example trigger code

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{state: "Draft"}
	],
	"actions":
	[
		{"action": "unassign",
			"approval": "Triagereview",
			"user": "5d52a37ef0f22a0da2d6f070"}
	]}
]
```

The Atlassian user Identification Number (`userID`) is visible in the URL when viewing the **User Profile**.

![Comala unassign trigger action code example](/cms_trial/assets/bff5489d-147d-4fc8-a731-f5dbcdad9cb2.png)

## Example

We can use the **Unassign** trigger action to remove a user as a reviewer in a state with multiple approvals.

For example, we have two approvals in the following **Rejected** state, each with assigned reviewers.

![Comala workflow popup with multiple approvals and assigned reviewers](/cms_trial/assets/d7639a9f-7abf-44a8-af75-3d9776229a84.png)

You can add the following workflow trigger with an **Unassign** action.

![Comala visual editor rejected trigger with unassign action in rejected state](/cms_trial/assets/ee684b07-cba7-497f-91d2-3c8ec0368bf0.png)

The **Unassign** action is added to remove a user from a rejected decision in the **Rejected** state.

![Comala visual editor unassign action in rejected state with no selections](/cms_trial/assets/494d1644-51ff-4ac5-99be-e948ebd158ba.png)

As the approval is not named in the trigger action, the assigned user is removed from the **default approval**, the **Primary** approval.

![Comala unassign trigger action workflow result](/cms_trial/assets/0d14019d-a35b-42da-9a06-4192b5e172b1.png)

The default approval is the approval in the state used in the workflow trigger condition. If there are multiple approvals in the state, this is the first approval listed in the state.

When the reviewer is unassigned, an entry is added to document activity for the page.

![Comala document report showing unassigned reviewer from trigger event](/cms_trial/assets/abeb639e-d468-4d8a-a257-7f267f842979.png)

In this example, a rejected event for either of the two approvals in the named state causes the **unassigned** trigger action.