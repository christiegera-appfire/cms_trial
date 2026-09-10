# Clear Field Value post function

**Want to try a new way of creating this post function?**

We’re working to make it even easier for you to build workflow rules with JSU. A simplified version of this post function is now available in our [Universal Rule Builder](/cms_trial/space/JSUCLOUD/12517805/Universal+Rule+Builder/), a new editor experience currently in beta.

## Description

The Clear Field Value post function clears the specified field after a transition is completed. This can be a system or a custom field. The field can be on the issue in transition(within the same issue) or on a related issue, such as a subtask, a linked issue, or an issue within an Epic (during the transition on the Epic). For example, if an issue is moved to re-open, you might want to clear the fix version or due date so new values can be entered.

See [Workflow post functions](/cms_trial/space/JSUCLOUD/12518401/Workflow+post+functions/) to learn how to add a JSU post function to a Jira workflow.

## Configuration

You can add any number of fields to be cleared. Select the **Add** button `+` to add additional fields to your configuration. In the example below, the `Flagged` and `Due Date` fields will be cleared following the transition.

![Screenshot of the Clear Field Value post function configuration page.](/cms_trial/assets/ecc1b48f-485b-4c67-a477-fd61049fafc8.png)

### Precondition

If you are using preconditions with a JSU post function, they can be evaluated in the following ways:

- **True** (Precondition must be true to execute the post function)
- **False** (Precondition must be false to execute the post function)

Learn more about JSU preconditions in [Workflow Preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/) or see our [use cases](/cms_trial/space/JSUCLOUD/12518052/Update+an+issue+only+in+certain+conditions/) for examples.

### Issue Relation

Several of JSU's workflow post functions have the option to define the scope of [related issues](/cms_trial/space/JSUCLOUD/12518756/Related+issues/). For example, you can copy a field within an issue during a post function to a subtask instead of copying it.

Related issues are identified by one of the following Jira concepts:

- **Issue link:**You can define the link type to define which issues will be modified by the operation. If the post function includes the link type is ANY option, the operation will be performed on any linked issues.
- **Parent / Sub-Task:** The related issue is either a parent or a subtask of the issue.
- **Epic / Issue in** **Epic:**The other issue is either an epic related by an epic link, or is part of an epic. This is only applicable if you have Jira Software installed.
- **JQL:**Use a JQL query to retrieve the issues the post function will modify. You can use some placeholders in the JQL query, which will be replaced with the current field values of the issue in transition. For tips on writing the JQL query, see [JQL reference](/cms_trial/space/JSUCLOUD/12518329/JQL+reference/) or our [JQL Use Cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/) for some examples.

Learn more about issue relation concepts in the [Related issues](/cms_trial/space/JSUCLOUD/12518756/Related+issues/) topic.

### Perform As User

Perform As User is a configuration option in JSU post functions. It lets you choose the user who acts on the post function when it runs. When choosing a user account to run a post function, the specified user account **must** **have** the appropriate permissions to perform the actions, such as creating an issue or adding a comment.

![The Perform as User options for JSU post functions.](/cms_trial/assets/c05cec1b-93f4-4c92-9248-e9e7df71ba36.png)

If JSU can’t impersonate the specified user, it executes the rule using the JSU Add-on user. This is displayed in the Execution Log as a success and includes a warning.

JSU can’t determine if the specified user is missing necessary Jira global permissions. In this case, the rule runs using the specified user. If the run encounters a Jira error, it will fail. This is displayed in the Execution Log with a permission error.

### **JSU Add-On User** (default)

The JSU Add-On User account is automatically added to an instance when JSU is installed and already has the required permissions to perform all actions across JSU post functions. If the permissions haven’t been manually removed from the JSU Add-On User, it should not impact its success as the Perform as User instead of another account.

If you don't specify a different option, the transition on the related issue is performed as the JSU Add-On User with its associated permissions. This option is useful for testing, and you can confirm the action in your issue activity.

When the JSU Add-On User makes changes to issues, you can see the changes in the *Activity* section of the issue:

![Jira issue history showing an automation was run as the JSU add-on user.](/cms_trial/assets/fd0be499-77d3-40b7-b614-4e9400e1db4e.png)

### **Initiating User**

The transition on the related issue is performed with the same user who triggered this post function on the origin issue. That user must have the necessary permissions on the related issue. In some restrictive setups, a user might not be allowed to perform the action or might not have permission to view the relevant project.

### **Choose user**

Use this option to specify a different user account that has been granted the necessary permissions. Typically, this user account is assumed to be used only for technical purposes (impersonation) and has broad permissions and is not used by individuals to log into Jira.

In combination with the [Permission condition](https://confluence.atlassian.com/adminjiracloud/advanced-workflow-configuration-776636620.html#Advancedworkflowconfiguration-conditions)in native Jira, or the [User Is In Any Users condition](https://appfire.atlassian.net/wiki/spaces/JSU/pages/12682480) from JSU, you can hide a transition from all users that do not have permission to execute it.

#### Initiating/Specified User

If you configure your post function for either the initiating user or a selected user, the relevant issue fields must be included in the associated issue screen.

For example, if you create a rule that updates a field in a related issue, the field must be included in the target issue *Edit* screen. Similarly, if you define a rule that creates a new issue, or copies a field to a new issue, the field must be included in the *Create* screen.

 If the field is not on the relevant screen, JSU cannot edit it unless the post function is set to run as the **JSU Add-on user**. This overrides the screen security configuration in Jira Cloud using the `overrideScreenSecurity` and `overrideEditableFlag` query parameters.

**Initiating user falls back to app user**: This global option lets you set the behavior for JSU run-as-user when a post function fails due to a permission error. If this option is selected, JSU will run the post function using the JSU App User as a fallback user. The original initiating user is displayed in the *Execution Log* page. See [Settings](/cms_trial/space/JSUCLOUD/12519472/Navigation+basics/) to learn more about options in JSU.

### Custom fields context

If you use custom fields, you can select which issue types and projects the custom field appears in. The JSU Add-on user can’t be used to override fields that are missing due to their screen context. For example, if you have configured a post function to edit a custom field that is used only on a bug issue type and it is executed when a user transitions a different issue type, the execution will fail. See [Configure custom field context](https://support.atlassian.com/jira-cloud-administration/docs/configure-custom-field-context/) in the Atlassian Support documentation to learn more.

### Deactivated users

If the selected Perform As User is deactivated after you configure a post function, JSU will use the JSU Add-on user to run the post function.

## Related pages

- [Key concepts](/cms_trial/space/JSUCLOUD/12518573/Key+concepts/)
- [Workflow preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/)