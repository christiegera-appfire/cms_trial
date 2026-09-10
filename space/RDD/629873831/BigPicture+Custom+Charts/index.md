# BigPicture Custom Charts

## Overview

Teams track many projects, products, and portfolios at once, each needing its own view of progress. The BigPicture Custom Charts gadget creates charts and tables from your BigPicture boxes so you can see that information in your dashboards.

You can use this gadget in both Dashboard Hub dashboards and native Jira dashboards.

This gadget integrates with [BigPicture](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm?hosting=cloud&tab=overview). Make sure you are using that app first.

BigPicture Boxes group your projects, products, teams, or portfolios. First, choose the content you want to display using the BigPicture search panel. Then use the gadget to display the results and choose how to visualize them.

We also offer a [BigPicture template](/cms_trial/space/RDD/1942979108/BigPicture+PPM+Insights+template/) configured with additional gadgets for a quick dashboard setup for BigPicture insights.

## Example use cases

Use this gadget to answer questions about your BigPicture data, such as:

- **Portfolio Overview**: Display a table of boxes with their status, leader, and dates to track progress across a portfolio.
- **Progress Tracking**: Chart tasks by status or created date to see how work is trending over a date range.
- **Workload Comparison**: Use grouped or stacked bar charts to compare tasks across boxes, teams, or assignees.
- **Time-Based Reporting**: Plot created and closed items over time with line or area charts.

## The BigPicture search panel

### Select and filter your boxes

The BigPicture search panel lets you filter out boxes you don’t need. Search through your boxes and select the ones you want to display in the gadget.

![Dashboard Hub select multiple boxes](/cms_trial/assets/0a23d09e-5eed-4606-be3b-989564653721.png)

You can refine your search by ID, status, Box type, start and end date range, or text. Text search filters on the BigPicture summary fields.

![Dashboard Hub BigPicture Custom Charts chart preview](/cms_trial/assets/9be87733-f621-41d9-8d04-56c1786cbe35.png)

The search also applies to all hidden fields and columns.

## Select the type of data

After you select the boxes that set the scope of your charts, choose whether to create the charts from box fields or task fields. If you select tasks, you can further filter the scope.

![Dashboard Hub select type data](/cms_trial/assets/76a38f7e-e376-4414-be67-9d28e6a1fedf.png)

### Boxes: Available types of fields

**BigPicture fields** can be configurable (for example, End Date), non-configurable (for example, Summary), or native app fields that don’t correspond to any external tool.

**Available fields**: ID, Type, Name, Status, Leader, Created Date, Start Date, End Date, Actual Cost, Archived, Budget, Description, Closed Date, Icon, Inactive For, Period Mode, Estimated Cost, and Sequentiality.

### Tasks: Available types of fields

**BigPicture built-in fields**: You can display all existing attributes of basic tasks using built-in fields. See the [Built in fields matrix](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298027369/Concept+of+a+field+in+BigPicture#Built-in-fields-matrix) for details.

![BigPicture_fields_mapping](/cms_trial/assets/90f4e1cc-6544-4539-82e0-d69bbd3bbe0f.png)

**Available fields:** Icon, Key, Summary, Status, Assignee, Scheduling Mode, Start Date, End Date, Actual Cost, Baseline End Date, Baseline End Date Discrepancy, Baseline Start Date Discrepancy, Baseline Start Date, Catalog, Color, Duration Calendar Days, Duration Working Days, Estimated Cost, Milestone, Modification Time, Original Estimate, Outline level, Overdue (End Date), Overdue (Start Date), Remaining Estimate, Progress, Risk Probability, Risk Consequence, Skills, Status Category, Sub-box, Story Points, Team, Task ID, Time Spent, Workload contouring mode, Time Tracking

**Filter your tasks**: Use the free text, assignee, status, and date filters to narrow down specific tasks.

---

If you selected **Chart** as a View type, you need to configure the chart before you can preview it.

## How to configure the gadget

### View type: Table

You can view the results of your BigPicture search as a table, where you can select the columns that are displayed. Using the **Table** view, you can display results as:

- A group of results
- An aggregation of results

![BigPictur Custom Charts gadget showing a table of boxes](/cms_trial/assets/d5685c78-8d10-41b5-9112-181cd6a54d24.png)

#### Group results

Select **Group results by selected columns** to group the results of your BigPicture search.

When you group results by the selected columns, the result rows are split into groups based on their values. Only one row displays for each group.

Choose your columns based on the results you want to display for each group. Grouping is typically combined with aggregations.

**Example**

f you group the previous list of issues by the **Status** column, the results show two rows: one for the status *To Do* and one for the status *Done*.

![Dashboard Hub BigPicture custom chart configuration with chart type options](/cms_trial/assets/cda52200-9d3d-4dd8-a39e-d3def96c0b64.png)

If you select the **Status**, **Name**, and **ID** columns, the resulting list displays three rows.

![Dashboard Hub BigPicture custom chart fields configuration](/cms_trial/assets/c7c83452-1c70-4c92-bff9-c7bdbc90b136.png)

### Aggregations

Aggregations take the values of grouped rows as input and return a calculated value. This gadget supports five functions:

- **Count**: Returns the number of rows in the group.
- **Sum**: Returns the total of the numbers in the group.
- **Min**: Returns the smallest value in the group.
- **Max**: Returns the largest value in the group.
- **Mean**: Returns the arithmetic mean, which sums the values of the grouped rows and divides the result by the number of rows.

For example, to view the number of boxes with a status, leader, and description:

![Dashboard Hub BigPicture custom chart preview with selected data](/cms_trial/assets/c7b76dde-f7c7-4d3b-a0e1-6956c2aaf51c.png)

---

### View type: Line chart

A line chart represents the results of your BigPicture search as a series of data points connected by a straight line. Use it to visualize trends over periods or dates on the x-axis.

- **Chart by**: The x-axis values (horizontal axis), also called the series. These are the concepts shown in the chart legend.
- **Type**: The aggregation you apply to the field (count, sum, max, min, or mean).
- **Field**: The y-axis values (vertical axis), which are what you plot in the chart.

In this example, the line chart plots the issues created and closed for a given date range.

![Dashboard Hub BigPicture custom chart datasource setup](/cms_trial/assets/70abedab-4996-4a13-b16b-08dcd1de0729.png)

### View type: Multi-line chart

A multi-line chart helps you compare time-series data or trends. In this example, the chart shows the issues with an end date and a description, grouped weekly for a given date range.

![Dashboard Hub BigPicture custom chart grouping settings](/cms_trial/assets/c4288b0b-492a-4ee8-b998-8e439c7a697a.png)

### View type: Tile chart

A tile chart presents the information in a set of tiles. You can display the results of your BigPicture search and apply aggregations. For example, you can view the status of your team activities, view progress, and count the number of boxes.

After you apply the filters to your query, the results display in tiles showing both the number and the percentage. In this example, the tiles show *In Progress*, *Not Started*, and *Closed*.

![Dashboard Hub BigPicture Custom Charts page example](/cms_trial/assets/777c12b2-e2e7-4a46-b6dd-a7b149d6d9b9.png)

### View type: Bar chart

A bar chart represents the results of your BigPicture search as a series of rectangular bars, where the height is proportional to the values. Use it to compare results of different types or categories.

In this example, the bar chart shows the created and closed issues for the selected date range on a quarterly basis. You can display the bars horizontally or vertically.

![Dashboard Hub BigPicture custom chart value settings](/cms_trial/assets/cbc60e7e-e82f-4de1-b11b-07326c4fde73.png)

### View type: Grouped bar chart

A grouped bar chart lets you compare the results of your query by grouping on specific fields.

![Dashboard Hub BigPicture custom chart dashboard preview](/cms_trial/assets/ff9d407c-8156-492a-8aa6-40f6d4451076.png)

### View type: Stacked bar chart

A stacked bar chart is similar to the bar chart, but the results of the groups are stacked on top of each other, so the height is the combined result. It isn’t suitable for negative values.

In this example, the chart displays all the tasks organized by their created date and with a description. The output shows the created dates distributed across each week in a month for the selected date range.

![Dashboard Hub BigPicture custom chart filter settings](/cms_trial/assets/7383d09b-0c5a-4422-8dc0-2e0e01d036ba.png)

### View type: Pie chart

A pie chart displays your data in a circular graph, where each slice represents the quantity of a result. When a pie chart has many slices, it’s hard to compare them, so the pie chart includes a table showing the value of each slice and the percentage it represents.

When the field selected in **Chart by** has a date format, such as Created, a new selector lets you group by day, week, month, quarter, or year.

![Dashboard Hub BigPicture custom chart report example](/cms_trial/assets/c9cd01ef-bb87-4f3e-8c8c-fbf36658ca98.png)

### View type: Area chart

An area chart represents the results of your BigPicture search as a series of data points connected by a straight line and filled with a colored area. The colored area emphasizes the magnitude of the values. Use it to show trends over time or categories, or to compare multiple series.

In this example, the chart plots issues by their created date and closed date, grouping the created dates by month.

![Dashboard Hub BigPicture custom chart completed configuration](/cms_trial/assets/33a8fb1f-ccc9-4888-a704-a88827f81ee4.png)

### View type: Stacked area chart

A stacked area chart is a variation of the area chart in which the areas are stacked rather than overlaid. Each stack represents a category or group, and its height represents the group’s total value. Use it to show each group’s contribution to the total and to track changes in the total over time. It isn’t suitable for negative values.

![Dashboard Hub BigPicture custom chart setup screen](/cms_trial/assets/d84c05bb-ca06-4e29-a823-af771e17d980.png)

### Switch between chart and table view

A switch in the gadget header lets you display the chart or a table with the underlying data. This option is available in the gadget’s main view when the dashboard is not in Edit mode.

![Dashboard Hub BigPicture Custom Charts page example](/cms_trial/assets/9a96573e-3168-4b7c-9d2b-92c5c77704b3.png)

---

## Custom colors

Colors communicate meaning and highlight information. Within teams, it’s common to associate concepts with specific colors, which makes ideas quicker to communicate.

Whenever you select a chart, you can set the color of each segment or value.

![Dashboard Hub BigPicture Custom Charts chart preview](/cms_trial/assets/7820f442-c526-4311-99d7-7c47c5237095.png)

The color picker lets you select a color by hexadecimal code, RGB, or from the predefined 24-color palette, chosen for the right contrasts and tones.

### Hide segments

Not all results are needed when you communicate information in a chart, sometimes because one value distorts the results or diverts attention.

Click the Eye icon to hide or show the corresponding segment in the chart.

![Dashboard Hub BigPicture Custom Charts chart preview](/cms_trial/assets/a08145ce-9e41-4e9a-9940-0f01783a5ab6.png)

### Reorder segments

Rearranging segments reinforces how you present information in your charts. Drag any segment or value from the handle on the left side and move it up or down to the correct place. The chart updates accordingly.

![Dashboard Hub BigPicture Custom Charts chart preview](/cms_trial/assets/764dc2f9-a897-4f2f-95d3-5bf338d2cfe6.jpg)

### Limit the number of segments on the X-axis

You can limit the number of segments displayed on the x-axis in charts.

- Set a maximum number of segments in the input field.
- The chart displays only the highest-value segments in the dataset.
- Any remaining segments are grouped into a segment labeled **Others**.

This helps simplify visualizations by focusing on the most relevant data.

![Dashboard Hub BigPicture custom chart example with configured data](/cms_trial/assets/884ff3f9-f38c-4541-8e29-11f48e98b7e7.png)

## Configuration

Give your gadget a meaningful name so it is clear what it does and how to use it. Fill out the remaining fields as applicable:

- The **data source**, where the source BigPicture instance is installed.
- **Select multiple boxes, and** use the Tree locator to select the data that you want to investigate**.**

If you don't select anything in the Tree locator and you limit your query to text or status, the search goes through the whole instance. This might cause performance issues.

- The **Configure filters to refine your search** lets you insert additional criteria. Choose from **Text, ID, Status, Type,** and **Dates.**
- The **View Type** Here, you choose the visual representation of your BigPicture search. Results can be displayed in table or chart format.
- **Columns** (just for the table view) allow you to choose the columns that you want to display.
- **Group results by selected columns.** Group your search results by the previously selected **Columns**.

## Related pages

- [BigPicture OKRs](https://support.appfire.com/space/RDD/3402104953)