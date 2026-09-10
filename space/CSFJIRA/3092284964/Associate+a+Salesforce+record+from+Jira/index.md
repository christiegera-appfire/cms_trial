# Associate a Salesforce record from Jira

You can associate a Jira work item with a Salesforce record and then push data from Jira to Salesforce or pull data from Salesforce to Jira.

## Before you start

To associate push or pull data:

- You must be a Jira user with the [Edit work item](https://confluence.atlassian.com/jiracorecloud/permissions-overview-765593621.html) permission.
- Your administrator must have created the [binding for the Jira space to a Salesforce connection](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/).

## Guide

1. In a Jira work item, look under *Connector for Salesforce* section on the right side of the screen.
2. Click **Associate**.

   ![contentId-3092284964](/cms_trial/assets/248b303d-7fc3-4db8-92a3-9d3ec4112463.png)

The **Associate Salesforce record** window opens.

![Associate Salesforce record](/cms_trial/assets/47d15761-c0ac-4804-b30c-389adc56891f.png)

1. From the **Object type** dropdown, select the Salesforce Object type.  
   The available Salesforce Object types depend on how the [mapping configuration is set up](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).
2. In the **Salesforce record** field, start typing the name of the Salesforce record you want to associate the Jira work item with.

   ![Salesforce record dropdown](/cms_trial/assets/88b5cd72-976d-4928-8414-83dde5da1449.png)
3. Configure your association with the following options:

   - **View only** - Manual and automatic synchronization are disabled.
   - **Automatic push** - Changes to this work item are pushed automatically to the associated Salesforce record.
   - **Automatic pull** - Changes to the associated Salesforce record are pulled automatically to this work item.
4. From the **After associating** dropdown, select what happens after the Salesforce record is associated:

   - Do nothing
   - Push to Salesforce
   - Pull from Salesforce
   - Push to Salesforce then Pull from Salesforce
   - Pull from Salesforce then Push to Salesforce
5. Click **Associate**.
6. The associated Salesforce record appears in the list in the *Connector for Salesforce* section:

   ![associated Salesforce record](/cms_trial/assets/d8f3b782-682c-44db-9d24-50f59a5cf343.png)

## View Salesforce record options

Click a listed Salesforce record to view the following options:

![Salesforce record options](/cms_trial/assets/0a085bee-70e5-4a3b-ab3e-ec3c814e4b1c.png)

- **Details** - Opens a window showing details of the Salesforce record.
- **Configure** - Opens configuration options for this association. See [Configuring an association](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/) for more information.
- **Push** - Synchronizes data from Jira to Salesforce.
- **Pull** - Synchronizes data from Salesforce to Jira.
- **Unlink** - Removes the association between this Jira work item and the Salesforce record.

Each Jira work item can be associated with a maximum of 1,000 Salesforce records.

## Next steps

You may want to:

- [Install the Salesforce Package for Salesforce & Jira Cloud Connector](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/)
- [View associated Salesforce records in Jira work item](/cms_trial/space/CSFJIRA/3091826604/View+associated+Salesforce+records+in+Jira+work+item/)

## Related information

- [Configuring an association](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/)
- [Working with attachments](/cms_trial/space/CSFJIRA/1754432218/Work+with+attachments/)