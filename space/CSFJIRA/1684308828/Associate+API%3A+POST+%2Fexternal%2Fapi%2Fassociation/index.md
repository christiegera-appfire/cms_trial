# Associate API: POST /external/api/association

## **Before you start**

Before you start working with REST APIs, make sure you have:

- Checked the [Authenticate API](/cms_trial/space/CSFJIRA/1853817917/Authenticate+REST+APIs/) instructions.
- Use the correct Connector for Salesforce and Jira Cloud instance URL: [https://sfjc.integration.appfire.app](https://sfjc.integration.appfire.app/) or [https://eu-sfjc.integration.appfir](https://eu-sfjc.integration.appfire/)[e](https://eu-sfjc.integration.appfire/).app, depending on your data residency location.

## **Endpoint: POST /external/api/association**?allowUpsert={}

### **Description**

The Associate API associates a Jira issue with a Salesforce record. You can specify whether the association should be view-only and configure automatic push and pull behaviors.

### Query Parameters

- `allowUpsert` (boolean, optional): Whether to allow upsert functionality (insert or update).   
  Default: `false`

### Example

```json
POST /external/api/association?allowUpsert=false
```

### **Request body**

- `jiraIssueId` (string, required): the Jira issue ID is the unique identifier of the Jira issue you want to associate.
- `son` (string, required): Salesforce object name, for example, `Case`, `Account`, `Contact`.
- `soid` (string, required): Salesforce object ID for the specific record to be associated with the Jira issue.
- `viewOnly` (boolean, optional): Set to `true` to create a view-only association.   
  Default: `false`
- `autoPush` (boolean, optional): Set to `true` to enable automatic data push from Jira to Salesforce.  
  Default: `false`
- `autoPull` (boolean, optional): Set to `true` to enable automatic data pull from Jira to Salesforce.  
  Default: `false`

### Example request body

```json
{
	"jiraIssueId": "10173",
	"son": "Case",
	"soid": "500Qy00000VvNShIAN",
	"viewOnly": false,
	"autoPush": true,
	"autoPull": true
}
```

### Example response body

```json
{
	"data": {
		"jiraIssueId": "10173",
		"son": "Case",
		"soid": "500Qy00000VvNShIAN",
		"viewOnly": false,
		"autoPush": true,
		"autoPull": true
	},
	"message": "Association created successfully",
	"success": true
}
```

## Related pages

- [Authenticate API](/cms_trial/space/CSFJIRA/1853817917/Authenticate+REST+APIs/)