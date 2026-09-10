# Migrate risks to Risk Management module

If your organization is transitioning from the Risks module to the new Risk Managementmodule, you can easily migrate your existing risk data by leveraging existing risk metrics mapping.

By mapping your Risk Management metrics to the same Jira fields used by your legacy Risks module, your historical risk data will automatically populate in the new module without requiring manual re-entry.

Below, you can watch a video overview of the migration process.

## How does it work?

By default, the Risk module stores risk metric values directly in the Jira **Risk Consequence** and **Risk Probability** fields.

When you map a metric in the Risk Management module to a Jira field that already contains risk data from the Risks module, the Risk Management module reads that data directly from Jira fields.

1. **Risks module** -> writes to **Jira fields**
2. **Risk Management module** <- reads from **Jira fields**

## 1. Prerequisites

### (Risk Management) Create a new Risk Register for your risks

Before you migrate your risks within your box:

1. Go to the Risk Management module. [Create a new Risk Register](/cms_trial/space/SPM/1918406430/Create+new+risk+register/) and configure it. You can create multiple Risk Registers with multiple frameworks in one box. Each framework in the Risk Register would need to be configured and have its metrics mapped individually.

important When creating a new Risk Register, select all work item type(s) relevant to your risks. The item types you select must match the item types used for your risks in the Risk module of your box.

![Jira work item type field on the Create new risk modal.](/cms_trial/assets/87710dd1-1fe2-4d6b-a9f5-8814ffdcc69a.png)

For example, if the risks in the Risk module are “Bug” and “Risk,” then all Risk Registers with one or both of these types defined will automatically add Bugs and Risks to their Risk tables. If you have a few risks of the “Task” type and don’t add “Task” to the Risk Register, the Task-type risks will not appear in the Risk table.

If you miss any of the types, don’t worry. You can edit [**Risk Register configuration**](/cms_trial/space/SPM/1918669173/Risk+register+settings/) after you create it.

### (Risks) Review risks configuration

Before configuring the Risk Management module, review the risk configuration for the Risks module in the **App Configuration** > **Modules** > **Risks**:

- **Task sources**. Here, you determine which Jira fields will store the risk values for the probability and consequence axes. By default, those are **Risk consequence** and **Risk probability**. However, you can sync risk data to other Jira fields, including custom ones.

![Dropdowns for probability and consequence fields.](/cms_trial/assets/27148ca9-a3bb-477f-bcf9-658a3a044bb6.png)

- **Risk value definition**. Here, you define values for the consequence and probability axes. Those values will be added to the Risk Register in the Risk Management module after you map the field. When the field is synced, you cannot edit those values in the Risk Register, so ensure those are the values you want to continue using with your migrated risks.

![Risk probability values in the App Configuration.](/cms_trial/assets/b812e473-20e7-4c7b-bf21-f5b89f1d7d9f.png)

- **Axis names**. Axis names are not saved to Jira, so they will not sync with the Risk Management module. You can leave them as-is.

### (Jira) Field scheme

Since the risk data is written to Jira fields, ensure the fields you have defined on the *App Configuration* page in BigPicture are added to the Field Scheme associated with your Jira space.

That applies to all risks in your box, including those from other Jira spaces. If the Jira fields are missing, the Risks Register will display blank metric values after migration.

![Find your field modal in Jira.](/cms_trial/assets/83c9a0a9-adc1-46bd-9fb4-ac87b68de51c.png)

## 2. Map Jira fields

Now that you have reviewed the Jira fields and risk values and created the Risk Register, your next step is to replicate the field mappings in the new Risk Management module settings.

1. Open **Risk Register Configuration**.
2. The **Risk register frameworks** tab displays.
3. Scroll down to the **Metrics** you want to map.
4. Toggle **Map metric to Jira custom field** to enable field mapping. Enable the toggle for Probability and Consequence.
5. The **Jira custom field displays**. From the dropdown, select the corresponding **Jira field** that matches the mapping specified in the **App Configuration**.

![Metrics mapping in the Risk Management module.](/cms_trial/assets/68195b9f-0efe-4e32-8911-a2a49f13db5e.png)

1. The field values read from the Jira field appear. You cannot remove any of the synced values, add new ones, or change their names. But you can edit their numeric **Value**.
2. After you migrate your risks, you can notice that the **Risk matrix** is blank. Customize it to suit your needs.
3. Optional: The **Risk levels** remain unaffected, but you can customize them as well.

![A blank risk matrix and default risk levels.](/cms_trial/assets/7b25c2f4-2ef1-4ac4-8f61-6d644fe9107f.png)

1. When done, click **Save**.

## 3. Data migration

Once the mapping is saved, the Risk Management module will automatically sync with the data stored in Jira fields of the respective Jira work items.

This means the app will assign each risk in the Risk table its respective Consequence and Probability values. Open a Risks Register and switch to the Risks table. Verify that your existing risks display the correct values:

- If any risks are missing values, they match the Jira work item type but were never risks in the Risk module. Therefore, their applicable Jira fields contain no risk data. You can assign them values manually if you want to treat them as risks, or leave them blank and treat them as non-risks.
- Click the value in the Probability or Consequence/Impact column to update it for the selected risk. When you change the original value, the Jira field will also update.

![A Risk table with several risks.](/cms_trial/assets/7438730c-6ad1-423b-9dba-e577874af7d5.png)