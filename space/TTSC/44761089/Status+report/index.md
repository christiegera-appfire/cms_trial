# Status report

The **SLA Status report** gives you a visual overview of your SLA statuses using a pie chart and a detailed summary table. Configure the report to see how your SLAs are distributed across statuses such as **Met**, **Exceeded**, **In Progress**, and **Inactive**.

## How to generate a Status report

1. In the Time to SLA top menu, click **Reports**.
2. From the *Generate new report*, click **Status**.

   ![image-20260714-134833.png](/cms_trial/assets/4c226ceb-136e-42e6-858f-616b9307bf01.png)

### Report configuration options

1. Filter your work items:

   - Use **Project**, **JQL**, or **Issue Filters** to refine the work items included in your report. When you select one, a new dropdown appears.
   - If you select **Issue Filters**, you can also apply Jira's built-in parameters or a previously saved work item filter.
   - Leave the filter type blank to include all work items.

When filtering your report, you **cannot** use `slaFunctions` in JQL. Instead, use the **+** **More** button to refine your SLA selection.

1. Select the SLAs:

   - Choose the SLAs you want to include in the report. The list displays all SLAs, both enabled and disabled.
   - Leave the field blank to include all SLAs.
2. Click **Chart Interval** to set a time period for your report. You can filter the chart data based on SLA Start Time, SLA End Time, or SLA Deadline within an interval you choose.
3. Use the **+ More** button to tailor the report to your needs.

For example, you can choose to display only the SLAs that are in the critical zone, or to show only the SLAs with an end date within a specific date range. You can add as many parameters as you'd like.

![Screenshot 2026-07-14 at 15.49.17.png](/cms_trial/assets/e71febf5-6212-4de8-97e4-4fe85883374e.png)

1. Choose a time format for the report.
2. Use the **SLA Columns** and **Issue Columns** dropdowns to add or remove columns from your report.

### Chart configuration options

1. Select how you want to group the pie chart:

   - **None**
   - **SLA and Goals –** If you select this one, a **Goal Details** dropdown appears. Here, you can enable or disable options like **Priority**, **JQL**, **Goal Type**, and **Value**.
   - **Assignee**
   - **Priority**

This section can be changed after generating the report. Your selected grouping is also used when you save or schedule the report.

![Time to SLA Status report grouping options with SLA and Goals, Assignee, and Priority](/cms_trial/assets/eb290df4-cc79-4223-84b4-a059cdd3ccce.gif)

1. Click **Generate** to create your report.

To generate the report automatically on a schedule, click the chevron next to **Generate**, then select **Schedule periodic report**. Configure the schedule, recipients, and other subscription settings, then save the subscription.

Scheduled reports are available from the [**Periodic reports**](/cms_trial/space/TTSC/36012105/Periodic+reports/) [page](/cms_trial/space/TTSC/36012105/Periodic+reports/). When a report is ready, the configured recipients receive an email notification.

The scheduled report contains the data from the report’s summary table. The pie chart itself is not included.

You can click **Save filter as** to save the configuration, which lets you reuse it in other reports. Once saved, the report filter will appear on the side panel.

## Understanding report results

![Time to SLA Status report pie chart with Exceeded, Met, In Progress, and Inactive segments](/cms_trial/assets/13ddc594-79f3-4e87-be0f-20ef3f307f9b.png)

The Status pie chart provides a clear and intuitive representation of your SLA statuses, with each status color-coded for easy identification:

- Red – SLAs that are **EXCEEDED**.
- Green – SLAs that are **MET**.
- Blue – SLAs that are **IN** **PROGRESS**.
- Grey – SLAs that are **INACTIVE**.

Below the pie chart, a **summary table** displays detailed SLA information. Refer to the following example:

![image-20260714-135033.png](/cms_trial/assets/b6767991-7405-447c-9b92-5368d8467b75.png)

### Interactive features

You can click a pie chart slice to get detailed issue information for that SLA status. Double-click a slice to automatically scroll to the corresponding section in the summary table for more in-depth data. Check out the image below to see how the pie chart changes after you click `MET`:

![Time to SLA Status report pie chart filtered to show Met SLAs only](/cms_trial/assets/3b93e9ea-1fd3-434b-a444-4b848a249949.png)

Click any legend label to hide or display specific SLA statuses in the chart. Removing a status dynamically updates the pie chart, as shown here:

![Time to SLA pie chart with Breached status hidden from legend](/cms_trial/assets/81b074b8-2faa-4683-bd27-38ce7163b5df.gif)

## Export the report

Using the button on the right-hand side, you can download your report as an XLSX or PDF file. Once you click the button, the download will start automatically.