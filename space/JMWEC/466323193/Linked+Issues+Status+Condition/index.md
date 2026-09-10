# Linked Issues Status Condition

A workflow condition that allows you to hide or show a particular transition from the list of available workflow actions based on the status of the issue's linked issues against certain conditions.

When you add this condition to a transition, the add-on checks the *Status* of the current issue's linked issues. If the linked issues of the specified issue link type and issue type respect the conditions specified against selected statuses, then the transition is available to the user. If not, the transition is hidden.

![Linked Issues Status configuration screen](/cms_trial/assets/45dc2ac4-847e-42a8-a827-79266c59f307.png)

**To add 'Linked Issues Status Condition' to a transition:**

1. Click **Edit** for the workflow that has the transition to which you wish to add the condition.
2. In the Workflow Designer, select the transition.
3. Click **Conditions** in the properties panel (or select the **Conditions** tab).
4. Click**Add condition**.
5. Select **Linked Issues Status Condition** from the list of conditions.
6. Click **Add.** The *Linked Issues Status Condition*screen will open, where you can configure the condition as needed. See below for more details on specific configurations.
7. Click **Add** to complete the configuration and add the condition.

## Configuration details

Configure the following:

- **Issue Link Type** - Select the issue link type that links the current issue to the linked issues to check the specified condition against.
- **Mode** - Select one of the following conditions the linked issue(s) must satisfy for the transition to be enabled:

  - **All issues must be in the selected statuses below** (default option)
  - **At least one issue must be in one of the selected statuses below**
  - **No issue must be in one of the selected statuses below**
  - **At least one issue must not be in one of the selected statuses below**
- **Issue Type** - Select the issue type of the linked issue(s) to check the specified condition against. Leave "Any (default option)" for no restrictions.
- **Statuses** - Select one or more statuses from the available list to check the specified condition against. Hold **Ctrl** to select multiple values, or select values one at a time to add them to the list. Use the **X** beside a value to remove it from the list.

The list of statuses that are displayed under the `Statuses` field has all the status values from across all workflows in your instance. This is because the workflow of an issue and that of its linked issues can be different.