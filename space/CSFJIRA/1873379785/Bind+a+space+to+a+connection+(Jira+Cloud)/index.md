# Bind a space to a connection (Jira Cloud)

This guide helps you bind a Jira Project to a Salesforce Connection.

You need to bind a Jira Space (previously called Project) to a connection before you can associate Jira work items with Salesforce records and synchronize the two.

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can set up the integration

- [Set up a connection to Salesforce (Jira Cloud)](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/).

<https://app.arcade.software/share/qaRJf295bpGPQQcldnBB>

## Follow the steps to set up integration in Jira

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![Appsettings.png](/cms_trial/assets/5474807c-0d67-4b4e-a987-95ccb2addab4.png)
3. Under *Connector for Salesforce*, select **Bindings**.
4. On the **Bindings** screen, click **+Add Binding** in the top right corner.   
   If this is your first connection, the *Bind your Jira project with Salesforce* panel appears, providing a brief explanation of the step and a link to more information. You can also click **+Add binding** here to open the *New Binding* dialog.

   ![connector-new-binding.png](/cms_trial/assets/c0958aa7-c36d-441d-b5ec-39ea274a2603.png)

   The*New Binding* dialog appears.

   ![contentId-1873379785](/cms_trial/assets/12587fce-0dc9-42a2-93fc-17aecd945dfe.png)
5. For **Project**, select a Jira Space you want to bind and the **Connection** you want to bind it to.
6. Click **Add**.  
   Connector begins automatically importing compact layouts. When finished, you are directed to the *Mapping Configuration* page to check your **Mapping** settings. For more information, see [Configuring Entity Mappings and Field Mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

   ![Bindings list](/cms_trial/assets/6f60a623-48d2-4cee-b32a-84c043b85289.png)

## Next steps

To complete your integration, you need to set up the integration in Salesforce and configure your settings. Follow the steps:

- [Set up your integration in Salesforce](/cms_trial/space/CSFJIRA/1873772649/Set+up+your+integration+in+Salesforce/)
- [Configure connection settings](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/)
- [Associate a Salesforce object record from Jira](/cms_trial/space/CSFJIRA/3092284964/Associate+a+Salesforce+record+from+Jira/)
- [Configure entity mappings and field mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/)