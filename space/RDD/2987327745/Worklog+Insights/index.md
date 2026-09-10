# Worklog Insights

## Overview

A Jira worklog records the time spent on an individual work item. This can help with planning, tracking progress, billing, and managing capacity, and priorities. However, consolidating and visualizing the data for reporting in Jira is challenging.

The Worklog Insights gadget helps you visualize who worked on what and when. It pulls worklog data from Jira so you can filter time entries for a single sprint, an entire space, a single user, or across multiple teams. Switch between a detailed table, a pie chart showing how time was distributed, or a bar chart tracking effort over time. Click into any chart segment to jump directly to the relevant issues in Jira.

![Worklog Insights gadget displayed in Table view.](/cms_trial/assets/c4e91b43-037b-4ebf-bdd3-1306639a1ae4.png)

## Example use cases

- **Project Leads**: Display a table of work logged per work item so you can audit time spent against specific tasks.
- **Resource Managers:** Visualize work logged by user over time (Bar/Line chart) to identify burnout or underutilization.
- **Program Managers**: Aggregate worklogs at the Project or Initiative level to report on high-level roadmap progress.
- **General Users**: Use JQL and date filters to dynamically narrow your time-tracking view to specific sprints or teams.
- **Migrations from Dataplane Reports**: The Work Logged By Date and User Work Logged By Date are automatically mapped to the Worklog Insights gadget in Dashboard Hub.

## How to configure the gadget

This section explains how to add and configure the gadget.

**To add the gadget to a dashboard:**

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. On the *Add gadget* page, search for and select **Worklog Insights**.
3. (*optional*) The name field is completed by default. You can edit the name to make it more meaningful to your team.
4. Select the datasource from which you want to retrieve work item statistics. To learn more about datasource types, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).
5. (*optional*) Use the filter options to limit the work items used to generate the statistics. You can select a Jira filter or enter a JQL query. See *How to filter the data* below for examples.
6. Select a date range for the worklogs you want to analyze: Last 4 months or Weekly. See *How to filter the data* below for examples.
7. Select how to group the results of the date range. You can group by Day, Week, Month, Quarter, or Year.
8. Select a view type to best visualize data. Options include table view, pie chart, and bar or line charts.
9. (*optional*) Depending on the view type you select, choose how to group the data. See the filtering options in the next section for more information.
10. Click **Add** to save the configuration and add the gadget to your dashboard.

You can resize or reposition any gadget on a dashboard to prioritize specific data and improve the layout.

## How to filter the data

The filter options let you focus only on the data you want to see for more granular insights and better performance.

### JQL

The JQL filter works the same way as in Jira. Enter a valid JQL query or select a saved filter to limit the work items used for the worklog report.

**Example queries:**

- `project = "Mobile App" AND issuetype = Story`
- `sprint in openSprints() AND assignee in membersOf("backend-team")`
- `labels = "Q2-Roadmap" AND status != Done`

### Date range

Select a preset or use **Custom** to select a date range to include in the report.

- **Group dates by**: Select an option to apply to the resulting work items. For example, if your date range is **This Quarter**, you might select **Group by week**.

Wide date ranges, for example, an entire year, across large spaces, can increase load times. If you experience slowness, narrow the date range or use a JQL filter first.

### Segments

Some view types include options to segment the data into smaller, meaningful groups so you can spot patterns and make better decisions. For example, in a Grouped bar chart, you can compare work logged across different spaces, see how time is spread across work types, or break down contributions by user.

- **Select projects**: If you use a chart to visualize the data, you can limit the work items to be analyzed to specific projects.
- **Work logged by**: If you use a chart to visualize the data, you can limit the work items to be analyzed to specific users.

## Migrations from Dataplane Reports

If you are migrating from Dataplane to Dashboard Hub, the Worklog Insights gadget is designed to consolidate three of your most-used legacy reports into a single, flexible report.

Refer to the table below to see how to replicate your existing Dataplane reports within this new gadget:

|  |  |
| --- | --- |
| **Legacy Dataplane Report** | **Dashboard Hub Configuration** |
| User Work Logged by Date | Use the Date range option to group data |
| Work Logged by Date | Set **Value Mode** to **Sum** and select your numeric field, for example, *Story Points* or *Original Estimate*. |