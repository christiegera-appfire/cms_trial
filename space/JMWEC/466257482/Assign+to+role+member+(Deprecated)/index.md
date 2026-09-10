# Assign to role member (Deprecated)

This post function has been deprecated for some time, and will be completely removed by the end of **December 2025**. Once this post function has been removed from JMWE, you will not be able to:

- **Add** another instance
- **Edit** any existing instances
- **Execute any instances - automatically or manually**

## Replacing this post function

This post function has been replaced with the [Assign issue(s)](/cms_trial/space/JMWEC/1133772861/Assign+issue(s)/) post function. Use the table below to migrate your configuration; settings should be migrated to the new post function exactly as they exist in the obsolete one, except where noted.

| **Configuration option** | **Migrate to** | **Notes** |
| --- | --- | --- |
| Target issues | Target issues |  |
| Project role | Select user → **Role member** | Set new **Project Role** field to the same value as the obsolete post function configuration. |
| **Note**: The [Assign issue(s)](/cms_trial/space/JMWEC/1133772861/Assign+issue(s)/) post function has expanded capabilities for determining issue assignment. Review **Multiple user options** and **Assignment behavior** in the new configuration and set as needed. |
| Send notifications | Advanced options → Settings → Allow Jira to send notifications |  |
| Advanced options → Settings → Run as | Advanced options → Settings → Run as |  |
| Advanced options → Settings → Run this post-function only if a condition is verified | Advanced options → Settings → Run this post-function only if a condition is verified |  |
| Advanced options → Settings → Delay the execution of this post-function | Advanced options → Settings → Delay the execution of this post-function |  |

A workflow post-function that assigns target issue(s) to a user from the specified role (works best if you have only one user in that role).

**To add the 'Assign to role member' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add` `post function`.
5. Select `Assign to role member` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.
7. Select the project role from the `Project Role` drop-down.
8. Click on `Add` to add the post-function to the transition.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

When you add this post-function to a transition and trigger the transition, the add-on assigns the target issue(s) to a member of the selected `Project Role`.

## Issue(s) to operate on

- **Current issue:** Select this option to set the assignee of the current issue. *This is the default option.*
- **Sub-tasks of the current issue:** Select this option to set the assignee of each sub-tasks of the current issue
- **Parent issue of the current sub-task:** Select this option to set the assignee of the parent of the current issue
- **Issues that belong to the current issue (Epic):** Select this option to set the assignee of each issue that belongs to the current Epic
- **Epic of the current issue:** Select this option to set the assignee of the Epic of the current issue
- **Child issues of the current issue in the Portfolio hierarchy:** Select this option to set the assignee of child issues of the current issue in the Portfolio hierarchy
- **Parent issue of the current issue in the Portfolio hierarchy:** Select this option to set the assignee of the parent issue of the current issue in the Portfolio hierarchy
- **Issues linked to the current issue through any link type:** Select this option to set the assignee of the current issues' linked issues
- **Issues linked to the current issue through the following link type:** Select this option to set the assignee of each issue linked to the current issue through a specific link type. Select the specific link type under “Issue link”
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

The easiest is to have only one user in the selected `Project Role` for each applicable project.

### Send notifications

Jira sends notifications for the change in the Assignee field value on the target issue. You can control the default value of the `"Send notifications"` option in the **Configuration** page under JMWE administration. Click [here](/cms_trial/space/JMWEC/465503776/JMWE+Administration/) for more information.

## Conditional execution

To execute this post-function based on the result of a Nunjucks template see [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/).

## Run As

- **Run as current user:** The current user will be the author of the assignee change.

- **Run as add-on user:** The add-on user will be the author of the assignee change.

- **Run as this user:** Any user selected in this field will be the author of the assignee change.

If you select any option other than "Run as add-on user", so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission.

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.