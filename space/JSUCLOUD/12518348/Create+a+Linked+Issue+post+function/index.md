# Create a Linked Issue post function

## Description

The Create a Linked Issue post function automatically creates a new issue that is linked to the original issue that triggered the post function. Any number of fields can be copied to the new issue and within the origin issue.

See [Workflow post functions](/cms_trial/space/JSUCLOUD/12518401/Workflow+post+functions/) to learn how to add a JSU post function to a Jira workflow.

## Interactive demo

Follow the interactive demo setup below for an example of how to configure the Create a Linked Issue post function.

<https://app.arcade.software/share/ob6NpUrxXNyibe0AzAIy>

## Configuration

![contentId-12518348](/cms_trial/assets/39cfa399-cb36-4b25-a908-0b631bbd0965.png)

[Infinite Loop Detection](/cms_trial/space/JSUCLOUD/256770940/Infinite+loop+detection/): An infinite loop can occur when executing the Create a Linked Issue post function. An infinite loop results in an endless cycle of issue creation and follow-up transitions following the triggering of the origin issue. When a loop is detected, JSU will stop the execution and log an execution failure.

When using post functions that create issues or follow-up transitions, consider the rule's outcome and the user permissions of your project teams. You can also use [preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/) to restrict when rules are run to reduce the likelihood of causing an infinite loop.

Post functions in JSU Cloud are executed asynchronously and a post function will be executed after the transition has been completed. If you use the Create a Linked Issue post function on a Create transition, the newly created issue will create another issue, which will create another issue, and so on. This results in an infinite loop and JSU will stop the execution to protect your instance.

### Precondition

If you are using preconditions with a JSU post function, they can be evaluated in the following ways:

- True (Precondition must be true to execute a post function)
- False (Precondition must be false to execute a post function)

Image — asset pipeline pending  
Setting options for JSU preconditions.

The precondition setting is available on our post function configuration pages, and it is set to **True** by default. You can learn more about our preconditions in [Workflow Preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/). See the Preconditions for Post Functions [uses cases](/cms_trial/space/JSUCLOUD/12518052/Update+an+issue+only+in+certain+conditions/) for examples.

### Copy attachments

Use it to define configurations to copy or move attachments to the newly created issue.

You can choose Move Attachments added during Transition. The user then adds some attachments on the transition screen of the origin issue.  
However, since they are moved to the newly created issue, it appears as if they added the attachments to the new issue.

### Conditional copying attachments

Conditional copying attachment (controlled by custom field) is always checked only for the issue in transition, regardless of whether it is a source or destination.

## Initial mandatory values for the new issue

Use this section to configure the mandatory fields for an issue. These are basic Jira fields. Remember that your Jira configuration may have additional mandatory fields (set these using the Copy operation).

Additionally, the summary will always be copied from the origin issue to the new issue. The reporter of the new issue will always be set to the user selected in the ‘Perform as User’ option. However, you might overwrite them later with [Copy to the New sub-function](https://appfire.atlassian.net/l/cp/oViikbxE).

### **Target project**

The target project can be set to:

- Inside same project: A new issue will be created in this same project
- Selected Project: A new issue will be created in the selected project.

### **This Issue will be related via**

The Create a Linked Issue post function allows you to create new issues that are connected not only with an issue link but instead in a parent / sub-task, as well as epic / issue in epic relation. See [Related Issues](https://appfire.atlassian.net/wiki/display/JSUCLOUD/Related+Issues) for more information.

### **Issue type**

Define the issue type of the new issue. The issue type you select here must be available in the target project.

### **Perform as User**

Perform As User is a configuration option in JSU post functions. It lets you choose the user who acts on the post function when it runs. When choosing a user account to run a post function, the specified user account must have the appropriate permissions to perform the actions, such as creating an issue or adding a comment.

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

### Sub-functions

In JSU, you can define configurations to modify fields on the origin and new issue; this feature is only available for the Create a Linked Issue post function.

- **Origin issue**: Issue that triggered the post function
- **New issue**: Issue to be created by the post function, which was triggered on the origin issue

![Diagram illustrating the outcomes of the post function when applied to a new issue and the origin issue.](/cms_trial/assets/ee46f6ac-ea47-474a-a775-8a493b97889b.png)

To add a sub-function:

1. Select **+ Add Configuration** to view the available operations.

   ![The Add Configuration button under the Sub-Functions section of the the Create a Linked Issue post function.](/cms_trial/assets/e0d0f67e-4634-430e-8114-2c7e5fd6cae5.png)
2. Select **Add** for the required operation.

   ![List of operations for the Create a Linked Issue sub-functions.](/cms_trial/assets/a07d91e8-318e-4ec2-9834-68e9f0ce624b.png)

   The following operations are available:

   - [**Copy to New**](/cms_trial/space/JSUCLOUD/12518106/Copy+to+New/)
   - [**Copy within Origin**](/cms_trial/space/JSUCLOUD/12518295/Copy+Within+Origin/)
   - [**Set**](/cms_trial/space/JSUCLOUD/12518116/Set/)
3. Configure the fields as required. See the<https://appfire.atlassian.net/l/cp/rpyvVZ8U> use case for an example setup.

### Organizing operations

You can configure any number of configurations; they are executed sequentially.

- You can rearrange the configurations by dragging the line using the handle on the left.
- You can also disable a configuration by unchecking the toggle next to the Delete button. Your operation will remain on your configuration but will be ignored.

![Screenshot of the subfunctions as described on this page.](/cms_trial/assets/00751d56-f58f-4a83-b8ae-82aa22f1c521.png)

## Related pages

- [Define field values for new linked issues](/cms_trial/space/JSUCLOUD/12518186/Define+field+values+for+new+linked+issues/)