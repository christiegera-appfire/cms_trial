# Create a two-way workflow between Jira work item and Salesforce Legal records

As a services manager, you often receive requests from different customers with different needs. Once you prepare a statement of work (SOW), you need to access the legal team for final contract preparation. You want to have a seamless workflow between the services team (working on Jira) and the legal team (working on Salesforce).

This use case shows you how to build a bidirectional workflow between Salesforce and Jira using Connector for Salesforce & Jira. Together with Jira's built-in functions like custom fields, workflows, post-functions, and Automation for Jira.

## Before you start

Make sure you have:

- Installed and set up Connector for Salesforce & Jira: [Installation](/cms_trial/space/CSFJIRA/1873477874/Installation/)

You will need some basic understanding of the following Jira features:

- [Salesforce custom fields](https://help.salesforce.com/s/articleView?id=platform.fields_creating_picklists.htm&type=5)
- [Create record type in Salesforce](https://help.salesforce.com/s/articleView?id=platform.creating_record_types.htm&type=5)
- [Jira custom fields](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/)
- [Jira workflows](https://www.atlassian.com/software/jira/workflows)
- [Automation for Jira](https://www.atlassian.com/software/jira/guides/expand-jira/automation)

## Complete scenario

**Teams:**

1. The team that resides on Salesforce is the Legal team.
2. The team that resides on Jira is the support and services team.

**Scenario:**

1. A customer reaches out to the organization's support team seeking their assistance.
2. Support/Services then creates an internal Jira ticket for their request of an SOW/pre-contract.
3. The created Jira ticket is associated with a Legal Case in Salesforce.
4. The Legal team will find a new Case created in Salesforce and work on it.
5. The Legal team updates the Case in Salesforce once they have provided what they need and it'll automatically get updated in Jira.
6. The Services team that is working with the customer can now update the customer with the information that they need.

## Build this use case

### 1. Set up Salesforce

In this scenario, we use the **Case** object. We will associate the **Case** object with Jira Task work types. First, we need to create Legal Case Record Type and custom fields in Salesforce to facilitate communication between the teams that use Salesforce.

1. Navigate to **Setup** > **Object Manager** > **Case** > **Record Types**.
2. Click **New** to add a new Record Type: **Legal Case**.  
   Apply a proper page layout to the record type you created.

   ![Screenshot of the Case Object with Record Types selected.](/cms_trial/assets/33702311-ff6c-4133-b08a-7f64dd3aec70.png)
3. Go to **Fields & Relationships** and create custom Case fields in Salesforce:

   - **Contract Type** (*Picklist* field)
   - **Contract Due Date** (*Date* field) used to specify the end of the contract.
   - (Optional) **Pending for Legal?** (*Picklist* field) with *Yes* and *No* options.

Now you can create a Case object as **Legal Case** with new custom fields visible.

![Screenshot of New Case Legal Case in Salesforce.](/cms_trial/assets/ff1c8710-870b-4a10-a8ea-9247b45bc74f.png)

### 2. Set up Jira

**Create custom fields in Jira**

Create custom fields in Jira that correspond to the custom fields you've already set up in Salesforce.

1. In Jira, go to **Settings** > **Work items** > **Fields** > **Create new field**.
2. Create these fields:

   1. **Contract Type** *select list (single choice)* field
   2. **Contract Due Date**  *date picker* field
   3. (Optional) **Pending for Legal?***select list (single choice)* field

### 3. Map entities and fields in Connector for Salesforce & Jira

1. In Jira, navigate to **Apps** > **Connector for Salesforce** > **App settings** > **Bindings.**
2. Click **Mapping** for the JSM project you’re linking it to.
3. Click **Add Entity Mapping,** and map:

   - Jira **Task** with Salesforce **Case** object

     ![Screenshot of adding entity mapping in Jira.](/cms_trial/assets/13e044a4-e44a-4f8e-b6b1-6f285a4845a6.png)
4. Click **Mappings** to map the fields from Salesforce to Jira for **Task** to **Case** field mappings:

   - Jira **Summary** field with the **Subject** field
   - Jira **Contract Type** field with the **Contract Type** field
   - Jira **Contract Due Date**  field with the **Contract Due Date**  field
   - (Optional) **Pending for Legal?** field with the **Pending for Legal?** field

     ![Screenshot of mapping the fields from Salesforce to Jira for task to case field mapping.](/cms_trial/assets/3e8d2a66-efb7-45c0-9b21-c8e61693d337.png)

### Associate Jira task with Salesforce records

1. Open the Jira task with the request of a SOW/pre-contract.
2. Under **Connector for Salesforce** click **Associate**.

   1. Select **Case** from the **Obcject Type** dropdown and find your Legal Case.
   2. Select **Push to Salesforce then Pull from Salesforce** from the **After associating** dropdown list to update the data in Salesforce.
3. Open Salesforce case to see updated fields.

### 4. Set up workflow statuses and post functions

1. Configure a new Jira workflow for the **Legal** team use case

   1. In Jira, go to **Settings** > **Work items** > **Workflows** and click **Add workflow.**
   2. Click **Add Status** to create the required statuses and configure the status category:

      - **Waiting for Legal**
      - **Waiting for Jira Team**
   3. Check the **Allow all statuses to transition to this one** for every created status.
2. Click the *transition* arrowto the **Waiting for Legal**status and click **Post Functions**.

   ![Screenshot showing the Legal workflow.](/cms_trial/assets/57f33da0-b5ef-45f0-9a36-00fdd7ef84f1.png)
3. Add the following post functions:

   1. The **Update Issue Custom Field** post function that automatically updates the **Pending for Legal?**field to **Yes** whenever this transition is made.
   2. The **Push to Salesforce** postfunction automatically pushes the mapped fields to Salesforce.

      ![Screenshot of the Transition Waiting for Legal workflow.](/cms_trial/assets/8af5b7ce-7a75-493f-a39d-d6d42509ff08.png)

### 5. Automation for Jira

We need to add an automation to enable the ability to transition the issue in Jira from Salesforce.

1. Navigate to **Settings > System > Global Automation.**
2. Click **Create Rule** > **Create from scratch**.
3. Select the **Field value changed** trigger and search for **Pending for Legal?**field and click **Next**.

   ![Screenshot of the Automation page showing the Field value changed trigger.](/cms_trial/assets/2da8cdbd-8205-465a-90e9-5b38560ec055.png)
4. Select **If: Add a condition**.
5. Select **User condition** and set:

   - **User who triggered the event** for the *User* field
   - **Is**for the *Check to perform* field
   - **Connector** **for** **Salesforce & Jira** for the *Criteria*field

     ![Screenshot of the Automation page with the User condition selected.](/cms_trial/assets/14b7d8ed-b8c5-4d88-ba44-2bde1ba2f9bd.png)
6. Click **Then: add an action**.
7. Select the **Transition work item**.

   ![Screenshot of the Automation page with the Transition work item selected as the action.](/cms_trial/assets/6d464457-286e-4680-b821-8d050b376b3b.png)
8. Choose **Waiting for Jira Team**for the *Destination Status and c*lick **Next**.

   ![Screenshot of the Automation page showing Waiting for jira team as the Destination status..](/cms_trial/assets/69c70654-ca65-432a-bc59-56731ca74a83.png)
9. Click **Turn on rule**.