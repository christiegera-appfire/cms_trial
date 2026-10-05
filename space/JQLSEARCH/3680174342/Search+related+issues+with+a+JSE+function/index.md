# Search related issues with a JSE function

## Search related issues with a JSE function

JQL Search Extensions functions let you perform searches that use other JQL queries as input. This lets to answer questions about relationships between groups of Jira issues.

In this example, you'll use `Issue in parentsOfIssuesInQuery` to find issues linked to issues returned by another JQL query.

## Search issues by their links

Suppose you want to find issues connected to issues in the `Bug` by a particular issue link type.

1. Open **JQL Search Extensions** > **Extended Search**.
2. Enter a query using

   `linkedIssueType = Bug`
3. Run the search.
4. Review the returned issues.

Replace `Bug` with a project key from your Jira instance and, if necessary, replace the link description with an issue link type used by your Jira configuration.

![2026-09-23_17-58-48.jpeg](/cms_trial/assets/e4ed48a1-582e-445c-93dd-3bafbea6250d.jpeg)

## How the query works

This search contains two parts.

**The inner query:**

`Project = BIG and type=Epic`

identifies the initial set of issues.

**The JSE function:**

`issue in parentsOfIssuesInQuery()`

uses those search results to find issues connected to them by the specified issue link relationship.

![2026-10-05_15-27-49.jpeg](/cms_trial/assets/02a842bb-960f-4343-a8ab-9b16311d0aca.jpeg)

There is an important difference between JSE keywords and functions:

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