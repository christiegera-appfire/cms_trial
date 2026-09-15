# Manage Workflow Intelligence reports

You can save a Workflow Intelligence report to return to the same point-in-time results later. Saved reports are kept for one year and can be organized into personal folders for easier access.

![image-20260915-002449.png](/cms_trial/assets/a95983e7-d9e8-4638-9f03-e71cdf55b3fd.png)

## 1. Customize the report display

You can change how durations appear in the report and add color thresholds that make longer or shorter durations easier to identify.

1. Click the **Display** button (1) in the upper-right corner.
2. Under **Duration format**, choose how duration values are displayed.

   ![Screenshot 2026-09-08 at 12.01.05.png](/cms_trial/assets/10ae8376-cce1-402e-a869-13ef7fcb9b2b.png)
3. To apply colors based on duration, check **Cell coloring**.
4. Under *Cells*, define the ranges used for individual duration cells. Enter a label and duration limit for each range.

   For example, you can configure the report to show:

   - Durations up to 4 hours as **Achieved**.
   - Durations from 4 hours to 1 day as **Warning**.
   - Durations longer than 1 day as **Failed**.
5. Under **Total**, define separate ranges for total duration values.
6. Select **Add coloring** to create another range, or use the delete icon to remove one.
7. Select **Apply**.

Enter duration limits using values such as `4h`, `1d`, or `1d 4h 30m`. Select **Cancel** to close the dialog without applying your changes.

## 2. Duplicate a report

Click the **Duplicate** button (2) to open the report configuration with the current settings. Update the date range, filters, columns, merged values, work item fields, or included SLAs, then click **Generate**.

This generates a new report with the updated configuration. It doesn’t update or replace the existing report.

![Screenshot 2026-09-15 at 02.21.17.png](/cms_trial/assets/cfdb6188-562c-4ed9-8f1b-cb48ac0474d7.png)

## 3. Export a report

Click the **Export** button (3) to download the generated report results. The exported `.CSV` data reflects the scope and column configuration used to generate the report.

## Save and share a report

You can save a Workflow Intelligence report to keep a snapshot of the report data and share it with others.

1. After generating a report, click **Save report** next to the *Unsaved* label. The *Save report* dialog appears.
2. Enter a **Report name**.

   ![Screenshot 2026-09-08 at 12.06.39.png](/cms_trial/assets/82fa5c12-e8da-4e48-89aa-da16cab1625f.png)
3. Optional: Under **Viewers**, select the users or groups who can view the saved report.
4. Optional: Under **Editors**, select the users or groups who can edit the report.
5. Click **Save**.

The saved report appears on the **Workflow Intelligence reports** page.

**Saved reports are point-in-time snapshots.** They preserve the report data from when the report was generated and are kept for one year.

## View saved reports

Go to **Reports** > **Workflow Intelligence** to view your saved reports.

![Screenshot 2026-09-15 at 02.19.09.png](/cms_trial/assets/098c77f4-2a30-43c3-ac4b-de4a8b3c534f.png)

The list includes each report’s:

- Name
- Columns
- Status
- Owner
- Role
- Request Date

Click a report name to open its results.

## Organize reports into folders

Use folders to group related reports, such as reports for a particular team, project, or type of analysis.

1. Go to **Reports** > **Workflow Intelligence**.
2. Open the **More actions** menu beside a report.

   ![Screenshot 2026-09-15 at 02.29.36.png](/cms_trial/assets/46043cc9-12b2-4d68-89a1-76f8fdcb6dc4.png)
3. Click **Move to folder**.
4. Create a new folder or select an existing one.

Reports that haven’t been added to a folder appear under **Other reports**.

Use the controls beside a folder to add reports, rename the folder, or delete it.

Folders are personal to each user. Changes to your folders don’t affect how other users organize their reports.