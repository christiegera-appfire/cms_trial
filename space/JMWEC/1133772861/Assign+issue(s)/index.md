# Assign issue(s)

A workflow post-function that assigns the current issue or target issue(s) related to the current issue.

**Note**: This post function should not be added to a **Create** transition in your Jira workflow; issue assignment is not applicable until after an issue has been created!

![JMWE for Jira Cloud assign issue post function configuration panel with assignee options](/cms_trial/assets/a81a05fe-83f1-4f8c-a025-0330daf81560.png)

**To add 'Assign issue(s)' post function to a transition:**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Assign issue(s)** from the list of post function.
6. Click **Add** to navigate to the *Assign issue(s) post function* screen where you can add configuration details to the post function. See below for more information.
7. Click on **Add** to add the post function to the transition.

When you add this post-function to a transition and trigger the transition, the add-on checks the **Select user** field for the user or role to use for assignment, and the **Assignment Behavior** setting to verify that the post-function’s assignment should be utilized. The post-function will update the Assignee of the **Target Issue** appropriately. Additional configurations are available to more tightly control when the post-function will execute.

**Please note**: This post-function replaces the [**Assign to role member**](https://appfire.atlassian.net/wiki/spaces/JMWE/pages/462062699) and [**Assign to last role member**](/cms_trial/space/JMWEC/466225934/Assign+to+last+role+member+(Deprecated)/) post-functions. These post-functions will not be removed at this time, but *should not be used in any new extensions*. Any workflows that use the deprecated extensions should be updated to use this post-function instead.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

## Issue(s) to operate on

Select the issues to set the assignee field on. They can be:

- **Target issues**

  - **Current issue:** Select this option to set the assignee of the current issue. *This is the default option.*
  - **Sub-tasks of the current issue:** Select this option to set the assignee of sub-tasks of the current issue
  - **Parent issue of the current sub-task:** Select this option to set the assignee of the parent of the current issue
  - **Issues that belong to the current issue (Epic):** Select this option to set the assignee of issues that belongs to the current Epic
  - **Epic of the current issue:** Select this option to set the assignee of the Epic of the current issue
  - **Child issues of the current issue in the Portfolio hierarchy:** Select this option to set the assignee of child issues of the current issue in the Portfolio hierarchy
  - **Parent issue of the current issue in the Portfolio hierarchy:** Select this option to set the assignee of the parent issue of the current issue in the Portfolio hierarchy
  - **Issues linked to the current issue through any link type:** Select this option to set the assignee of the current issues' linked issues
  - **Issues linked to the current issue through the following link type:** Select this option to set the assignee of issues linked to the current issue through a specific link type. Select the specific link type under “Issue link”
  - **Issues returned by the following Nunjucks template:**Select this option to set the assignee of the issues returned by the result of a Nunjucks template. Input a Nunjucks template which is a comma-separated list of valid issue keys. For example:

    - `"TEST-1"`
    - `"TEST-1","TEST-2"`
    - `{{ issue.fields.parent.key }}`
    - `{{ issue.fields.subtasks | join(",", "key") }}`
  - **Issues returned by a JQL search**: Select this option to set the assignee of the issues returned by a JQL search. Input a JQL search expression. For example:

    - `project = TEST` returns issues of the project with the key TEST
    - `project = {{ issue.fields.project.key }} and assignee = {{currentUser._accountId}}` returns issues of a project that belong to the project with key TEST and the assignee is the current user
    - ```text
      {% if issue.fields.assignee %}
          assignee = {{issue.fields.assignee._accountId}}
      {% else %}
          issuekey=INVALID-1
      {% endif %}
      ```

      Note that the {% if %} block is necessary to avoid an invalid JQL query when the issue is unassigned. In that case, the template will return a valid JQL query that returns no issue (`issuekey=INVALID-1`).
- **Issue Link** - *Only available when* ***Target issues****, above, is set to* ***Issues linked to the current issue through the following link type***. Select the required link type between the current issue and the issue to be updated.
- **Nunjucks template** - *Only available when* ***Target issues****, above, is set to* ***Issues returned by the following Nunjucks template****.* Enter a Groovy script that returns the ID values for the issue or issues to be updated. See [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) for more information on Nunjucks.
- **JQL expression** - *Only available when* ***Target issues****, above, is set to* ***Issues returned by the following JQL search****.* Enter a JQL expression that returns the ID values for the issue or issues to be updated. See [Using Jira Expressions](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/) for more information on JQL.

## Assign to

Select the user to whom the target issue will be assigned:

- **Select user**

  - **Current user** - Assign to the user who triggered the transition
  - **Reporter** - The user value of the **Reporter** field for the issue
  - **Project lead** - The project lead for the project to which the issue belongs
  - **Default assignee for the project** - The user set as the default assignee for the project to which the issue belongs
  - **User who last commented**
  - **By username** - Manually select a specific user (See **Username or email** field, below)
  - **Component lead** - The user set as the lead for the selected Component (see **Component** field, below).
  - **User from user object field** - The user value from the selected field (see **Field** field, below).
  - **Last role member** - The previous role member who was assigned this issue.
  - **Role member** - Select the Role to which the user belongs as well as the Multiple user options to determine which specific user should be assigned (see **Role** and **Multiple user options**, below).
  - **User returned from script** - Enter a Nunjucks template that returns the user value for the assignee.
- **Username or email** - *Only visible when* ***Select user*** *is set to ‘By username’.* Enter the name or email address of the user to whom the issue should be assigned.
- **Component** - *Only visible when* ***Select user*** *is set to ‘Component lead’.* Select the required Component or start typing to search all Jira Components.
- **Field** - *Only visible when* ***Select user*** *is set to ‘User from user object field’.* Select the required user object field or start typing to search the list of fields.
- **Project Role** - *Only visible when* ***Select user*** *is set to ‘Last role member’ or ‘Role member’.* Select the required role to which the potential users belong, or start typing to search the list of Jira roles.
- **Include the reporter** - *Only visible when* ***Select user*** *is set to ‘Last role member’*. Include the reporter of the issue in the pool of users to whom the issue can be assigned.
- **Exclude the current assignee** - *Only visible when* ***Select user*** *is set to ‘Last role member’*. Exclude the current assignee from the pool of users to whom the issue can be assigned.
- **Skip inactive users** - *Only visible when* ***Select user*** *is set to ‘Last role member’*. Check this option to force JMWE to skip any inactive Jira users when searching for valid assignees.
- **Multiple user options** - *Only visible when* ***Select user*** *is set to an option that may return multiple users, such as ‘User from user object field’, ‘Role member’, and ‘User returned from script’*. When a specific role is selected for assignment, that role may have multiple users assigned to it; this option sets which user within that set will be assigned to the issue. The options are:

  - **Assign to the first matching user in alphabet order** - The first user in alphabetical order, *by display name*. **Please note**: this is case sensitive.
  - **Assign to the least busy matching user** - The user who has the least number of assigned tickets without resolution.
  - **Assign to a randomly selected user**
  - **Specify the user with a custom script**

    - **Assignment script** - Enter a Nunjucks template that will return a user value.
- **Throw an exception if no user matches the specified criteria** - Check this option to cause the extension to throw an error if no user is determined with the configured behavior.

## Advanced options

Expand this section to see advanced configurations including which user will run the post function, conditional execution, and delayed execution.

## Run As

This option enables you to configure as which Jira user the post-function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

## Conditional execution

It is possible to configure the post-function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.