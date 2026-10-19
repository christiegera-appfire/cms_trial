# Search related issues with a JSE function

JQL Search Extensions functions lets you perform searches that use other JQL queries as input. This lets you answer questions about relationships between groups of Jira users.

In this example, we’ll use `issue in parentsOfIssueInEpic (“Type = Epic”)` to find the parents of the work items returned by the nested JQL query.

Suppose you want to find work items connected to the `Epic` work item type through a specific issue link. Follow the steps below:

1. Open **JQL Search Extensions** > **Extended Search**.
2. Enter a query using `issue In parentsOfIssueInEpic (“Type = Epic”)`
3. Run the search.
4. Review the returned issues.

![contentId-3680174342](/cms_trial/assets/88aa27f6-843f-41b8-8d37-78e233cce874.png)

## How the query works

A JQL Search Extensions search combines a JQL query with a JSE function to find work items based on specific criteria and their relationships with other work items. The search consists of two main Components: the Inner Query and the JSE Function.

**The inner Query:**

This defines the initial set of work items you want to search. For example -

`Project = BIG and type=Epic`

This query finds all Epic work items in the BIG project.

**The JSE Function:**

It uses the work items identified by the inner query to find other work items based on their relationships or hierarchy. For example -

`issue in parentsOfIssuesInQuery()`

This function searches for the parent work items of the Epics returned by the inner query. By combining the inner query with a JSE function, you can extend your search beyond standard JQL and more easily discover relationships between work items.

![2026-10-05_15-27-49.jpeg](/cms_trial/assets/02a842bb-960f-4343-a8ab-9b16311d0aca.jpeg)

There is an important difference between JQL keywords and functions:

- **Keywords** let you search additional issue information.
- **Functions** let you perform more complex searches using parameters or the results of another query.

JSE includes functions for searching issue relationships, hierarchies, links, and other criteria that are difficult or impossible to express using standard JQL alone.

See the [**JQL functions and keywords reference**](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/) for the complete set of available functions and examples.

## You've extended your Jira search

You've now used JSE in two ways:

- An extended keyword to search additional issue information.
- A function to perform a search based on relationships between issues.

These searches become even more useful when you save them for later use.

Continue to [Save and reuse an extended search.](/cms_trial/space/JQLSEARCH/3680174212/Save+and+reuse+an+extended+search/)