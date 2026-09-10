# Assign Record Types to manually or automatically created Salesforce objects from Jira

## Purpose

Salesforce users have multiple record types for their objects and want to assign a specific record type to a Salesforce object when creating a new record, whether manually or automatically.

This article helps you understand how to select the record type during the creation process.

## Answer

1. In Jira, click **Settings** (▢)> **Work items** > under **Fields**, click **Fields.**

   ![Fields view](/cms_trial/assets/0ed2fa38-c71b-4eb5-aa8e-d030441e95e8.png)
2. Click **Create new field**.
3. Search and select “**Select List (Single choice)**” custom field (for example **Record Type**).
4. In the **Options** field, add all the record types that the connector will use.
5. Click **Create**.
6. Then, map the custom field with the relevant project screens and click **Update**.
7. Search for the field you have created and click **Contexts and default value**.   
   Edit the default value or options necessary.

   ![Edit Optins.png](/cms_trial/assets/2005ca7c-1b9a-4852-ace8-f12d3d385f96.png)
8. Map the **Record Type** Jira field with the **Record Type ID** Salesforce field. 

   ![contentId-1596719355](/cms_trial/assets/dccc9f5e-3288-44b5-a85a-20eec0eceee0.png?version=1&modificationDate=1679627845140&cacheVersion=1&api=v2)
9. In Salesforce, go to **Setup** > **Object Manager** > **Case** > **Record types** and click the **Record type** name. The ID of that Record type can be taken from the URL:

   ![ID.png](/cms_trial/assets/f5018470-1b5f-4af7-af42-b49a5a4f7a3c.png)
10. Map the options of the **Record Type** field with the ID of the Case Record Types and click **Save**.

    ![Stor to Cae Configuration.png](/cms_trial/assets/5f3ceba6-e7ef-4c23-9739-fcf67197d176.png)
11. Now, by manually or automatically creating a Salesforce Record from the association tab in Jira issues, the Record type will be assigned to the created Salesforce Objects from Jira.