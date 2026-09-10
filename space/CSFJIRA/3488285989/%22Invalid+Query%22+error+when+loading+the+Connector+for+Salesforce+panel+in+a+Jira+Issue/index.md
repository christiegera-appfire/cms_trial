# "Invalid Query" error when loading the Connector for Salesforce panel in a Jira Issue

## Summary

Users may encounter an **"Invalid Query"** error when loading the **Connector for Salesforce** panel in a Jira issue. This occurs when the Connector queries a Salesforce field that is no longer available or accessible, such as a deleted, renamed, or feature-dependent field.

If you encounter this error **while configuring a connection**, refer to <https://support.appfire.com/space/CSFJIRA/3156836381/An+%22Invalid+Query!%22+Error+pops+up+when+configuring+connection+in+Jira> instead.

## Environment

- Product: Connector for Salesforce & Jira
- Hosting: Cloud
- Related vendor(s): Salesforce, Jira

## Problem

- An "**Invalid Query**" error message pops up when accessing a Jira Issue.
- The **Connector for Salesforce** panel is infinitely loading.
- The browser network tab shows a `400 Bad Request` for the `associatedObjects` API endpoint.

![image-20260728-000034.png](/cms_trial/assets/5cb02cdb-71bd-46bb-a03e-b664781c4772.png)

## Cause

The connection configuration includes a field in its "Fields" list that is either:

1. **Deleted/Renamed:** The field was removed/renamed from the Salesforce object but remains in the Connector's configuration.
2. **Feature Disabled:** This can also occur when the queried field belongs to a Salesforce feature that has been disabled for the object. For example, the `LastActivityDate` field requires **Allow Activities** to be enabled.

## Solution

To resolve this, you must remove the problematic field from the Connection configuration:

1. Navigate to **Apps** > **Connector for Salesforce** > **Connections**.
2. Locate the affected connection and click **Configure**.
3. Find the Salesforce Object causing the error (e.g., "Sales Request" or `Research_Assessment__c`).
4. Click on the **Fields** button for that object.
5. Review the field list and identify any invalid fields (shown in red), or fields that no longer exist in Salesforce.

   ![image-20260728-001200.png](/cms_trial/assets/8f0a405b-e406-44ec-ad81-cdbb9da71744.png)
6. **Remove** the problematic field(s) from the selection.
7. Click **Apply Changes** at the bottom of the configuration page to save.

### Validation steps

- Refresh the Jira issue page and expand the “Connector for Salesforce” panel.

## Before contacting Support

If the issue persists after following the steps above, collect the following information before contacting Support:

- **Connection Export:** Go to the Connection configuration and provide the JSON export of the settings.
- **Salesforce Object Details:** A screenshot of the Object Manager details for the affected Salesforce object.

## Related articles

- <https://support.appfire.com/space/CSFJIRA/3156836381/An+%22Invalid+Query!%22+Error+pops+up+when+configuring+connection+in+Jira>
- <https://support.appfire.com/space/CSFJIRA/1873347420/Configure+Salesforce+objects+and+fields+in+connection+search+results>