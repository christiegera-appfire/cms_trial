# Will the Connector be impacted after changing Jira Instance URL?

## Purpose

Atlassian has recently released the Cloud Site Rename feature which allows changing the Jira instance URL.

More details are available in the following [documentation](https://support.atlassian.com/organization-administration/docs/update-a-product-url/), and Atlassian recommends [checking the apps from the top vendors in the Atlassian Marketplace](https://jira.atlassian.com/browse/CLOUD-10809) to find out if they're compatible with instance URL changes and if so, how that may affect your installed app.

## Answer

Per [this list](https://jira.atlassian.com/browse/CLOUD-10809), Connector for Salesforce & Jira is compatible with the Cloud Site Rename feature. Furthermore, as per our tests, changing the Jira instance URL does not have any impact on the connector, however, you will need to reauthorize the connection to ensure the connection between Jira and Salesforce continues to work.

Here's how to reauthorize the connection:

1. Log into your Jira.
2. In Jira > **Salesforce** > **Connections** > locate your connection > click **Revoke Access** then click **Revoke** to confirm.

   ![contentId-3091597377](/cms_trial/assets/ccdf45dd-ee23-4c29-81b7-cad29c06dbb5.png)
3. Click **Authorize**.

   ![Authorize.png](/cms_trial/assets/c0971e61-bd0e-4662-9d8d-c93d8a86abcf.png)
4. Select the environment type of your Salesforce instance, either **Production** or **Sandbox**.  
   Then click **Authorize** to authorize the connection.

   ![Authorize connection.png](/cms_trial/assets/a8379588-e4f8-4a5c-922c-3c2fb0e6f727.png)

   If you're not logged into Salesforce, the browser will load a new page and prompt you to enter your Salesforce credentials.
5. If the authorization was successful, the **Status** will change to **Authorized**.

   ![authorized.png](/cms_trial/assets/b012d1dc-db0f-40c1-a8ea-79735d0505a0.png)
6. After the connection is successfully authorized in Jira, [follow the steps in this page](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754678/Setting+up+a+connection+to+Jira) to update the API Access Token in Salesforce.