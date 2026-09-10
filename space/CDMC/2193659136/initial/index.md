# initial

## Overview

One or more [conditions](/cms_trial/space/CDMC/2193852785/Trigger+conditions/)can be set for a trigger for a named[event](/cms_trial/space/CDMC/2193950329/Trigger+events/) in the workflow. Adding a condition is optional.

Adding the **Is Initial State** as a **True** condition to a trigger ensures it only listens for events that occur when the current state is the **initial state** of the workflow.

![Comala visual editor trigger with initial state condition and clean messages](/cms_trial/assets/57465cc1-0188-480d-9c6d-954dc49d69f1.png)

The condition is a Boolean value—**true** or **false**.

When the specified workflow event occurs, the trigger evaluates the condition. If the condition is met, it executes one or more defined actions.

To limit the initial condition to a specific state in the workflow, combine it with the **"state"** condition. When used together, both conditions are evaluated using an **AND** logic, meaning **both must be true** for the trigger to execute.

**JSON Condition**

`"initial":(boolean true/false)`

**JSON code**

```json
"conditions":
[
	{"initial":true}
],
```

**Note**

The trigger action occurs if the current state is the `initial` state.

The `initial` condition is constrained to a named state by including the [trigger state condition](https://appfire.atlassian.net/wiki/spaces/CDMCD/pages/656637975)

- `"conditions":[{"initial":true},{"state":"Review"}],`

The `initial` parameter value is a boolean

- `"initial":true`
- `"initial":false`

The `initial state` in Confluence Cloud is the first workflow state applied when a workflow is added to a document. It is the first state listed in the workflow template.

## Example trigger code

```text
{
      "event": "on-change-state",
      "conditions": [
        {
          "initial": true
        }
      ],
      "actions": [
        {
          "action": "clean-messages"
        }
      ]
}
```