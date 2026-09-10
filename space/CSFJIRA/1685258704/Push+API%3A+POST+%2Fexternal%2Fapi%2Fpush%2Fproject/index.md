# Push API: POST /external/api/push/project

## **Before you start**

Before you start working with REST APIs, make sure you have:

- Checked the [Authenticate API](/cms_trial/space/CSFJIRA/1853817917/Authenticate+REST+APIs/) instructions.
- Use the correct Connector for Salesforce and Jira Cloud instance URL: [https://sfjc.integration.appfire.app](https://sfjc.integration.appfire.app/) or [https://eu-sfjc.inte](https://eu-sfjc.integration.appfire/)[gration.appfire](https://eu-sfjc.integration.appfire/).app, depending on your data residency location.

## **Endpoint**: POST **/external/api/push/project/{projectId}/issue/{issueId}/to/{son}/{soid}**

### **Description**

The Push API allows you to push updates from Jira to Salesforce. This API is not required to create the association but is useful for scenarios where you need to sync data between Jira and Salesforce after the association is established. For example, you might use the Push API to ensure updates to a Jira issue are reflected in the associated Salesforce record.

### Path parameters

- `projectId` (string, required): The ID of the Jira project to which the issue belongs.
- `issueId` (string, required): The Jira issue ID of the Jira issue that you want to synchronize.
- `son` (string, required): The name of the Salesforce object to which the Jira issue is associated (for example, `Case`, `Opportunity`).
- `soid` (string, required): Salesforce object ID for the specific record synchronized with the Jira issue.

### Example

```json
POST /external/api/push/project/10001/issue/11816/to/Case/500J80000019IF9IAM
```

## Related pages

[Authenticate SFJC REST APIs](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1694138509)