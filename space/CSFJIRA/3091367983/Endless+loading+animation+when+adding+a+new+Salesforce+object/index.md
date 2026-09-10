# Endless loading animation when adding a new Salesforce object

## Summary

The load animation spins endlessly when adding the Salesforce objects and fails to complete the action.

![add salesforce error.png](/cms_trial/assets/53c8e002-24ea-4d2d-a162-be866814be5a.png)

## Environment

- Jira Data Center
- Jira Cloud

## Diagnostics Steps

1. In Jira, go to **Apps** > **Salesforce** > **Connections** > **Configure** > **Add Salesforce Object.**
2. Select a Salesforce Object to add.
3. Enable **Import Layout** option and click **Next**.
4. The load animation goes on endlessly without completing the action.

## Cause

Due to multiple Record Types configured in the Salesforce object, when the import layout option is enabled, the connector does not have the capability to select the correct Record Type of the object that has the layout that needs to be imported.

This results in the connector getting stuck in an endless loading cycle.

## Workaround

- N/A

## Resolution

1. Disable the **Import layout** option when adding Salesforce objects to your Jira connection.
2. Click **Next** to manually add the fields to the compact layout.

For more information regarding the compact layout, check "Step 9" of this [documentation](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754669).