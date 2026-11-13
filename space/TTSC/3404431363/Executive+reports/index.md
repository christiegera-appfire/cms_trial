# Executive reports

Executive reports provide a high-level overview of SLA performance using completed SLA data. They help teams review SLA trends, compare performance across groups, and share clear SLA insights with stakeholders.

Use Executive reports when you need to monitor SLA performance over time without reviewing each work item individually. Refer to the [use case](/cms_trial/space/TTSC/3426714512/I+want+to+review+cross-project+SLA+compliance+data+without+manual+spreadsheet+exports/) to learn more.

Executive reports include **completed SLA cycles** only.

## Before you begin

- To create Executive reports, you must have the [**SLA Reports**](/cms_trial/space/TTSC/36110655/Manage+permissions/) [permission](/cms_trial/space/TTSC/36110655/Manage+permissions/) in Time to SLA. Executive reports can be shared with Viewers and Editors. Report owners always have full access.
- Executive reports have generation limits to help maintain report performance. You can create up to 10 Executive reports per Jira instance. Reports created from the [Details view](/cms_trial/space/TTSC/3404431363/Executive+reports/) aren’t included in this limit.
- Executive report updates are tracked in audit logs. Use the [audit log page](/cms_trial/space/TTSC/36110718/Audit+logs/) to review changes made to Executive reports.

Watch the video below to learn how to create an Executive report and get a quick overview.

## Create an Executive report

1. Go to **Reports**.
2. Click **Executive**. The *Create new report* screen opens.

   ![Executive reports New report creation page.](/cms_trial/assets/6a19c2ae-cdb5-4bb9-8392-c99d478829f3.png)
3. Enter a descriptive name. This helps you identify the report later on the **Executive reports** page.
4. Select which date the report should use when calculating the period. The selected date field and date range determine which completed SLA cycles are included in the report. Available options include:

   - **Work item created**
   - **Work item resolution date**
   - **SLA start date**
   - **SLA end date**
5. Select the SLAs you want to include. You can select one or more SLAs, or use **All SLAs** to include all available SLAs.
6. Use filters to limit the data included in the report. For example, you can use spaces, priorities, work types, assignees, and more.

   To add a filter:

   1. Select **Add filter**.
   2. Choose the field you want to filter by.
   3. Select the values you want to include.

Executive reports support both system fields and custom fields as filters. For number and date fields, the filter uses a range. Enter values in the **From** and **To** fields to include results that fall within that range.

![Filter by dialog showing available report filters.](/cms_trial/assets/f7d2d2aa-704c-4a7d-abb0-fe2dc0c63e06.png)

Filter logic works as follows:

- Different filters are connected with **AND**.
- Values within the same filter are connected with **OR**.

For example, if you filter by **Priority = High or Highest** and **Assignee = Alex**, the report includes work items where the priority is either High or Highest, and the assignee is Alex.

1. Use **Group by** to organize report data into meaningful sections. The available options are issue priority, issue type, assignee, reporter, component, labels, and Jira field.   
   For example, you can group a report by space, add multiple issue priorities, and then add an assignee for a deeper breakdown. You can add up to three groups.  
   To add a group:

   - Select a field from the **Group by** dropdown.
   - Select **Group +**.
   - Repeat the steps to add more groups.
2. Click the **Generate** button.

Time to SLA starts creating the Executive report. While the report is being generated, you’ll see a message confirming that the report is in progress. You can stay on the page or leave it. Leaving the page does not cancel report generation.

Report generation may take a few moments, depending on the report scope. Larger reports may take longer to generate, especially when they include a wide timeframe, multiple SLAs, several filters or groups, or a large amount of completed SLA data.

After the report is generated, it appears on the **Executive reports** page. For more information about the report, see [Executive report table overview](/cms_trial/space/TTSC/3423928348/Executive+report+table+overview/).

![Executive reports list of SLA Breaches per app - Last 30 days.](/cms_trial/assets/e3d45757-cadc-4364-acb5-c5eaaf177522.png)

### Share an Executive report

You can share an Executive report with other users and assign **Viewer** or **Editor** access.

- **Viewers** can open the report, review aggregated report data, and open detailed drill-downs.
- **Editors** have Viewer access and can also edit the report configuration, generate the report again, manage saved Detailed Reports, update sharing settings, and delete the report.
- The report owner always retains full access.

To share a report:

1. Open the Executive report.
2. Select **Share**.
3. Add the users you want to give access to.
4. Add them as **Viewers** or **Editors**.
5. Configure whether saved Detailed Reports are shared with everyone who can access the Executive report.
6. Save your changes.

If you select **Keep saved detailed reports private**, each saved Detailed Report is available only to its creator and the Executive report owner. Otherwise, saved Detailed Reports are shared with everyone who can access the parent Executive report.

**Important:** Executive report access can expose work item data to users who don't otherwise have permission to view those work items in Jira. Review the report contents before sharing it.