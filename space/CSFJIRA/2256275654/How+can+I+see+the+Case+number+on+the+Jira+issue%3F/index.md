# How can I see the Case number on the Jira issue?

## Summary

Sometimes, after configuring the Connector and an association has been made between a Jira issue and a Salesforce Case, we do not see the Case number on the Salesforce section of a Jira issue:

![contentId-2256275654](/cms_trial/assets/47ba2637-59e2-465a-a083-38ecce75688d.png?version=1&modificationDate=1678856773656&cacheVersion=1&api=v2)

In the above screenshot, we can see the **subject** of the Case being displayed. However, we need the case number to be displayed instead.

## Environment

- Any Jira version
- The Connector for Salesforce & Jira DC and Cloud

## Diagnostics Steps

Not applicable.

## Cause

The Salesforce field to be displayed on the Jira issue is directly related to Connection configuration where we select available fields for a particular Salesforce object:

![contentId-2256275654](/cms_trial/assets/2d01c4b1-df5f-45b4-a228-b42fb28ffdb6.png?version=1&modificationDate=1678856773858&cacheVersion=1&api=v2)

Related documentation: [Configuring Field Displays and accessing the Details Display screen](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754317/Configuring+Field+Displays+and+accessing+the+Details+Display+screen)

## Workaround

Not applicable.

## Resolution

1. Go to **Salesforce section** in Jira > **Connections** > click **Configure** on the chosen Connection.
2. Click **Fields** next to Case.

   ![contentId-2256275654](/cms_trial/assets/8b828a15-9b07-4c5c-a0d6-f6c50be3a040.png?version=1&modificationDate=1678856774052&cacheVersion=1&api=v2)
3. Move the **Case Number** field to the top to make it the primary field:

   ![contentId-2256275654](/cms_trial/assets/49b19c76-732c-4ed8-98aa-0381ce0dfc5b.png?version=1&modificationDate=1678856773926&cacheVersion=1&api=v2)
4. Click **Next** and then **Apply changes**.
5. Now that the **Case Number** field has been chosen as the primary field, we will see it in the Jira issue as expected:

   ![contentId-2256275654](/cms_trial/assets/f3058ccc-1d9a-412b-91f5-f5b39b36bfe1.png?version=1&modificationDate=1678856773987&cacheVersion=1&api=v2)