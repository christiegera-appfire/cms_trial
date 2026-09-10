# Create a two-way workflow between JSM and Salesforce on-site support

As a support manager who manages locally-based support teams using Salesforce and offline support teams using Jira, you will want the two teams to share information across Jira and Salesforce seamlessly.

This use case shows you how to configure Jira and Salesforce for the online and offline support teams to provide customer the best support experience.

## Before you start

Make sure you have:

- Installed and set up Connector for Salesforce & Jira: [Installation](/cms_trial/space/CSFJIRA/1873477874/Installation/)
- Installed Jira Service Management™ (JSM) Connector for Salesforce

You will need some basic understanding of the following Jira and Salesforce features:

- [Salesforce custom fields](https://help.salesforce.com/s/articleView?id=platform.fields_creating_picklists.htm&type=5)
- [Create record type in Salesforce](https://help.salesforce.com/s/articleView?id=platform.creating_record_types.htm&type=5)
- [Jira custom fields](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/)

## Complete scenario

**The Teams:**

1. The Jira support team resides on Jira and uses JSM as the medium to directly communicate with customers.
2. The On-site support team works out of Salesforce and is dispatched to the customer’s place to troubleshoot hardware issues.

**The Scenario:**

1. The customer raises a support ticket using the JSM portal to the support team in Jira.
2. Jira Support team tries to resolve the issue online using email.
3. Jira team is able to retrieve the customer’s information using the JSM connector. Information retrieved includes the customer’s email (the **Reporter’s email** field). The Reporter’s email field is mapped with Salesforce’s Contact **Email** field.
4. If the L1 support team is unable to provide the resolution remotely, they can raise a ticket **(Salesforce Case)** to arrange the on-site visitation.
5. The Jira team confirms with the customer if their *registered*phone number is still in use. If it’s outdated and requires updating, the Jira support rep uses the **Updated Phone Number** field (*explained below)*to push the update to Salesforce’s **Contact** field and update the phone number.
6. The Salesforce team can use the updated phone number to reach out to the customer to arrange for the on-site visit.

## Build this use case

### 1. Set up Salesforce

In this scenario, we will be using the Case object type.

1. (Optional) If needed, you can create a Record Typefor the Support team to use and label it as *Support Chain.*)

   1. Navigate to **Setup** > **Object Manager** > **Case > Record Types**.
   2. Click **New** to add a new Record Type: **Support Chain**.  
      Apply a **Case (Support) Layout** to the record type you created.

      ![Screenshot showing example Record Types.](/cms_trial/assets/30aabf81-20fa-4370-b016-1a2cba462438.png)
2. To create custom Case fields in Salesforce for the on-site support team, navigate to **Setup** > **Object Manager** > **Case** > **Fields & Relationships**.
3. Click **New** and create:

   - **Date of Visitation** (*Date* field) to specify the appointment date after the customer agreed on it.
   - **Time Slot for Visitation** (*Picklist* field) to specify the time slot for the visitation, for example, 8 AM - 10 AM or 2 PM - 4 PM.
4. Select the **Case (Support) Layout** to include the created fields.   
   The **Support Chain** record type now has custom fields specifically for the Support Team, such as the **date of Visitation** and **the Time Slot for Visitation**.

   ![Screenshot showing an example New Case Support Chain.](/cms_trial/assets/c3ac9be1-3f0f-4cee-b8c4-fa7db40a9b36.png)

### 2. Set up Jira

**Before you start:**

- Make sure you have a JSM project created on your Jira instance.
- Create custom fields in Jira that correspond to the custom fields you've already set up in Salesforce.

1. Create custom fields in Jira.  
   In Jira, go to **Settings** > **Work items** > **Fields** > **Create new field**:

   1. **Updated Phone Number** (*Short text* *plain text only* field)
   2. **Reporter’s email**  (*Short text* *plain text only* field)
   3. **Date of Visitation** (*Date Picker* field)
   4. **Time Slot for Visitation** *(Select List cascading* field)  
      These fields will push data to Salesforce when the customer has changed their phone number and email, and synchronize information on the visitation time.

      ![Screenshot showing the Internet issue work item in Jira.](/cms_trial/assets/ba2f6257-9bf2-4f5c-9de6-63b9d1a11189.png)

### 3. Map entities and fields in Connector for Salesforce & Jira

1. In Jira, navigate to **Apps** > **Connector for Salesforce** > **App settings** > **Bindings**.
2. Click **Mapping** for the JSM project you’re linking it to.
3. Click **Add Entity Mapping,** and map:

   - Jira **Task** with Salesforce **Case** object
   - Jira **Task** with Salesforce **Contact** object

     ![Screenshot showing entity mapping.](/cms_trial/assets/aed23134-b9f7-4c14-8310-19dc46d5dfbf.png)
4. Click **Mappings** to map the fields from Salesforce to Jira for each of the **Issue types**:

   - For **Task** to **Case** field mappings:

     - Jira **Summary** field with the **Subject** field
     - Jira **Description** field with the **Description** field
     - Jira **Date of Visitation** field with the **Date of Visitation** field
     - Jira **Time Slot for Visitation** field with the **Time Slot for Visitation** field

       ![Screenshot of mapping between Jira and Salesforce items.](/cms_trial/assets/9b8d6f98-999f-49bc-9a4b-e1425848dd69.png)
   - For **Task** to **Contact** field mappings map:

     - Jira **Reporter’s email** field with the **Email** field
     - Jira **Updated Phone Number** field with the **Business** **Phone** field

       ![Screenshot showing the Task to Contact field mappings.](/cms_trial/assets/7e969dc0-132a-48f3-a08c-d4567d3997c0.png)

### 4. Associate Jira task with Salesforce records

1. Open the Jira task with the updated contact data.
2. Under **Connector for Salesforce** click **Associate**.

   1. Select **Contact** from the **Obcject Type** dropdown and find your Contact name.
   2. Select **Push to Salesforce then Pull from Salesforce** from the **After associating** dropdown list to update the Contact’s data in Salesforce.
3. Click **Create Salesforce Object** to create a **Case** object and push it to Salesforce.

   ![Screenshot showing the associated Jira tasks for the Salesforce records.](/cms_trial/assets/bf33d114-f326-49dc-bf64-712f009cc66c.png)
4. Open Salesforce Case record.  
   You can now see the updated email address and the phone number directly in Salesforce.

   ![Screenshot of the Case Details page showing the updated email address.](/cms_trial/assets/7c969858-3cd0-44e5-922d-48725536df14.png)

### 5. Automation for Jira

In this particular use-case, we didn't use any Automation for Jira. However, if you wish to do so, you can refer to this link;  [How to enable status transition from Salesforce to Jira via Automation for Jira](/cms_trial/space/CSFJIRA/1874002066/How+to+enable+status+transition+from+Salesforce+to+Jira+using+Automation+for+Jira/)  to setup your Automation to best-fit your scenario.