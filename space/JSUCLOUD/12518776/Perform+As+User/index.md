# Perform As User

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