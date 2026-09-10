# How to run the association report via REST API

The Connector for Salesforce & Jira app supports reporting Jira work items associated with Salesforce records. To learn more about the association report, see the [Run an association report](https://appfire.atlassian.net/wiki/x/XYVtd) page.

The association report lists all Jira work items associated with Salesforce records. You can access this report through:

- The Jira user interface
- REST API calls

## Instructions

### For Jira UI

1. In Jira, click the **Apps** menu.
2. Under *Connector for Salesforce*, select **Reports**.
3. Enter the **JQL** query to filter the results.  
   For example, to show only Jira work items associated with a Salesforce case with the Record ID `5000K00002c6XA5QAM`.

#### Example JQL query

```text
salesforceAssociatedIds ~ 5000K00002c6XA5QAM
```

![reports.png](/cms_trial/assets/54272fb0-4539-4d79-a2c3-63d6d9237aae.png)

### For REST API calls

### Before you start

Make sure to replace the following values:

- Replace `{JIRA_URL}` with your actual Jira Base URL
- Replace `5000K00002c6XA5QAM` with your target Salesforce Record ID (when searching for a specific record)

You can run these API requests using [Postman](https://www.postman.com/), or by entering the URL in your browser while logged into Jira.

- To search for work items linked to a specific Salesforce record, run the following request:

```html
{JIRA_URL}/rest/api/2/search?jql=salesforceAssociatedIds~5000K00002c6XA5QAM%20&properties=com.servicerocket.jira.cloud.issue.salesforce.associations&fields=key
```

- To search for all associated Jira work items (without filtering the results) with any Salesforce connection, run the following request:

```text
{JIRA_URL}/rest/api/2/search?jql=salesforceAssociatedIds is not EMPTY &properties=com.servicerocket.jira.cloud.issue.salesforce.associations&fields=key
```