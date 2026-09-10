# How to Display the Results of a JQL Query in a Graph

To display the results of your JQL query in a graph, you must add the JQL Custom Charts gadget.

When the JQL Custom Charts gadget is added, you proceed to configure it

1. In the Dashboard of your selected project, add the JQL Custom Charts gadget.

The Add gadget page is displayed.

1. Fill in the Add gadget page:

   1. Name the gadget referring to your query.
   2. Select the datasource, for example `This Jira Instance`.
   3. Select `Filter or Custom JQL` .
   4. Click on  `Load` to upload the data from your datasource.
   5. In  `View Type,` select how to display your results.
2. Click on Add to display the report with your results in the Dashboard.

If you choose to display your results in a table, you can drag and drop to change the order, and performing grouping and/or aggregations

For example, to list all the issues in the “Teams in Space” project (project = “TIS”) and still pending to do (status = "TO DO") sorted by CreationDate in descending order (ORDER BY created DESC) Type the following JQL query:

`project = "TIS" AND status = "TO DO" ORDER BY created DESC`

[Get started with JQL](https://www.atlassian.com/software/jira/guides/expand-jira/jql) or have a look to the [Advanced Search](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/) to master queries in Jira