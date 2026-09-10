# Determine the Salesforce integration user

## Purpose

In some scenarios, you may need to find out which user is being used for Salesforce integration to check whether they have the right permissions. This FAQ helps you find the user on the Salesforce side, whether for general checking or troubleshooting purposes.

## Answer

The integration user can be determined via the Salesforce Setup page. The steps are:

1. In the connected Salesforce instance, click the **Cog Icon** on the top right and click **Setup***.*
2. Continue to **Apps > Connected Apps > Connected Apps OAuth** **Usage**.  
   ℹ️ Alternatively, you can search for **Connected Apps OAuthUsage**in the search bar.
3. On the page, look for **Salesforce & JIRA Cloud Connector** (or **Salesforce & JIRA Server Connector**depending on the case).

   ![image-20250807-075602.png](/cms_trial/assets/491186e9-e4b3-4a0d-b995-a9fcf020d2a9.png)
4. In the **User Count**column, click the number.
5. Find the user used for the integration by referring to the **Initial Connection**or**Last Used** column. In the example below, the first user is the one being used for integration, based on the most recent **Last Used** and **Initial Connection** dates.

   ![the user used for the integration](/cms_trial/assets/020edf4e-13a8-4134-9fc8-74ad6d0cbd92.png)