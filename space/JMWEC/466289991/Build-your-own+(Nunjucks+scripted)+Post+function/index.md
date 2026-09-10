# Build-your-own (Nunjucks scripted) Post function

This post function allows you to run an Nunjucks template (script) when a transition is triggered. This can be used to create entirely custom own post functions.

![Scripted post function configuration screen](/cms_trial/assets/a54c2fdb-8ee5-42e2-9a8e-6d51fb2ffb8f.png)

**To add the 'Build-your-own (Nunjucks scripted)' post function to a transition:**

1. Click **Edit** for the workflow that has the transition to which you wish to add the post function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Build-your-own (scripted) Post-function** from the list of post function.
6. Click **Add** to navigate to the *Build-your-own (Nunjucks scripted) Post-function* screen where you can add configuration details. See below for more information.
7. Click on **Add** to add the post function to the transition.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

## Custom script

Configure your custom script:

- **Description** - Give the post function a meaningful description.
- **Nunjucks script** - Enter the script that should be executed when the post function runs.

## Advanced options

Expand this section to see advanced configurations including delayed execution.

### Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.