# Set Issue Security Level

A workflow post-function that sets the **Security Level** of the current issue based on the project role to which the current user belongs.

When you add this post-function to a transition and trigger the transition, the add-on sets the selected issue security level on the current issue, if and only if the current user belongs to the selected project role.

This function can be used on the Create transition to set a different issue security level depending on whether the issue is being created by an internal user or by an external user (e.g. a customer).

**Warning**: JMWE cannot take any actions or make any changes to an issue that has a Security Level to which the JMWE Addon user does not have permissions. This includes, but is not limited to, setting the Security Level of an issue. Additionally, if the **Set Issue Security Level** post function is used to change an issue’s Security Level to a level at which JMWE does not have permissions, it creates a scenario where JMWE cannot make any changes.

![JMWE for Jira Cloud set issue security level post function configuration](/cms_trial/assets/87a7792f-dde7-47b0-9446-3e0629877a89.png)

**To add the 'Set Issue Security Level' post function to a transition:**

1. Click **Edit** for the workflow that has the transition you wish to add the post function to.
2. Select the transition in the Workflow Designer.
3. Click **Post Functions** in the properties panel (or select the **Post Functions** tab).
4. Click**Add post function**.
5. Select *Set Issue Security Level* from the list of post functions.
6. Click **Add**. The *Set Issue Security Level post function*screen will open, where you can configure the post function as needed. See below for more information.
7. Click **Add** to complete the configuration and add the post function to the transition.

After adding, move the post function to the appropriate position according to [Placing post functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=mwecs&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=1126793316).

## Configuration options

- **Project Role** - Select the Project Role to which the user who triggers the transition must belong; if the user belongs to that Project Role, the issue will be set to the selected security level.
- **Issue Security Level** - Select the security level for the issue.

## Advanced options

Expand this section to see advanced configurations including which user will run the post function, conditional execution, and delayed execution.

## Conditional execution

Check **Run this post-function only if a condition is verified** to execute this post function based on the result of a Nunjucks template; see [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/).

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.