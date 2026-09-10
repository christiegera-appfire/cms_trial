# Guide to JSU error messages

This page provides information about the different types of errors that can occur in JSU Cloud and actions you can take to resolve them. The messages below are listed alphabetically by error title.

If a JSU rule execution fails, JSU displays an error message and records the error in the [Execution Log](/cms_trial/space/JSUCLOUD/138149902/Execution+Log/).

### Field does not exist

This error occurs when a field to be actioned does not exist. This can happen if you configure your workflow and then later delete the field defined in the configuration from the origin or target work item. The message includes the field component ID.

**Solution**: In the rule that produced the error, update the field component with a valid field then publish the workflow again.

---

### Field was not found on screen

This error occurs when a field is absent from the specified screen type. The message includes the post function, relevant field ID, work item type, and screen type.

**Solution**: Add the missing field to the specified screen type. Alternatively, set the Perform as User option to `JSU Add-On User` in the specified post function to override this requirement.

If this error occurs for a Create Linked Issue post function, add the missing field to the Create transition screen. The perform as JSU Add-on user option can’t override missing fields on the Create transition.

---

### Invalid workflow rule configuration

This error occurs when a rule is configured so that it can’t be executed. This can be because of missing parameters or incorrect or incompatible options selected in the configuration. For example, you may have configured a Create a Linked Issue post function where the work item type for the new work item and the work item relation were not compatible.

**Solution**: Review the rule, make any necessary adjustments then publish the workflow again. If you can’t identify the problem, contact our support team, referencing the log ID provided in the error message.

---

### JSU can’t find the transition ID

This is an internal error with JSU that occurs when it can’t identify a transition ID.

**Solution**: Contact Appfire Support referencing the log ID provided in the error message.

---

### JSU encountered an internal error

An internal error occurs with JSU and not with your configuration. You do not need to make any changes to your workflow to resolve this error.

**Solution**: Try refreshing your browser page. If the error persists, contact our support team.

---

### Missing permissions

This error occurs when the Perform As User (or actor) defined for a post function does not have the necessary permissions to perform the action following a transition. For example, you have configured the Update Any Issue Field post function to change the assignee when a work item moves to IN PROGRESS but set the Perform As User to a named user who does not have permission to change the *Assignee* field.

**Solution**: Change the [Perform As User](https://appfire.atlassian.net/wiki/spaces/JSU/pages/12682394) to a different user with the required permissions, or use the JSU Automation Suite for Jira Workflows user. This user setting contains all the necessary permissions to perform your rule actions.

---

### No work item found

This error occurs when JSU can’t find the work item to be actioned. For example, you configure a Linked Issue post function to action a subtask of the work item in the transition, but the work item does not have any subtasks.

**Solution**: Change the work item relation type for the post function or create the required work items for the selected relation type, for example, add subtasks to the triggering work item. See [Related Issues](/cms_trial/space/JSUCLOUD/12518756/Related+issues/) to learn more.

---

### Required field missing

*(Create a Linked Issue post function)*

This error occurs when a value for a required field is missing for the new work item, and therefore, it can’t be created for the selected work item type.

**Solution**: Set the field as optional in your Jira field configuration or change the selected work item type in the post function configuration.

---

### Required field missing

*(Transition screen)*

This error occurs when a value for a required field for a transition screen is not provided. The message contains the name of the missing field.

**Solution**: In Jira, set the field as optional or add an update field component for the required field.

---

### Transition can’t be completed

This error occurs if a work item in a source status does not have a transition to the destination status.

**Solution**: Choose a valid destination status in your transition work item component, or modify the corresponding workflow to create a transition from the source status to the destination status.

---

### Transition caused infinite loop

This message is displayed when an automation rule results in an endless cycle of work item creation and follow-up transitions following the triggering of the origin work item. Performing this transition would result in an infinite loop, so JSU stops it to protect your system.

**Solution**: Review your automations across all apps, including built-in automation. Automations that trigger follow-up automations should be reviewed, changed, or removed. If you need help, contact Appfire Support referencing the log ID

See [Infinite loop detection](/cms_trial/space/JSUCLOUD/256770940/Infinite+loop+detection/) to learn more.

---

### Transition does not exist

This error can occur if the transition configured for the rule has been deleted or is hidden by a workflow condition.

**Solution***:* Update the transition work item component with a valid transition, or change the workflow itself and implement a valid transition to use in the rule.

---

### Validation rejected the transition

This error occurs when a validator (check) rejects the transition.

**Solution**: Change or remove the validator from the workflow. Alternatively, update the rule so that it complies with the selected validator. If you have multiple workflow apps installed, check if any conditions or validators configured are affecting your JSU rules.

See [Workflow validators](/cms_trial/space/JSUCLOUD/12518578/Workflow+validators/) to learn more.