# How to add Jira status in Salesforce Record

## Purpose

This article provides the steps for showing the status of the linked Jira tickets in the Salesforce Record.

## Answer

To achieve this, you can use either one of these two methods:

## Adding more fields into the "Jira Issues" section

The connector comes with the "Jira Issues" lightning component to show the list of Jira tickets associated with a Salesforce Record. We can add the "Status" field so the linked ticket will show the current Jira tickets status. The steps are:

1. Navigate to **Salesforce Setup > Apps > Packaging > Installed Packages.**
2. Click on "Configure" on "Jira Cloud for Salesforce"(Or, "Jira Server for Salesforce" if you are running on the Server version)
3. In the **Available Fields** section, click **Add Jira Fields**.
4. Select **Status**.  
     
   Check the **Jira Issues** section of a linked Salesforce Record to check the changes. Example:

   ![contentId-3091466320](/cms_trial/assets/cb840c8c-e1f4-490c-a6ea-1548fce7a585.png)

   For more details about configuring the package: [Configuring settings in the Salesforce Package](/cms_trial/space/CSFJIRA/1873445530/Configure+settings+in+the+Salesforce+package/)

## Linking a Salesforce Field to the Jira Status field

By mapping the two fields, when pushing the update of a Jira ticket to the Salesforce Record, the Salesforce Field will be updated with the current Jira status. The steps are below:

1. Create a text Salesforce Field called "Jira Status"
2. Map it into the necessary Salesforce Object
3. In Jira, navigate to **Apps/Manage Apps > Salesforce > Bindings.**
4. Click **Mappings** on the necessary object.
5. Click **Mappings** again on the necessary issue type.
6. Do the mapping between Jira "Status" field and Salesforce "Jira Status" field.
7. Click **Add**.
8. Click on the"←" arrow to disable "Incoming Sync" as it is not supported.

   ![02-How to add Jira status in Salesforce Record.png](/cms_trial/assets/efebd72f-3874-49ea-a493-8cd1a61fe742.png)
9. Save the settings.

With this, when pushing the update to the associated Salesforce Record, the "Jira Status" field will be updated with the status.

![03-How to add Jira status in Salesforce Record.png](/cms_trial/assets/ed71d8a9-a362-406c-a8d0-54f12c23f480.png)![04-How to add Jira status in Salesforce Record.png](/cms_trial/assets/7d145057-418e-487e-8cb6-b3d5be174eeb.png)

## Disadvantage

As the field mapping is a 1-to-1 relationship, if the Salesforce Record is linked to multiple Jira tickets, it will be updated with the last Jira ticket that synced to it.