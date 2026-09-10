# Associate a Jira work item from Salesforce with Jira Issues (NextGen)

Associate a Salesforce record (for example, an Account, a Case, or a Contact) with a Jira work item, from within Salesforce.

By doing so, you can link a Jira work item with the current record, and configure its sync behavior.[unmapped inline: placeholder]

For example, when Salesforce agents receive a Case caused by a known bug, they can associate the Case with an existing Jira work item containing the bug report. This way, both the team working in Jira and the team working in Salesforce can see all related Cases and Jira issues, and push or pull data between the systems.

## Before you start

- Your administrator has completed a [project binding](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/) as well as [entity and field mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/) in Jira.
- Your administrator has [configured the Visualforce pages](/cms_trial/space/CSFJIRA/1873511459/Use+Jira+Issues+(NextGen)+with+Visualforce/) required for objects.

## Associate a Salesforce record with a Jira work item

1. In a Salesforce record, click **Associate/Create**.

   ![contentId-3092284698](/cms_trial/assets/b1fd170e-e429-47f2-8409-aa4084119d3d.png)

   The **Associate/Create Jira Issue** window appears.
2. To associate a Jira issue, search for your Jira issue by entering the **Issue Key** or **Issue Summary** in the search box.
3. If there are multiple matches, the most recently created issues appear first.  
   Only issues belonging to Projects bound to the authorized Connection are searchable.

   ![Associate or Create Jira Issue .png](/cms_trial/assets/c569110b-2304-48f0-b467-388ca25330a9.png)
4. After selecting a Jira issue from the search results, the **Associate Jira Issue**pop-up window will appear.

   ![contentId-3092284698](/cms_trial/assets/10fc17b5-8066-4b60-b4c5-c1a5c948fc64.png)
5. To associate multiple Jira issues,repeat *step 2*and select more Jira issues to associate.
6. You can choose to toggle the following options:

Some combinations are not possible and cannot be selected. Click **Synch Info** for a more detailed explanation of the sync configuration actions.

![image-20250414-113912.png](/cms_trial/assets/05e87f8d-52c0-483a-b69b-71db2469701d.png)

**View Only** - Manual and automatic synchronization will be disabled.  
**Auto Pull** - Changes to the associated Jira issue will be pulled automatically to this record.  
**Auto Push** - Changes to this record will be pushed automatically to associated Jira issues given respective triggers are installed.

1. You can also choose what to do after the Jira issue is associated by choosing from the following options:

![csfjira-after-associating.png](/cms_trial/assets/7b61cedf-a9de-48c0-b479-340efc508290.png)

• Do nothing  
• Pull from Jira  
• Push to Jira  
• Push to Jira then Pull from Jira  
• Pull from Jira then Push to Jira

1. When you are satisfied with your configuration, click **Associate**.
2. Upon successful association, the **Issue associated successfully** message is shown.  
   **Tiles view:**

   ![csfjira-tiles-view.png](/cms_trial/assets/428003b0-b2ca-4f2d-8f3c-39c11fd4c91b.png)

   **Table view:**

   ![csfjira-table-view.png](/cms_trial/assets/bf7baf50-b62b-4dc8-bdbd-6783390a061e.png)

- Each Jira issue can be associated with a maximum of 1000 Salesforce records.
- You can display up to 50 Jira associations using the Salesforce NextGen Lighting Component.

## Related information

- [Configure an association](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/)
- [Create a Jira Issue from Salesforce with Jira Issues (NextGen)](/cms_trial/space/CSFJIRA/3092088339/Create+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/)