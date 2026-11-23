# Find work items linked to epics

Use JQL Search Extensions to find work items linked to multiple epics in one search. This helps you review dependencies and related work without checking each epic's links individually.

Jira's [built-in linked-issue search](https://support.atlassian.com/jira-work-management/docs/advanced-search-reference-jql-functions/) uses `linkedIssues()` with the key of a specific work item. In contrast, `linkedIssuesOfQuery()` accepts a JQL query to select a group without listing individual keys.

To find work items linked to epics:

1. From the native Jira search bar, enter the following query:

   ```text
   issue in linkedIssuesOfQuery("type = Epic")
   ```

Note that JQL Search Extension queries can also be run directly in dashboard gadgets.

1. On the *Classic JQL* tab, enter the following query:
2. Press Enter to run the search.
3. Review the returned work items.

The results table lists work items linked to epics. The example image shows the query and its results.

![JQL Search Extensions Extended Search showing work items linked to epics.](/cms_trial/assets/939b75c5-bd17-4987-8630-fb1e701c8dd5.png)

The sample query above runs across *all* Jira projects. To limit results to a single project, change the query to (replace Project name with the name of your Jira project).

```text
issue in linkedIssuesOfQuery("type = Epic" and project = 'Project name'")"
```

## How the query works

Read the query from the inside out.

### The inner query identifies the epics

The text inside the quotation marks, `type = Epic`, is the **inner query**. It finds the epics whose links the function searches.

This condition doesn’t limit the final results to epics. Linked tasks, bugs, and other work items can also display in query results.

### The function finds linked work items

The `linkedIssuesOfQuery()` function returns work items connected through lissue links to any of the epics identified by the inner query.

For example, a bug linked to one of those epics can appear in the results even through the bug’s work item type is not Epic.

## Understand the search results

Results can include tasks, bugs, and other epics.

For example, a bug linked to an epic through a **blocks** relationship can appear in the results. The bug doesn't need to be an epic itself.

Review the **Status** and **Assignee** columns to identify unfinished or unassigned work that needs follow-up.

The query includes all issue link types, such as **blocks** and **relates to**, so not every result is a blocker. Open a returned work item and review its links to see how it relates to an epic.

This search follows [issue links](https://support.appfire.com/space/JQLSEARCH/604209269/Issue+links), not the parent-child hierarchy. A work item doesn't appear just because it belongs to an epic.

## Explore other searches with keywords and functions

JQL Search Extensions provides two ways to extend your searches:

- **Extended keywords** filter work items by additional information, such as the number of issue links. For example, `linksCount > 0` finds work items that have issue links.
- **Functions** accept inputs, such as a JQL query, to find related work items or perform other searches.

Explore searches for work items with attachments, epics with matching child work items, and other criteria. See the [JQL functions and keywords reference](https://support.appfire.com/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference) for syntax and examples.

## Save and reuse this search

You've used a function to find work items linked to epics.

Save the search as a filter to reuse it instead of rebuilding the query.

Continue to [Save and reuse an extended search](https://support.appfire.com/space/JQLSEARCH/3680174212/Save+and+reuse+an+extended+search).