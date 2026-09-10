# Import/Export

By using the Import/Export functions, you can utilize SLAs that exist in another service space. This prevents you from losing important data while transitioning from one instance to another.

![Time to SLA Import and Export page with import export controls](/cms_trial/assets/c4cef02a-8c42-4446-afc2-94f18ddc86f3.png)

## Import

With the **Import** function, you can:

- Restore from backup
- Import configurations from another instance
- Apply changes from your test environment

To import your SLAs, follow these steps:

1. Go to **Import/Export** on the sidebar and click **Import**.
2. Upload the file you want to import, select its source (Cloud or On-Prem), and specify where it’s coming from.

   ![Time to SLA Import and Export wizard showing file selection](/cms_trial/assets/fb416217-dd18-49b2-b995-4e52b4928366.png)
3. Select how you’d like to merge imported configurations with existing ones.

   ![Time to SLA Import and Export wizard showing import options](/cms_trial/assets/27cd66aa-92ec-4882-b108-dd884f8ea49b.png)
4. Select and match the components you want to import.
5. On the **Summary** screen, check for mistakes in your selections. After you make sure everything is as it should be, click **Import**.
6. Once the process is done, it will look like this and the imported configurations will appear on your related screens:

   ![Time to SLA Import and Export wizard showing mapping options](/cms_trial/assets/e2db8936-0cd7-449e-bfc8-c911d43ccf34.png)

The way the SLAs are set up in the source space will affect the performance of the import.

## Export

With the **Export** function, you can:

- Take a backup of your SLA configuration and calendars
- Copy your configurations and calendars from this instance to another Jira instance
- Transfer changes from a test environment to your product environment

To export your SLAs, follow these steps:

1. Go to **Import/Export** on the sidebar and click **Export**.
2. Select the SLAs you want to export.

   ![Time to SLA Import and Export progress screen](/cms_trial/assets/10012b02-ed1c-4b82-8636-a86afd4f8086.png)
3. Select the calendars you want to export and click the chevron icon to transfer them to the other side.

   ![Time to SLA Import and Export results screen with completed status](/cms_trial/assets/2b42d441-1b82-4876-b857-7698c46d0653.png)
4. Check your selections in the *Export* section, and click **Export** once you think they are ready.
5. Your export will be downloaded automatically in `.json` format.