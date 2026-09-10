# Durations report

The **SLA Durations report** helps you analyze SLA duration data using bar or line charts and a detailed summary table. Configure the report to compare SLA durations over time and choose how the data is displayed.

## How to create a Durations report

1. Navigate to **SLA Reports**.
2. From the *Generate new report*, click **Duration**.

   ![image-20260713-233240.png](/cms_trial/assets/b1cf7b94-b5c7-4556-abe6-a13cfc02fa3e.png)

### Report configuration options

1. Filter your work items:

   - Use **Project**, **JQL**, or **Issue Filters** to refine the work items included in your report. When you select one, a new dropdown appears.
   - If you select **Issue Filters**, you can also apply Jira's built-in parameters or a previously saved work item filter.
   - Leave the filter type blank to include all work items.

1. Select the SLAs:

   - Choose the SLAs you want to include in the report. The list displays all SLAs, both enabled and disabled.
   - Leave the field blank to include all SLAs.
2. Click **Chart Interval** to set a time period for your report. Options include **Custom**, **Last Month**, **Past One Month**, and more.
3. Use the **+ More** button to tailor the report to your needs.

For example, you can choose to display only the SLAs that are in the critical zone, or to show only the SLAs with an end date within a specific date range. You can add as many parameters as you'd like.

![TTS- More filter selection-20260713-232748.gif](/cms_trial/assets/a372461e-d3ea-4268-b488-b7ff80d14f6f.gif)

### Chart configuration options

1. Choose your **chart type**: **Line** or **Bar**.
2. Determine what to display on the **X-Axis** (**SLA Start Time, SLA End Time, SLA Deadline).**
3. Select the unit for your **Y-Axis** (**Days**, **Hours**, **Minutes**, **Seconds**).
4. Select whether the data will be displayed **Monthly** or **Weekly**.
5. Click **Generate** to create your report.

To generate the report automatically on a schedule, click the chevron next to **Generate**, then select **Schedule periodic report**. Configure the schedule, recipients, and other subscription settings, then save the subscription.

Once generated, scheduled reports are available on the Periodic Reports page. Recipients receive an email notification when the report is ready.

Scheduled Durations reports contain the report’s summary-table data. The chart itself is not included.

## Examples

### Line chart

![Time to SLA Durations report line chart showing SLA elapsed time over monthly periods](/cms_trial/assets/08f29923-39c7-4102-8e5d-b7afef1afbff.png)

### Bar chart

![image-20260713-233744.png](/cms_trial/assets/148d881a-4a38-47b6-a0e7-2c5236ac0a42.png)

### SLA Deadline visualization

![Time to SLA Durations report chart grouped by SLA Deadline](/cms_trial/assets/c0754d1f-7086-423f-8279-ee0a139e7d90.png)

### Impact of Y-Axis format on chart visualization

Below are two examples showing how the Y-Axis format impacts the visualization:

![Time to SLA Durations bar chart with Y-Axis formatted in Days](/cms_trial/assets/f2bd8c1e-4c62-4d45-8e41-66ed24067028.png)

![Time to SLA Durations bar chart with Y-Axis formatted in Hours](/cms_trial/assets/7e3937fc-0578-477d-9f51-4689a3a08250.png)

The only difference between the two screenshots is that the duration format of the Y-Axis was changed from `Days` to `Hours`. Notice how a single change in the SLA value format alters the chart's presentation.

## Export the report

Using the button on the right-hand side, you can download your report as an XLSX or PDF file. Once you click the button, the download will start automatically.