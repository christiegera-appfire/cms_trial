# Use Jira custom fields with historical values

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

## Use Jira custom fields with historical values (old navigation)

Click to expand the guide

If you decide to use Jira custom fields in prioritization formulas as a replacement for existing prioritization metrics, you may want to preserve the historical values in those custom fields. This can be achieved by exporting data from the Priorities module and importing it into Jira using Jira’s import functionality.

1. Create custom fields in Jira that mirror the priority metrics (e.g., an Ease custom field).

   ![image-20260108-095051.png](/cms_trial/assets/02690aea-4ca6-491f-abe0-4d4eb1de28be.png)
2. Add these custom fields to the appropriate Jira screens for the relevant spaces so they are visible on all work item types.
3. In **BigPicture** > **Priorities module**, click the **Export table in CSV** button.

   ![image-20260109-080205.png](/cms_trial/assets/2c75ec35-ee9b-4e55-9430-2919e5f1ed33.png)
4. In the exported file, split the work item key and summary into separate columns and save the file as a CSV.

   ![image-20260109-080242.png](/cms_trial/assets/ef1efe64-3080-4a6e-b3be-9c8248180b41.png)
5. In Jira admin settings, go to **System** > **Import and Export**, then click **External System Import**.
6. **Important:** Switch to the old experience (the new experience does not allow updating existing tickets).

   ![image-20260108-100508.png](/cms_trial/assets/843f7b6c-03f7-4edd-8592-c6111b669c75.png)
7. Follow the steps in the wizard and select the appropriate Jira space.
8. Map CSV fields to Jira fields. Make sure to map the work item key. If a work item with the same key already exists in Jira, it will be updated.

   ![image-20260108-100808.png](/cms_trial/assets/91e1057d-c637-4453-a338-732357bf5d65.png)
9. Run the import.
10. In **BigPicture** > **Priorities module**, add the newly created custom fields to the template. Do not change the formula or remove any metrics at this stage.   
    IMPORTANT Do NOT delete metrics until you verify that the custom fields have the same values as the Priorities module’s metrics.
11. Only after confirming that all custom fields contain the correct values can you modify the formula.

    ![image-20260108-101350.png](/cms_trial/assets/0090edb7-b4fb-4833-8c17-166b1b932296.png)

## Use Jira custom fields with historical values (new navigation)

Click to expand the guide

If you decide to use Jira custom fields in prioritization formulas as a replacement for existing prioritization metrics, you may want to preserve the historical values in those custom fields. This can be achieved by exporting data from the Priorities module and importing it into Jira using Jira’s import functionality.

1. Create custom fields in Jira that mirror the priority metrics (e.g., an Ease custom field).

   ![image-20260108-095051.png](/cms_trial/assets/02690aea-4ca6-491f-abe0-4d4eb1de28be.png)
2. Add these custom fields to the appropriate Jira screens for the relevant spaces so they are visible on all work item types.
3. In **BigPicture** > **Priorities module**, click the **Export table in CSV** button.

   ![Screenshot of the Export button in the Priorities module.](/cms_trial/assets/3ea44bb4-7dcf-4136-9dae-1de1aa6ea25f.png)
4. In the exported file, split the work item key and summary into separate columns and save the file as a CSV.

   ![image-20260109-080242.png](/cms_trial/assets/ef1efe64-3080-4a6e-b3be-9c8248180b41.png)
5. In Jira admin settings, go to **System** > **Import and Export**, then click **External System Import**.
6. **Important:** Switch to the old experience (the new experience does not allow updating existing tickets).

   ![image-20260108-100508.png](/cms_trial/assets/843f7b6c-03f7-4edd-8592-c6111b669c75.png)
7. Follow the steps in the wizard and select the appropriate Jira space.
8. Map CSV fields to Jira fields. Make sure to map the work item key. If a work item with the same key already exists in Jira, it will be updated.

   ![image-20260108-100808.png](/cms_trial/assets/91e1057d-c637-4453-a338-732357bf5d65.png)
9. Run the import.
10. In **BigPicture** > **Priorities module**, add the newly created custom fields to the template. Do not change the formula or remove any metrics at this stage.   
    IMPORTANT Do NOT delete metrics until you verify that the custom fields have the same values as the Priorities module’s metrics.
11. Only after confirming that all custom fields contain the correct values can you modify the formula.

    ![Screenshot of historical values in the Priorities module.](/cms_trial/assets/c3029e79-c0f8-4364-9d4d-ab7af0ecbe3a.png)