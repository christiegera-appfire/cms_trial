# Document Workflow Custom Charts

## Overview

The Document Workflow Custom Charts gadget lets you create customized charts and tables using data from [Comala Document Management (CDM)](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=datacenter&tab=overview) and Confluence fields.

It offers the ability to visualize and analyze document lifecycles, workflow statuses, and other crucial metrics by leveraging workflow parameters as well as essential fields like Workflow name, Last state transition date, Pending Approvers, Finished Approvers, Due date, and more. This feature-rich tool is designed to facilitate informed decision-making and improve document management efficiency. Thereby, enhancing the overall visibility of your documentation and aiding in the improvement of compliance control across Confluence spaces.

The Document Workflow Custom Charts gadget is only available for [Comala Document Management Data Center](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=datacenter&tab=overview). If you're using Comala Document Management Cloud, you should use our [Custom Reports](/cms_trial/space/RDD/1529219266/Custom+Reports+-+REST+API+integration/) gadget.

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/bc41f5d1-1c35-4135-9378-ce70617aef2f.jpg)

## Confluence Query Language (CQL) to search and filter

Queries rely on the [Confluence Query Language (CQL)](https://developer.atlassian.com/server/confluence/advanced-searching-using-cql/) to formulate searches based on criteria such as page properties, labels, creators, and modification dates, facilitating the retrieval of relevant page data.

For example, to list all the pages (type = page) in the space, *Teams in Space* (space = TIS) with the label space\_mission (label = space\_mission), you can use the following CQL query:

`space = TIS and type=page and label = space_mission`

See the complete [CQL documentation](https://developer.atlassian.com/server/confluence/advanced-searching-using-cql/) to learn more about using queries in Confluence.

The Comala Document Management app provides several CQL fields that can be used to filter your search. Find all workflow CQL searchable fields listed in [Comala Document Management CQL Rest API](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649921636) page together with the [Atlassian Confluence CQL fields](https://developer.atlassian.com/server/confluence/cql-field-reference/). We’ll see some examples in the next section.

## Available field types

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/b263b2db-a66f-44ae-bdae-23c2b58b7fda.jpg)

### Dashboard Hub macros

See the following topics to learn about our macros

### Confluence fields

**Available Confluence fields**: Title, Space, Type, Last Modifier, Last Modified Date, Labels, Creator, Created Date.

### CDM built-in fields

**Available CDM built-in fields**: Workflow Name, Current State, State Start Date, State Started by, Final State, State Due date, Final Version Date, Pending Approvers, Finished Approvers, Last Final Version Approvers, Current Pending Approvals, Current Approved Approvals, Current Rejected Approvals.

### CDM Workflow parameters

**Workflow parameters are customizable placeholders** for values such as reviewer names, content expiry durations, labels, categories, departments... Users can update these reference values as needed, to ensure flexibility throughout the workflow process.

![Dashboard Hub workflow parameter](/cms_trial/assets/b1c47029-1024-45a8-8f11-6295682dbda8.png)

**Available workflow parameters**: Those configured by users, more information <https://appfire.atlassian.net/wiki/spaces/CDML/pages/649726186>.

### CQL Examples

Write the following in the CQL input field:

**1.- Pages with a workflow and pending to approve by user Mike**

`awphasworkflow = "true" AND approvalassignee = "Mike"`

**2.- Pages with a workflow already approved by user Mike**

`awphasworkflow = "true" AND approver = "Mike"`

**3.- Pages with a workflow in the Rejected state**

`awphasworkflow = "true" AND state = "Rejected"`

**4.- Pages that transitioned to the Approved state during the last month**

`state = "Approved" AND statechange >now("-1M")`

**5.- Pages with a workflow** **named "Editor and staff approval workflow" that transitioned to the Ready state during the last month** **AND** **pending to approve by user cowens**

`awphasworkflow = "true" AND approvalassignee = "cowens" AND state = "Ready" AND workflowName = "Editor and staff approval workflow" AND statechange >now("-1M")`

![Dashboard Hub cql cdm](/cms_trial/assets/c9b42e14-c905-417a-b7c3-cdf5d4f885f3.png)

See more CDM built-in fields to improve your CQL filter:

- <https://appfire.atlassian.net/wiki/spaces/CDML/pages/649693514>
- <https://appfire.atlassian.net/wiki/spaces/CDML/pages/649824034>

## View type: Table

View the results of your CQL query as a table, where you can select which columns are displayed.

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/fe7e9a28-0380-4a63-9ce4-09dada32f90f.jpg)

### Group results

`Group results by selected columns` If you are familiar with the `GROUP BY` statement in SQL, you’ll quickly find interesting uses to group the results of your CQL. If you select to group the results by the previously selected columns, **the result rows will be split into groups, based on their values**. Thus, only one row will be displayed for each of the groups, so be careful because this implies constraints on the columns.

The grouping of columns is typically combined with aggregations, which moves us to the next section, where we’ll see an example.

### Aggregations

Aggregations are also common in the SQL domain. These functions get the values of grouped rows as the input of that function to return a calculated value. This gadget currently supports three functions:

- **Count**. It returns the number of rows in that group.
- **Min**. It returns the smallest value of the range of values of the group.
- **Max**. It returns the largest value of the range of values of the group.

example For example, if we want to calculate how many pages with a worfklow are in each space with a state “Approved”, use the following CQL `awphasworkflow = "true" AND state = "Approved"` , add space as a column, enable group result and add an aggregation to count the number of pages.

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/87b09560-d1fe-4bcd-b1f3-477577b2764a.png)

---

## View type: 1D Pivot table

The 1D Pivot Table view shows a perspective on your data in a single dimension (1D) of your dataset. In other words, one level of grouping, expressed when you select the value for the Rows field.

Users can select a specific attribute or field to act as the basis for organizing and aggregating data. The resulting table presents a clear representation of the chosen dimension, summarizing key metrics and allowing for efficient analysis.

The elements of the 1D pivot table are as follows:

- **Rows (dimensions)** The selected row represents the Confluence field used for grouping.
- **Aggregation** Aggregations get the values of grouped rows as the input of that function to return a calculated value. Check the [aggregations](/cms_trial/space/RDD/874905671/Document+Workflow+Custom+Charts/) section.
- **Field** The displayed field values depend on the chosen aggregation type.

## View type: 2D Pivot table

The 2D Pivot Table view introduces a second dimension (2D) to expand on the capabilities of the 1D Pivot Table. Select 2 different fields (rows and columns) to cross-tabulate data to analyze data across both dimensions simultaneously.

![Dashboard Hub Document Workflow Custom Charts report preview](/cms_trial/assets/98a6b77c-e859-444a-8ea9-2cef63ee652d.png)

The elements of the 2D pivot table are as follows:

- **Rows (dimensions)** The selected row represents the Confluence or CDM field that is used for grouping.
- **Columns (dimensions)** The selected column represents the Confluence or CDM field that is used for grouping.
- **Aggregation** Aggregations get the values of grouped rows as the input of that function to return a calculated value. Check the [aggregations](/cms_trial/space/RDD/874905671/Document+Workflow+Custom+Charts/) section.
- **Field** The displayed field values depend on the chosen aggregation type.

## View type: Chart

Remember that:

**Chart by**. Indicates the dimension or the x-axis values (horizontal axis), also referred to as the series, or in layman’s terms, the concepts we see in the legend of the chart.

**Group by**. The second dimension for grouped, stacked or multi charts.

**Aggregation + field**. The aggregation you want to apply to the **field**: count, max, min (see the [aggregations](/cms_trial/space/RDD/874905671/Document+Workflow+Custom+Charts/) section), to plot the values in the chart (y-axis or vertical axis).

### Line chart

A line chart represents the results of your CQL query as a series of data points connected by a straight line. It’s common to visualize trends over periods or dates in the x-axis.

### Multi line chart

This chart is a line chart with more than one line, which is useful when we need to compare data in a time series or trends.

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/f5e25fad-acc7-4f68-86c0-a707ee96d182.png)

### Tile chart

This visual representation presents the information in a set of tiles. You can display the result of your CQL and apply aggregations. For example, you can display the number of pages per current state.

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/b9a0c8e3-e220-4de1-85b7-b5465962c4f2.png)

### Bar chart

A bar chart represents the results of your CQL query as a series of rectangular bars with the height proportional to the represented values. It’s useful to compare results of different types or categories.

### Grouped bar chart

We can perform more complex comparisons of the information returned by our CQL query by grouping by specific fields.

### Stacked bar chart

Similar to the grouped bar chart, but in this case, the combined results of the groups are on top of each other. Thus, the height is the combined result, making it not appropriate for cases with negative values.

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/401118d6-0151-40ab-a5e8-bc95ddf6454e.png)

### Show trend line for bar charts and stacked bar charts

A toggle switch lets you easily show or hide the trend line for bar charts and stacked bar charts, providing a quick way to visualize data trends and gain deeper insights into chart patterns.

#### Customizing the Trend Line Color

Users can select a custom color for the trend line.

Trend lines are only available for bar charts and stacked bar charts.

![Image showing the trend line for bar charts and stacked bar charts.](/cms_trial/assets/3f6e4588-68f5-4334-b884-94088edf7fd6.png)

### Pie chart

A pie chart is a visualization of your data in a circular graph, where each slice indicates the quantity of the result of your CQL. When a pie chart has several sections or slices, it’s difficult to compare one with another. To overcome this inconvenience, the pie chart comes with a table indicating the values of each slice and the % it represents.

When the field selected in “Chart by” has a **date format** e.g., Created Date, **a new selector appears to allow grouping by day, week, month, quarter, or year**, making the results easier to understand and communicate.

### Multi pie chart

This chart adds one more dimension to the pie chart, so users can compare sets of information within a single chart. Just add a new field to the “Group By” to display the values in the second ring.

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/dae1bc1a-4b60-4f76-b016-fcb06b164a69.png)

### Area chart

An area chart is a visualization that represents the results of your CQL query as a series of data points connected by a straight line and filled with a colored area beneath it, which can help emphasize the magnitude of the values being represented. An area chart is often used to show trends over time or categories, as well as to compare multiple series of data.

### Stacked area chart

A stacked area chart is a variation of the area chart where the areas are stacked on top of each other instead of being overlaid. Each stack represents a category or a group, and the height of the stack represents the total value of the group. It's useful for showing the relative contribution of each group to the total, as well as for tracking changes in the total over time. However, stacked area charts may not be suitable for displaying negative values, as they can become difficult to read.

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/eec9353b-ea02-4265-8e75-3f70c0d42a9a.png)

---

## Customizations

### Custom colors

Colors have the power to communicate meaning, provoke emotions, and highlight information. Within our organizations and teams, it’s common to associate concepts with specific colors, making easier and quicker the communication of ideas and information.

Whenever you select a chart, you’ll be able to select the color 🔵 of each specific segment or value of it:

![Dashboard Hub color pallete](/cms_trial/assets/f0f9b9d6-0dc6-4468-ae46-6fbcff70c522.jpg)

The color picker allows the selection of color either by hexadecimal code, RGB, or our pre-defined 24-color palette (selected based on the right contrasts and tones).

### Hide segments

Not all the results are needed when communicating information in a chart, sometimes because one of those values or segments distorts the results or deviates the attention.

Clicking on the 👁 eye icon, the corresponding segment is hidden (or shown) in the chart:

![Dashboard Hub hide segments](/cms_trial/assets/dadebcfc-2dd5-4319-b532-658e9a415113.png)

### Reorder segments

In the same line of hiding segments or customizing the colors of our charts, rearranging the position of the existing segments or values reinforces the way we transmit the information with our charts.

Just drag and drop any segment or value from the **six dots** on the left side of the segments and move it upwards or downwards to the correct place, and the chart will be updated accordingly.

![Dashboard Hub reorder segments](/cms_trial/assets/e87e23f6-4839-40e0-84db-375904cc54fc.png)

### Normalized charts

Normalized charts adjust data for fair comparisons, ensuring that segments are proportionate relative to 100%, facilitating accurate insights across varying scales or sizes.

![Dashboard Hub Document Workflow Custom Charts chart preview](/cms_trial/assets/62f90c91-37e7-457f-a82b-fa14b123c1af.png)

---

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, where the CDM instance is installed.
- The **CQL (Confluence Query Language) query** to filter the list of content (see the [CQL documentation](https://developer.atlassian.com/server/confluence/advanced-searching-using-cql/)). If you don’t add any, the gadget will not request any content, because it would fetch all the content in the source instance, causing performance issues. You have to add at least one clause, for example to list a space `space = TIS`. And remember that the gadget returns the results of the query, which are dynamic and could change over time.
- The **View Type** parameter to indicate the visual representation of the CQL query results in a table, line chart, tile chart, pie chart, bar chart or area chart.
- The **Chart by** parameter (just for charts) to select the x-axis value, in other words, what you see in the horizontal axis. These values or concepts are indicated in the chart legend.
- **Group by**. The second dimension for grouped, stacked or multi charts.
- **Aggregation + field**. The aggregation you want to apply to the **field**: count, sum, max, min, mean (see the [aggregations](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) section), to plot the values in the chart (y-axis or vertical axis).
- The **columns** (just for the table view) that will appear in the list to display the search results. At least one column has to be present. Drag and drop to reorder the columns.
- **Group results by selected columns** (just for the table view) in case you want to group the results of the query by the previously selected **columns**. The resulting rows the result rows will be split intogroups, based on their values. Check the [group results](/cms_trial/space/RDD/874905671/Document+Workflow+Custom+Charts/) section.
- The **aggregations** (just for the table view) in case you need to perform calculations -Count, sum, max, min- over the results. Check the [aggregations](/cms_trial/space/RDD/874905671/Document+Workflow+Custom+Charts/) section.
- Indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option saves you from configuring each gadget individually.

## Integrations

- [confluence icon]

Confluence

## See also