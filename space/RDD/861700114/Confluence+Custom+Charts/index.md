# Confluence Custom Charts

## Overview

The Confluence Custom Charts gadget presents queried results in customizable tables and charts, allowing users to select from a range of visualization options, including pivot tables, bar charts, pie charts, line charts, and more.

![Dashboard Hub confluence custom charts](/cms_trial/assets/f85a7c31-b684-4e7a-a133-c4ac174cc0b8.jpg)

Whether tracking project progress, analyzing content trends, or monitoring user contributions, this gadget offers a powerful solution for visualizing Confluence page data with precision and clarity.

### Search Confluence content

Queries to search for your Confluence content rely on the Confluence Query Language ([CQL](https://developer.atlassian.com/server/confluence/advanced-searching-using-cql/)) to formulate searches based on criteria such as page properties, labels, creators, and modification dates, facilitating the retrieval of relevant page data.

For example, to list all the pages (type = page) in the space *Teams in Space* (space = TIS) with the label space\_mission (label = space\_mission) use the following CQL query:

`space = TIS and type=page and label = space_mission`.

Refer to the [CQL documentation](https://developer.atlassian.com/server/confluence/advanced-searching-using-cql/) to learn more about using CQL queries in Confluence.

If you aren’t familiar with CQL, you can use the set of filters we provide to retrieve your Confluence data: Title, space, creator, type, and updated date.

![Dashboard Hub Confluence Custom Charts filter configuration](/cms_trial/assets/1621f196-7e91-4e30-a643-fa536f63900c.png)

## View type: Table

View the results of your CQL query as a table, where you can select which columns are displayed.

![Dashboard Hub confluence custom charts table](/cms_trial/assets/4e7f217a-1e1f-49cc-8671-be5845252274.jpg)

### Group results

`Group results by selected columns`: If you are familiar with the `GROUP BY` statement in SQL, you’ll quickly find interesting uses to group the results of your CQL. If you select to group the results by the previously selected columns, **the result rows will be split into groups, based on their values**. Thus, only one row will be displayed for each of the groups, so be careful because this implies constraints on the columns.

The grouping of columns is typically combined with aggregations, which moves us to the next section, where we’ll see an example.

### Aggregations

Aggregations are also common in the SQL domain. These functions get the values of grouped rows as the input of that function to return a calculated value. This gadget currently supports three functions:

- **Count**. It returns the number of rows in that group.
- **Min**. It returns the smallest value of the range of values of the group.
- **Max**. It returns the largest value of the range of values of the group.

example For example, if we want to calculate how many pages are in each space, add space as a column, enable group result and add an aggregation to count the number of pages.

![Dashboard Hub group aggregation](/cms_trial/assets/5a25ce5f-e0a2-4a85-918d-4ba4578112e3.jpg)

---

## View type: 1D Pivot table

The 1D Pivot Table view shows a perspective on your data in a single dimension (1D) of your dataset. In other words, one level of grouping, expressed when you select the value for the Rows field.

Users can select a specific attribute or field to act as the basis for organizing and aggregating data. The resulting table presents a clear representation of the chosen dimension, summarizing key metrics and allowing for efficient analysis.

The elements of the 1D pivot table are as follows:

- **Rows (dimensions)** The selected row represents the Confluence field used for grouping.
- **Aggregation** Aggregations get the values of grouped rows as the input of that function to return a calculated value. Check the [aggregations](/cms_trial/space/RDD/861700114/Confluence+Custom+Charts/) section.
- **Field** The displayed field values depend on the chosen aggregation type.

## View type: 2D Pivot table

The 2D Pivot Table view introduces a second dimension (2D) to expand on the capabilities of the 1D Pivot Table. Select 2 different fields (rows and columns) to cross-tabulate data to analyze data across both dimensions simultaneously.

![Dashboard Hub Confluence Custom Charts report preview](/cms_trial/assets/5694a998-40b0-4535-b420-ee6c3b3b870e.jpg)

The elements of the 2D pivot table are as follows:

- **Rows (dimensions):** The selected row represents the Confluence field that is used for grouping.
- **Columns (dimensions):** The selected column represents the Confluence field that is used for grouping.
- **Aggregation:** Aggregations get the values of grouped rows as the input of that function to return a calculated value. Check the [aggregations](/cms_trial/space/RDD/861700114/Confluence+Custom+Charts/) section.
- **Field:** The displayed field values depend on the chosen aggregation type.

## View type: Chart

**Chart by**. Indicates the dimension or the x-axis values (horizontal axis), also referred to as the series, or in layman’s terms, the concepts we see in the legend of the chart.

**Group by**. The second dimension for grouped, stacked or multi charts.

**Aggregation + field**. The aggregation you want to apply to the **field**: count, max, min (see the [aggregations](/cms_trial/space/RDD/861700114/Confluence+Custom+Charts/) section), to plot the values in the chart (y-axis or vertical axis).

### Line chart

A line chart represents the results of your CQL query as a series of data points connected by a straight line. It’s common to visualize trends over periods or dates in the x-axis.

### Multi-line chart

This chart is a line chart with more than one line, which is useful when we need to compare data in a time series or trends.

![Dashboard Hub confluence custom charts multi line](/cms_trial/assets/3cdd956d-1701-4f75-bd2f-ecb136c817e3.png)

### Tile chart

This visual representation presents the information in a set of tiles. You can display the result of your CQL and apply aggregations. For example, you can display the number of pages created pages per space or per creator.

![Dashboard Hub confluence custom charts tile](/cms_trial/assets/ee952f36-a8dd-40b9-884b-bed10b5eb7cf.png)

### Bar chart

A bar chart represents the results of your CQL query as a series of rectangular bars with the height proportional to the represented values. It’s useful to compare the results of different types or categories.

### Grouped bar chart

We can perform more complex comparisons of the information returned by our CQL query by grouping by specific fields.

### Stacked bar chart

Similar to the grouped bar chart, but in this case, the combined results of the groups are on top of each other. Thus, the height is the combined result, making it not appropriate for cases with negative values.

![Dashboard Hub confluence custom charts stacked horizontal](/cms_trial/assets/0237e53e-9140-4ec3-9785-4c28717be90a.jpg)

### Show trend line for bar charts and stacked bar charts

A toggle switch lets you easily show or hide the trend line for bar charts and stacked bar charts, providing a quick way to visualize data trends and gain deeper insights into chart patterns.

#### Customizing the Trend Line Color

Users can select a custom color for the trend line.

Trend lines are only available for bar charts and stacked bar charts.

![Image showing the trend line for bar charts and stacked bar charts.](/cms_trial/assets/45d269da-aaf3-4ac9-bfb8-d2f9211dede5.png)

### Pie chart

A pie chart is a visualization of your data in a circular graph, where each slice indicates the quantity of the result of your CQL. When a pie chart has several sections or slices, it’s difficult to compare one with another. To overcome this inconvenience, the pie chart is accompanied by a table indicating the values of each slice and the % it represents.

When the field selected in “Chart by” has a **date format** for example, Created Date, **a new selector appears to allow grouping by day, week, month, quarter, or year**, making the results easier to understand and communicate.

### Multi pie chart

This chart adds one more dimension to the pie chart, so users can compare sets of information within a single chart. Just add a new field to the “Group By” to display the values in the second ring.

![Dashboard Hub confluence custom charts multi pie](/cms_trial/assets/c4164938-c85d-494f-9217-e4b03a7c22bd.jpg)

### Area chart

An area chart is a visualization that represents the results of your CQL query as a series of data points connected by a straight line and filled with a colored area beneath it, which can help emphasize the magnitude of the values being represented. An area chart is often used to show trends over time or categories, as well as to compare multiple series of data.

### Stacked area chart

A stacked area chart is a variation of the area chart where the areas are stacked on top of each other instead of being overlaid. Each stack represents a category or a group, and the height of the stack represents the total value of the group. It's useful for showing the relative contribution of each group to the total, as well as for tracking changes in the total over time. However, stacked area charts may not be suitable for displaying negative values, as they can become difficult to read.

![Dashboard Hub Confluence Custom Charts chart preview](/cms_trial/assets/62a54926-33b8-4edf-8683-78a189e7c376.jpg)

---

## Customizations

### Custom colors

Within our organizations and teams, it’s common to associate concepts with specific colors, making it easier and quicker to communicate ideas and information.

When you select a chart, you can select the corresponding color of each segment or value.

![Dashboard Hub color pallete](/cms_trial/assets/4599900d-d92f-4800-af62-af0d3c4807fd.jpg)

The color picker supports hexadecimal code, RGB, or our pre-defined 24-color palette (selected based on the right contrasts and tones).

### Hide segments

Not all the results are needed when communicating information in a chart, sometimes because one of those values or segments distorts the results or diverts attention.

Use the **Eye** icon to set whether the segment is hidden (or shown) in the chart:

![Dashboard Hub hide segments](/cms_trial/assets/79040417-6d11-403e-add3-f422ed371129.png)

### Reorder segments

In the same line of hiding segments or customizing the colors of our charts, rearranging the position of the existing segments or values reinforces the way we transmit the information with our charts.

Drag any segment or value from the **six dots** on the left side of the segments and move it upwards or downwards to the correct place, and the chart will be updated accordingly.

![Dashboard Hub reorder segments](/cms_trial/assets/b9a2eaf4-7cb4-40b0-85de-7ee3b861de05.png)

### Normalized charts

Normalized charts adjust data for fair comparisons, ensuring that segments are proportionate relative to 100%, facilitating accurate insights across varying scales or sizes.

![Dashboard Hub Confluence Custom Charts chart preview](/cms_trial/assets/bbd99cc8-5c50-4eaa-9465-9a6eb7332b55.jpg)

---

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, where the Confluence instance is installed.
- The **CQL (Confluence Query Language) query** to filter the list of content (see the [CQL documentation](https://developer.atlassian.com/server/confluence/advanced-searching-using-cql/)). If you don’t add any, the gadget will not request any content, because it would fetch all the content in the source instance, causing performance issues. You have to add at least one clause, for example to list a space `space = TIS`. And remember that the gadget returns the results of the query, which are dynamic and could change over time.
- The **View Type** parameter to indicate the visual representation of the CQL query results in a table, line chart, tile chart, pie chart, bar chart, area chart…
- The **Chart by** parameter (just for charts) to select the x-axis value, in other words, what you see in the horizontal axis. These values or concepts are indicated in the chart legend.
- **Group by**. The second dimension for grouped, stacked or multi charts.
- **Aggregation + field**. The aggregation you want to apply to the **field**: count, max, min (see the [aggregations](/cms_trial/space/RDD/861700114/Confluence+Custom+Charts/) section), to plot the values in the chart (y-axis or vertical axis).
- The **columns** (just for the table view) that will appear in the list to display the search results. At least one column has to be present. Drag and drop to reorder the columns.
- **Group results by selected columns** (just for the table view) in case you want to group the results of the query by the previously selected **columns**. The resulting rows the result rows will be split intogroups, based on their values. Check the group results section.
- The **aggregations** (just for the table view) in case you need to perform calculations -Count, sum, max, min- over the results. Check the [aggregations](/cms_trial/space/RDD/861700114/Confluence+Custom+Charts/) section.
- Indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option saves you from having to configure each gadget individually.

## Integrations

- [confluence icon]

Confluence

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget is not included in any pre-defined dashboard.