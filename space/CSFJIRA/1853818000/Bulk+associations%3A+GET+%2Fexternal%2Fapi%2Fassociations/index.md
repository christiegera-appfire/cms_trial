# Bulk associations: GET /external/api/associations

## **Before you start**

Before you start working with REST APIs, make sure you have:

- Checked the [Authenticate API](/cms_trial/space/CSFJIRA/1853817917/Authenticate+REST+APIs/) instructions.
- Use the correct Connector for Salesforce and Jira Cloud instance URL: [https://sfjc.integration.appfire.app](https://sfjc.integration.appfire.app/) or [https://eu-sfjc.inte](https://eu-sfjc.integration.appfire/)[gration.appfire](https://eu-sfjc.integration.appfire/).app, depending on your data residency location.

## Endpoint: GET /external/api/associations?jiraIssueId={}

### Description

Retrieves all associations with Salesforce records for a specified Jira issue.

### Query parameters

- `jiraIssueId` (string, required): The Jira issue ID.

### Example

```json
GET /external/api/associations?jiraIssueId=11816
```

### Response parameters

- `jiraIssueId` (string, required): the Jira issue ID is the unique identifier of the Jira issue you want to associate.
- `son` (string, required): Salesforce object name, for example, `Case`, `Account`, `Contact`.
- `soid` (string, required): Salesforce object ID for the specific record associated with the Jira issue.
- `viewOnly` (boolean, optional): `true` for a view-only association.
- `autoPush` (boolean, optional): `true` for automatic data push from Jira to Salesforce.
- `autoPull` (boolean, optional): `true` for automatic data pull from Jira to Salesforce.

### Example response

```text
{
    "data": [
        {
            "jiraIssueId": "11816",
            "son": "Case",
            "soid": "500J80000019IF9IAM",
            "viewOnly": false,
            "autoPush": false,
            "autoPull": false
        }
    ],
    "message": "Associations fetched successfully",
    "success": true
}
```

## Related pages

[Authenticate SFJC REST APIs](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1694138509)