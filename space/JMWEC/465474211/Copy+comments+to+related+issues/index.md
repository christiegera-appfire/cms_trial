# Copy comments to related issues

A workflow post-function that copies all comments, or just the latest comment, from the current issue to related issues (such as linked issues, Stories of an Epic, Epic of a Story, sub-tasks of an issue, issues returned by a Nunjucks Template, or a JQL search, etc.)

When you add this post-function to a transition and that transition is triggered, the add-on copies the comment(s) of the current issue to all the target issues; this process will ignore previously added comments.

![Copy comments post function configuration screen](/cms_trial/assets/d454719d-0e5c-42d7-9847-e97e82a3a865.png)

**To add 'Copy comments to linked issues' post-function to a transition :**

1. In Jira Administration, go to **Workflows** and click the **Edit** link to open the workflow.
2. Select the required transition.
3. Click the **Post Functions** tab and click **Add post function**.
4. Select **Copy comments to linked issues** from the list of post-functions.
5. Click on **Add** to add the post-function on the transition.
6. Set the **Target issue** field to configure which issues should receive the copied comments (see **Issue(s) to operate on**, below, for more information on the possible values).
7. Select from the options provided to add the required parameters (see below for more details on required parameters).

## Issue(s) to operate on

Select the issues to which the comments should be copied to. They can be:

- **Target issues**

  - **Sub-tasks of the current issue** - Select this option to copy the comments to each sub-task of the current issue
  - **Parent issue of the current sub-task** - Select this option to copy the comments to the parent of the current issue
  - **Issues that belong to the current issue (Epic)** - Select this option to copy the comments to each issue that belongs to the current Epic
  - **Epic of the current issue** -Select this option to copy the comments to the Epic of the current issue
  - **Child issues of the current issue in the Portfolio hierarchy** - Select this option to copy the comments to each child issue of the current issue in the Portfolio hierarchy
  - **Parent issue of the current issue in the Portfolio hierarchy** - Select this option to copy the comments to the parent issue of the current issue in the Portfolio hierarchy
  - **Issues linked to the current issue through any link type** - Select this option to copy the comments to the current issues' linked issues
  - **Issues linked to the current issue through the following link type** - Select this option to copy the comments to the issues linked to the current issue through a specific link type. Select the specific link type under “Issue link”
  - **Issues returned by the following Nunjucks template** -Select this option to copy the comments to the issues returned by the result of a Nunjucks template. Input a Nunjucks template which is a comma-separated list of valid issue keys. For example:

    - `"TEST-1"` (to copy to a specific issue, e.g. the issue TEST-1)
    - `"TEST-1","TEST-2"` (to copy to multiple specific issues, e.g. issues TEST-1 and TEST-2)
    - `{{ issue.fields.parent.key }}`
    - `{{ issue.fields.subtasks | join(",", "key") }}`
  - **Issues returned by a JQL search** -Select this option to copy the comments to the issues returned by a JQL search. Input a JQL search expression. For example:

    - `project = TEST` returns issues of the project with the key TEST
    - `project = {{ issue.fields.project.key }} and assignee = {{currentUser._accountId}}` returns issues of a project that belong to the same project as the source issue and the assignee is the current user
  - ```text
    {% if issue.fields.assignee %}
        assignee = {{issue.fields.assignee._accountId}}
    {% else %}
        issuekey=INVALID-1
    {% endif %}
    ```

    Note that the {% if %} block is necessary to avoid an invalid JQL query when the issue is unassigned. In that case, the template will return a valid JQL query that returns no issue (`issuekey=INVALID-1`).

## Comments to copy

- **All comments** -Copies all the comments on the current issue to all the target issues
- **Latest comment** -Copies the latest comment on the current issue to all the target issues
- **The comment added on the transition screen, if any** -Copies the comment added on the transition screen, if any, to all target issues

Note that the post function won't copy already copied comments.

- **Filter comments to copy** -Filters comments to copy based on the result of a Nunjucks template

## Advanced options

Expand this section to see advanced configurations including how to handle inline images and attachments, the author of the comments, comment visibility, which user will run the post function, conditional execution, and delayed execution.

### Inline images and attachments

- **Copy inline images** -Copies images that appear inside the comments to the destination issue(s)
- **Copy attachments mentioned in comments** -Copies attachments that are mentioned inside the comments to the destination issue(s)

When attachments from comments are copied between issues, JMWE checks for duplicate files using several properties including filename, mime-type, and file size. If duplicate files are detected on the destination issue, the new attachments will have their filename appended when they are copied.

### Author of copied comments

- **Original author (or "run as" user if original author has no permission)** -The author of a comment on the current issue will be the author of the comment created on the target issues. If the original author has no permission then the user selected in the "Run as" section (explained [below](#)) will be the author.
- **The add-on user** -The add-on user will the author of the comments on the target issues.
- **This user** -The user selected here will be the author of the comments on the target issues.

### Comment visibility

- **Retain existing comment visibility restrictions** -Retains the existing comment visibility restrictions of the current issue to the comments on the target issues.
- **Use the following comment visibility**

  - **Restrict to Group** -Restricts the visibility of the comment to a specified group. When you select a valid group name in the `Restrict to Group` field, the comment will be visible only to the members of the specified group. For no restriction, leave the field blank.
  - **Restrict to Project Role** -Restricts the visibility of the comment to a selected project role. When you select a project role from the `Restrict to Project Role` drop-down, the comment will be visible only to the members of the selected project role. For no restriction, leave the field blank.
  - **Restrict to Internal (Jira Service Desk only)** -Restricts the visibility of the comment to the Service Desk Agents and Collaborators only.

### Run As

Select one of the following to set the creator of the issue:

This option enables you to configure as which Jira user the post-function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

### Conditional execution

It is possible to configure the post-function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

### Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.