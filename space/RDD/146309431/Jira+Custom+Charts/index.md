# Jira Custom Charts

This page provides an example of how to use the Jira Custom Charts gadget in Dashboard Hub to build customized reports based on JQL.

## Overview

The needs of Jira users vary across organizations. Users often need to run a JQL query in Jira to find relevant information. Custom Charts is a flexible, highly customizable gadget that displays the result of a JQL query or an existing [filter](https://support.atlassian.com/jira-software-cloud/docs/save-your-search-as-a-filter/), as a table or a chart. You can select a predefined filter or a custom JQL, then indicate how you want to display the results, the columns you want to display in your report and perform grouping and aggregations.

### Example

To list all the work items in the Teams in Space project (`project = “TIS”`) in To Do (`status = "TO DO"`), sorted by CreationDate in descending order (`ORDER BY created DESC`) use the following JQL query:

`project = "TIS" AND status = "TO DO" ORDER BY created DESC`

[Get started with JQL](https://www.atlassian.com/software/jira/guides/expand-jira/jql) or have a look at the [Advanced Search](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/) to master queries in Jira.

## How to use the Jira Custom Charts gadget

This section explains how to add and configure the gadget.

**To add the gadget to a dashboard:**

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the *Search* bar in the *Add gadget* page to find the required gadget.
3. Select the **Jira Custom Charts** gadget. The *Add Gadgets* page displays.

   ![The Jira Custom Charts configuration page in Dashboard Hub.](/cms_trial/assets/09b51b4a-f9b5-4eac-ba4f-9373a410a806.png)
4. (*optional*) The name field is completed by default. You can edit the name to make it more meaningful to your team.
5. Select the datasource from where you want to retrieve work item statistics. To learn more about datasource types, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).
6. Use the filter options to limit the data you analyze; select a Jira filter or enter a JQL query, then click **Load**. If you don’t add any, the gadget will request all the content in the source instance; this might cause performance issues. We recommend adding at least one clause, for example, to list all the issues of the project Teams in Space use the clause `project = "TIS”`. Remember that the gadget returns query results that are not fixed and can change over time.
7. Select a view type to best visualize data. You can select any of the following visual formats to represent the resulting data of the JQL query: table, line chart, tile chart, pie chart, bar chart, grouped bar chart, stacked bar chart, or multi-line chart.
8. (*optional*) Depending on the view type you select, choose how to group the data. See the options in the next section for more information.
9. Click **Add** to save the configuration and add the gadget to your dashboard.

---

## View types and groupings

### Table

View the results of your JQL query as a table, where you can select which columns are displayed. If you select a table view type, there are additional options to consider:

- The **columns** that will appear in the list to display the search results. At least one column has to be present. Drag to reorder the columns.
- **Group results by selected columns** in case you want to group the results of the query by the previously selected **columns**. The resulting rows are split intogroups, based on their values. Check the [group results](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) section.
- The **aggregations** in case you need to perform calculations -Count, sum, max, min, mean- over the results. Check the [aggregations](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) section.

![Example Jira Custom Chart displaying data in a table.](/cms_trial/assets/dbbf77b7-da52-4a32-bce6-fda485785b56.png)

### Calculated columns

In this field, you find columns that are not natively available in Jira as .

**Customer Portal**

This column provides a link for the referred issue to the corresponding Customer Portal link for users of the Customer Portal. This is useful when you share a dashboard with customers. See [Manage access to the Jira Service Management Customer Portal](/cms_trial/space/RDD/146309699/Manage+access+to+the+Jira+Service+Management+Customer+Portal/)) for more information.

Instead of

```text
https://acme.atlassian.net/browse/ISM-12
```

this column would link to

```text
https://acme.atlassian.net/servicedesk/customer/portal/1/ISM-12
```

### Group results

`Group results by selected columns`: If you choose to group the results by the previously selected columns,the result rows will be split into groups, based on their values. Therefore, only one row will be displayed for each group.

For example, if we filter the previous list of issues by the column **Status**, the results will show only two rows, one for the status *To Do* and the other for the status *Done*.

![Example configuration of a Jira Custom Chart with results grouped by column.](/cms_trial/assets/2202f451-f299-484b-beb8-061a6fb0fb41.png)

If we select these three columns: **Status, Assignee,** and **Project**, the resulting list will display three rows, like in the following image:

![Dashboard Hub Jira Custom Charts configuration screen](/cms_trial/assets/7379f447-c0aa-400b-ad12-6e370ba5210d.png)

The grouping of columns is typically combined with aggregations.

### Aggregations

Aggregations are also common in the SQL domain. These functions get the values of grouped rows as input to that function to return a calculated value. This gadget currently supports five functions:

- **Count**.: Returns the number of rows in that group.
- **Sum**: Returns the sum of the sequence of numbers in the group.
- **Min**: Returns the smallest value of the range of values of the group.
- **Max**: Returns the largest value of the range of values of the group.
- **Mean**: The arithmetic mean sums the values of the grouped rows and divides the result by the number of rows being averaged.
- **Show values** (only in Tile charts): Displays the raw values of the returned range.

For example, if you want to calculate the mean of the story points:

![Dashboard Hub Jira Custom Charts chart type options](/cms_trial/assets/654db4df-5aab-48e7-a4cb-0b02a20bcff0.png)![Dashboard Hub Jira Custom Charts gadget preview](/cms_trial/assets/ecfb6b4c-bbd4-46bb-b45f-cbb83c853f48.png)

---

## 1D Pivot Table

The 1D Pivot Table view provides a single-dimensional (1D) perspective on your data. In other words, one level of grouping is expressed when you select the value for the Rows field.

You can select a specific attribute or field to act as the basis for organizing and aggregating data. The resulting table presents a clear representation of the chosen dimension, summarizing key metrics and allowing for efficient analysis.

![Dashboard Hub Jira Custom Charts dynamic filter configuration](/cms_trial/assets/e1db692a-050d-4b23-86fb-edc6f8222fb1.png)

The elements of the 1D pivot table are as follows:

- **Rows (dimensions) :**The selected row represents the Jira field used for grouping.
- **Aggregation:** Aggregations get the values of grouped rows as the input of that function to return a calculated value. Check the [aggregations](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) section.
- **Field:** The displayed field values depend on the chosen aggregation type.

## View type: 2D Pivot table

The 2D Pivot Table view introduces a second dimension (2D) to expand on the capabilities of the 1D Pivot Table. Select 2 different (rows and columns) to cross-tabulate data to analyze data across both dimensions simultaneously.

![Dashboard Hub Jira Custom Charts chart preview setting](/cms_trial/assets/38eb2b0f-1b37-4df2-848d-72ad31ff3170.png)

The elements of the 2D pivot table are as follows:

- **Rows (dimensions):** The selected row represents the Jira field that is used for grouping.
- **Columns (dimensions):** The selected column represents the Jira field that is used for grouping.
- **Aggregation:** Aggregations get the values of grouped rows as the input of that function to return a calculated value. Check the [aggregations](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) section.
- **Field:** The displayed field values depend on the chosen aggregation type.

## Chart

If you use a chart view type, there are additional options to consider.

- The **Chart by** parameter to select the x-axis value, in other words, what you see in the horizontal axis. These values or concepts are indicated in the chart legend.
- The **Type** parameter to indicate what type of aggregation you want to apply to the **field** parameter: Count, sum, max, min, or mean. *Show values* is only available for Tile charts. Check the [aggregations](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) section.
- The **Field** parameter to select the y-axis values (vertical axis), think of what you want to count (or any other aggregation), and plot in the chart.

**Chart by**: Indicates the dimension or the x-axis values (horizontal axis), also referred to as the series, or in layman’s terms, the concepts we see in the legend of the chart.

**Group by**: The second dimension for grouped, stacked or multi charts.

**Aggregation + field**: The aggregation you want to apply to the **field**: count, sum, max, min, mean (see the [aggregations](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) section), to plot the values in the chart (y-axis or vertical axis).

### Line chart

A line chart represents the results of your JQL query as a series of data points connected by a straight line. It’s common to visualize trends over periods or dates in the x-axis.

![Dashboard Hub Jira Custom Charts table configuration](/cms_trial/assets/9ab4c039-69c1-424f-b2af-af59e7c15c01.png)

### Multi line chart

This chart is a line chart with more than one line, which is useful when we need to compare data in a time series or trends.

![Dashboard Hub Jira Custom Charts 2D pivot table](/cms_trial/assets/92adde72-3790-43c9-b959-caa5c717623c.png)

### Tile chart

This visual representation presents the information in a set of tiles. You can display the result of your JQL and apply aggregations. For example, you can display the number of requests of each request type of your Jira Service Management support desk, or display the sum of all the original estimates of the assigned issues, by assignee.

![Dashboard Hub Jira Custom Charts chart preview](/cms_trial/assets/f5c6a93e-94fa-4176-bfbd-2f9c002f2605.png)![Dashboard Hub Jira tile chart showing values](/cms_trial/assets/bb40a2f2-faa2-4a7d-9d34-a6e9d0d9f643.png)

### Bar chart

A bar chart represents the results of your JQL query as a series of rectangular bars with the height proportional to the represented values. It’s useful to compare results of different types or categories.

For example, **Chart by** *assignee*, **type** *count,* and **field** *issues* would display a chart where each assignee would display the number of assigned issues:

![Dashboard Hub Jira Custom Charts chart layout options](/cms_trial/assets/08c0b45b-2d72-43af-8b56-43604e3170bd.png)![Dashboard Hub Jira Custom Charts chart preview](/cms_trial/assets/a090dffe-6710-4b23-be3f-57a9d79fa4b2.png)

### Grouped bar chart

We can perform more complex comparisons of the information returned by our JQL query by grouping by specific . In the previous example, we could add a **Group by** *status*, and we’d see the number of issues by assignee grouped by the issue status:

![Dashboard Hub Jira Custom Charts stacked horizontal bar chart](/cms_trial/assets/a24a5612-c2b5-439b-b7f8-37bc7fbec1ac.png)

So for each category, in our case, the **Chart by** *Assignee*, there are two or more colored bars, whose labels can be seen at the top of the chart.

### Stacked bar chart

Similar to the grouped bar chart, but in this case, the combined results of the groups are on top of each other. Thus, the height is the combined result, making it not appropriate for cases with negative values.

![Dashboard Hub Jira Custom Charts multi pie chart](/cms_trial/assets/0e702880-8848-45d1-abc8-bb8d49454585.png)

### Pie chart

A pie chart is a visualization of your data in a circular graph, where each slice indicates the quantity of the result of your JQL. When a pie chart has several sections or slices, it’s difficult to compare one with another. To overcome this inconvenience, the pie chart comes with a table indicating the values of each slice and the % it represents.

When the field selected in “Chart by” has a date format e.g., Created, a new selector appears to allow grouping by day, week, month, quarter, or year, making the results easier to understand and communicate.

![Dashboard Hub Jira Custom Charts chart preview](/cms_trial/assets/711224b5-ae46-4075-9f19-a763bb503131.jpg)

### Multi pie chart

This chart adds one more dimension to the pie chart, so users can compare sets of information within a single chart. Just add a new field to the “Group By” to display the values in the second ring.

![Dashboard Hub Jira multipie custom chart example](/cms_trial/assets/4c76b0f7-02ed-4754-8c0c-95cee046f05b.png)

### Area chart

An area chart is a visualization that represents the results of your JQL query as a series of data points connected by a straight line and filled with a colored area beneath it, which can help emphasize the magnitude of the values being represented. An area chart is often used to show trends over time or categories, as well as to compare multiple series of data.

![Dashboard Hub Jira Custom Charts chart preview](/cms_trial/assets/3cd821b9-9f9f-4ac4-bf72-170c51c5910b.png)

### Stacked area chart

A stacked area chart is a variation of the area chart in which the areas are stacked on top of each other rather than overlaid. Each stack represents a category or group, and its height indicates the group's total value. It's useful for showing each group's relative contribution to the total, as well as for tracking changes in the total over time. However, stacked area charts may not be suitable for displaying negative values, as they can become difficult to read.

![Dashboard Hub Jira Custom Charts chart preview](/cms_trial/assets/440e3edb-ca75-4f16-bc02-f08daedc79a5.png)![Dashboard Hub Jira Custom Charts chart preview](/cms_trial/assets/5eba1017-0c36-46bd-acc4-971810825872.png)

---

## Supported field types

### Jira built-in system fields

Expand to view full list of built-in fields 

|  |  |
| --- | --- |
| **Jira Built-in field** | **Supported in Custom Charts** |
| Assignee | ✅ |
| Attachment | ❌ |
| Comment | ❌ |
| Components | ✅ |
| Created | ✅ |
| Creator | ✅ |
| Description | ✅ |
| Due date | ✅ |
| Environment | ✅ |
| Fix versions | ✅ |
| Images | ❌ |
| Issue Type | ✅ |
| Key | ✅ |
| Labels | ✅ |
| Last Viewed | ❌ |
| Linked Issues | ❌ |
| Log Work | ❌ |
| Original estimate | ✅ |
| Parent | ❌ |
| Priority | ✅ |
| Progress | ❌ |
| Project | ✅ |
| Remaining Estimate | ✅ |
| Reporter | ✅ |
| Resolution | ✅ |
| Resolved | ✅ |
| Restrict to | ❌ |
| Security Level | ✅ |
| Status | ✅ |
| Status Category | ✅ |
| Status Category Changed | ✅ |
| Sub-tasks | ❌ |
| Summary | ✅ |
| Time Spent | ✅ |
| Time tracking | ❌ |
| Updated | ✅ |
| Votes | ✅ |
| Watchers | ✅ |
| Work Ratio | ❌ |
| Σ Original Estimate | ❌ |
| Σ Progress | ❌ |
| Σ Remaining Estimate | ❌ |
| Σ Time Spent | ❌ |

### Custom field types

The list of available custom fields is pulled directly from your connected Jira instance. Only supported custom field types appear in the selection menu.

Expand to view supported custom field types

## Work item panel

| **Custom field type** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| checkbox | ✅ | ✅ |
| date | ✅ | ✅ |
| dropdown | ✅ | ✅ |
| formula | ✅ | ✅ |
| labels | ✅ | ✅ |
| number | ✅ | ✅ |
| paragraph | ✅ | ✅ |
| people multi | ✅ | ✅ |
| people single | ✅ | ✅ |
| short text | ✅ | ✅ |
| timestamp | ✅ | ✅ |
| url | ✅ | ✅ |

## Standard

| **Custom field type** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| checkboxes | ✅ | ✅ |
| Date Picker | ✅ | ✅ |
| Date Time Picker | ✅ | ✅ |
| Labels | ✅ | ✅ |
| Number Field | ✅ | ✅ |
| Paragraph | ✅ | ✅ |
| Radio Buttons | ✅ | ✅ |
| Select List (cascading) | ❌ | ✅ (has `option-with-child` ) |
| Select List (multiple choices) | ✅ | ✅ |
| Select List (single choice) | ✅ | ✅ |
| Short text (plain text only) | ✅ | ✅ |
| URL Field | ✅ | ✅ |
| User Picker (single user) | ✅ | ✅ |

## Other

| **Custom field** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| Assets objects | ❌ | ✅ (has `cmdb-object-field` renderer) |
| Date of First Response | ✅ | ✅ |
| Days since last comment | ❌ | ✅ (Dashboard Hub calculated field) |
| Domain of Assignee | ❌ | ❌ |
| Domain of Reporter | ❌ | ✅ (Dashboard Hub calculated field) |
| Global Rank | ❌ | ❌ |
| Group Picker (multiple groups) | ❌ | ✅ (has `group` rendered) |
| Group Picker (single group) | ❌ | ✅ (has `group` rendered) |
| Last commented by a User Flag | ❌ | ❌ |
| Last public comment date | ❌ | ❌ |
| Message Custom Field (for edit) | ✅ | ✅ |
| Message Custom Filed (for view) | ✅ | ✅ |
| Number of attachments | ❌ | ❌ |
| Number of comments | ❌ | ❌ |
| Participants of an issue | ✅ | ✅ |
| Project Picker (single project) | ✅ | ✅ |
| Text Field (read only) | ✅ | ✅ |
| Time in Status | ❌ | ❌ |
| User Picker (multiple users) | ✅ | ✅ |
| User Property Field (< 255 characters) | ✅ | ✅ |
| Username of last updater or commenter | ✅ | ✅ |
| Version Picker (multiple versions) | ✅ | ✅ |
| Version Picker (single version) | ✅ | ✅ |

## Jira Product Discovery

| **Custom field type** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| Checkbox | ✅ | ✅ |
| Connection | ❌ | ❌ |
| Custom formula | ✅ | ✅ |
| Rating | ✅ | ✅ |
| Reactions | ✅ | ✅ |
| Slider | ✅ | ✅ |
| Time interval | ✅ | ✅ |

## Atlassian (built-in)

| **Field name** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| Sprint (Atlassian) | ✅ | ✅ |

## Customizations

### Custom colors

Colors have the power to communicate meaning, provoke emotions, and highlight information. Within our organizations and teams, it’s common to associate concepts with specific colors, making it easier and quicker to communicate ideas and information.

Whenever you select a chart, you’ll be able to select the color of each specific segment or value of it:

![Dashboard Hub Jira Custom Charts chart preview](/cms_trial/assets/ecc577e5-79b3-40c3-bc46-408e945f17b6.png)

The color picker allows the selection of color either by hexadecimal code, RGB, or our pre-defined 24-color palette (selected based on the right contrasts and tones).

### Limit segments

**Maximum segments**: To better manage the representation of data in charts, set the maximum number of segments to display.

![Dashboard Hub Limit segments](/cms_trial/assets/9867dfd2-3d4e-4785-ad3c-29fa8f428bf7.png)

These segments are ordered by their respective quantities, and once the “Maximum segments” limit is reached, **the remaining data is grouped under an “Others” segment**. This ensures that the chart remains clear and focused on the most relevant data.

### Hide segments

Not all the results are needed when communicating information in a chart, sometimes because one of those values or segments distorts the results or diverts attention.

Clicking on the 👁 eye icon, the corresponding segment is hidden (or shown) in the chart:

![Dashboard Hub Jira Custom Charts chart preview](/cms_trial/assets/20423b5a-5be2-4780-ae9f-60dba97f83e3.png)

### Reorder segments

In the same line of hiding segments or customizing the colors of our charts, rearranging the position of the existing segments or values reinforces the way we transmit the information with our charts.

Just drag and drop any segment or value from the six dots on the left side of the segments and move it upwards or downwards to the correct place, and the chart will be updated accordingly.

![Dashboard Hub Jira Custom Charts chart preview](/cms_trial/assets/9522f4c5-10f0-43db-a9db-17d635bb705a.jpg)

### Normalized charts

Normalized charts adjust data for fair comparisons, ensuring that segments are proportionate relative to 100%, facilitating accurate insights across varying scales or sizes.

![Dashboard Hub Jira normalized stacked bar chart with statistics](/cms_trial/assets/dff933a2-43f7-4989-80d9-6a06d0d4c2a6.png)

### Cumulative charts

Cumulative charts show progress over time, revealing trends and cumulative totals effortlessly, illustrating the cumulative impact of actions or metrics over a period.

### Linear trend line

Bar charts, stacked bar charts and stacked area charts allow adding a linear trend line. It provides insights into the overall trend of the data, helping to identify patterns based on the trajectory of their metrics over time or across segments.

![Dashboard Hub Jira custom chart trend line example](/cms_trial/assets/bfa1c185-d369-4f82-afd0-f29a9ef73b0e.png)

## Dashboards

This gadget is not included in any pre-defined dashboard.