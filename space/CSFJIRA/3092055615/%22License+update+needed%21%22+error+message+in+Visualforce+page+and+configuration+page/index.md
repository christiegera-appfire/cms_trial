# "License update needed!" error message in Visualforce page and configuration page

## Summary

When accessing the JIRA Cloud for Salesforce configuration page or a Visualforce page in Salesforce, an error message appears saying "License update needed!"

![image-20250603-121406.png](/cms_trial/assets/13bdc676-8f69-4f80-8f94-7869304a5ce2.png)

## Environment

- JIRA Cloud
- Any version of Salesforce & JIRA Cloud Connector

## Cause

A new license or renewed license has been applied to the Salesforce & JIRA Cloud connector in JIRA, and the cache is not refreshing from the database.

## Workaround

Since the cache has not refreshed, you have to manually do so by disabling and re-enabling the Salesforce & JIRA Cloud Connectorwith the following steps:

1. Click the Settings (▢) icon **> Apps > Manage apps.**
2. Look for **Connector for Salesforce & Jira**.
3. Expand the section and click **Unsubscribe** and **Uninstall.**  
   Your data and license are safe but need to be revoked.

   ![Unsubscribe.png](/cms_trial/assets/75364844-0303-4d21-a5dc-2e81acaf17b9.png)
4. Install the app again.

## Resolution

Not applicable.