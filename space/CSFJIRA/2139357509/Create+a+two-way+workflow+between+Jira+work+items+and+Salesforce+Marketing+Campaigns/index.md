# Create a two-way workflow between Jira work items and Salesforce Marketing Campaigns

As a marketing manager working with Salesforce as a tool for tracking your marketing campaigns, updating a different Jira project separately for all your various marketing tasks can be cumbersome. You would want to configure your Salesforce and Jira to sync marketing campaigns and leverage Jira's agile methodology to track marketing tasks.

## What you'll learn

- How to synchronize Salesforce campaigns with Jira epics
- Set up task synchronization between both platforms
- Create smooth workflows for campaign approval and execution
- Enable real-time status updates across teams

## Before you start

Make sure you have:

- Installed and set up Connector for Salesforce & Jira: [Installation](/cms_trial/space/CSFJIRA/1873477874/Installation/)
- Admin access to both Salesforce and Jira

You will need some basic knowledge of:

- [Jira custom field](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/)
- [Jira workflows](https://www.atlassian.com/software/jira/workflows)
- [Automation for Jira](https://www.atlassian.com/software/jira/guides/expand-jira/automation)
- [Salesforce custom fields](https://help.salesforce.com/s/articleView?id=platform.fields_creating_picklists.htm&type=5)
- [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/)

## Complete scenario

**Teams:**

1. The team that resides on Salesforce is the Upper Management team for the Marketing team. They oversee the tasks that need to be worked on and create campaigns.
2. The team that resides on Jira is the team that works directly on the tasks created by the Upper Management team, using Agile Methodology to work and track.

**Scenario:**

1. The Salesforce team creates a Campaign in Salesforce.
2. The Campaign record is automatically pushed to Jira as a newly created epic linked to the Campaign.
3. The Jira team works on the tasks and tracks them using Agile Methodology. They can also get the reports from either the JSW's report feature or from the Connector for Salesforce & Jira Reports.
4. The Jira team can change the status of the task and push it to Salesforce for reviewing.
5. The Salesforce team can review and request the Jira team to re-check, which will be pushed back to Jira and get the Jira team to improve on the work.
6. After the Salesforce team approves the work, the Jira team can publish (if it requires any publishing) or mark the task as done.

## Build this use case

### 1. Set up Salesforce

In this scenario, we use the **Campaign** and **Task** objects. We will associate the **Campaign** object with Jira Epic and the **Task** object with Jira Task and Social work types. First, we need to create custom fields in Salesforce.

#### Campaign object setup

1. In Salesforce, navigate to **Setup** > **Object Manager** > **Campaign** > **Fields & Relationships**.
2. Click **New** and create two *Text* fields: **Epic Issue Key** and **Summary**.

   1. Make the field visible for all required profile types.
   2. Add the fields to the **Campaign layout**. You can easily design the field order in the **Page Layouts**.

**Task object setup**

1. Create custom fields for the **Task** object. navigate to **Setup** > **Object Manager** > **Activity** > **Fields & Relationships**.
2. Navigate to **Setup** > **Object Manager** > **Activity** > **Fields & Relationships** to create custom fields for the **Task** object.
3. Click **New** and create these fields:

   - **Epic Issue Key** (*Text* field)
   - **Summary** *(Text* field)
   - **Need to re-check** (*Picklist* field)
   - **Campaign Type** (*Picklist* field)
   - **Account Concerned** *(Multi-Select**Picklist* field*)*

     ![Screenshot of a new campaign configuration.](/cms_trial/assets/4d3e4446-e41a-4752-b68a-47fc602bc2a1.png)

### 2. Set up Jira

**Create custom fields in Jira**

1. In Jira, go to **Settings** > **Work items** > **Fields** > **Create new field**.
2. Create these fields:

   1. **Account Concerned** *(Checkboxes* field)
   2. **Campaign Type** *(Select list single choice* field)
   3. **Need to re-check (SF)** *(Select list single choice* field)

**Create a custom work type in Jira**

1. Navigate to **Work types**.
2. Click **Add work type** and name it **Social**.
3. Click **Work type schemes** and add the Social work item to your project’s scheme.

### 3. Map entities and fields in Connector for Salesforce & Jira

1. In Jira, navigate to **Apps** > **Connector for Salesforce** > **App settings** > **Bindings**.
2. Click **Mapping** for the JSM project you’re linking it to.
3. Click **Add Entity Mapping,** and map these Jira work types with Salesforce objects:

   - Jira **Epic** with Salesforce **Campaign** object
   - Jira **Task** with Salesforce **Task** object
   - Jira **Social** with Salesforce **Task** object

     ![Screenshot of the Mapping configuration page. ](/cms_trial/assets/5f5bef41-6a63-47bc-a800-adc4c4f35d85.png)
4. Click **Mappings** to map the fields from Salesforce to Jira for each of the **Issue types** and configure the synchronization direction.

   - **Epic** to **Campaign:**

     - Jira **Summary** field with the **Summary** field
     - Jira **Epic Name** field with the **Name** field
     - Jira **Key** field with the **Epic** **Issue** **Key** field
     - Jira **Status** field with the **Status** field
     - Jira **Campaign Type** field with the **Type** field

       ![Screenshot showing the Epic to Campaign field mappings.](/cms_trial/assets/90741730-62cc-4cfc-8cc3-e0c24ab4983d.png)
   - **Task** to **Task** and **Task** to **Social** field mapping should be the same:

     - Jira **Summary** field with the **Summary** field
     - Jira **Epic Link** field with the **Epic Link** field
     - Jira **Account Concerned** field with the **Account Concerned** field
     - Jira **Status** field with the **Status** field
     - Jira **Need to re-check (SF)** field with the **Need to re-check** field

       ![Screenshot showing the task to task field mappings.](/cms_trial/assets/e29723d4-e252-4be4-a651-95227119924f.png)

### 4. Set up workflow statuses and post functions

1. Configure a new Jira workflow for the **Marketing** team use case.

   1. In Jira, go to **Settings**>**Work items**>**Workflows** and click **Add workflow.**
   2. Click **Add Status** to create each required status and configure the status category.
   3. Check the **Allow all statuses to transition to this one** for every created status.

      ![Screenshot showing the set up of the workflow statuses.](/cms_trial/assets/a8b141aa-e532-4d9a-9a96-16fd907cc8da.png)
2. Click the *transition* arrow to Add the **Push to Salesforce** post-function so that any transition will push the updates made in Jira to Salesforce.
3. Add the following post functions to **In Progress** status

   1. Add the **Update Issue Custom Field** post function to set the **Need to re-check (SF)** customfield to **No** value.
   2. Add the **Update Issue Field** post function to set the **Resolution** field to **None** value.  
      This setting will synergize with the **Automation** configuration below.

      ![Screenshot showing the Transition In Progress workflow.](/cms_trial/assets/65a576e2-125d-4840-9e9b-20008a56ef3f.png)

### **5. Configure Status value mapping**

Salesforce and Jira have different lists of statuses. For example, there’s a **Published** valuein Jira but not in Salesforce, and a **Completed** value in Salesforce but not in Jira. Configuring the field mapping can specify the value mapping in both platforms. This allows Connector for Salesforce & Jira to translate mapped values and avoid errors during synchronization.

1. Go to **Bindings** and click **Mapping** for your project.
2. Click **Mappings** for each entity mapping.
3. Click **Configure** on the Status field:

   ![Screenshot showing the task to task field mappings.](/cms_trial/assets/4c8890f8-968f-4955-a4eb-66f92b3a005a.png)
4. Map the values that don’t match between Jira and Salesforce:

   ![Screenshot showing the Task to Task Configuration.](/cms_trial/assets/aa45bd77-1af3-4ab8-ab3f-654a44f139f8.png)
5. Repeat the steps for all entity mappings.

### 6. Create Jira epic from Salesforce

1. Open the Salesforce Campaign record.
2. Click **Associate/Create** under *Jira work items*.
3. Click **Create Jira Issue**and the **Create Jira Issue** pop-up window will appear.

   ![Screenshot of the Associate or Create Jira Issue window.](/cms_trial/assets/23e45c24-16f4-41fc-9eba-8c9bf463357f.png)
4. Choose the desired **Jira Project** and select **Epic** for the **Issue**
5. Select **Auto Push** to **push** changes automatically to the associated Jira epic.

### 7. Automation for Jira

We’ve created an automation rule in Jira to allow status transition from Salesforce. To learn more, follow the steps on the article [How to enable status transition from Salesforce to Jira via Automation for Jira](/cms_trial/space/CSFJIRA/1874002066/How+to+enable+status+transition+from+Salesforce+to+Jira+using+Automation+for+Jira/).

The automation will transition the issue from any statuses to **Re-check** in Jira, when:

- The **Need to re-check (SF)** field value is changed from **No** to **Yes**.
- The user who performs this change is the **Salesforce & Jira Cloud Connector** add-on user.

  ![Screenshot of the Automation Rule details.](/cms_trial/assets/f18ded6b-a255-4a07-9f59-7d61d5d9acd3.png)