# Set up a connection to Salesforce (Jira Cloud)

A connection links a Jira instance to a Salesforce org, allowing the two systems to exchange data. Once set up, work items and records can be associated and kept in sync across both platforms without manual copying.

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can set up the integration.
- [Installed the Connector in Jira Cloud](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/).

## Create a new connection

Establish the initial authorization between Jira and Salesforce.

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce and Jira,* click **Menu** (▢) > **App settings**.

   ![Appsettings.png](/cms_trial/assets/e8968385-0970-4ffa-9544-95be1ca105c8.png)
3. Under *Connector for Salesforce and Jira*, click **Connections**.
4. Click **+Connection**.

   ![image-20260915-082549.png](/cms_trial/assets/023e9cd0-3568-4865-8c91-4ae70cea2582.png)
5. Enter a **Connection name** (for example, *My connection*).

   ![Connection name ](/cms_trial/assets/3698e10b-5f65-4413-8c44-97d8f74fe97f.png)
6. Select your *Salesforce environment* by choosing either **Production** or **Sandbox** as the Salesforce instance environment type.
7. Click **Authorize and continue** to authenticate with Salesforce.

   ![Authorize and continue](/cms_trial/assets/bd05d1f1-dd1d-43a4-90f4-518fbbc300c1.png)

   If you're not logged into Salesforce, the browser loads a new Salesforce login page and prompts you to enter your Salesforce credentials.  
   When the authorization is successful, the *Status* changes to authorized.

Make sure your Salesforce account has object and layout permissions. For details, see [How to set object permissions in profiles for a Salesforce user?](https://appfire.atlassian.net/wiki/x/wAVLu) If authorization fails, you can click **Retry authorization**.

## Import Salesforce object types and fields

Once authorization is complete, the *Importing* step opens. Here, you can import the compact layout fields from Salesforce. Decide on Salesforce object types you want to have available in Jira. Based on these settings, you can later associate and synchronize data. This quickly pre-populates the objects and fields available through the connection.

1. Select the checkboxes for the Salesforce object types you want to import (for example, Case, Account, and Opportunity).

   ![object types you want to import](/cms_trial/assets/7c6173e2-a071-4fa9-9414-4064398639c1.png)
2. Click **Save and continue** to finalize the setup.  
   Your new connection now appears in your *Connections* list with the authorized status.

   ![Connections list ](/cms_trial/assets/e41ce26e-4863-4a5e-99ca-981ac2dfa33c.png)

Later, you can always add more Salesforce objects and configure details for your connection (notifications, attachments, comments, query, presets, rich text). For details, see [Configure connection settings](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/).

1. Follow the next steps to set up bidirectional sync in Salesforce and bindings to complete your configuration.

## Next steps

- (Optional) Configure the connection's object access, sync rules, notifications, and defaults for how Jira work items and Salesforce records link and update [Configure connection settings](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/).
- To enable bi-directional data sync and viewing Jira data in Salesforce, you need to [set up your integration in Salesforce](/cms_trial/space/CSFJIRA/1873772649/Set+up+your+integration+in+Salesforce/).
- Before you can associate Jira work items with Salesforce records and synchronize them, bind a Jira space to a connection [Bind a Jira Project space a Salesforce Connection](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/).