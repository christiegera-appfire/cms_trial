# Post migration

The **Post Migration** page is only visible on instances where JMCF has been migrated from **Jira Data Center** to **Jira Cloud**.

The **Post Migration** page provides a way for you to view and address any issues that were encountered during the migration of JMCF custom fields from **Jira Data Center** to **Jira Cloud** using the Jira Cloud Migration Assistant (JCMA). These errors and warnings must be addressed in order for your custom fields to function properly.

The Post Migration displays a tile for each migration with a status indicator for that migration as it relates to the JMCF custom fields you included in the migration. Click the arrow to the right to expand the tile and view the status of each custom field that was migrated.

## Addressing errors and warnings

To manually address each error:

1. Click the **Fix now** button next to the error.
2. For individual custom fields, the **My custom fields** window will open with the specific custom field at the top of the list. You can update the custom field from here.
3. Save the updated custom field, and it will be marked as resolved in the Post migrations page automatically.

Repeat these steps for all custom fields that encountered warnings or errors.

**Note**: Resolving all errors and/or warnings should result in your custom fields calculating/recalculating correctly. However, as migration of JMCF is still considered a Beta process, it is **highly recommended** that you verify your screen configurations before migrating your Production instance!

For custom fields that are included in multiple contexts in your Data Center instance, you will need to manually reconfigure any contexts beyond the first!

You are viewing the documentation for **Jira Cloud**.