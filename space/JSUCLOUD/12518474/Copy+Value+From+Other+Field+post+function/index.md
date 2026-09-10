# Copy Value From Other Field post function

## Description

The Copy Value From Other Field post function copies the value of one field to another field in the origin issue or to a different issue. You can configure any number of source/destination field pairs. You can also use this post function to copy from/to comments.

See [Workflow post functions](/cms_trial/space/JSUCLOUD/12518401/Workflow+post+functions/) to learn how to add a JSU post function to a Jira workflow.

## Interactive demo

Follow the interactive demo setup below for an example of how to configure the Copy Value From Other Field post function.

## Configuration

For the field to copy, you must specify the relation between the source and destination issues. You can add any number of from/to field pairs for the copy operation. Click **Add new** ( **+** ) to add another source field.

![Configuration page for the Copy Value From Other Field post function.](/cms_trial/assets/4f361dd0-2dc6-4ecf-bcfa-0a56beb27c6c.png)

### Precondition

If you are using preconditions with a JSU post function, they can be evaluated in the following ways:

- True (Precondition must be true to execute a post function)
- False (Precondition must be false to execute a post function)

Image — asset pipeline pending  
Setting options for JSU preconditions.

The precondition setting is available on our post function configuration pages, and it is set to **True** by default. You can learn more about our preconditions in [Workflow Preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/). See the Preconditions for Post Functions [uses cases](/cms_trial/space/JSUCLOUD/12518052/Update+an+issue+only+in+certain+conditions/) for examples.

### Issue Relation

Most of JSU's workflow post functions have the option to define the scope of related issues. For example, instead of copying a field within an issue for a post function, you can copy it to a subtask.

![A list of issue relation options in JSU post functions.](/cms_trial/assets/92eecb57-82a8-49eb-80ba-4a446b9ded7d.png)

## Types of issue relations

Related issues are identified by one of the following Jira concepts:

- **Issue link:**You can choose the link type to define which issues will be modified by the operation. If the post function includes the link type as ANY option, the operation will be performed on any linked issues.
- **Parent / Sub-Task:** The related issue is either the parent or a subtask.
- **Epic / Issue in** **Epic:**The other issue is either an epic related to an epic link or it is part of an epic. This is only applicable if you have Jira Software installed.
- **JQL:**Use a JQL query to retrieve the issues the post function will modify. You can use some placeholders in the JQL query, which will be replaced with the current field values of the issue in transition. For tips on writing the JQL query, see [JQL Reference](/cms_trial/space/JSUCLOUD/12518329/JQL+reference/) or our [JQL Use Cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/) for some examples.

### Issue in transition

*Issue in Transition* refers to the issue for which a workflow condition is checked, a workflow validator is examined, or a workflow post function is performed; in other words, the issue that triggered a workflow condition/validator/post function to be executed.

### Source and destination

For some post functions, you can choose whether the issue in transition serves as the source or the destination. For example, the [Copy Value From Other Field](/cms_trial/space/JSUCLOUD/12518474/Copy+Value+From+Other+Field+post+function/) post function allows you to define the issue in transition as the source or destination of the copy operations. In contrast, you define the other end with an issue relation. The field value is then read from the source issue and written to the destination issue. Other post functions do not have a source and destination; you simply define the issue relation that applies to the post function. For example, the [Create a Linked Issue](/cms_trial/space/JSUCLOUD/12518348/Create+a+Linked+Issue+post+function/) post function creates a new issue and then connects it through an issue relation to the issue in transition.

### Related issues limitations

While we try to execute as many configurations as possible, you should keep some restrictions in mind.

- Copy Value From Other Field post function: There should be only one source issue; otherwise, it is unclear from which issue the value should be read. The current implementation will simply select one of them and ignore the rest.
- If you use the Create a Linked Issue post function to create a new subtask, you must also configure the post function to create the new issue as a subtask issue type. The target project must be the same as the one for the issue in transition.

[unmapped inline: placeholder]

### Perform As User

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

### Copy fields

![contentId-12518474](/cms_trial/assets/fbdd2287-3d9c-4591-9663-a312ed64e809.png)

[Excerpt "copy fields" from page "Copy fields configuration" not found]

## Example

A workflow rule is configured so the Resolve transition uses the Copy Value From Other Field post function. The value of the *Assignee* field is copied from the origin issue to the ‘TextField' field in all the issue’s subtasks. If a user resolves an issue on this workflow, the value of the *Assignee* field will be copied to the 'TextField' field after the issue is resolved.

## Supported field types