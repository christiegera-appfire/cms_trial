# Send Slack message

A workflow post function that sends a message to Slack - to selected channel or channels, or to specific users.

**Note**: To utilize this post function, there are a few considerations outside of JMWE:

1. Use of this post function requires the free Slack app **Notifier by Appfire**. You will be prompted to install this app on Slack the first time you connect JMWE to your Slack workspace.
2. You must be an administrator of the Slack workspace to which you want to send messages; workspace administrator permissions are only required when connecting JMWE to a workspace, not for sending messages to a workspace.
3. You only need to connect to a workspace once.

**Note**: The **Send Slack message** post function does not include configuration options to Run As any user other than the app user; this is due to permission requirements within Slack when using the **Notifier by Appfire** app.

![Send Slack Message post function.](/cms_trial/assets/b8e67c8b-bb50-49c6-9667-a33207894f45.png)

**To add the 'Send Slack message' post function to a transition**:

1. Click **Edit** for the workflow that has the transition to which you wish to add the post function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Send Slack message** from the list of post functions.
6. Click **Add** to navigate to the *Send Slack Message*screen where you can add configuration details to the post function. See below for configuration details.
7. Click **Add** to add the post function to the transition.

After adding the post function, move the post function to the appropriate position according to [Placing post functions in a transition](/cms_trial/space/JMWEC/466289149/Adding+extensions+to+transitions/) document.

## Connect a Slack workspace

Before sending messages to Slack, you must connect JMWE to a Slack workspace. The first time you configure the **Send Slack message** post function, you will be prompted to connect to a workspace. To connect to a Slack workspace:

1. In the **Send Slack message** post function configuration page, click **Connect new workspace** to the right of the **Slack Workspace** pulldown menu.
2. A new tab will open.

   1. If this is your first connected workspace, the tab will include dialog for logging into your Slack workspace; enter your Slack URL and click **Continue**.
   2. If you have connected a workspace previously, but want to connect to a different workspace, select **Add another workspace** from the pulldown menu in the upper right corner. Enter the new Slack URL and click **Continue**.
3. You must install Notifier by Appfire in your Slack workspace. Click **Allow**.
4. Close the tab when prompted.

In the post function configuration screen, your Slack workspace should now be available in the **Slack Workspace** pulldown menu.

## Issue(s) to operate on

Select the issues to set the assignee field on. They can be:

- **Target issues**

  - **Current issue:** Select this option to set the assignee of the current issue. *This is the default option.*
  - **Sub-tasks of the current issue:** Select this option to set the assignee of sub-tasks of the current issue.
  - **Parent issue of the current sub-task:** Select this option to set the assignee of the parent of the current issue.
  - **Issues that belong to the current issue (Epic):** Select this option to set the assignee of issues that belongs to the current Epic.
  - **Epic of the current issue:** Select this option to set the assignee of the Epic of the current issue.
  - **Child issues of the current issue in the Portfolio hierarchy:** Select this option to set the assignee of child issues of the current issue in the Portfolio hierarchy.
  - **Parent issue of the current issue in the Portfolio hierarchy:** Select this option to set the assignee of the parent issue of the current issue in the Portfolio hierarchy.
  - **Issues linked to the current issue through any link type:** Select this option to set the assignee of the current issues' linked issues.
  - **Issues linked to the current issue through the following link type:** Select this option to set the assignee of issues linked to the current issue through a specific link type. Select the specific link type under “Issue link”.
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

## Recipients

Select workspace, channels and users to which the message will be sent.

- **Slack Workspace** - Select the workspace to which the message will be sent. See **Connect a Slack workspace**, above, for more information on connecting JMWE to Slack.
- **Slack Channels** - Select the channel or channels to which the message should be sent. Select multiple channels to add them to the list, and use the **X** to the right of a channel name to remove it.
- **Slack Users** - Select the users to whom the message should be sent. Select multiple users to add them to the list, and use the **X** to the right of a user name to remove it.

## Message content

Compose the content of the message. You can build Messages dynamically using Nunjucks templates to access Jira data within the message body.

- **Mode** - Select the composition mode.

  - **Plain text** - The message will be sent in plain text.
  - **Slack Block-kit** - Compose the message using the [Slack Block-kit API](https://api.slack.com/block-kit/building).
- **Message** - Compose your message.

## Advanced options

Expand this section to see advanced configurations, including conditional execution and delayed execution.

## Conditional execution

Check **Run this post-function only if a condition is verified** to execute this post function based on the result of a Nunjucks template; see [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/).

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.