# How to change the Salesforce integration user

## Purpose

When an administrator installs Space to migrate individual pages and authorizes a Connection, the administrator will automatically be the integration user for the Connector since a Connection is authorized using the Jira administrator's Salesforce credentials.

If the user ceases to be the Jira administrator, you might want to change the integration user for the Connector.

## Answer

Revoke the Connection from within both Salesforce and Jira to force creation of a new token.

1. Log out of Salesforce first (⚠️ Important).
2. In your Jira instance, navigate to **Jira Apps** > **Connector for Salesforce** > **Connections**
3. Click **Revoke Access** to revoke the connection.
4. While on the same page, click **Authorize**.

## Authorize the connection

1. [Authorize the connection](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=csfjira&title=Set%20up%20a%20connection%20to%20Salesforce%20%28Jira%20DC%29&linkCreation=true&fromPageId=2256308548) - More secure and follows current best practices  
   In case you need to set it up again, go to the detailed [instructions](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=csfjira&title=Set%20up%20a%20connection%20to%20Salesforce%20%28Jira%20DC%29&linkCreation=true&fromPageId=2256308548).
2. Select the environment type of your Salesforce instance: **Production** or **Sandbox.**
3. Click **Authorize**.
4. After successfully logging into Salesforce, return to your Jira instance (do not close the Salesforce window yet).   
   Click **Menu** (

   [Unmapped macro: inline-media-image — no content to fall back on]

   )> **API Access token** > **Copy**.
5. Return to the Salesforce window. Click **Setup** > **Installed packages** > **Configure** the Jira for Salesforcepackage.
6. Click **Revoke Access.**
7. Paste the API Access token you copied into the **Access token** field and click **Save**.