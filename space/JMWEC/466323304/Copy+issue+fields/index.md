# Copy issue fields

A workflow post function that allows you to copy the values of one or more fields from the current issue or related issue(s) or a set of filtered issues to the specified destination issue(s).

**Note**: When copying field values using this post-function, some consideration is required for specific fields in the destination issue(s):

- **Sprint** - If you are setting the **Sprint** field and you try to copy the value for a closed sprint, that value will not copy. If you are copying multiple sprint values to the **Sprint** field and one of those values is a closed sprint, that value will not be copied (but the other sprint values will be copied).

![Copy Issue Fields configuration screen](/cms_trial/assets/7dd4adfc-b57e-47df-bccf-7ad23ebcda1c.png)

**To add the 'Copy issue fields' post-function to a transition**:

1. Click **Edit** for the workflow that has the transition to which you wish to add the post-function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel (or select the **Post Functions** tab).
4. Click**Add post function**.
5. Select **Copy issue fields** from the list of post functions.
6. Click **Add.** The *Copy issue fields post-function*screen will open, where you can configure the post function as needed. See below for more details on specific configurations.
7. Click **Add** to complete the configuration and add the post-function.

After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=mwecs&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=448497512) document.

## **Issue(s) to operate on**

- **Source Issue(s)** - Select the issues from which the specified field(s) from the **Fields to copy** section are copied. Select one of the following:

  - **Current issue** - Select this option to copy the value of the selected field(s) from the current issue. *This is the default option.*
  - **Sub-tasks of the current issue** -Select this option to copy the value of the selected field(s) from the sub-tasks of the current issue.
  - **Parent of the current sub-task** - Select this option to copy the value of the selected field(s) from the parent of the current issue.
  - **Issues that belong to the current issue (Epic)** - Select this option to copy the value of the selected field(s) from the issues that belong to the current Epic.
  - **Epic of the current issue** -Select this option to copy the value of the selected field(s) from the Epic of the current issue.
  - **Child issues of the current issue in the Portfolio hierarchy** - Select this option to copy the value of the selected field(s) from the child issues of the current issue in the Portfolio hierarchy.
  - **Parent issue of the current issue in the Portfolio hierarchy** - Select this option to copy the value of the selected field(s) from the parent issue of the current issue in the Portfolio hierarchy.
  - **Issues linked to the current issue through any link type** - Select this option to copy the value of the selected field(s) from all the issues linked to the current issue.
  - **Issues linked to the current issue through the following link type** - Select this option to copy the value of the selected field(s) from the issues linked to the current issue through a specific link type. Select the specific link type under “Issue link”.
  - **Issues returned by the following Nunjucks template** -Select this option to copy the value of the selected field(s) from the issues returned by the result of a Nunjucks template. Enter a Nunjucks template, which is a comma-separated list of valid issue keys. For example:

    - `"TEST-1"`
    - `"TEST-1","TEST-2"`
    - `{{ issue.fields.parent.key }}`
    - `{{ issue.fields.subtasks | join(",", "key") }}`
  - **Issues returned by the following JQL search** - Select this option to copy the value of the selected field(s) from the issues returned by a JQL search. Enter a JQL search expression. For example:

    - `project = TEST` returns issues of the project with the key TEST
    - `project = {{ issue.fields.project.key }} and assignee = {{currentUser._accountId}}` returns the issues belonging to the same project as the current issue that are assigned to the current user
    - ```text
      {% if issue.fields.assignee %}
          assignee = {{issue.fields.assignee._accountId}}
      {% else %}
          issuekey=INVALID-1
      {% endif %}
      ```

Note that the {% if %} block is necessary to avoid an invalid JQL query when the issue is unassigned. In that case, the template will return a valid JQL query that returns no issue (`issuekey=INVALID-1`).

- **Destination Issue(s**) - Select the issues to which the specified field(s) from the **Fields to copy** section are copied. The options available here are the same as those from **Source Issue(s)**.

Ensure the number of source issues times the number of destination issues does not exceed a limit of 1000 issues. In such a scenario, the post function will be not run and an error will be logged.

## Fields to copy

This section allows you to add a list of fields to copy from the source issue to the destination issue. Specify the following:

- **Source Field** - Select a field from the source issue(s) to copy the respective field value.
- **Destination Field** - Select a field from the destination issue(s) to which the source field value is copied.
- **Options** - Select one or more options for copying the values. Available options:

  - **Set only if field is empty** - Sets the value of the selected destination field only if the field in the destination issue(s) is empty.
  - **Create missing value(s)** - Allows creating any missing component(s) or version(s) while copying to a field that expects Versions or Components. This is applicable for version and component fields.
  - **Ignore empty value** - Does not copy the source value to the destination issue, if the source value is empty or null. This means a blank value will not be assigned to the destination field and the respective field value will be retained as-is.
  - **Append value(s) to the field** - Appends the value(s) to the selected field of the destination issue, instead of replacing its value. This applies to only multi-valued fields.
  - **Use value before current transition** -Takes the selected Source Field value as it was before the transition. This is useful in cases where the user modifies the source field on the **Transition screen**during the transition and needs the field value prior to the modification.

Click **Add another field** to add one more field to the list.

Click **Remove** ( ▢ ) next to a field to stop copying that field.

## Advanced Options

### Run As

Select one of the following:

This option enables you to configure as which Jira user the post-function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

### Conditional Execution

It is possible to configure the post-function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

### Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.

- **Send notifications** - Select this option to allow Jira to send notifications for the change in the values of the selected field(s) on the destination issue(s).

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. This message is only displayed if the current user is a Jira administrator.