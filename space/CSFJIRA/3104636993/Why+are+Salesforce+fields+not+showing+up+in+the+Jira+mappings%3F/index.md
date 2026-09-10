# Why are Salesforce fields not showing up in the Jira mappings?

## Purpose

When trying to map Salesforce fields into Jira, the fields are not showing in the mappings screen.

## Answer

In normal cases, the issue is explained in detail in this documentation: [Salesforce custom fields are not visible for mapping](/cms_trial/space/CSFJIRA/1596326940/Salesforce+custom+fields+are+not+visible+for+mapping/) and is related to a formula field based on a child object which is not supported as mentioned [here](https://apps-docs.servicerocket.com/salesforce-jira/does-the-connector-support-synchronizing-child-obj).

If the knowledge base above do not solve the issue for you. The next solution to try is to check if the profile of the integration user does have visibility of the fields.

1. Go to **Setup**> **Connected Apps OAuth Usage**.
2. On the page, look for **Salesforce & JIRA Cloud Connector** (or **Salesforce & JIRA Server Connector**depending on the case).
3. In the **User Count**column, click the number and click on the user.
4. Check and make sure the profile shows "System Administrator".

   ![system admin.png](/cms_trial/assets/9b235f8e-7f6f-4055-8f35-82c24ad9c2d5.png)
5. Next, go to **Setup** > in the Quick Find Box search for **Object Manager** and click on it.
6. Select the object with the fields that you want to map and click **Fields & Relationships**.
7. Click the field name > **Edit** > Change Type File.
8. On the **Establish field-level security** screen, search for the profile of the integration user and make sure the visibility box is checked. Then, click **Save**.
9. Repeat "step 8". for all the fields that you want to see on the bindings.