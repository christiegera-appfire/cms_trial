# Set up a connection to Salesforce (Jira Cloud)

A connection links a Jira instance to a Salesforce org, allowing the two systems to exchange data. Once set up, work items and records can be associated and kept in sync across both platforms without manual copying.

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can set up the integration

- [Installed the Connector in Jira](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/).

## Follow the steps to set up integration in Jira

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   Image — asset pipeline pending  
   Appsettings.png
3. Under *Connector for Salesforce*, click **Connections**.
4. At the **Salesforce Connections** screen, click **+Add Connection**.   
   If this is your first connection, the *Connect with Salesforce* panel appears, providing a brief explanation of the step and a link to more information. You can also click **+Add connection** here to open the *Authorize Connection* dialog.

   ![connector-add-connection.png](/cms_trial/assets/aa16dbf1-2b83-4d56-bad3-465caeab6f48.png)

   The *Authorize Connection* dialog appears.

   ![connector-auth-connection.png](/cms_trial/assets/daeac981-4296-4c89-bef4-607edb268a61.png)
5. Enter a **Connection Name**, and select **Production** or **Sandbox** as the Salesforce instance environment type**.** Click **Authorize**.

   If you're not logged into Salesforce, the browser loads a new Salesforce login page and prompts you to enter your Salesforce credentials.
6. When the authorization is successful, you can import the compact layout fields from Salesforce. This quickly pre-populates the objects and fields available through the connection.  
   This step is optional; you can always [configure](/cms_trial/space/CSFJIRA/1873347420/Configure+Salesforce+objects+and+fields+in+connection+search+results/) it later.
7. Click **Import** to proceed.

   ![Import Contact layouts window](/cms_trial/assets/a6e443cd-7ced-4c1b-a359-135d607e9778.png)
8. When the authorization is successful, the *Status* changes to authorized.

![contentId-1873379599](/cms_trial/assets/a9f2f94d-0ce3-4af1-9428-d367ddfa3450.png)

## Next steps

To complete your integration, follow the steps:

- [Bind a Jira Project space a Salesforce Connection](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/) (Jira Cloud)
- [Configure connection search results](/cms_trial/space/CSFJIRA/1873347420/Configure+Salesforce+objects+and+fields+in+connection+search+results/)