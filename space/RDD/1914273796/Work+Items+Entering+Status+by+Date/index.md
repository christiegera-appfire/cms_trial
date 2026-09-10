# Work Items Entering Status by Date

## Overview

Track the number of issues entering specific statuses or group statuses over selected dates. Identify trends, bottlenecks, or workflow shifts.

- **Workflow Insights:** See when issues enter key statuses or group statuses to track trends over time.
- **Bottleneck Detection:** Identify slowdowns or drop-offs in issue flow.
- **Flexible Visualization:** Choose different type of charts like multi line charts, stacked/grouped bar chars or stacked area charts.

![Examples of different chart configurations](/cms_trial/assets/f67a337c-43d9-4bd6-95e7-34f885b54fc3.png)

---

## Configure your transitions

Configure status groups to track when issues **first or last enter selected statuses**. The report counts issues by date based on their first transition or last transition into each group, this option can be configured by status or status group. You can add multiple transition statuses per **Status group**.

![Dashboard Hub transition fields for work items entering status by date](/cms_trial/assets/0bf5fb75-c03f-4630-810a-c40b2d990808.png)

Jira statuses can be entered multiple times during an issue's lifecycle. Use the first-last toggle to calculate time based on either the first or last transition into a status.

![Dashboard Hub Work Items Entering Status by Date status selector](/cms_trial/assets/733f0a4d-c3cc-4142-b0db-30aa66f881e3.png)

## Report type

### Report by date

Track the number of issues entering specific statuses over selected dates (day, week, month, quarter, year). This allows teams to track and analyze status durations across the whole portfolio, seeing its evolution over time, plotted against a timeline.

Select any of the four **view types**: Multi-Line chart, Stacked Area chart, Stacked Bar chart, or Grouped. Each segment (for example, each line in the multi-line) represents one status transition.

![Dashboard Hub Work Items Entering Status by Date issue report](/cms_trial/assets/dc8b2338-7ecb-4f48-ab4f-4da53e3efe1b.png)

### Switch Between Chart and Table View

A switch in the gadget header lets users choose to display the chart or a table with the underlying data. [table data icon] to switch to the chart view and [chart table icon] to switch to the table view.

This option is available in the gadget’s main view when the dashboard is in **view mode**.

![Dashboard Hub Work Items Entering Status by Date date report](/cms_trial/assets/62069e5c-dbfc-4de1-a654-36385e37fd8b.png)

---

## Configuration

### History to retrieve

To improve the precision of your report, you can trim the issue history. Thus, you can filter out historical data within a specified timeframe. This involves choosing both a "before" and "after" date to exclude data, ensuring that the time in status of relevant issues during that period is excluded from calculations.

![Dashboard Hub trim dates setting](/cms_trial/assets/ba395746-0198-4e9c-853a-a1b8220e5de5.png)

### Format

You can display the time in five different formats: days, weeks, months, quarters, and years.

### Show statistics

You can select which statistics to display in the report. All available statistics are shown by default.

![Dashboard Hub work items entering status statistics table](/cms_trial/assets/c9ada03b-e27d-4d58-86ca-48fa229f8c1d.png)

## Customizations

### Custom colors

The color picker lets you to select the color for each segment or value using hexadecimal code, RGB, or our predefined 24-color palette (selected for optimal contrast and tone).

![Charts extra settings color configuration panel](/cms_trial/assets/f2522c8e-cd57-4f45-87cb-6301868180d9.png)

### Hide segments

When you click the **Eye** icon, the corresponding segment is hidden (or shown) in the chart.

### Reorder segments

Just drag and drop any segment or value from the six dots on the left side of the segments and move it upwards or downwards to the correct place, and the chart will be updated accordingly.

---

## Dashboards

This gadget is not included in any pre-defined dashboard.