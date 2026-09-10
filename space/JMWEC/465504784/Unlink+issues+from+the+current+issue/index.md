# Unlink issues from the current issue

A post-function that will unlink issues from the current issue based on the result of a Nunjucks condition.

When you add this post-function to a transition and trigger it, the add-on checks the specified condition against each linked issue of the current issue. If the condition evaluates to any text except *false* or an empty string, it will remove the issue link. If not, it will not remove the link.

![Unlink Issues configuration screen](/cms_trial/assets/cf0bbd65-0ad7-4db0-97e1-5744db533ddd.png)

**To add 'Unlink issues from the current issue' post-function to a transition:**

1. Click **Edit** for the workflow that has the transition to which you wish to add the post-function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel (or select the **Post Functions** tab).
4. Click**Add post function**.
5. Select **Unlink issues from the current issue** from the list of post functions.
6. Click **Add.** The *Unlink issues from the current issue post-function*screen will open, where you can configure the post function as needed. See below for more details on specific configurations.
7. Click **Add** to complete the configuration and add the post-function.

After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=MWECS&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=448497512) document.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

## Issues to unlink

- **Condition** - Input a [c](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)ondition that will return an issue ID or IDs using [Nunjucks annotations](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/). You can insert [issue, linkedIssue, transition, linkTypeName, currentUser and now](/cms_trial/space/JMWEC/465373277/Variables+in+Nunjucks+Templates/) variables in your condition and test it using the [Nunjucks tester](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=mwecs&title=Nunjucks%20template%20editor%20and%20tester&linkCreation=true&fromPageId=449446200).  
  **Examples:**  
  `{{linkTypeName == "blocks"}}`returns `true` for all linked issues linked to the current issue with `blocks` link type  
  `{{linkedIssue.fields.status.name == "Rejected"`}} returns `true` for all linked issues that are in the `Rejected` status.

## Advanced options

### Run As

This option enables you to configure as which Jira user the post-function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

### Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.