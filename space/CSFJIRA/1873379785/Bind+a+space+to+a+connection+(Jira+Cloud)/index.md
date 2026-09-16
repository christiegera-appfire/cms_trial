# Bind a space to a connection (Jira Cloud)

Bindings connect specific Jira spaces to your Salesforce connection independently. You can create a separate binding for every space in your instance. Each space binding defines its own mapping between Jira work item types and Salesforce object types so different teams or projects can sync exactly the work items they need without affecting other spaces. You need to bind a Jira space to a connection before you can associate Jira work items with Salesforce records and synchronize the two.

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can set up the integration.
- [Connect with Salesforce](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/)

## Follow the steps

1. Under *Connector for Salesforce and Jira*, click the **Bindings** tab on the left menu.

   ![image-20260904-125304.png](/cms_trial/assets/8995ede0-f562-473d-89c3-57d6110d2084.png)
2. Click **+ Binding**.
3. From the dropdown, select a **Jira space** you want to bind.

   ![Binding step](/cms_trial/assets/b59bd6b3-d707-4162-a796-d87ac89e0528.png)

   If you already have space bindings, those spaces are not listed in the dropdown. You can select only spaces with no bindings.
4. Select the **Connection** you want to bind it to.  
   You can select only authorized connections.
5. Click **Next**.  
   You’ve saved your binding configuration. To complete the setup, you need to map entities.

## Next steps

- [Configure entity and field mappings](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/)