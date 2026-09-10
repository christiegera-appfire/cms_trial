# Bulk associations: POST /external/api/associations

## **Before you start**

Before you start working with REST APIs, make sure you have:

- Checked the [Authenticate API](/cms_trial/space/CSFJIRA/1853817917/Authenticate+REST+APIs/) instructions.
- Use the Connector for Salesforce and Jira Cloud instance URL: [https://sfjc.integration.appfire.app](https://sfjc.integration.appfire.app/) or [https://eu-sfjc.inte](https://eu-sfjc.integration.appfire/)[gration.appfire](https://eu-sfjc.integration.appfire/).app, depending on your data residency location.

## **Endpoint: POST/external/api/associations?jiraIssueId{a Jira issue Id}&replace={true/false}**

### Description

Allows adding multiple associations for a single Jira issue. The `replace` parameter determines whether existing associations are overwritten.

### Query parameters

- `jiraIssueId` (string, required): The Jira issue ID
- `replace` (boolean, optional): Whether to replace existing associations. The default value is set to false.

### Example

```json
POST /external/api/associations?jiraIssueId=11816&replace=true
```

### Request body

- `son` (string, required): Salesforce object name, for example, `Case`, `Account`, `Contact`.
- `soid` (string, required): Salesforce object ID for the specific record associated with the Jira issue.
- `viewOnly` (boolean, optional): `true` for a view-only association.
- `autoPush` (boolean, optional): `true` for automatic data push from Jira to Salesforce.
- `autoPull` (boolean, optional): `true` for automatic data pull from Jira to Salesforce.

### **Example request body**

```text
{
    "associations": [
        {
            "son": "Case",
            "soid": "500J80000019IF9IAM",
            "viewOnly": false,
            "autoPush": false,
            "autoPull": false
        }
    ]
}
```

### **Example response body**

`totalAssociations` is the total association count on the Jira issue

```text
{
	"data": {
		"totalAssociations": 2
	},
	"message": "Associations created successfully",
	"success": true
}
```

### Constraints

- Maximum **1000 associations** per Jira issue.
- When `replace=true`, all previous associations are removed before adding the new ones.
- Existing associations are not duplicated when `replace=false`.

## Related pages

[Authenticate SFJC REST APIs](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1694138509)