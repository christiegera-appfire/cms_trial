# approve

## Overview

You can use this action in a workflow trigger to approve a workflow. This action completes the approval, even if there are pending assigned reviewer decisions or a reviewer rejection decision.

![Comala approve trigger action configuration dialog](/cms_trial/assets/736a0cd9-7742-439e-b5e9-ef6464324bf3.png)

The **approve action** requires that you specify a user. This user is logged in the document activity report as the approving reviewer.

By default, the approval action applies to the first named approval in the workflow state specified by the trigger event. You can optionally configure the action to target a different approval within the workflow.

When the workflow trigger event occurs, the trigger checks that any required conditions are met, and if met, the `"approve"` action approves a named approval.

## `"approve"`

The trigger action "`approve"` sets an approved decision for a named approval if the provided parameters are valid.

- **action (*****approve*****)**

  - **approval** Name of the Approval. If not specified, the **default approval**† is used
  - **user❗️** Atlassian `userID` of the approver

---

### **❗️ Mandatory parameter**

**user**

The trigger action must define a value for the user parameter for the **approve** action to take place.

---

### † Default approval

If **no approval name is specified** in the trigger action, the **default approval** is the approval in the state named in the trigger event condition.

Ifthe state has**multiple approvals**, the **default approval** is the first approval listed in the state's JSON markup.

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
		{"action": "approve",
			"approval": "Sign-off",
			"user":"5d52a37ef0f22a0da2d6f070"}
	]}
]
```

The Atlassian user Identification Number (`userId`) is visible in the URL when viewing the **User Profile**.

![Comala approve trigger action code snippet](/cms_trial/assets/9b39984f-e946-481c-858e-5ffd9ce94bbc.png)

You can add or edit a workflow trigger using the workflow visual editor. For the JSON code example above:

![Comala visual editor trigger with state changed and final approve action](/cms_trial/assets/ebdf73e0-04f2-4d7b-ae85-6db6a1ba47bd.png)

This includes the **Approve** action for the **Sign-off** approval.

![Comala visual editor approve trigger with signoff approval](/cms_trial/assets/552a07d3-3ae0-4df7-8e37-1f5c0fadc658.png)