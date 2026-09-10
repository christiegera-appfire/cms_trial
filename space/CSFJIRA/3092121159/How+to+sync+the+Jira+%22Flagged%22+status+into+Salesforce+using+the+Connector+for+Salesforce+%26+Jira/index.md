# How to sync the Jira "Flagged" status into Salesforce using the Connector for Salesforce & Jira

## Problem

Users want to automatically reflect the **Flagged** status of a Jira work item (such as a Task, Story, Bug, or Epic) into a field in Salesforce. However, even though the work item is marked as **Flagged** in Jira, the corresponding field in Salesforce remains **empty** or does not display the expected value.

## Solution

To sync the **Flagged** status into Salesforce, follow this approach:

1. Understand the **Flagged** fieldbehavior in Jira.

   - If a Jira work item is flagged, the value of the **Flagged** field is set to **"Impediment**.”
   - If the Jira work item is **not flagged**, the field remains **empty**.
2. Create a new **Text** field in Jira.

   1. In Jira, go to **Settings** > **Work Items** > **Fields**.
   2. Create a **Text Field** (e.g., `Jira Flagged Status`).
   3. Add this custom field to the **Create** and **Edit** screens for the relevant work types.
   4. Optionally, include it in the **View** screen.
3. Map the **Custom Field** in Connector for Jira & Salesforce.

   1. Go to **Jira** > **Apps** > **Connector for Salesforce** > **Bindings** > **Mappings**.
   2. Map the custom Jira text field (for example, `Jira Flagged Status`) to the appropriate **Salesforce field** (for example, a text or boolean field).  
      Example mapping:

      ![2025-09-24_07-34-11.png](/cms_trial/assets/4c93c670-3d53-480b-9e67-d6726dd76329.png)
4. Configure **Value mapping** forthe **Flagged** field**.**

   1. Navigate to the **Field Mapping Configuration**.
   2. Map the values as follows:  
      `yes` value in Jira mapped to `true` value in Salesforce  
      `no` value in Jira mapped to `false` value in Salesforce  
      This ensures that flagged work items in Jira are represented accurately in Salesforce.  
      Example mapping:

      ![values configuration for field mapping](/cms_trial/assets/0a02e1a6-0d5f-4aa1-88a7-389302b77c7b.png)
5. Automate the **Flagged** field updatein Jira.

   To ensure the custom field in Jira is updated when a work item is flagged:

   1. Go to **Jira** > **Settings** > **System** > **Global Automation** > **Create Rule**.
   2. Click **Create from scratch**.
   3. Configure a rule as follows:

      - **Trigger**: Field value changed → **Flagged**.

        ![Field value changed](/cms_trial/assets/ab8162da-f80c-43e7-972c-54ffe15f4b7b.png)
      - Add **Condition**:   
        IF Flagged = **"Impediment"**, update the custom text field with **"Yes"**.

        ![If block example](/cms_trial/assets/f1126816-cd69-47d9-b806-22d92fb8b10b.png)
      - **THEN Add an action**: **Edit work item** → Select the Jira custom field and set the value to “yes”

        ![Edit work item with the value set to yes](/cms_trial/assets/c27da9f2-950d-46a6-9956-843edf23c9a7.png)
      - **Condition**: click **Add else** > **Add condition** > **Work item fields condition** and set it:

        - **Field**: **Flagged**
        - **Condition**: **is empty**

          ![2025-09-23_14-19-49.png](/cms_trial/assets/8ecb663f-2cc2-45bd-ac46-50c39d53e096.png)
      - **THEN: Add an action**: **Edit work item**: Select the Jira custom field and set the value to “no”

        ![Edit work item example](/cms_trial/assets/4c71f879-d8d3-4290-b279-05fd5efd22bd.png)

Here is an overview of the Automation:

![Automation overview](/cms_trial/assets/35a904e8-de1b-4312-bb26-51408f85555b.png)

**Result**:

1. When flagging a Jira issue, the **custom text field** is updated to **"yes**." If not, the value will be **“no”**
2. This triggers the **Auto-Push** to Salesforce, and the corresponding Salesforce field will display the value **"true" or “no”** depending on the Flagged field value.

- The **Auto-Push** feature must be enabled in the Jira-Salesforce connector so the changes can sync automatically.
- This solution provides a clear and automated method to reflect the **Flagged** status in Salesforce without manual intervention.