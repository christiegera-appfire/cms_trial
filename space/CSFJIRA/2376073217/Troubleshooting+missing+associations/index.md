# Troubleshooting missing associations

## Change overview

We've madearchitectural changes to how associations are stored and accessed in Connector for Salesforce. Associations are no longer stored in Jira's Entity Properties system and have been moved to a dedicated database for better performance and scalability.

The new solution enables you to have more than 300 associations per issue and improves performance and reliability for large-scale usage

## Key changes

- Associations are no longer stored under the `com.servicerocket.jira.cloud.issue.salesforce.associations` Entity Property key
- While this key still exists after your update, it is no longer the source of truth for your associations
- All associations have been moved to a dedicated database system
- The plugin now only updates the `ids` and `types` fields in the Entity Property
- The `associations` field will be overwritten the first time you modify an issue's associations

Any custom integrations reading from Entity Properties will break

### New API endpoints

The `com.servicerocket.jira.cloud.issue.salesforce.associations` Entity Property key is deprecated. You need to stop using Entity Properties for association data. Instead, use the new required API endpoints. For details on the API, see the [API reference](/cms_trial/space/CSFJIRA/1685193166/API+reference/).

## Are you affected?

You are likely affected if:

- You have custom scripts or integrations that read association data
- You're missing associations that existed before the update
- Your third-party tools can no longer access Salesforce association data
- You're seeing errors in applications that previously worked with associations

You should not be affected if:

- You only use the plugin's built-in interface (no custom integrations)
- All your associations are still visible and working normally

## What to do

Use the new API endpoints required. For details on the API, see the [API reference](/cms_trial/space/CSFJIRA/1685193166/API+reference/).