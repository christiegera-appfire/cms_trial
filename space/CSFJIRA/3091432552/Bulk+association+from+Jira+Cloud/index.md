# Bulk association from Jira Cloud

This page guides you on how to use the bulk associate feature to associate your Jira issue with multiple Salesforce object records.

## Before you start

To use the bulk associate feature:

- You must be a Jira Cloud user with [Edit Issue](https://confluence.atlassian.com/jiracorecloud/permissions-overview-765593621.html) permission.
- You must have a connection to Salesforce. If you don’t have a connection to Salesforce, see [Set up a connection to Salesforce](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1493172335) for instructions.
- You must have project binding. See [Bind the Jira project to a Salesforce connection](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/).

## Configure the bulk association

1. Open a Jira issue, and from the *CONNECTOR FOR SALESFORCE* section, click **Associate** > **Bulk Associate**.

   ![bulk associate option on Jira issue page](/cms_trial/assets/3cd70593-adb5-4635-956a-1c656d95ac35.png)

   The *Bulk Salesforce Associate* page opens to *Step 1 of 3: Select Salesforce records*.

   ![select Salesforce records page](/cms_trial/assets/e3eeda78-1ee3-4627-afe6-e9ea6b4fa6e0.png)
2. Under the *Salesforce Object Records* heading, select an object type from the **Object Type** dropdown. The list of available object types appears. To further refine your search, enter a search term in the **Search for Records** field.
3. Select the records to associate with the Jira issue. Click a page number or **Next** to move through the pages of results.   
   If you select a record from one object type and attempt to change to another object type, you will see a message indicating that your selected records will be lost. Click **Yes** to continue to the new object type, or **No** to return to the current object type.

   ![sfjc-lost-object-message.png](/cms_trial/assets/ac45d1a6-b900-4ce6-94dd-361b274bdd1c.png)
4. Click between *Results* and *Selected records* to move between the list of all results that match your search and the list of selected records.
5. Once you have selected all the records you want to associate with your Jira issue, click **Next** in the lower left side of the page.
6. Review the selected records. If the selected records are correct, click **Next** in the lower left corner to proceed to *Step 2 of 3: Overview*.

   ![selected Salesforce records](/cms_trial/assets/10bab5a8-207d-4bf7-8a4d-167d93397367.png)
7. Confirm the records you have selected are the ones you want to associate with the Jira issue. If you need to make a change, click **Back** to return to the *Step 1 of 3* page. Otherwise, click **Bulk Associate** to associate your selected records to the Jira issue. Depending on the number of records you are associating with this Jira issue, this can take some time to complete.
8. When successful, you will see a success message indicating the number of successful associations between the Salesforce records and the Jira issue. If the association is not successful, you will see a message indicating the number of Salesforce records that were not associated. Click **Contact support** in the message box to proceed to **Support** where you can submit a ticket.

   ![sfjc-step3.png](/cms_trial/assets/9db87fc6-c3b9-466d-bfa5-c29c75e76f61.png)
9. Click **Finish** to return to the Jira issue.

Each Jira issue can be associated with a maximum of 1000 Salesforce records.