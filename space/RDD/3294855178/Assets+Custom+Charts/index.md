# Assets Custom Charts

## Overview

new Dashboard Hub’s **Assets Custom Charts** gadget lets you create customized charts, pivot tables, and tables using data from [Atlassian Assets](https://www.atlassian.com/platform/platform-apps/assets) (CMDB). Query your asset objects with Assets Query Language (AQL), then aggregate and visualize the results, for example, chart laptop counts by service status, track software license expiry dates by vendor, or compare asset status distributions across office locations.

![Asset Custom Charts showing assets per status in a pie chart and table view.](/cms_trial/assets/f175aead-5195-4bf9-96ab-dab8f72f7cae.jpg)

Knowledge of AQL is required to write your queries. For example, to retrieve software licenses expiring in the next 90 days, use

`objectType = "Software" AND "License Expiry Date" < now(90d)`

or to retrieve all objects in the Schema “states” with a status set, use

`objectSchema = "states" AND "Current status" is not EMPTY`

See [Using Assets Query Language](https://support.atlassian.com/assets/docs/use-assets-query-language-aql/) to learn more about AQL syntax.

### Example use cases

Use this gadget to answer questions about your Assets data, such as:

- **Asset Distribution**: See how many assets are assigned to each department, location, or owner using a pie or bar chart.
- **Status Breakdown**: Visualize the distribution of asset statuses, for example, Active, Retired, or In Repair, across object types.
- **License Tracking**: Chart software license counts by vendor, expiry date, or assignment status.
- **Inventory Reporting**: Create pivot tables that cross-reference asset categories with locations or cost centers.

## How to configure the gadget

This section explains how to add and configure the gadget.

**To add the gadget to a dashboard:**

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the **Search** bar in the *Add gadget* page to find the required gadget.
3. Select the **Assets Custom Charts** gadget.
4. **Name** (*optional*): The name field is completed by default. You can edit the name to make it more meaningful to your team.
5. **Datasource**: Select an Atlassian Assets datasource. To learn more about datasource types, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).
6. **AQL query**: Enter an AQL query to define which Assets objects to include.
7. **View type**: Select a view type to best visualize data. You can select any of the following visual formats to represent the resulting data of the AQL query: table, pivot table, pie chart, bar chart, line chart, and area chart.

   ![Asset Custom Charts configuration options.](/cms_trial/assets/50cba73f-cedd-4ef8-ba00-2d0d8c6032e6.png)
8. (Optional) Depending on the view type you select, choose how to group the data. See the options in the next section for more information.
9. A preview of the chart displays in the configuration page. When you are ready, click **Add** to save the configuration and add the gadget to your dashboard.

You can resize or reposition any gadget in a dashboard to prioritize specific data and enhance the dashboard layout.

## View types and groupings

### **Tables**

Display the results of your AQL query as a table with selectable columns.

![Assets Custom Charts showing a table view.](/cms_trial/assets/3070f1f7-dde8-4eaa-8d83-cb250ba0ae85.jpg)

**Example:** List all active services and their key details.

**AQL**:

`objectSchema = "Services" AND Status = "Active"`

Or

`objectType in ("Software Services", "Applications", "Business services", "Capabilities")`

![Example of the Services schema tree in Assets.](/cms_trial/assets/4d994263-ba82-4013-b96c-4b097226ad38.jpg)

If you select a table view type, there are additional options to consider:

- The **columns** that will appear in the list to display the search results. For example, Name, Key, Revision, Tier, or Creation date. At least one column has to be present. Drag a column name to reorder the columns.
- You canenable **Group results by selected columns** if you want to group results by the previously selected columns, for example, select `Department` to see one row per department. See the [group results](/cms_trial/space/RDD/3294855178/Assets+Custom+Charts/) section for more information.
- Select an aggregation if you need to perform calculations:Count, sum, max, min, mean, or average over the results. For example, add a count aggregation to show how many laptops each department has. See the [aggregations](/cms_trial/space/RDD/3294855178/Assets+Custom+Charts/) section for more information.

### Group results

Group results by selected columns. If you group the results by the previously selected columns,the result rows are split into groups based on their values. Therefore, only one row displays for each group. Column groups are usually combined with aggregations.

### Aggregations

These functions get the values of grouped rows as input to that function to return a calculated value. This gadget currently supports five functions:

- **Count**.: Returns the number of rows in that group.
- **Sum**: Returns the sum of the sequence of numbers in the group.
- **Min**: Returns the smallest value of the range of values of the group.
- **Max**: Returns the largest value of the range of values of the group.
- **Mean**: The arithmetic mean sums the values of the grouped rows and divides the result by the number of rows being averaged.
- **Show values** (only in Tile charts): Displays the raw values of the returned range.

### Limit segments

**Maximum segments**: To better manage the representation of data in charts, set the maximum number of segments to display.

These segments are ordered by their respective quantities, and once the maximum number of segments is reached, the remaining data is grouped under an *Others* segment. This ensures that the chart remains clear and focused on the most relevant data.

### 1D Pivot Table

The 1D Pivot Table view provides a single-dimensional (1D) perspective on your data. In other words, one level of grouping is expressed when you select the value for the Rows field.

You can select a specific attribute or field to act as the basis for organizing and aggregating data.

**Example**: Count hardware assets by customer. The resulting table shows one row per customer with the total count of assets in each.

![An assets custom chart showing a 1D table for assets per customer.](/cms_trial/assets/55ee0aab-76fd-4263-b2af-f8434a657c9f.jpg)

1D pivot table options:

- **Rows (dimensions)**:The selected row represents the field used for grouping.
- **Aggregation**: Aggregations get the values of grouped rows as the input of that function to return a calculated value.
- **Field:** The displayed field values depend on the chosen aggregation type.

### 2D Pivot Table

The 2D Pivot Table view introduces a second dimension (2D) to expand on the capabilities of the 1D Pivot Table. Select two different rows and columns to cross-tabulate data to analyze data across both dimensions simultaneously.

**Example**: Cross-tabulate asset statuses by location. The resulting table shows asset statuses as rows, office locations as columns, and the count of assets at each intersection.

![The Asset Custom Charts gadget showing a 2D pivot table for the status of assets per location.](/cms_trial/assets/f403dc8c-bc05-4433-a036-ce4deb499098.jpg)

2D pivot table options:

- **Rows (dimensions)**:The selected row represents the field that is used for grouping.
- **Columns (dimensions)**:The selected column represents the field that is used for grouping.
- **Aggregation**: Aggregations get the values of grouped rows as the input of that function to return a calculated value. See the [aggregations](https://support.appfire.com/space/RDD/146309431/Jira+Custom+Charts#Aggregations) section for more information.
- **Field**:The displayed field values depend on the chosen aggregation type.

## Charts

If you use a chart view type, there are additional options to consider.

- The **Chart by** parameter to select the x-axis value, in other words, what you see in the horizontal axis. These values or concepts are indicated in the chart legend.
- The **Type** parameter to indicate what type of aggregation you want to apply to the **field** parameter: Count, sum, max, min, or mean. *Show values* is only available for Tile charts. Check the [aggregations](https://support.appfire.com/space/RDD/146309431/Jira+Custom+Charts#Aggregations) section.
- The **Field** parameter to select the y-axis values (vertical axis), think of what you want to count (or any other aggregation), and plot in the chart.

**Chart by**: Indicates the dimension or the x-axis values (horizontal axis), also referred to as the series, or in layman’s terms, the concepts we see in the legend of the chart.

**Group by**: The second dimension for grouped, stacked or multi charts.

**Aggregation + field**: The aggregation you want to apply to the **field**: count, sum, max, min, mean (see the [aggregations](https://support.appfire.com/space/RDD/146309431/Jira+Custom+Charts#Aggregations) section), to plot the values in the chart (y-axis or vertical axis).

### Line chart

A line chart represents the results of your AQL query as a series of data points connected by a straight line. It’s common to visualize trends over periods or dates in the x-axis.  
**Example**: Track how many new assets were added over time.

### Multi-line chart

This is a line chart with multiple lines, which is useful to comparing time-series data or trends. **Example**: Compare asset creation trends across the different service statuses.

![The Assets Custom Chart showing a multi-line chart for crated objects by status.](/cms_trial/assets/61603691-6c49-4916-acb2-2b5283f49d0d.jpg)

### Tile chart

This visual representation presents the information in a set of tiles for a dashboard-style overview. You can display the result of your AQL and apply aggregations to show total asset counts by status at a glance.

![Asset Custom Charts gadget showing a tile chart for service status by location.](/cms_trial/assets/58ba659a-c4ec-49e4-8f1a-2ad7ba654da9.jpg)

### Bar chart

A bar chart represents the results of your AQL query as a series of rectangular bars with the height proportional to the represented values.   
**Example**: Compare the number of assets assigned to each department.

### Grouped bar chart

We can perform more complex comparisons of the information returned by our AQL query with specific grouping.  
**Example**: Compare asset types across departments.

![Asset Custom Charts gadget showing a bar chart for assets types across departments.](/cms_trial/assets/c3aae7cd-0fbc-40f3-9974-3f981c48b191.png)

### Stacked bar chart

Similar to the **Grouped bar chart**, but the combined results of the groups are on top of each other. If you want to show asset status distribution per location, each bar represents a location with stacked segments for Active, In Repair, and Retired assets. The total height shows the combined count.

If you need to display the number of assets created per customer and service status, you could use a normalized stacked bar chart, grouped by customer and service status:

![Stacked bar chart showing assets created per customer and status.](/cms_trial/assets/3b500ebd-bd6b-4b1a-ad72-c07e97ced995.jpg)

### Pie chart

A pie chart is a visualization of your data in a circular graph, where each slice indicates the quantity of the result of your AQL. When a pie chart has several sections or slices, it’s difficult to compare one with another. To resolve this, the pie chart includes a table showing the value of each slice and the % it represents.   
**Example**: Each slice could represent an asset type (Laptops, Phones, Servers, Printers), or the internal tiers we use to split the assets. The accompanying table shows values and percentages.

![Assets Custom Charts gadget showing a pie chart for assets per tier.](/cms_trial/assets/f3e5ad41-0f89-45b3-9a87-bc0b57a506d2.jpg)

### Multi pie chart

This chart adds one more dimension to the pie chart, so users can compare sets of information within a single chart. Add a new field to group by to display the values in the second ring.   
**Example**: To compare asset creation dates by status, the inner ring shows the creation month; the outer ring shows the status breakdown within each month.

![Assets Custom Charts gadget showing a multi-pie chart for assets created by month.](/cms_trial/assets/b784784a-48c7-4f04-991e-d2db611755e4.jpg)

### Area chart

An area chart is a visualization that represents the results of your AQL query as a series of data points connected by a line and filled with a colored area beneath it, which can help emphasize the magnitude of the values being represented. An area chart is often used to show trends over time or across categories, as well as to compare multiple data series.

### Stacked area chart

A stacked area chart is a variation of the area chart in which the areas are stacked rather than overlaid. Each stack represents a category or group, and its height indicates the group's total value. It's useful for showing each group's relative contribution to the total and for tracking changes in the total over time. However, stacked area charts might not be suitable for displaying negative values, as they can become difficult to read.   
**Example**: Show cumulative asset intake by type over time. Each stacked layer represents an asset type, showing both individual and total intake trends.

![Stacked area chart from the Assets Custom Charts gadget.](/cms_trial/assets/69770cc1-40c6-4d2d-9c56-19806c1555dc.png)

---

## Customizations

Extra settings let you customize the order and colors of the chart segments.

To modify the chart’s appearance, click **Charts extra settings**.

![The Charts extra settings shown in the gadget configuration.](/cms_trial/assets/3e1341f2-aeb0-444b-b460-b7ef3504b077.png)

### Hide segments

Not all the results are needed when communicating information in a chart, sometimes because one of those values or segments distorts the results or diverts attention.

Click the **Show**/**Hide** icon to switch the corresponding segment to hidden (or shown) in the chart.

### Reorder segments

Rearranging the positions of existing segments or values reinforces how we convey information in our charts. Drag any segment or value using the handle on the left side of the segments and move it upwards or downwards to the correct place, and the chart will be updated accordingly.

### Custom colors

Colors can communicate meaning, provoke emotions, and highlight information. Within our organizations and teams, it’s common to associate concepts with specific colors, making it easier and quicker to communicate ideas and information.

Click a color icon to open the color picker. You can define a color by hexadecimal code, RGB, or select from the predefined 24-color palette. These were selected for optimal contrast and tone.

## Integrations

- Assets in Jira Service Management (formerly, Insight)

## Dashboards

This gadget isn’t included in any of our dashboard templates.