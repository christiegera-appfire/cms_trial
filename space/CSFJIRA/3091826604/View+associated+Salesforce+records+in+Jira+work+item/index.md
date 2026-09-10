# View associated Salesforce records in Jira work item

You can view associated Salesforce object records within a Jira work item.

## Before you start

- You must be a Jira user with the [Edit Issue](https://confluence.atlassian.com/jiracorecloud/permissions-overview-765593621.html) permission.
- You need to have made some [associations](/cms_trial/space/CSFJIRA/3092284964/Associate+a+Salesforce+record+from+Jira/) already.

## Guide

1. In a Jira work item, look under the *Connector for Salesforce* section on the right side of the screen.  
   The list of associated object types and records appears there.

   ![Jira work item showing the Connector for Salesforce section with associated Case and Opportunity records and Create Salesforce Object and Associate buttons.](/cms_trial/assets/e5cc82ec-ba21-40ea-b9a7-bbf3c9863739.png)
2. To see more details, go to the *Activity section* and select the *Salesforce records* tab.

   ![Activity section in a Jira work item with the Salesforce records tab selected.](/cms_trial/assets/7dd1799c-1b70-4545-94a2-1e8de413c2fc.png)
3. Select a **Salesforce object** type to display its records.  
   The most recently associated records appear at the top.

   ![Salesforce records tab displaying Case records in a table with Subject, Priority, Status, and Case Number columns.](/cms_trial/assets/eb1e0943-e71e-4dd8-858f-ce0c4643c9c7.png)
4. Select the **Columns** with mapped fields you want to view.

![Columns dropdown menu showing selectable mapped fields including Subject, Priority, Status, and Case Number.](/cms_trial/assets/4ecab326-fa6a-4fd1-bb89-1d73b3f6bbe0.png)

If some fields don’t appear, contact your admin. Only admins can configure the connection and add missing fields for Salesforce object types. For instructions, see [Configure field displays and access the Details screen](/cms_trial/space/CSFJIRA/1873511110/Configure+field+displays+and+access+the+Details+screen/).

1. Click a record link to open the associated records directly in Salesforce.

To run an association report, see [Run an association report](/cms_trial/space/CSFJIRA/3091596677/Run+an+association+report/) instructions.