# Create a Workflow Intelligence report

Create a Workflow Intelligence report from scratch or start with a template for a common analysis scenario. Before generating the report, you can define which work items to include, how to group their duration data, and whether to include SLA details.

## Create the report

1. Go to **Time to SLA** > **Reports**. The report catalogue opens.
2. Select **Workflow Intelligence**.

   - You can also go to **Reports** > **Workflow Intelligence** from the side menu.
3. On the **New workflow intelligence report** page, choose how you want to start:

   ![Screenshot 2026-09-07 at 17.45.05.png](/cms_trial/assets/ff365fab-3dc1-4b05-ac70-9661e3d6b54e.png)
   - To create a report from scratch, click **Create** under **Blank report**.
   - To start with a predefined configuration, find a template and click **Use template**. You can click **Details** to review the template before using it.

The following templates are available:

| **Template** | **Description** |
| --- | --- |
| **Assignee by status** | View each team member’s time, broken down by workflow status. |
| **Status by assignee** | View time spent in each status, broken down by team member. |
| **Status over time** | Track status duration trends across custom time periods. |
| **Time period by status** | Analyze workflow status distribution grouped by time frame. |
| **Time in assignee** | Track working time and SLA performance per team member. |
| **Time in status** | Measure time spent in each status alongside SLA outcomes. |

## Configure the report

![Screenshot 2026-09-07 at 17.45.42.png](/cms_trial/assets/e065f2a0-7cfa-4f46-bfc8-0f47784f9178.png)

1. Define which work items to include in the report:

   - From Date field, select **Work item created** or Work item resolution date. The selected field determines which date the report uses when applying the *Date range*.
   - Use **Date range** to select the period you want to analyze.
   - Select the **Calendar** used to calculate durations. The selected calendar determines how durations are calculated. Only time within the calendar’s configured working hours is counted; non-working hours, weekends, and holidays are excluded where configured.
   - Under **Filter by**, select a **Filter type**, choose one or more **Spaces**, and use **Filter +** to add more conditions.
2. Under **Columns**, select the **Main column**. The values from this field become the primary groups in the report.

   - To break each group down further, select **Break the main column down by a sub column**, then choose a **Sub column**.

For example, select **Assignee** as the main column and **Status** as the sub-column to see how long each work item spent in each status while assigned to a particular person.

1. Use **Merge columns** to group several values from the main or sub-column under one name. The report totals their tracked time in a single column, while values you don’t include continue to appear separately. To merge values:

   ![Screenshot 2026-09-07 at 17.56.55.png](/cms_trial/assets/67c08f88-ac81-4a80-ad12-75451da9d25f.png)
   - Click **Merge columns** under the main or sub-column.
   - Click **Add column**.
   - Enter a **Column name**.
   - From the **Values** dropdown, select the values you want to group.
   - To create another merged column, click **Add column** again and repeat the steps.
   - Click **Apply**.

For example, you could group several priority values into an **Urgent** column or combine multiple completed statuses into a **Done** column.

The selected values and their durations appear together under the new column in the generated report. Values that aren’t added to a merged column are reported on their own.

1. Use **Work item columns** to add fields that provide more information about each work item. **Issue** and **Summary** are always included in the report. You can add fields such as **Assignee**, **Status**, or other Jira and custom fields.

Work item columns provide context about each item. They don’t change how the report’s duration data is grouped.

1. To include SLA information, click **Display SLA detail columns per work item**. Then use **Include SLAs** to select specific SLAs or include all SLAs.

Including SLAs adds SLA indicators to the report and makes SLA insights and detailed SLA breakdowns available after the report is generated.

1. Click **Generate**.

To clear the current configuration and start again, click **Reset**.