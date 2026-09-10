# How to set the Jira Reporter as the current Salesforce user when creating the Jira work item.

## Problem

When you create a Jira work item from Salesforce using the **Connector for** **Salesforce & Jira**, the system maps the Jira **Reporter** field to the Connector for Salesforce and Jira user by default. If you use the [Changing Reporter/Assignee using Case Owner email](/cms_trial/space/CSFJIRA/3091400759/Changing+Reporter%2FAssignee+using+Case+Owner+email/) approach, the system maps the field to the **Salesforce Owner ID** or **CreatedBy ID**. However, neither option represents the Salesforce user who actually clicked the button to create the Jira work item.

## Solution

The Connector doesn't natively capture the Salesforce user who clicks the button to create the Jira work item. However, you can implement the workaround below, which dynamically sets the current Salesforce user ID into a custom field before creating the Jira work item.

#### **Step 1:** Add a custom **Formula** and **Text** field in Salesforce

1. In Salesforce go to  **Setup** > **Object Manager** >your Object (for example, **Opportunity**, **Case,** etc.)> **Fields & Relationships** > **New**.
2. Choose the **Text** field and name it.
3. Repeat step 1 and create the **Formula** field.
4. Set `$User.Email` as the formula value.
5. Name the field, for example, **"Current user email,"** and add it to the relevant page layout.

#### **Step 2: Create a Salesforce Flow to capture the current user**

1. In Salesforce, go to **Setup** > **Flows** > **New Flow**.
2. Select **Record-Triggered Flow**.
3. Configure the Flow:

   - **Trigger** **the Flow When**: **A record is updated**

     ![A record is updated option](/cms_trial/assets/f5092ce0-86bc-42ca-b5d9-f06b7ae29af6.png)
4. Click the **Plus** ( + ) icon to add a new element.

   ![Add element](/cms_trial/assets/93df0fe1-5bc8-42df-9647-a0379c628865.png)
5. Select **Update Related Records** and set this element as follows:

   1. For **How to Find Records to Update and Set Their Values** select the **Use the case record that triggered the flow** option.

      ![Use the case record that triggered the flow option.](/cms_trial/assets/4038d507-3318-4578-a2b6-5536dd09f97d.png)
   2. For **Field**, select the text field you created in Step 1,
   3. For **Value**, paste the following value `{!$Record.Current_User_Email__c}` . This approach follows the methodology outlined in the [Changing Reporter/Assignee using Case Owner email](/cms_trial/space/CSFJIRA/3091400759/Changing+Reporter%2FAssignee+using+Case+Owner+email/) article.
6. Click **Activate** to enable the Flow.