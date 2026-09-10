# Log Work

When you add this post function to a transition and trigger it, the add-on adds to the Worklog for the issue using a script to determine the amount to add.

![JMWE for Jira Cloud log work post function configuration with time tracking options](/cms_trial/assets/03997fa9-33f0-4d44-8da5-fcce9ab8fadf.png)

**To add the 'Log Work' post function to a transition:**

1. Click **Edit** for the workflow that has the transition to which you wish to add the post function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Log Work** from the list of post functions.
6. Click **Add** to navigate to the *Log Work post-function* screen where you can add configuration details. See below for more information.
7. Click **Add** to add the post function to the transition.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. This message is only displayed if the current user is a Jira administrator.

## Issue(s) to operate on

Select the issues on which the selected fields should be cleared. They can be:

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

## Time spent

Enter a Nunjucks script that returns the amount of time to add to the Worklog. The script should return either a number of seconds or a string in the format `‘3d 5h 10m 30s’`.

**Note**: Due to an Atlassian limitation, the Log Work post function does not support parsing weeks from a string; for example, `‘2w 3d 5h 10m 30s’` will not log the correct number of hours, but `‘13d 5h 10m 30s’` will work. In this scenario, 5 days represent a full week’s work.

## Start date and time

Select the start time for the worklog entry. The available options are:

- **Now**
- **Current time minus time spent**
- **Custom**

Additionally, you can set the following options related to the start date and time:

- **Script** - *Only available when* ***Start time****, above, is set to* ***Custom****.* Enter a Nunjucks script that returns the date and time that should be used for the worklog.
- **Adjust remaining estimate** - This option will apply the logged time to the issue’s estimate and decrease the Remaining Estimate value.

## Work description

*This configuration is optional.* Enter a Nunjucks script that returns the description to add to the worklog entry.

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

## Notifications

Check the box **Allow Jira to send notifications for this change** if you want to have a notification sent when the post function adds the worklog entry.