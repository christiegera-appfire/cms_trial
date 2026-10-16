# Set Issue Security Level

A workflow post function that sets the **Security Level** of the current issue based on the project role to which the current user belongs.

When you add this post function to a transition and trigger the transition, the add-on sets the selected issue security level on the current issue, if and only if the current user belongs to the selected project role.

This function can be used on the Create transition to set a different issue security level depending on whether the issue is being created by an internal user or by an external user (e.g. a customer).

**Warning**: JMWE cannot take any actions or make any changes to an issue that has a Security Level to which the JMWE Addon user does not have permissions. This includes, but is not limited to, setting the Security Level of an issue. Additionally, if the **Set Issue Security Level** post function is used to change an issue’s Security Level to a level at which JMWE does not have permissions, it creates a scenario where JMWE cannot make any changes.

[Unmapped macro: 47fa61b6-fe1c-40c9-b236-623cdbc35833/4d8fa66b-88bf-4899-a37e-5926131c46ac/static/multiexcerpt-fast-include-block-macro — no content to fall back on]

![postFunction-SetIssueSecurityLevel.png](/cms_trial/assets/5178522b-a17f-41ef-b29b-854bc5dbde39.png)

After adding, move the post function to the appropriate position according to [Placing post functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=mwecs&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=1126793316).

## Configuration options

- **Project Role** - Select the Project Role to which the user who triggers the transition must belong; if the user belongs to that Project Role, the issue will be set to the selected security level.
- **Issue Security Level** - Select the security level for the issue.

## Advanced options

Expand this section to see advanced configurations including which user will run the post function, conditional execution, and delayed execution.

## Conditional execution

It is possible to configure the post function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post function, so that the sub-tasks are created before they are transitioned.

Where possible, it is recommended to use the [Sequence of post-functions](/cms_trial/space/JMWEC/466322933/Sequence+of+post+functions/) post function or [Shared action](/cms_trial/space/JMWEC/466323396/Shared+Action+post+function/) post function to execute a series of post functions in a specific sequence instead of applying a delay.