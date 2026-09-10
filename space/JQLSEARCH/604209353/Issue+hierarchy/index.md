# Issue hierarchy

This page describes JQL functions that help you search across Jira issue hierarchies. You can use these functions to find parent issues, child issues, or recursive relationships between issues in both the standard Jira hierarchy and Advanced Roadmaps hierarchy levels. These functions are useful when building filters, reports, or searches that depend on issue relationships rather than individual issue attributes.

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Jira hierarchy JQL functions

**JQL functions** are accessible from the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page or [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in Jira advanced search. When using functions, the issues returned are based on the subquery defined in parentheses.

### parentsOfIssuesInQuery()

For a given JQL subquery, it finds the parents of the resulting issues. It supports Advanced Roadmaps “Parent Link” and a standard Jira Hierarchy Epic → Story → Subtask.

Also, refer to ParentsOfIssuesInQueryRecursive.

**Examples**

`issue in parentsOfIssuesInQuery("project='ACME' and type=Epic")` finds all parents of epics in project ACME. Parents of epics are usually called Initiative.  
`issue in parentsOfIssuesInQuery("assignee=currentUser()")` finds parents of all of my issues.

### parentsOfIssuesInQueryRecursive()

For a given JQL subquery, it finds issues in the hierarchy above the resulting issues up to an optional depth. It supports Advanced Roadmaps “Parent Link” and a standard Jira hierarchy Epic → Story → Subtask.

**Examples**

`issue in parentsOfIssuesInQueryRecursive("project='ACME' and type=Epic")` finds all parents of epics in project ACME, and parents of parents, and so on. Parents of epics are usually called Initiative.  
`issue in parentsOfIssuesInQueryRecursive("assignee=currentUser() and issueType in subtaskIssueTypes()", 2)` finds parents of my subtasks and epics of the parents, skips anything above epics.

### childrenOfIssuesInQuery()

For a given JQL subquery, it finds the children of the resulting issues. It supports Advanced Roadmaps “Parent Link” and a standard Jira hierarchy Epic → Story → Subtask. Also, have a look at ChildrenOfIssuesInQueryRecursive.

**Examples**

`issue in childrenOfIssuesInQuery("project='ACME' and type=Initiative")` finds all epics in initiatives in project ACME.  
`issue in childrenOfIssuesInQuery("assignee=currentUser()")` finds children of all of my tickets.

### childrenOfIssuesInQueryRecursive()

For a given JQL subquery, it finds issues in the hierarchy below the resulting issues up to an optional depth. It supports Advanced Roadmaps “Parent Link” and a standard Jira hierarchy Epic → Story → Subtask.

**Examples**

`issue in childrenOfIssuesInQueryRecursive("project = 'ACME' and type = Initiative")` finds all epics, stories, and subtasks in initiatives in project ACME.  
`issue in childrenOfIssuesInQueryRecursive("assignee = currentUser() and type = Initiative", 2)` finds epics and stories of all of my epics and skips the subtasks.

## Issue hierarchy keywords

### childrenCount

Find issues with a specific number of immediate children (one level down in hierarchy). This keyword is applicable to all issue types in both standard and custom hierarchies. Use `childrenCount` when you want to filter by the number of direct children only, or when you want to identify issues without children (childrenCount = 0)

For epic-specific children counts with status breakdowns, use issuesInEpicCount or bugsInEpicCount instead.

**Examples**

`childrenCount = 0` Finds issues that don't have any children.

`type = Epic AND childrenCount > 5` Finds epics with more than five children.

`project = ACME AND childrenCount = 3` Finds issues inthe ACME project with exactly three children.

`childrenCount > 0` Finds issues with at least one child.