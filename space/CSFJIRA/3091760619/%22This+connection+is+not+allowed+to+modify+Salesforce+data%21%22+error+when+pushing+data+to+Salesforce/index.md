# "This connection is not allowed to modify Salesforce data!" error when pushing data to Salesforce

## Summary

In Jira issue view, when clicking **Push**, an error message "This connection is not allowed to modify Salesforce data!" appears on the screen.

![08a13d66-1022-46de-a8c6-68d7f1582122.png](/cms_trial/assets/780703d9-e5f0-4230-8b5c-a6e4b945cffa.png)

## Environment

- JIRA Cloud
- JIRA Server
- JIRA Data Center

## Diagnostics Steps

Not applicable.

## Cause

The **Allow Modification** connection is configured as read-only, restricting the user from performing a manual push to Salesforce.

## Workaround

Not applicable.

## Resolution

1. Go to **Apps** > **Salesforce**> **Connections**.
2. Click **Configure** on the existing connection.
3. Scroll to the "Connection Settings" section.
4. Enable the **Allow Modification** toggle.

   ![contentId-3091760619](/cms_trial/assets/42c25ef1-51d9-4af7-ab22-382a90208577.png)

   ​​