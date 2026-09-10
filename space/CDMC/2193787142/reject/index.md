# reject

## Overview

You can use this action in a workflow trigger to reject a workflow approval. This action completes the approval (as a rejection) even if there are pending assigned reviewer decisions or a reviewer approval decision.

![Comala reject trigger action configuration dialog](/cms_trial/assets/445e2f8f-15d6-4870-9948-e3e1e4ab10f9.png)

The **reject action** requires that you specify a user. This user is logged in the document activity report as the rejecting reviewer.

By default, the approval action applies to the first named approval in the workflow state specified by the trigger event. Optionally, you can configure the reject action to target a different approval within the workflow.

When the workflow trigger event occurs, the trigger checks that any required conditions are met, and if met, the `"reject"` action rejects a named approval.

## `"reject"`

The trigger action `"reject"` sets a rejected decision for a named approval if the provided parameters are valid.

- **action (*****reject*****)**

  - **approval**Name of the approval to be rejected. If not specified, **default approval****†** is used
  - **user ❗️** Atlassian `userID` of the rejector

### **❗️ Mandatory parameter**

**user**

The trigger action must define a value for the user parameter for the **reject** action to take place.

### †Default approval

If the trigger action does not specify a named approval, the action uses the **default approval** in the workflow.

The **default approval** is the approval in the state named in the trigger event condition. If there are multiple approvals in the state, the default approval is the first approval listed in the JSON markup.

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
		{"action": "reject",
			"approval": "Sign-off",
			"user":"5d52a37ef0f22a0da2d6f070"}
	]}
]
```

The Atlassian user Identification Number (`userId`) is visible in the URL when viewing the **User Profile**.

![Comala reject trigger action code example](/cms_trial/assets/04726d98-dd67-4b16-9623-314c8c4e2554.png)