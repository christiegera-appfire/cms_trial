# Use Jira custom fields with historical values

If you decide to use Jira custom fields in prioritization formulas as a replacement for existing prioritization metrics, you may want to preserve the historical values in those custom fields. This can be achieved by exporting data from Foxly and importing it into Jira using Jira’s import functionality.

1. Create custom fields in Jira that mirror the priority metrics (e.g., an Ease custom field).

   ![Foxly related Jira custom field details page for Ease metric](/cms_trial/assets/14dedb74-8266-45d1-adfd-5fc21b39f237.png)
2. Add these custom fields to the appropriate Jira screens for the relevant spaces so they are visible on all work item types.
3. In **Foxly**, click the **Export table in CSV** button.

   ![Foxly Priorities table with Export table in CSV button highlighted](/cms_trial/assets/447f9927-2c9d-4040-873c-b5b6a3d0e70f.png)
4. In the exported file, split the work item key and summary into separate columns and save the file as a CSV.

   ![Foxly exported CSV with work item key and summary split into columns](/cms_trial/assets/3b0cd8d8-a9d1-48ac-b23e-a08f1e8547c1.png)
5. In Jira admin settings, go to **System** > **Import and Export**, then click **External System Import**.
6. **Important:** Switch to the old experience (the new experience does not allow updating existing tickets).

   ![Jira External System Import page with Switch to old experience link](/cms_trial/assets/d3491c7d-a4af-4f49-b8d9-f55170581522.png)
7. Follow the steps in the wizard and select the appropriate Jira space.
8. Map CSV fields to Jira fields. Make sure to map the work item key. If a work item with the same key already exists in Jira, it will be updated.

   ![Jira CSV import field mapping page with work item key mapped](/cms_trial/assets/aa6c47fd-c880-4feb-a457-a29b93b9570c.png)
9. Run the import.
10. In **Foxly**, add the newly created custom fields to the template. Do not change the formula or remove any metrics at this stage.   
    IMPORTANT Do NOT delete metrics until you verify that the custom fields have the same values as Foxly’s metrics.
11. Only after confirming that all custom fields contain the correct values can you modify the formula.

    ![Foxly formula editor with custom fields added to template](/cms_trial/assets/921a7658-62dd-49c4-94f0-222ef9714465.png)