# How to auto-associate a Salesforce record with a Jira issue upon Jira issue creation in Jira Cloud

## Problem

Currently, the Connector cannot automatically link a Salesforce record with a Jira issue when it’s created. However, you can set up automation with the Jira [REST API](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470757333/Jira+REST+API+association?src=search), within the project to facilitate the auto-association process.

To make the automation work, manually add the Salesforce Object ID in a custom field when creating the Jira issue.

**Compatibility:** This method works with both standard Jira and Jira Service Management (JSM).

Scope: This guide focuses exclusively on one-to-one associations.

## Instructions

### Part 1: Create a Jira custom field

First, we'll create a custom field to capture the Salesforce Object ID.

1. Navigate to **Settings** > **Work Items** > **Fields**.
2. Click **Create new field**.

   1. Field type: **Short Text (plain text only)**
   2. Name: In this example, the name of the field is `Case ID.`
3. Add this field to your **Create screen** for the relevant Issue Type.
4. (Optional) Add the field to the **View** and **Edit** screens.

### Part 2: Create the Jira automation

Jira Automation allows us to automatically send a web request to edit the entity property of the Jira issue and then associate the Salesforce record.

1. Go to **Project** > **Project Settings** > **Automation** (in the left panel).
2. Click **Create Rule**.
3. Select **Field value changed** as your trigger and set it as follows:

   - **Fields to monitor for changes**: `Case ID`
   - **Change type**: `Any changes to the field value`
   - **For**: `Create issue`

![Field value changed screen with Fields to monitor for changes, Change type and For fields](/cms_trial/assets/b00fe125-0374-417f-a598-3ea9456ff97c.png)

1. Click **Add Component** > **IF: Add a condition** > **{{smart values}} condition**.  
    This ensures that our agents/customers add the correct ID of the configured object. In this example, the Case Object type is used.

   - **First value**: `{{issue.<customField_Id>}}`
   - **Condition**: `Starts with`
   - **Second Value**: `Object ID prefix`

Ensure you utilize the field ID corresponding to the field you created on your instance in Part 1 of this documentation. To find the Custom Field ID, see [How to find the ID for custom field(s)](https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html?__hstc=72543820.dca6847bc67d72cb12dda09618bcbbf0.1610352968903.1663293812024.1663296455536.959&__hssc=72543820.27.1663296455536&__hsfp=3395054717).

See the [Salesforce Object Key Prefix List | Salesforce Ben](https://www.salesforceben.com/salesforce-object-key-prefix-list/) documentation to find the right prefix for your object type.

![smart values condition page with First value, Condition, and Second value fields](/cms_trial/assets/c13000ff-99de-4e05-97b7-7ec873241442.png)

1. Click **Next** > **Add an action** > **Create variable** and set the component as follows:

   - **Variable name**: `CaseID`
   - **Smart value**: `{{fieldChange.toString}}`

This helps update the JSON file in the web request.

![Create variable screen with Variable name and Smart value fields](/cms_trial/assets/90baab1a-9e60-4726-b095-7846fba07b95.png)

1. Click **Next** > **Add Component** > **IF: Add a condition** > **{{smart values}} condition** and set the component as follows:

   - **First value**: `{{CaseID.length()}}`
   - **Condition**: `equals`
   - **Second value**: `18`

This helps to verify that the added ID is the correct length.

![smart values condition screen with First value, condition and Second value fields](/cms_trial/assets/0cae5fa2-d24f-4d6e-89a4-7033fe23021a.png)

1. Set the **Web Request URL** with the URL according to your Jira environment:

   - Jira Cloud EU: `eu-sfjc.integration.appfire.app/external/api/association?allowUpsert=true`
   - Jira Cloud Rest of the World: `https://sfjc.integration.appfire.app/external/api/association?allowUpsert=true`
2. In a new tab, navigate to **Jira > Apps > Connector for Salesforce > Connections** > click the 3 dots next to your connection > **API Access Token** > Select the **REST API token** lifespan and copy the token shown at the bottom.

   ![image-20250722-141733.png](/cms_trial/assets/0bb9d925-afc2-4780-8ed1-4970e5ec48e4.png)
3. Go back to the automation and in the *Headers* section, set the **Key** name as `Authorization`.
4. Set the **Value** as `JWT <REST API Token>`
5. Set the **HTTP Method** to `POST` and select the **Delay execution** option.
6. Set the **Web Request body** as Custom data and use the following JSON file in the **Custom data** field. In this example, a case object type is used.

   ```text
   {
   	"jiraIssueId": "{{issue.id}}",
   	"son": "Case",
   	"soid": "{{CaseID}}",
   	"viewOnly": false,
   	"autoPush": true,
   	"autoPull": true
   }
   ```

   The web request component up to this point looks like the following:

   ![image-20250722-142144.png](/cms_trial/assets/065eb4d4-4606-4325-bd36-762548f24c8b.png)
7. Click **Next** > **Add Component** > **THEN: Add an action** > **Re-fetch issue data**.  
   Overview of the final automation:

   ![image-20250723-134035.png](/cms_trial/assets/f12c0b7d-26c8-48b3-8cda-69a568d468ee.png)

   Now, if you add the Salesforce Object ID within the Case ID field after creating a Jira issue, the automation associates that record with the created Jira issue.

This auto-association won’t trigger the default post-actions; you’ll need to manually push the information to Salesforce.