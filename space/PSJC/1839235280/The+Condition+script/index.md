# The Condition script

The Condition script lets you define whether an action should be:

- Available for users to execute
- Visible but disabled (shown but unable to be executed)
- Completely hidden from the user interface

## Default configuration

When you add a new action, it includes this default Condition script:

```text
number ENABLED = 1;
number DISABLED = 2;
number HIDDEN = 3;

return ENABLED;
```

This default makes your action immediately available to all users.

The script returns one of the three predefined state variables

| **Variable** | **Value** | **Behavior** |
| --- | --- | --- |
| `ENABLED` | `1` | Action is fully available for users to execute. |
| `DISABLED` | `2` | Action button appears but is greyed out and cannot be clicked |
| `HIDDEN` | `3` | Action is completely invisible in the UI. |

## How to create dynamic conditions

Because Condition scripts use [SIL](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489652), you can create sophisticated rules based on issue properties, user permissions, or other factors.

```text
// Define the three possible state variables
number ENABLED = 1;
number DISABLED = 2;
number HIDDEN = 3;

i// Determine action state based on conditions
if(<some_condition>){
	return ENABLED;  // Action will be available if this condition is true
}
if(<some_other_condition>){
	return DISABLED; // Action will be visible but disabled if this condition is true
}
return HIDDEN;       // Action will be hidden if no conditions above are met
```

### Example

This example Condition script creates intelligent, context-aware behavior for your custom action:

```text
number ENABLED = 1;
number DISABLED = 2;
number HIDDEN = 3;

if(status == "In Progress"){
    return ENABLED;
}

if(priority == "High" && status != "In Progress"){
    return DISABLED;
}

return HIDDEN;
```

Here’s what the script does:

- The action will be fully available only when an issue is in *In Progress* status.
- The action will be visible but disabled for high-priority issues that aren't in *In Progress* status. This provides a visual cue that the action exists but isn't currently applicable.
- The action will be completely hidden for all other issues, that is for all low or medium priority issues that aren't in *In Progress*.

This type of smart visibility control helps keep your Jira interface clean and intuitive by only showing relevant actions based on the current context of the issue.