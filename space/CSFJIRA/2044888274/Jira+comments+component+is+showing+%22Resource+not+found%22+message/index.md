# Jira comments component is showing "Resource not found" message

## Issue

When accessing a Salesforce Record, the Jira Comment component shows a “Resource not found” error message, and no comments are loaded.

![contentId-2044888274](/cms_trial/assets/c1775fbf-32d3-4196-acde-7df404448d20.png)

Additionally, the following issues might occur:

- The same “Resource not found” error message displays when the record is loaded.

  ![contentId-2044888274](/cms_trial/assets/e9b8f709-559c-46fa-96a5-90147fafea8f.png)
- The existing Jira ticket associations are missing from the Jira Issues component.

## Solution

The issue occurs because the integration hasn’t been updated to the new RPC URL following the infrastructure transition. To resolve it, follow the steps:

1. In Salesforce *Setup*, navigate to **Apps > Packaging > Installed Packages**.
2. Click **Configure** for **Jira Cloud for Salesforce** packageto check if a message prompts you to update the URL.

   ![contentId-2044888274](/cms_trial/assets/ee5cc50c-fb78-432e-8856-b8e82873eaae.png)
3. List the new URL as instructed in the article [Transitioning of Connector for Salesforce & Jira to Appfire infrastructure](/cms_trial/space/CSFJIRA/2258305251/Transitioning+of+Connector+for+Salesforce+%26+Jira+to+Appfire+infrastructure/), and update the URL.
4. Re-authorize the integration:

   1. Revoke the connection from both Jira and Salesforce
   2. Authorize the connections. Follow the [How to change the Salesforce integration user](/cms_trial/space/CSFJIRA/2256308548/How+to+change+the+Salesforce+integration+user/) steps.

Revoking the existing connection would not remove any existing data **as long the existing connection is not deleted.**

When re-authorizing, ensure that you have direct access to the Salesforce Integration User. The **Log in as user** option can’t be used for authorization.