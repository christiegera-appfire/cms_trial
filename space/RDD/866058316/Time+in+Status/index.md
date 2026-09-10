# Time in Status

## Overview

Use the Time in Status gadget to identify bottlenecks and gain insights into the time issues spend in different statuses. Analyze status time per issue, per status, per assignee, or over a specific date range.

- **Bottleneck Identification**: Easily spot bottlenecks in your projects by analyzing how long statuses remain active in your Jira issues.
- **Performance Evaluation**: Evaluate team performance by seeing who's effectively moving issues through various statuses.
- **Issue Analysis**: Dive deep into individual issues to understand how much time each issue has spent in different statuses.
- **Cross-Project Reports**: Generate comprehensive reports across multiple projects to track time spent on each status, assignee, etc.

![Dashboard Hub preview time in status by date](/cms_trial/assets/566cf428-4d4d-4d6b-9ad4-c7a1fa238f66.png)

![Dashboard Hub preview time in status per status](/cms_trial/assets/7281958a-d62f-4aff-8a1e-9f0130803afd.png)

---

## Select statuses

You can select which statuses to include in the report. You can view individual statuses or all statuses in a specific category by selecting TO DO, IN PROGRESS, or DONE sections. Follow the following interactive demo to learn how.

<https://demo.arcade.software/JpOWTaoWEX495XpDUGQy?embed&show_copy_link=true>

### Status groups

You can create your own status groups and merge multiple statuses into a single category, simplifying and enhancing your reporting capabilities.

Some aggregations might not make sense if you combine individual statuses with groups that include some of those included statuses, for example, a group called Already done containing Failed and Completed used together with the status Failed.

![Dashboard Hub create status groups time in status](/cms_trial/assets/8cdf787a-57eb-4088-8cb7-c84f6d70837c.png)

![Dashboard Hub status groups time in status](/cms_trial/assets/0579d6e6-ad9e-41a7-8942-6e0f997f01ea.png)

![Dashboard Hub status groups time in status chart](/cms_trial/assets/a5606c17-ca7d-4a6d-8f23-ed3b58072cb2.png)

## Report type

### Report by status

Analyze time distribution across statuses to identify workflow bottlenecks and optimize efficiency.

Select either of the two view types: Pie chart or 1D Pivot Table

![Dashboard Hub time in status report by status pie](/cms_trial/assets/a6e59a5a-1719-42d8-9832-c3cf168fd8ab.png)

![Dashboard Hub time in status report by status](/cms_trial/assets/69edf5fc-cbcf-4476-9ed7-055408c472a5.png)

### Report by assignee

Evaluate how different team members are progressing through tasks and how much time they spend in each status.

Select any of the three view types: 2D Pivot Table, Stacked Bar Chart, Grouped Bar Chart

![Dashboard Hub Time in Status report preview](/cms_trial/assets/f419684c-ed10-4114-acb3-1a14fa3b2b2e.png)

![Dashboard Hub Time in Status report preview](/cms_trial/assets/b96837a8-676c-403f-af8f-58dfccca9afe.png)

![Dashboard Hub Time in Status report preview](/cms_trial/assets/e55a5111-541b-4016-a169-7118cb66c8e3.png)

### Report by issue

Dive deep into individual issues to understand their status progression through their lifecycle and identify areas for improvement.

### Report by date

Track how long issues have stayed in each status for a specific period of time (day, week, month, quarter, year). This allows teams to track and analyze status durations across the whole portfolio, seeing its evolution over time, plotted against a timeline.

For example, last week:

- An issue TIS-1 was 2 hours in the **To Do** status, 3 hours in the **In Progress** status,
- and TIS-2 was 5 hours in the **To Do** status and 8 hours in the **In Progress** status.

Then, the 'Report by date' report shows for **Last Week** 7 hours in the **To Do** status and 11 hours in the **In Progress** status.

Select any of the four **view types**: Multi Line chart, Stacked Area chart, Grouped Bar chart, Stacked Bar chart. Each segment (e.g., each line in the multi-line) represents one status.

![Dashboard Hub Time in Status gadget example](/cms_trial/assets/57c87789-c0e9-4260-87d0-c46d471aeee0.png)

### Switch between Chart and Table view

A switch in the gadget header lets you choose to display the chart or a table with the underlying data.

This option is available in the gadget’s main view when the dashboard is not in Edit mode.

![Dashboard Hub Time in Status configuration row](/cms_trial/assets/5de753d7-b347-4361-ad73-26ee618b98fb.png)

---

## Configuration

### Issue history

To improve the precision of your report, you can trim the history of your issues to filter out historical data within a specified timeframe. Select a before and after date to exclude data, ensuring that the time in status of relevant issues during that period is excluded from calculations.

![Dashboard Hub trim dates setting](/cms_trial/assets/58b8f662-8a96-48f0-a4aa-928e4858d219.png)

### Format

You can display the time in three different formats: hours, days, or time-centric (w for weeks, d for days, h for hours, m for minutes).

### Measure

You can decide how to calculate the time in each status:

- **Mean**: The average of all the time spent in each status.
- **Sum**: The total sum of all the time spent in each status.
- **Max**: The maximum time spent in a status.
- **Min**: The minimum time spent in a status.

**Time in Status** is cumulative per status, and the total time is averaged across statuses.

**Lead time** counts the time from the moment a piece of work is in a *To Do* status until the moment that piece of work reaches a *Done* status. However, **Time in Status** doesn’t stop counting when that work reaches the *Done* status.

*Unassigned* is included as *None* in reports.

### Show statistics

You can select which statistics to display in the report. All available statistics are shown by default.

![Available statistics for the Time in Status gadget.](/cms_trial/assets/8cb71149-9836-4f7a-b017-e0898a9827b2.png)

## Customizations

### Custom colors

The color picker allows you to select the color of each specific segment or value either by hexadecimal code, RGB, or our pre-defined 24-color palette (selected based on the right contrasts and tones).

![Dashboard Hub chart color picker](/cms_trial/assets/abe06fd9-f0c5-4584-a7bd-0f44bd2e5a8f.png)

### Hide segments

Click the **Eye** icon to show or hide the corresponding segment in the chart.

### Reorder segments

You can drag any segment or value from the six dots on the left side of the segments and move it up or down to the correct place; the chart will be updated accordingly.

---

## Dashboards

This gadget is not included in any pre-defined dashboard.