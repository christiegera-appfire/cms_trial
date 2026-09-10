# Epics

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Epics JQL functions

**JQL functions** are accessible from the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page or [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in Jira advanced search. When using functions, the issues returned are based on the subquery defined in parentheses.

### epicsOfChildrenInQuery()

For a given JQL subquery, it finds the epics of the resulting issues.

Examples:

`issue in epicsOfChildrenInQuery("'Team Name'='My great team'") and status='To Do'` finds my team’s epics that are still in progress  
`issue in epicsOfChildrenInQuery("assignee=currentUser() AND updated>-1d")` finds epics of my issues that were updated over the last day

### childrenOfEpicsInQuery()

For a given JQL subquery, it finds the children of the resulting epics.

Examples:

`issue in childrenOfEpicsInQuery("resolution is not empty") AND resolution is empty` finds issues in progress that belong to an epic which has finished  
`issue in childrenOfEpicsInQuery("fixVersion='21.0.1' AND component=UI AND labels='review'")` finds children of epics with a specific version, component, and label

## Epics JQL keywords

The following table summarizes the JQL keywords for ticket counts in the epic. Counts are based on the issue type and status.

| **Status \ Issue type** | **Any status** | **TO DO** | **IN PROGRESS** | **DONE** |
| --- | --- | --- | --- | --- |
| Any issue type | issuesInEpicCount | issuesInEpicToDoCount | issuesInEpicInProgressCount | issuesInEpicDoneCount |
| Story | storiesInEpicCount | storiesInEpicToDoCount | storiesInEpicInProgressCount | storiesInEpicDoneCount |
| Bug | bugsInEpicCount | bugsInEpicToDoCount | bugsInEpicInProgressCount | bugsInEpicDoneCount |

### issuesInEpicCount

Search for epics with a specific number of child issues regardless of issue type.

### bugsInEpicCount

Search for epics with a specific number of bugs.

### storiesInEpicCount

Search for epics with a specific number of stories.

### issuesInEpicToDoCount

Search for epics with a specific number of child issues in the To Do status.

### issuesInEpicInProgressCount

Search for epics with a specific number of child issues in the In Progress status.

### issuesInEpicDoneCount

Search for epics with a specific number of child issues in the Done status.

### bugsInEpicToDoCount

Search for epics with a specific number of bugs in the To Do status.

### bugsInEpicInProgressCount

Search for epics with a specific number of bugs in the In Progress status.

### bugsInEpicDoneCount

Search for epics with a specific number of bugs in the Done status.

### storiesInEpicToDoCount

Search for epics with a specific number of stories in the To Do status.

### storiesInEpicInProgressCount

Search for epics with a specific number of stories in the In Progress status.

### storiesInEpicDoneCount

Search for epics with a specific number of stories in the Done status.