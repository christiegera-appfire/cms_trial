# Current Status Condition

A workflow condition that lets you hide/show a particular transition from the list of available workflow actions based on the current status of the issue.

 This is especially useful to hide Global transitions from multiple statuses. The transition on which the condition is configured will be available only if the issue is in one of the selected status(es). When you add this condition to a transition, the add-on checks the current status of the issue. If the issue is in one of the selected statuses, then the transition will be available to the user. If not, the transition will be hidden.

![JMWE for Jira Cloud current status condition configuration with status selection options](/cms_trial/assets/e20da21d-b289-4aad-8163-42f2a74e56cd.png)

**To add 'Current Status Condition' to a transition:**

1. Click **Edit** for the workflow that has the transition you wish to configure the condition on.
2. In the Workflow Designer, select the transition.
3. Click **Conditions** in the properties panel.
4. Click **Add condition**.
5. Select **Current Status Condition** from the list of conditions.
6. Click **Add** to add the condition on the transition.
7. Select the current status(es) from the **Current Status** field.
8. Click **Add** to add the condition to the transition.