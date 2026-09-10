# Troubleshooting missing associations after update

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

The `com.servicerocket.jira.cloud.issue.salesforce.associations` Entity Property key is deprecated. You need to stop using Entity Properties for association data. Instead, use the new API endpoints required: `POST /api/associations` (learn more [POST /api/associations](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/2375843900)) and `GET /api/associations` (learn more: [GET /api/associations](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/2376138754)).

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

If the upgrade fails, contact our support team - we can help you complete the migration safely. Your existing associations remain safe in the Entity Properties until migration completes.

If your upgrade succeeds, make sure all your associations have been migrated, and check the migration log.

## Migration log

When you upgrade, an automatic migration process runs to move all existing associations from Entity Properties to the new database system. The migration log CSV file provides detailed information on migration issues needed for database upgrade operations. This feature helps you monitor the success and failure of individual migration tasks during system upgrades. Thanks to it, you can identify missing associations and identify reasons for failure.

## Download migration log

You can download the migration log as a CSV file for analysis and record-keeping purposes.

1. Log in to your Jira Data Center instance as an administrator with the Jira System Administrators permissions.
2. Click the **cog icon** on the top bar and select, choose **Manage apps**.
3. On the left under **SALESFORCE**, open the **Settings** page.
4. Click **Download Migration Log** under the **Migration log** section and download the CSV file.

   ![image-20250825-123434.png](/cms_trial/assets/5f900eaf-3273-47c7-881b-c8bd10b4f2fe.png)

The downloaded CSV file contains information about your migration process result:

- Total number of successfully migrated issues
- Information about any issues that failed to migrate
- Reasons of failure

This data helps you understand the overall success of your migration and identify any issues that require your attention.

### Migration log entries

The migration log contains entries with different severity levels and detailed messages about what occurred during migration. Here are examples of common failure types you might see:

**Invalid SOID (Salesforce Object ID) Format:**

```text
WARN,TEST-711,"Issue TEST-711(10709) is associated with an invalid SOID 'Z9D4CTJPBY4HHtLLVM,DMYwmbnU9tx43t0740', cannot migrate. Skipping."
```

This indicates the association had a malformed Salesforce Object ID and couldn't be migrated.

**Missing required field values:**

```text
WARN,TEST-325,"Association between S9JxSLQchF4hQUmLJC and TEST-325(10318) does not contain valid 'son', cannot migrate. Skipping."
```

This shows an association was missing required field data (in this case, the 'son' field) and was skipped during migration.

**Invalid viewOnly Property:**

```text
WARN,TEST-429,"Association between 3nXgwpVsistGcVY42Q and TEST-429(10418) does not contain valid 'viewOnly', cannot migrate. Skipping."
```

This indicates the association had invalid or missing viewOnly permission settings.

**Successful Migration Summary:**

```text
INFO,null,"Found 21320 associations, will batch insert"
INFO,null,"Association migration completed successfully."
```

These entries show the total number of associations processed and confirm successful completion.

### Handling failed migrations

When the log shows failed migrations, contact our support team.