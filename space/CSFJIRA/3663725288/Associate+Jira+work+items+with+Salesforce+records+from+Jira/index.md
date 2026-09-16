# Associate Jira work items with Salesforce records from Jira

Associating a Jira work item with a Salesforce record creates a link and lets you configure its sync behavior.

When Salesforce agents receive a Case caused by a known bug, they can associate the Case with an existing Jira bug. This way, both the team working in Jira and the team working in Salesforce can see all related Cases and Jira work items and push or pull data between the systems.

## Before you start

Make sure you have:

- Completed a [project binding](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/) as well as [entity and field mappings](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/) in Jira.
- [Configured a Salesforce record page to view Jira details directly in Salesforce](/cms_trial/space/CSFJIRA/3608707174/Configure+Salesforce+record+page+to+view+Jira+details+directly+in+Salesforce/).

## Associate a Salesforce record with a Jira work item

1. Search work items by *Summary* keywords or the work item key.  
    Results are limited to work items in the bound space with no associations. If multiple items match, the most recently updated ones appear first.

   ![image-20260907-080847.png](/cms_trial/assets/61a09be4-6ff4-4aa5-a737-0f65d08205f0.png)
2. Click **Associate** next to the selected work item.  
   The *Associate work item to Salesforce record* window opens.
3. Click **Associate** to associate the work item withan existing Salesforce record.  
   You can also click **Create Salesforce record** to create a new record.

   ![image-20260907-081039.png](/cms_trial/assets/6bb180c5-a3ca-45cd-aecc-1417f396381e.png)

   The *Associate Salesforce record* window opens.

   ![Associate Salesforce record](/cms_trial/assets/fd1fde33-23e2-4942-b287-c1e42a5fe42a.png)
4. From the **Object type** dropdown, select the Salesforce Object type. For example, a Case.  
   The available Salesforce Object types depend on how the [mapping configuration is set up](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/).
5. In the **Salesforce record** field, start typing the name of the Salesforce record you want to associate the Jira work item with.

   ![Salesforce record dropdown](/cms_trial/assets/148da8fc-c53a-46fe-9bf0-a925bc06179f.png)
6. Configure your association with the following options:

   - **View only** - Manual and automatic synchronization are disabled.
   - **Automatic push** - Changes to this work item are pushed automatically to the associated Salesforce record.
   - **Automatic pull** - Changes to the associated Salesforce record are pulled automatically to this work item.
7. From the **After associating** dropdown, select what happens after the Salesforce record is associated:

   - **Do nothing**
   - **Push to Salesforce**
   - **Pull from Salesforce**
   - **Push to Salesforce then Pull from Salesforce**
   - **Pull from Salesforce then Push to Salesforce**
8. Click **Associate**.
9. The associated Salesforce record appears next to the Jira work item.  
   The *Subject*, *Description,* and *Priority* fields are already synchronized, displaying the same information in Jira and in Salesforce.
10. You can click the Salesforce link to open the associated Salesforce record.

    ![image-20260907-083424.png](/cms_trial/assets/28f426f1-7f1e-47dc-b658-69bdb28fdb0f.png)

    The Salesforce case record is updated, and you can see Jira work item details displayed under the **Jira Issues** component.

    ![image-20260907-084846.png](/cms_trial/assets/166d6efa-7849-4742-bb4f-052e6a651241.png)

## Next

You can also:

- [Associate a Jira work item from Salesforce with Jira Issues (NextGen)](/cms_trial/space/CSFJIRA/3092284698/Associate+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/)
- [Create a Jira work item from Salesforce with Jira Issues (NextGen)](/cms_trial/space/CSFJIRA/3092088339/Create+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/)
- [Create a Salesforce record from Jira](/cms_trial/space/CSFJIRA/3092284964/Associate+a+Salesforce+record+from+Jira/)