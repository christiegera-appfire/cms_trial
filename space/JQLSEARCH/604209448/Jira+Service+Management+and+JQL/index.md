# Jira Service Management and JQL

Jira provides good support for querying issues [by their SLAs](https://support.atlassian.com/jira-service-desk-cloud/docs/write-jql-queries-for-slas/). There are also more advanced and very useful processes that you can set up with the help of [JQL Search Extensions](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira-reports?hosting=cloud&tab=overview&utm_source=documentation&utm_medium=link&utm_campaign=jsd_jql_page).

## Find Jira issues that are awaiting response

### Special issue status: Waiting for customer

You are in the simplest situation if your workflow has a special issue type to which issues are moved when they are waiting for the customer response. JSD administrators typically set up automation rules that transition issues to *Waiting for customer* status whenever an operator adds a comment.

You can simply search for issues in the *Waiting for customer* status:

```sql
project="JQL Search Extensions" AND issuetype="Waiting for customer"
```

### Last commented by operator

Alternatively, you can search for issues that were last commented by an operator. We assume it’s the customer’s turn to respond:

```sql
commentLastCreatedBy in membersof(jsd-operators-staff) AND resolution is EMPTY
```

### Time since last commented

You can also identify the tickets that nobody commented on for a while. To find issues that were last commented on over 3 days ago:

```sql
commentLastCreatedOnDate < -3d
```

And to find the issues that require the operator’s attention:

```sql
commentLastCreatedOnDate < -1d AND commentLastCreatedBy not in membersof(jsd-operators-staff) AND resolution is EMPTY
```

In the above query, the last comment was created by a customer because they are not in the *jse-operator-staff* user group.