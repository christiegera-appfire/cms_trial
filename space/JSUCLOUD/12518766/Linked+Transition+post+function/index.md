# Linked Transition post function

## Description

The Linked Transition post function triggers a transition on a [related issue](/cms_trial/space/JSUCLOUD/12518756/Related+issues/). It can be very powerful, especially when used with the [Create a Linked Issue](/cms_trial/space/JSUCLOUD/12518348/Create+a+Linked+Issue+post+function/) post function to *connect* the workflows of two issues. You can also specify any number of fields to be copied to the related issue.

See [Workflow post functions](/cms_trial/space/JSUCLOUD/12518401/Workflow+post+functions/) to learn how to add a JSU post function to a Jira workflow.

**Want to try a new way of creating this post function?**

We’re working to make it even easier for you to build workflow rules with JSU. A simplified version of this post function is now available in our [Universal Rule Builder](/cms_trial/space/JSUCLOUD/12517805/Universal+Rule+Builder/) – a new editor experience currently in beta.

## Interactive demo

Follow the interactive demo setup below for an example of how to configure the Copy Value From Other Field post function.

## Configuration

You must specify the workflow and transition that you want to apply to the related issue.

![Example configuration of the Linked Transition post function.](/cms_trial/assets/c79b4ea7-4473-465f-af9a-06ed0b803174.png)

### Precondition

If you are using preconditions with a JSU post function, they can be evaluated in the following ways:

- True (Precondition must be true to execute a post function)
- False (Precondition must be false to execute a post function)

Image — asset pipeline pending  
Setting options for JSU preconditions.

The precondition setting is available on our post function configuration pages, and it is set to **True** by default. You can learn more about our preconditions in [Workflow Preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/). See the Preconditions for Post Functions [uses cases](/cms_trial/space/JSUCLOUD/12518052/Update+an+issue+only+in+certain+conditions/) for examples.

### Issue relation

Choose the type of issue that you want to transition to the new status.

Related issues are identified by one of the following Jira concepts:

- **Issue link:**You can define the link type to define which issues will be modified by the operation. If the post function includes the link type is ANY option, the operation will be performed on any linked issues.
- **Parent / Sub-Task:** The related issue is either a parent or a subtask of the issue.
- **Epic / Issue in** **Epic:**The other issue is either an epic related by an epic link, or is part of an epic. This is only applicable if you have Jira Software installed.
- **JQL:**A JQL query will be executed to retrieve the issues that the post function will modify. You can use some placeholders in the JQL query, which will be replaced with the current field values of the issue in transition. For tips on writing the JQL query, see [JQL reference](/cms_trial/space/JSUCLOUD/12518329/JQL+reference/) or our [JQL use cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/) for some examples.

### Transition

When the post function is performed, it triggers the transition with that particular ID on the linked issues. It appears as if the transition ID is available on the target issue, no matter what workflow and transition name you picked in the configuration screen (that is only to make it easier to find a particular transition ID during configuration).

If the transition with that ID is not available on the linked issue (probably because it is in a different status) nothing will happen. Also, no comments or fields are copied, and no resolution is set.

It is important to keep this in mind and design your workflows accordingly to prevent them from becoming out of sync. You might also use several Linked Transition post functions in the same transition, each calling a different target transition to match different possible statuses of the linked issue.

Be aware that configured workflow conditions or validators might prevent a transition from being performed.

### Conditional statuses

Use this option if you want the issue to be transitioned only when ALL of the sibling issues are in a specified status. Only the last issue will trigger a linked transition.  
Consider a test case issue that has several linked bugs. The bugs are linked as 'from test' to the test case. Only when the last bug is fixed, the test case should be set to the Status 'Ready for Re-Test'.  
This prevents this transition from being executed when the first bug is fixed.

### Optional settings

![Linked Transition post functions optional settings as described on this page.](/cms_trial/assets/016f0f05-691f-4eef-9dfd-f9d098ec15de.png)

### Resolution

1. To set the resolution, you need a resolution field on the transition screen. For more information, see Atlassian’s [Mapping a Screen to a Workflow Transition](https://confluence.atlassian.com/jirakb/mapping-a-screen-to-a-workflow-transition-720634253.html) page.
2. If any transition screen contains the resolution field, that field becomes mandatory. Here, you can set a value for the resolution required to perform that transition.

| Resolution in the post function configuration | Resolution on the issues at the start when the transition is performed | What happens? |
| --- | --- | --- |
| Empty | (does not matter) | The resolution on the issue will not change. |
| Any value | Any other value | The resolution will be set to the defined value. |

### Perform As User

The transition on the linked issue will be performed as the user defined by the **Peform As User** option. Perform As User is a configuration option in JSU post functions. It lets you choose the user who acts on the post function when it runs. When choosing a user account to run a post function, the specified user account **must** **have** the appropriate permissions to perform the actions, such as creating an issue or adding a comment.

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

### Copy fields

These fields will be copied to the linked issue upon completion of the transition. The conditions and validators of your linked transition will still use the old field values.

### Supported field types

## Troubleshooting

If a linked transition does not get triggered or even blocks your origin transition, there are a few things to check:

- Did you check the log files? There are cases when the linked transition is not performed silently. But you will find a message in the log files on the server.
- What happens when you manually click the linked transition? Does it work?
- Does this problem only happen to other users? Check that the user performing the origin transition has enough permissions for the linked transition.
- Is there a transition screen for the linked transition? Is there a condition, validator, or post function on the linked transition? Could these prevent the transition from being performed in an automated way (with the Linked Transition post function)?
- In the order of all post functions of the origin transition, the Linked Transition post function must be the last one.
- Did you try to set a particular Resolution in the linked transition? Or with 'Resolution=empty' - does it then work?

### Infinite Loop Detection

An infinite loop can occur when executing the Linked Transition post function. An infinite loop results in an endless cycle of issue creation and follow-up transitions following the triggering of the origin issue. When a loop is detected, JSU will stop the execution and log an execution failure.

When using post functions that create issues or follow-up transitions, consider the outcome of the rule and the user permissions of your project teams. You can also use [preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/) to restrict when rules are run to reduce the likelihood of causing an infinite loop. Learn more about how JSU identifies an infinite loop in [Infinite Loop Detection](/cms_trial/space/JSUCLOUD/256770940/Infinite+loop+detection/).

## Related pages

- [Key concepts](/cms_trial/space/JSUCLOUD/12518573/Key+concepts/)
- [Define field values for new linked issues](/cms_trial/space/JSUCLOUD/12518186/Define+field+values+for+new+linked+issues/)