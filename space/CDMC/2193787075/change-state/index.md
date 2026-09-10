# change-state

You can use the **Change State** action in a trigger to automatically update the workflow state in response to a workflow event.

![Comala visual editor changestate trigger with named state condition](/cms_trial/assets/47c7a876-20f2-481f-9c73-cff719ef094d.png)

For example, it can be used to fast-track a single reviewer’s rejection decision when multiple reviewers are assigned to an approval.

![Comala visual editor changestate trigger on reviewer rejected event](/cms_trial/assets/9b632005-f792-4eb9-aa46-026081d96a1e.png)

## Change State action parameters

| **Action Parameter** | **Value** | **Notes** |
| --- | --- | --- |
| **State** MANDATORY | Use the dropdown to select one of the states in the workflow. | The state options are populated by the states in the workflow.  Changing the state name in the workflow might cause a validation error |

You can add a **Change State** action to a workflow trigger. When the workflow Event occurs, the trigger checks that any required Conditions are met, and if they are met, the **Change State** action forces a change of the state to a specified state.

This lets you respond flexibly to workflow events, such as when a single reviewer approves a page.

## “change-state” JSON code

A **Change State** workflow trigger action added using the [visual editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/) is automatically displayed as the `“change-state”` trigger action in the workflow code editor.

![Comala code editor changestate trigger on rejected event](/cms_trial/assets/3fb32a3a-17a2-4ce6-a61b-c6466a24be72.png)

You can also use the code editor to add the workflow trigger and the `“change-state”` action.

## "change-state" parameters and workflow example code:

### `"change-state"`

The trigger action `"change-state"` causes the state to change to the specified state if the provided parameters are valid.

- **action (*****change-state*****)**

  - **state❗️** destination workflow state for the action

    - state must be a state in the workflow
    - state names are case-sensitive

**❗️ Mandatory parameter**

- **state parameter**
- state parameter must be included with a valid value for the destination state

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
		{"action": "change-state",
			"state": "Archive"}
	]}
]
```

The example trigger listens for the workflow's change of state to the final state and immediately moves the workflow to the **Archive** state.

The destination state must be included in the `"change-state"` action.

Here is the JSON code for the example trigger that fast-tracks a single rejected decision. You can use this to prompt remedial actions quickly, for example, when multiple reviewers are assigned to an approval.

```text
"triggers":
[
	{"event": "on-reject",
	"conditions":
	[
		{"state":"Review"}
	],
	"actions":
	[
		{"action": "change-state",
			"state": "Draft"}
	]}
]
```

The trigger action moves the workflow from the **Review** state, which contains an approval, to the **Draft** state when a reviewer rejects the page.