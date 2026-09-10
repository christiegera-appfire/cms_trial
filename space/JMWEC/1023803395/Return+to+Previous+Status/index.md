# Return to Previous Status

A workflow post-function that moves an issue back to its previous status (the status it had before its current status).

**Note**: This post-function will only succeed if there is a transition available from the issue’s current status to the destination status (the previous status). If it is never possible to transition an issue between the issue’s current status and its previous status (even manually), this post-function will fail.

![JMWE for Jira Cloud return to previous status post function configuration](/cms_trial/assets/a42e9ce5-aafc-4c11-8fd5-1f55ecd96abd.png)

**To add the 'Return to Previous Status' post-function to a transition**:

1. Click **Edit** for the workflow that has the transition where you wish to add the post-function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Return to Previous Status** from the list of post-functions.
6. Click **Add** to navigate to the *Return to Previous Status post-function*screen, where you can add configuration details to the post-function. See below for configuration details.
7. Click **Add** to add the post-function to the transition.

After adding the post-function, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=mwecs&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=1011351630) document.

## Configuration

The following options are available for this post function:

**Note**: Some system actions in Jira can create issue metadata that will trigger this post function but recognize the “previous” status value of the issue as being the same as its current status value. The option below should be used if your post function fails to move an issue to the appropriate status.

- **Return to the previous distinct status?** - Check this box to guarantee that the issue will be returned to a status value that is distinct from the current status.

## Run As

Select one of the following to set the user triggering the transition:

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