# Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.

![JMWE for Jira Cloud delayed execution configuration for workflow transitions](/cms_trial/assets/da776230-5b7b-4991-b459-721b0cdfd501.png)

### Sample use cases for Delayed execution

[light bulb on icon] *On the creation of a Bug, assign it to a member of the QA team and then add the Assignee to the Watchers.*

Steps

|  |
| --- |
| - Create a **QA** project role, with the testers as its members. - Add the *Assign to role member* post-function to the transition **Create** of the Bug workflow. - Select `QA` as the project role to look for. |

|  |
| --- |
| - Add the *Copy value from field to field* post-function to the **Create** transition of the Bug workflow. - Select `Assignee` as the `From` field. - Select `Watchers` as the `To` field. - Select the `Delayed execution` option and select `5 sec` from the `Delay` drop-down. |

[light bulb on icon]*On the approval of a Story, create subtasks for Development and QA, and transition them to In Progress status.*

Steps

|  |
| --- |
| - Add the *Create issue* post-function to the Approve transition of the Story workflow. - Select `Same as current issue` from the `Project` field. - Select `Subtask` from the `Issue type` field. - Select `Current issue` from the `Parent issue`field. - Repeat the above steps for the `Development`subtask. |

|  |
| --- |
| - Add the *Transition linked issues* post-function to the Approve transition of the Story workflow. - Select `Issue Link Type` as `is Parent of.` - Select the `Delayed execution` option and select `10 sec` from the `Delay` drop-down. |