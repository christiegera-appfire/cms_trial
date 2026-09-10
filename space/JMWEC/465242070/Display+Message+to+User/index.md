# Display Message to User

A workflow post-function that displays a message on the issue view page to the user triggering the transition.

When you add this post-function to a transition and trigger the transition, a message is displayed to the user triggering the transaction as a “flag” in the top right corner of the issue view page. The displayed message (see **Example message**, pictured below) can be customized, including the message type (icon), the message header and body, and action links.

![Display Message post function configuration screen](/cms_trial/assets/e81b89b2-a880-44d6-a242-46d2cb1edb6b.png)

**To add 'Display Message to User' post function to a transition:**

1. Click **Edit** for the workflow that has the transition to which you wish to add the post function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Display Message to User** from the list of post function.
6. Click **Add** to navigate to the *Display Message to User post-function* screen where you can add configuration details. See below for more information.
7. Click on **Add** to add the post function to the transition.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

![JMWE for Jira Cloud display message to user interface showing user notification](/cms_trial/assets/4c648486-5d29-48ae-8a45-b33ea2360e03.png)

## Options

The two primary options are the message title and the message body. You can set these as static strings or you can use Nunjucks to insert issue or user data into either value; see [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) for more information on creating dynamic values.

- **Message title** - Enter the message title (the bold text at the very top of the message flag).
- **Message body** - Enter the message text (the text just below the message title).

## Advanced options

Expand this section to see advanced configurations including which user will run the post function, conditional execution, and delayed execution.

### Message type

You can set the message type, which control the visual appearance of the flag including its icon.

- **Message type** - Select the type of message.
- **Automatically close message** - Automatically close the message without user interaction.

### Action link

You can add an action link to the message which, when clicked, can navigate to another issue or to a selected URL.

- **Add action link** - Add an action link at the bottom of the message flag.

  - **Action title** -Input the title of the action link that will be displayed at the bottom of the message.
  - **Action type** -Select the type of action to be performed.

    - **Navigate to URL** - Input a text that represents a valid URL or a [Nunjucks template](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) that returns a valid URL. For example:

      ```groovy
      https://www.appfire.com
      ```
    - **Navigate to another issue:** Input a valid issue key or a [Nunjucks template](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) that returns an issue key. For example:

      ```groovy
      TEST-1
      ```

      ```groovy
      {{ issue.fields.parent.key }}
      ```

## Conditional execution

It is possible to configure the post-function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.