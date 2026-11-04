# Find work items linked to epics

Use JQL Search Extensions to find work items linked to multiple epics in one search. This helps you review dependencies and related work without checking each epic's links individually.

Jira's [built-in linked-issue search](https://support.atlassian.com/jira-work-management/docs/advanced-search-reference-jql-functions/) uses `linkedIssues()` with the key of a specific work item. In contrast, `linkedIssuesOfQuery()` accepts a JQL query to select a group without listing individual keys.

To find work items linked to epics:

1. In Jira, go to **Apps** > **JQL Search Extensions** > **Extended Search**.
2. On the *Classic JQL* tab, enter the following query:

   ```text
   issue in linkedIssuesOfQuery("type = Epic")
   ```
3. Press Enter to run the search.
4. Review the returned work items.

The results table lists work items linked to epics. The example image shows the query and its results.

![JQL Search Extensions Extended Search showing work items linked to epics.](/cms_trial/assets/939b75c5-bd17-4987-8630-fb1e701c8dd5.png)

## How the query works

Read the query from the inside out.

### The inner query identifies the epics

The text inside the quotation marks, `type = Epic`, is the **inner query**. It finds the epics whose links you want to search.

This condition applies to the starting work items, not to the work items returned in the final results.

### The function finds linked work items

The `linkedIssuesOfQuery()` function uses the epics found by the inner query to identify work items connected to them through issue links.

The `issue in` clause selects those linked work items as the search results.

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