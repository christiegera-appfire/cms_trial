# Create a two-way workflow between Jira work items and Salesforce Manufacturing request

As a Manufacturing Manager, you'll often need to have access to the inventory management team to request resupply of stocks. When you are working on Salesforce and the inventory management team is working on Jira, you'll want a seamless workflow between these two divisions.

This use case shows you how to build a bidirectional workflow between Salesforce and Jira using Connector for Salesforce & Jira.

## Before you start

Make sure you have:

- [Installed the Salesforce package](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/)
- [Configured a connection](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/)

You will need some basic understanding of the following Jira and Salesforce features:

- [Jira custom field](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/)
- [Salesforce custom fields](https://help.salesforce.com/s/articleView?id=platform.fields_creating_picklists.htm&type=5)
- [Salesforce field dependencies](https://developer.salesforce.com/files/accessibility/customize-a-salesforce-object/picklists-field-dependencies/index.html)
- [Configure Jira cascading fields to work with Salesforce dependent fields](/cms_trial/space/CSFJIRA/1873413246/Configuring+Jira+cascading+fields+to+work+with+Salesforce+dependent+fields/)

## Complete scenario

**The Teams:**

1. The team that resides on Salesforce is the team that is in charge of receiving manufacturing requests.
2. The team that resides on Jira is the team that is working on stock and inventory management.

**The Scenario:**

1. A customer reaches out to the organization seeking to manufacture a custom door frame. The team in Salesforce receive the request from the customer.
2. The team in Salesforce raised a case that is synced with Jira issue to request for resupply of inventory.
3. The Jira team can communicate with the Manufacturing team in Salesforce through the synced Jira issue.

## Build this use case

### 1. Set up Salesforce

In this scenario, we will be using the Case object type.

1. To facilitate communication among Salesforce-using teams, create a **Record Type** in Salesforce and label it as *Supply Chain***.**
2. Navigate to **Setup** > **Object Manager** > **Case > Record Types**.
3. Click **New** to add a new Record Type: **Supply Chain**.  
   Apply a proper page layout to the record type you created.

   ![Screenshot showing the Supply Chain Record Type you just created.](/cms_trial/assets/b70eadc2-ee22-4d11-9a33-61d2912ab8ef.png)
4. Having two **Record Types** allows you to create cases with different page layouts, similar to *Work Item Types* in Jira.

   ![Screenshot of the Legal Case and Supply Chain Record Types.](/cms_trial/assets/15d391a3-6f2c-43a9-8e00-3ec8074761fb.png)
5. To create custom Case fields in Salesforce, navigate to **Setup** > **Object Manager** > **Case** > **Fields & Relationships**.
6. Click **New** and create:

   - **ItemFamily** (*Picklist* field)
   - **Item Request #1** (*Picklist Multi-Select* field)
   - **Item Request #1 Amount** (*Picklist Multi-Select* field)
7. Click **Field Dependencies** to create a dependencyfor **Item Family** and **Item Request #1**. This will allow **Item Request #1** field to display different values depending on the value selected for the **Item Family** field.

   ![edit field dependency page showing an example Item Family and Item Request.](/cms_trial/assets/df7bf7cf-2724-4a92-9023-60c77919f665.png)

   The **Supply Chain** record type now has custom fields for the Manufacturing Team, such as: **Item Request #1** and **Item Request #1 Amount**.

![Screenshot showing New Case Supply Chain with custom fields for the Manufacturing Team..](/cms_trial/assets/49e4a225-efe9-4bec-9182-efe2d2003a96.png)

### 2. Set up Jira

Create custom fields in Jira that correspond to the custom fields you've already set up in Salesforce.

1. In Jira, go to **Settings** > **Work items** > **Fields** > **Create new field**.
2. Create these fields:

   - **Item Request #1** (*Select List Cascading field)*
   - **Item Request #1 Amount** *(Number field)*type
   - **Item Request #2** (*Select List Cascading field)*
   - **Item Request #2 Amount** *(Number field)*type

### 3. Map entities and fields in Connector for Salesforce & Jira

1. In Jira, navigate to **Apps** > **Connector for Salesforce** > **App settings** > **Bindings**.
2. Click **Mapping** for the project you’re linking it to.
3. Click **Add Entity Mapping,** and map Jira work type with Salesforce objects:

   - Jira **Task** with Salesforce **Case** object
4. Click **Mappings** to map the fields from Salesforce to Jira for each of the **Issue types**. We can map cascading fields.

   1. Jira **Description** field with the **Description** field
   2. Jira **Item Request #1** field with the **ItemFamily** and the dependent **Item Request #1** field
   3. Jira **Item Request #1 Amount** field with the **Item Request #1 Amount** field
   4. Jira **Item Request #2** field with the **ItemFamily** and the dependent **Item Request #2** field
   5. Jira **Item Request #2 Amount** field with the **Item Request #2 Amount** field

      ![2025-11-25_14-11-23.png](/cms_trial/assets/f5960902-e10c-442b-ad11-294f9c733984.png)

### 4. Associate Jira task with Salesforce records

1. Open the Jira task with the request.
2. Under **Connector for Salesforce** click **Associate**.

   1. Select **Case** from the **Object Type** dropdown and find your Salesforce record.
   2. Select **Push to Salesforce then Pull from Salesforce** from the **After associating** dropdown list to update the data in Salesforce.

### 5. Automation for Jira

In this particular use-case, we didn't use any Automation for Jira. However, if you wish to do so, you can refer to this link; [How to enable status transition from Salesforce to Jira via Automation for Jira](/cms_trial/space/CSFJIRA/1874002066/How+to+enable+status+transition+from+Salesforce+to+Jira+using+Automation+for+Jira/) to set up your Automation to best-fit your scenario.

- [Configure Jira cascading fields to work with Salesforce dependent fields](/cms_trial/space/CSFJIRA/1873413246/Configuring+Jira+cascading+fields+to+work+with+Salesforce+dependent+fields/)