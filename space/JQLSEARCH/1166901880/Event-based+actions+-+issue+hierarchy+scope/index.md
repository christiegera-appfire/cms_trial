# Event-based actions - issue hierarchy scope

The following use cases use JQL Search Extensions (JSE) hierarchy recursive functions to set the scope for an [event-based action](https://appfire.atlassian.net/wiki/x/9I__Gw) in JMWE.

**Recursive functions**  
When you want the scope of your search filter to apply to the hierarchy above or below the initial query, you can use JSE’s `ParentsOfIssuesInQueryRecursive()` or `ChildrenOfIssuesInQueryRecursive()` functions. For example, you can copy a comment from an epic to all the corresponding stories and their subtasks.

## Problem to solve

Organizations managing complex projects in Jira often struggle to maintain clarity and ensure consistent communication across hierarchies, such as Epic-to-Story and Story-to-Subtask relationships. When there are key updates, like issue status changes or the closure of parent issues, the associated child or parent issues are not automatically updated with relevant information. This creates bottlenecks in communication and project alignment, as team members may miss critical updates unless they manually check related issues. This leads to inefficiencies, potential errors, and delays in project delivery, particularly in industries where managing dependencies across multiple levels is essential.

## Solution

Combine JQL Search Extensions issue hierarchy functions with JMWE’s event-based actions to automatically update all child or parent issues. The following examples resolve the problem scenario using JQL Search Extensions recursive functions.

## When an issue is updated, add a comment on all parent issues

|  |  |
| --- | --- |
| **JSE function** | `ParentsOfIssuesInQueryRecursive()` |
| **JMWE event** | Issue Updated |
| **JMWE action** | Comment Issues |
| **Method** | 1. In JQL Extended Search, perform a search for parent issues matching a given query, for example:  ```text    issue in parentsOfIssuesInQueryRecursive("project='ACME' and status=Approved")    ``` Screenshot of the Extended Search page in JSE with the query as described on this page. 2. Save the query as a filter. For this example, the filter is called `JSE-ACME-parents of approved`. 3. In JMWE, create or edit an [event-based action](https://appfire.atlassian.net/wiki/x/9I__Gw) to use the *Issue Updated* event. 4. Set the scope to **Only apply to issues that match a JQL filter**. 5. Click the JQL input box, then search using the filter name, for example, `filter="JSE-ACME-parents of approved"`. 6. Click **Save**. The filter is added to your event-based action configuration. 7. Add the *Comment issues* post function. 8. Save the action. Screenshot of the configured JMWE Issue Updated event as described on this page. Now, when an issue meeting the JQL filter criteria is updated, the comment configured for step 7 is added to the issue. You can apply the same use case to other [events](https://appfire.atlassian.net/wiki/x/9I__Gw), for example, Issue Deleted. |

## When a parent issue is closed, add a comment on all matching child issues

|  |  |
| --- | --- |
| **JSE function** | `ChildrenOfIssuesInQueryRecursive()` |
| **JMWE event** | Issue Closed |
| **JMWE action** | Comment Issues |
| **Method** | 1. In JQL Extended Search, perform a search for child issues matching a given query, for example:  ```none    issue in childrenOfIssuesInQueryRecursive("project='ACME' and type=Epic     and status=Closed")    ``` Screenshot of the Extended Search page in JSE with a query as described on this page. 2. Save the query as a filter. For this example, the filter is called `JSE Children of Closed Epics`. 3. In JMWE, create or edit an [event-based action](https://appfire.atlassian.net/wiki/x/9I__Gw) to use the *Issue Closed event*. 4. Set the scope to **Only apply to issues that match a JQL filter**. 5. Click the JQL input box, then search using the filter name, for example, `filter="JSE Children of Closed Epics"`. 6. Click **Save**. The filter is added to your event-based action configuration. 7. Add the *Comment issues* post function. 8. Save the action. Screenshot of the configured JMWE Issue Closed event as described on this page. Now, when an Epic is closed, the comment configured for step 7 is added to the issues meeting the JQL filter criteria. |

If you are not already using JMWE, you can try out these features with a free trial license. Visit our JMWE [marketplace listing](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?hosting=cloud&tab=overview) to learn more.