# I get an "Waiting for Jira data" message when there is a Salesforce field that has been modified or removed

## Summary

A "Waiting for Jira data" message keeps appearing when accessing a Jira work item or trying to pull data from Salesforce.

Sometimes, even the Salesforce panel in the Jira work item would not load.

![image-20250603-122418.png](/cms_trial/assets/4d6f81e3-50d1-4d46-8e72-0c94989a7583.png)![waiting for jira.png](/cms_trial/assets/eaca7f32-0d34-4be4-a48e-33b8574e95e7.png)

​

## Environment

- Jira DC
- Jira Cloud

## Diagnostics steps

1. In Jira, under **Connector for Salesforce** app click **Connections**.
2. Click **Configure** next to your connection.
3. Click **Fields** for the object you are working with.

   ![image-20250604-065224.png](/cms_trial/assets/28088040-73ec-420b-a2d9-5253927863f4.png)
4. Check if one or more fields are highlighted in red.

   ![image-20250604-071203.png](/cms_trial/assets/103dec3f-6e04-4cec-9644-2392beb6b7a3.png)
5. Alternatively, click **Bindings**> **Mapping** for a selected project.
6. Click **Mappings** for selected entities to check if one or more fields are highlighted in red.

   ![field missing.png](/cms_trial/assets/cbebe346-97f7-449c-ad0a-1697a9cf379a.png)

## Cause

Some Salesforce fields might have been modified or removed.

## Workaround

Not applicable.

## Resolution

You need to remove the fields and mappings with the highlighted fields that are no longer available in Salesforce.