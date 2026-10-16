# Increase value of field

A workflow post function that increases the value of a selected numerical field by one.

When you add this post function to a transition and trigger the transition on an issue, the add-on increments the selected field value by one.

**Note**: This post function is applicable to numerical fields only!

[Unmapped macro: 47fa61b6-fe1c-40c9-b236-623cdbc35833/4d8fa66b-88bf-4899-a37e-5926131c46ac/static/multiexcerpt-fast-include-block-macro — no content to fall back on]

![Increase Value of Field post function configuration screen](/cms_trial/assets/f1f42592-0275-41e1-a155-f86c25bdbf75.png)

## Options

The primary option is the field that should be increased by one.

- **Field** - Select the field to increase.

Only one field can be selected for each instance of this post function.

## Advanced options

Expand this section to see advanced configurations including conditional execution, delayed execution, and whether or not Jira will send a notification when the post function is executed.

## Run as

This option enables you to configure as which Jira user the post function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

## Conditional execution

It is possible to configure the post function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post function, so that the sub-tasks are created before they are transitioned.

Where possible, it is recommended to use the [Sequence of post-functions](/cms_trial/space/JMWEC/466322933/Sequence+of+post+functions/) post function or [Shared action](/cms_trial/space/JMWEC/466323396/Shared+Action+post+function/) post function to execute a series of post functions in a specific sequence instead of applying a delay.

## Send notifications

You can configure your post function to trigger a Jira notification when they make changes to a work item. JMWE will use the [Jira notification scheme](https://support.atlassian.com/jira-cloud-administration/docs/configure-notification-schemes/) for the space where the post function executes to notify the appropriate users.

Check the option **Allow Jira to send notifications for this change** to enable notifications for the post function.

## Run in background

Jira Cloud generally allows a short window (approximately 25 seconds) for a post function to complete. If your post function performs an action on a large number of work items, enable background execution to give it more time to finish.

Check **Run this post function in the background** to enable long-running execution.