# Event-based actions - issue links scope

The following use cases use JQL Search Extensions (JSE) [issue links keywords](/cms_trial/space/JQLSEARCH/604209269/Issue+links/) to set the scope for[event-](https://appfire.atlassian.net/wiki/x/9I__Gw)[based](https://appfire.atlassian.net/wiki/x/9I__Gw) [actions](https://appfire.atlassian.net/wiki/x/9I__Gw) in JMWE.

## Problem to solve

In project workflows where issues are often linked to other tasks or bugs, status updates on one issue may not automatically reach related tickets, resulting in communication delays and overlooked dependencies. For instance, when a bug is resolved, any associated tasks or customer support tickets should ideally receive an update so relevant teams can take appropriate action.

## Solution

Combine JQL Search Extensions with JMWE’s event-based actions to ensure timely updates and notifications on linked issues.

## For issues linked to bugs, comment on the linked ticket when resolved

|  |  |
| --- | --- |
| **JSE keyword** | `linkedIssueType` |
| **JMWE event** | Issue Resolved |
| **JMWE action** | Comment Issues |
| **Method** | 1. In JQL Extended Search, perform a search for issues linked to bugs, for example:  ```text    linkedIssueType = Bug    ```   You can refine this by adding other criteria if needed. Screenshot of the Extended Search page with the query as described on this page. 2. Save the query as a filter. For this example, the filter is called `Issues linked to bugs`. 3. In JMWE, create or edit an [event-based action](https://appfire.atlassian.net/wiki/x/9I__Gw) to use the *Issue Resolved* event. 4. Set the scope to **Only apply to issues that match a JQL filter**. 5. Click the JQL input box, then search using the filter name, for example, `filter="Issues linked to bugs"`. 6. Click **Save**. The filter is added to your event-based action configuration. 7. Add the *Comment issues* post function. 8. Save the action. Screenshot of the configured JMWE Issue Resolved event as described on this page. Now, when an issue is resolved, issues meeting the JQL filter criteria are updated with the comment configured for step 7. You can apply the same use case to[other events](https://appfire.atlassian.net/wiki/x/9I__Gw), for example, Issue Deleted. |

## When an issue moves to In Progress, change any linked issue in the To Do status to In Progress

|  |  |
| --- | --- |
| **JSE keyword** | `linkedIssueStatus` |
| **JMWE event** | Issue Transitioned |
| **JMWE action** | Transition Issue |
| **Method** | 1. In JQL Extended Search, perform a search for child issues matching a given query, for example:  ```text    linkedIssueStatus = "To Do"    ``` Screenshot of the Extended Search page with the query as described on this page. 2. Save the query as a filter. For this example, the filter is called `Linked issues in To Do`. 3. In JMWE, create or edit an[event-based action](https://appfire.atlassian.net/wiki/x/9I__Gw) to use the *Issue Transitioned* event. 4. Set the scope to **Only apply to issues that match a JQL filter**. 5. Click the JQL input box, then search using the filter name, for example, `filter="Linked issues in To Do"`. 6. Click **Save**. The filter is added to your event-based action configuration. 7. Add the *Transition issues* post function. 8. Save the action. Screenshot of the configured JMWE Issue Transitioned event as described on this page. Now, when an issue is transitioned to in progess linked issues meeting the JQL filter criteria are transitioned from To Do to In progrss . |