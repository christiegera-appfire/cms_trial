# Transition Time from Status to Status

## Overview

The Transition Time from Status to Status gadget lets you measure and optimize the time it takes for work items to move between statuses. You can analyze transition time per work item and within date ranges.

- **Workflow Efficiency**: Understand how long it takes for work items to transition between key statuses to optimize team processes and reduce delays.
- **Bottleneck Detection**: Identify stages in your workflow where work items get stuck or take too long to progress between statuses.
- **Flexible Filtering**: Generate reports by date, by work item, and by time intervals, for example, daily, weekly, or monthly.

![A dashboard displaying the Transition Time from Status to Status gadget through different report and view types.](/cms_trial/assets/1cb1d6f8-aec2-440a-8197-223ec22e27a6.jpg)

---

## How to add the gadget

This section explains how to add and configure the gadget. For more details on the configuration options, refer to the Configuration sections below.

**To add the gadget to a dashboard:**

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the **Search** bar in the *Add gadget* page to find the required gadget.
3. Select the **Transition Time from Status to Status** gadget.
4. **Name** (*optional*): The name field is completed by default. You can edit the name to make it more meaningful to your team.
5. **Datasource**: Select the datasource from where you want to retrieve work item statistics. To learn more about datasource types, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).
6. Use the filter options to limit the data you analyze. Select a Jira filter or enter a JQL query.
7. Select a date range for the work items you want to track. For example, Last 4 months, Weekly, or define a custom date range.
8. Select the transitions that you want to measure.
9. Select the report type and view type that you want to use to visualize the data.
10. Select how to group the results of the date range. You can group by Day, Week, Month, Quarter, or Year.
11. Select the statistics that you want to display in the gadget.
12. When you are ready, click **Save**. You can use the preview on the configuration page to refine the configuration before saving.

## Configuration options

### Configure your transitions

Select which status transitions to include in the report. You can include any number of From/To transition statuses with pauses in specific statuses. The transitions can be either the first transition to a status or the last transition to a status. You can also configure the gadget to use **Direct transitions only**. This option counts only transitions that move directly between the selected statuses.

![The tranisiton configuration options in the gadget confiration page.](/cms_trial/assets/ce625276-cc81-45c5-9f9e-79fecbe014c3.png)

**Pause count on**

Use this option to exclude specific statuses from time aggregation. For example, in Jira, for certain statuses, such as Waiting for Customer, you might not want to contribute to the total time calculation. Configuring the pause count ensures that time spent in these statuses is excluded from the overall transition time.

You can **add multiple statuses to the pause count** for a specific transition.

Jira statuses can be entered multiple times during an issue's lifecycle. Use the first-last toggle to calculate time based on either the first or last transition into a status.

![contentId-1898709009](/cms_trial/assets/3164b579-cece-48f7-b7f6-1f5d5adcb97c.png)

## Report types

### Report by issue

Dive deep into individual work items to understand their progression through the lifecycle and identify areas for improvement. Select any number of status transitions and their pauses to display a list of work items with their transition times.

![The Transition Time from Status to Status gadget rendered in a table view.](/cms_trial/assets/a84c91d0-afcd-4d24-a5fa-914e300a7d01.png)

### Report by date

Track how long work items have stayed in each status over a specific period of time (day, week, month, quarter, year). This allows teams to track and analyze status durations across the entire portfolio, visualizing their evolution over time on a timeline.

Select any of the three **view types**: Multi-Line chart, Stacked Area chart, or Stacked Bar chart. Each segment, for example, each line in the multi-line chart, represents one status transition.

![The Transition Time from Status to Status gadget rendered as bar chart by date report.](/cms_trial/assets/bb8999fb-bed7-4f81-9cbc-02508de271de.png)

### Switch between chart and table view

A selector in the gadget header lets users choose to display the chart or a table with the underlying data. Select Chart ([table data icon]) to switch to the chart view or Table ([chart table icon]) to switch to the table view.

This option is available in the gadget’s main view when the dashboard is in **view mode**.

![transition_time_date_data.png](/cms_trial/assets/c3e8a3f2-ce12-4744-9945-c4c0c540c6fa.png)

---

## Configuration

### History to retrieve

To enhance the precision of your report, you can **trim the history of your issues**. Thus, you can filter out historical data within a specified timeframe. This involves choosing both a "before" and "after" date to exclude data, ensuring that the time in status of relevant issues during that period are disregarded in calculations.

![Time_in_status_trim_dates.png](/cms_trial/assets/a01e0656-4f32-4a88-b16a-c69b93d1dbaf.png)

### Format

You can display the time in three different formats: hours, days, or time-centric (w for weeks, d for days, h for hours, **m** for minutes).

### Measure

You can decide how to calculate the time in each status:

- **Mean**: The average of all the time spent in each status transition.
- **Sum**: The total sum of all the time spent in each status transition.
- **Max**: The maximum time spent in a status transition.
- **Min**: The minimum time spent in a status transition.

### Show statistics

You can select which statistics to display in the report. All available statistics are shown by default.

![The Show statistics option with four statistics selected.](/cms_trial/assets/13f9385c-6310-4e4a-87fd-6a92704e9e09.png)

## Customizations

### Custom colors

The color picker lets you choose the color for each segment or value using hexadecimal code, RGB, or our predefined 24-color palette (selected for optimal contrast and tone).

![The color selector in the gadget configuration.](/cms_trial/assets/36f58bbd-1a9a-43ef-8397-5472282bcd70.png)

### Hide segments

When you click the **Eye** icon, the corresponding segment is hidden (or shown) in the chart.

### Reorder segments

Drag any segment or value from the six dots on the left side of the segments and move it upwards or downwards to the correct place, and the chart will be updated accordingly.

---

## Dashboards

This gadget is not included in any pre-defined dashboard.