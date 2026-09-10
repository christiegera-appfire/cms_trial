# Link to other Jira work items from Salesforce when creating a new Jira issue (NextGen)

This page explains how to link to a Jira issue when creating a new Jira work item from a Salesforce record.

By linking a Jira work item in Salesforce, you can communicate the linking information from the Salesforce record to a Jira issue, keeping the Jira team within the loop.

## Before you start

- Your administrator has completed a [project binding](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/) as well as [entity and field mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/) in Jira.
- Your administrator has configured [the Visualforce pages](/cms_trial/space/CSFJIRA/1873511459/Use+Jira+Issues+(NextGen)+with+Visualforce/) required for the Object.

## Linking a Jira Issue

1. In a Salesforce record, click **Associate/Create.**

   ![contentId-3091334501](/cms_trial/assets/35bea278-2748-4a1a-b814-bb6debb9b893.png)
2. Click **Create Jira Issue,** and the issue creation window appears.

   ![screenshot of Associate or Create Jira issue popup window](/cms_trial/assets/0419c7c1-629d-481a-8566-3790092bd51e.png)
3. Choose the desired **Jira Project** and **Issue Type**. All field and value mappings set by your administrator will be used to create the Jira issue.

   ![Screenshot of More fields to review ](/cms_trial/assets/c83651f8-9bf6-4aad-b31c-81a1c34af8d7.png)
4. Click *More Fields to Review*to show the **Linked Issues** textboxes.

   ![screenshot of Create Jira issue window](/cms_trial/assets/e3f9992d-d430-4cd0-b741-e47d294bb344.png)
5. In the *Linked Issues*column, choose the type of association for the linked issues and type into the search bar for the issue that you want to link with. The dropdown lists issues based on what you type, click on the relevant issue.

   ![screenshot of linked issues dropdown](/cms_trial/assets/05e6d357-a75d-42bf-b513-e2d746ef9dbb.png)
6. Once the *Linked Issues* section has been filled, click **Create**.

   ![screenshot of Create Jira issue window](/cms_trial/assets/9610226c-6e94-4019-b26b-ddf87eb54f43.png)
7. Upon successful creation, the *Issue created successfully* and the *Issue linked successfully* messages appear.

   **Jira view**

   ![screenshot of Jira view foe linked work item](/cms_trial/assets/f4a5b14d-997e-42c0-8132-9cbf25ee2ffe.png)

## Related information

- [Create an issue link](https://support.atlassian.com/jira-work-management/docs/link-an-issue/)
- [Configure an association](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/)
- [Associate a Jira Issue from Salesforce with Jira Issues (NextGen)](/cms_trial/space/CSFJIRA/3092284698/Associate+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/)