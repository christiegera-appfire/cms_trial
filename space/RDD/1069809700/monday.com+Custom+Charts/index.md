# monday.com Custom Charts

## Overview

You can visualize all of your team’s work creating and customizing tables and charts from [monday.com](http://monday.com) data, and enhance data analysis and reporting using filters.

---

## View type: table

View the results of your filtered items as a table from the selected board and workspace, where you can select which columns are displayed.

![monday.com Custom Charts table](/cms_trial/assets/8fa63495-6ccc-4b1f-8e2d-c9c278389b1e.png)

### Group results

`Group results by selected columns`

If you are familiar with the `GROUP BY` statement in SQL, you’ll quickly find interesting uses to group the results of your filter. If you select to group the results by the previously selected columns, **the result rows will be split into groups based on their values**. Only one row will be displayed for each group, so be careful because this implies constraints on the columns.

![monday.com group chart results](/cms_trial/assets/67653e9b-0efa-458d-9ed7-142817a9a857.png)

The grouping of columns is combined with aggregations.

### Aggregations

Aggregations are also common in the SQL domain. These functions get the values of grouped rows as the input of that function to return a calculated value. This gadget currently supports five functions:

- **Count**: Returns the number of rows in that group.
- **Sum**: Returns the addition of the sequence of the numbers of the group.
- **Min**: Returns the smallest value of the range of values of the group.
- **Max**: Returns the largest value of the range of values of the group.
- **Mean**: Adds the values of the grouped rows and divides the result by the number of rows being averaged.

![a screenshot of the configuration of Dashboard Hub for monday.com](/cms_trial/assets/c038cb42-aea4-40e3-ba96-1bdb2bbd0c91.png)

---

Keep in mind that in [monday.com](http://monday.com) table views, filtered data (items and columns) can still be accessed through the shared views by technically savvy users, although it is *hidden.*

However, in [monday.com](http://monday.com) Custom Charts filtered out data is not shared in public views! For more information, see this [comparison table](https://appfire.atlassian.net/wiki/x/AoBkQ).

## View type: 1D pivot table

The 1D pivot table view shows a perspective on your data in a single dimension (1D) of your dataset.

Users can select a specific attribute or field to act as the basis for organizing and aggregating data. The resulting table presents a clear representation of the chosen dimension, summarizing key metrics and allowing for efficient analysis.

![monday.com 1D pivot table](/cms_trial/assets/ff147823-3db9-40ea-a853-c9e937d24f84.png)

The elements of the 1D pivot table are as follows:

- **Rows (dimensions)**:The selected row represents the monday.com field used for grouping.
- **Aggregation**:Aggregations get the values of grouped rows as the input of that function to return a calculated value. See [aggregations](/cms_trial/space/RDD/1069809700/monday.com+Custom+Charts/).
- **Field**:The displayed field values depend on the chosen aggregation type.

## View type: 2D pivot table

The 2D pivot table view introduces a second dimension (2D) to expand on the capabilities of the 1D Pivot Table. Select two different fields (rows and columns) to cross-tabulate data to analyze data across both dimensions simultaneously.

![2d pivot table](/cms_trial/assets/0f07d327-fc78-4581-8840-9cea7838fdcf.png)

The elements of the 2D pivot table are as follows:

- **Rows (dimensions)**:The selected row represents the Jira field that is used for grouping.
- **Columns (dimensions)**:The selected column represents the Jira field that is used for grouping.
- **Aggregation**:Aggregations get the values of grouped rows as the input of that function to return a calculated value. See [aggregations](/cms_trial/space/RDD/1069809700/monday.com+Custom+Charts/).
- **Field**:The displayed field values depend on the chosen aggregation type.

## View type: chart

Remember that:

**Chart by**: Indicates the dimension or the x-axis values (horizontal axis).

**Group by**: The second dimension for grouped, stacked, or multi charts.

**Aggregation + field**: The aggregation you want to apply to the **count**, **sum**, **max**, **min**, **mean** fields(see the [aggregations](/cms_trial/space/RDD/1069809700/monday.com+Custom+Charts/) section) to plot the values in the chart (y-axis or vertical axis).

### Line chart

A line chart represents the results of your filter as a series of data points connected by a straight line. It’s common to visualize trends over periods or dates in the x-axis.

![line chart](/cms_trial/assets/f042f224-383a-413a-a63e-5f9fcdbe7faa.png)

### Multi line chart

This chart is a line chart with more than one line, which is useful when we need to compare data in a time series or trends.

![line chart](/cms_trial/assets/28380f5b-f289-4c41-a2ad-d01372b1fabf.png)

### Tile chart

This visual representation presents the information in a set of tiles. You can display the result of your filter and apply aggregations. For example, you can display the number of requests of each request type of your monday.com instance, or display the sum of all the original estimates of the assigned items, by assignee.

![tile chart](/cms_trial/assets/904cc1a0-ddb7-4e3c-b3bf-9c7fcdc589c1.png)

### Bar chart

A bar chart represents the results of your filter as a series of rectangular bars with the height proportional to the represented values. It’s useful to compare results of different types or categories.

For example, **Chart by** **type** **count***,* and **field** **status** would display a chart where each status would display the number of assigned items:

![bar chart](/cms_trial/assets/e5166afe-a1a7-4209-b8ea-0ef979df95ec.png)

### Grouped bar chart

We can perform more complex comparisons of the information returned by our filter by grouping by specific fields. In the previous example, we could add a **Group by status**, and we’d see the number of items by assignee grouped by the item status:

![group by status](/cms_trial/assets/f81f1b29-5676-4b87-8d6b-3f06e872f57b.png)

### Stacked bar chart

Similar to the grouped bar chart, but in this case, the combined results of the groups are on top of each other. The height is the combined result, making it not appropriate for cases with negative values.

![stacked bar chart](/cms_trial/assets/cb311223-d370-469a-81ba-a801a0ef4261.png)

### Show trend line for bar charts and stacked bar charts

A toggle switch lets you easily show or hide the trend line for bar charts and stacked bar charts, providing a quick way to visualize data trends and gain deeper insights into chart patterns.

#### Customizing the Trend Line Color

Users can select a custom color for the trend line.

Trend lines are only available for bar charts and stacked bar charts.

![Dashboard Hub monday.com custom chart configuration screen](/cms_trial/assets/957405fa-b5a6-4923-9807-5ed9fcfaa791.png)

### Pie chart

A pie chart is a visualization of your data in a circular graph, where each slice indicates the quantity of the result of your filter. When a pie chart has several sections or slices, it’s difficult to compare one with another. To overcome this inconvenience, the pie chart comes with a table indicating the values of each slice and the % it represents.

![pie chart](/cms_trial/assets/4c3b8aae-7590-4228-a97b-3c4284e89ffa.png)

### Multi pie chart

This chart adds one more dimension to the pie chart, so users can compare sets of information within a single chart. Just add a new field to the **Group By** to display the values in the second ring.

![monday.com multi pie chart](/cms_trial/assets/3dcb47b8-ce1f-4ac8-9204-8599363ff671.png)

### Area chart

An area chart is a visualization that represents the results of your filter as a series of data points connected by a straight line and filled with color beneath it, which can help emphasize the magnitude of the values being represented. An area chart is often used to show trends over time or categories, as well as to compare multiple series of data.

![area chart](/cms_trial/assets/5e1fab95-7285-4ddd-b52e-0bdbfa1dcb92.png)

### Stacked area chart

A stacked area chart is a variation of the area chart where the areas are stacked on top of each other instead of being overlaid. Each stack represents a category or a group, and the height of the stack represents the total value of the group. It's useful for showing the relative contribution of each group to the total, as well as for tracking changes in the total over time. However, stacked area charts may not be suitable for displaying negative values, as they can become difficult to read.

![stacked area chart](/cms_trial/assets/836022b4-2b5b-469f-a370-57ab3e488057.png)

### Switch Between Chart and Table View

A switch in the gadget header lets users choose to display the chart or a table with the underlying data.

This option is available in the gadget’s main view when the dashboard is not in **edit mode**.

![Dashboard Hub monday.com Custom Charts configuration row](/cms_trial/assets/72077e54-bfae-494a-b7e5-6b75e549c05b.png)

---

## Customizations

### Hide segments

Not all the results are needed when communicating information in a chart, sometimes because one of those values or segments distorts the results or deviates the attention.

Clicking on the [eye icon] eye icon, the corresponding segment is hidden (or shown) in the chart:

![pie chart with customizations ](/cms_trial/assets/da170a8d-d4db-4239-9017-311ae5527da9.png)

### Reorder segments

In the same line of hiding segments or customizing the colors of our charts, rearranging the position of the existing segments or values reinforces the way we transmit the information with our charts.

Just drag and drop any segment or value from the six dots on the left side of the segments and move it upwards or downwards to the correct place, and the chart will be updated accordingly.

![pie chart reordered segments ](/cms_trial/assets/2dc76722-5ce5-4a2f-9d33-818b454935ad.jpg)

### Limit the Number of Segments on the X-Axis

You can limit the number of segments displayed on the X-axis in charts.

- Set a maximum number of segments in the input field.
- The chart displays only the highest-value segments in the dataset.
- Any remaining segments are grouped into a synthetic segment labeled **Others**.

This helps simplify visualizations by focusing on the most relevant data.

![Dashboard Hub monday.com custom chart example with configured data](/cms_trial/assets/8f1f9982-1799-4445-a032-96b098d04c07.png)

### Normalized charts

Normalized charts adjust data for fair comparisons, ensuring that segments are proportionate relative to 100%, facilitating accurate insights across varying scales or sizes.

![chart view types](/cms_trial/assets/9b614ec0-a264-4bfe-b5b7-84ee4fca984f.png)

### Cumulative charts

Cumulative charts show progress over time, revealing trends and cumulative totals effortlessly, illustrating the cumulative impact of actions or metrics over a period.

## Configuration

Name your gadget meaningfully so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- **Datasource** where the source monday.com instance is installed.
- **Workspace, board and filters** to narrow the list of items. The gadget will automatically reload upon selecting a filter. Remember that the gadget returns the query results, which are not fixed and could change over time.
- **View Type** parameter to indicate the visual representation of the filter results in a table, line chart, tile chart, pie chart, bar chart, area chart, etc.
- **Chart by** parameter (just for charts) to select the x-axis value, in other words, what you see in the horizontal axis. These values or concepts are indicated in the chart legend.
- **Aggregation** parameter (just for charts) to indicate what type of aggregation you want to apply to the **field** parameter (count, sum, max, min, mean). Check the [aggregations](/cms_trial/space/RDD/1069809700/monday.com+Custom+Charts/) section.
- **Fields** parameter (just for charts) to select the y-axis values (vertical axis), think of what you want to count (or any other aggregation), and plot in the chart.
- **Columns** (just for the table view) that will appear in the list to display the search results. At least one column has to be present. Drag and drop to reorder the columns.
- **Group results by selected columns** (just for the table view) in case you want to group the results of the query by the previously selected **columns**. The resulting rows the result rows will be split intogroups, based on their values. Check the [group results](/cms_trial/space/RDD/1069809700/monday.com+Custom+Charts/) section.
- The **aggregations** (just for the table view) in case you need to perform calculations (count, sum, max, min, mean) over the results. Check the [aggregations](/cms_trial/space/RDD/1069809700/monday.com+Custom+Charts/) section.
- Indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option saves you from configuring each gadget individually.

## Dashboards

This gadget is not included in any pre-defined dashboard.