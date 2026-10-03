# Dashboard Hub

**About the BigPicture gadgets**

BigPicture gadgets are supported with[**BigPicture Standard**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/).

**Exception**: The OKR gadget is supported **only** with [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). The OKR module is not available in the standard version of BigPicture.

Bring your BigPicture data into centralized, shareable dashboards and report on it your way.

## What is the integration with Dashboard Hub?

Dashboard Hub from Appfire lets you build advanced, shareable dashboards so you can turn the work you already manage in BigPicture into clear charts, tables, and KPIs that stakeholders and managers see at a glance. Create custom visualizations of your BigPicture data and build dashboards that give a unified view of multiple projects.

Dashboard Hub displays data using gadgets: the components that fetch data from a datasource and render it in tables, charts, tiles, and more. The integration offers two gadgets:

- [BigPicture Custom Charts](https://support.appfire.com/space/RDD/629873831/BigPicture+Custom+Charts): Build charts and tables from your BigPicture boxes and tasks.
- NEW [BigPicture OKRs](https://support.appfire.com/space/RDD/3402104953/BigPicture+OKRs): Report on your BigPicture OKR progress directly in a dashboard.

You can use both gadgets in Dashboard Hub dashboards and native Jira dashboards.

To learn more about Dashboard Hub and to start a free trial, visit our [Atlassian Marketplace page](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=overview).

## Why use both apps together

- Create custom BigPicture charts and dashboards.
- Share dashboards externally with password-protected links in seconds.
- Combine and integrate different datasources, instances, and products into the same dashboard – creating a single reference point for their team. By having all the data in the same place, users can stop jumping from one tool to another. Teams migrating can display data from Cloud and Data Center instances to ease their migration journey.
- Access the BigPicture metrics from Jira, Confluence, Bitbucket, or even monday.com, thanks to the Dashboard Hub family of apps.
- Leverage all Dashboard Hub's powerful features:

  - Advanced restrictions/permissions on charts and dashboards
  - Dashboard subscriptions
  - Dynamic filtering
  - Creating custom charts with JQL and formulas
  - Templates and nearly 100 prebuilt gadgets

## Requirements

- Add BigPicture as a datasource in Dashboard Hub
- For the OKRs gadget, you also need access to the BigPicture OKR module and a BigPicture OKR API token.
- Add the BigPicture Custom Charts or BigPicture OKRs gadget to a dashboard.

## How to use the BigPicture Custom Charts gadget

### The BigPicture Search Panel

The BigPicture search lets you search through your boxes and select the elements you want to display in your BigPicture Custom Charts gadget, filtering out unwanted tasks or projects.

You can search through the selected box by:

- ID
- Status
- Box type
- Text search mode filters information based on the BigPicture summary fields. Available text fields depend on your data source.
- Start/end date range

The search also applies to all hidden fields and columns.

### Selecting the fields for the BigPicture Custom Charts

![bigpicture-custom-charts-main-view.png](/cms_trial/assets/f6157433-659d-4feb-8615-343c9eeb81db.png)

1. Select the BigPicture Custom Charts gadget from the gadget selector in Dashboard Hub or Jira.
2. Give your gadget a meaningful name so it is clear what it does and how to use it.
3. Select the datasource where the source BigPicture instance is installed.
4. In the *Select and filter your boxes* section, click the Select Multiple Boxes field. The Tree locator displays the fields in your BigPicture instance for the selected data source.
5. Use the checkboxes to select the box ID where the content will be displayed in the BigPicture Custom Charts gadget.
6. Select the View Type (chart or table).
7. Click Configure filters to refine your search to add additional search criteria.
8. Check the preview to confirm how the gadget will display.
9. Click **Add** to save the gadget on the Dashboard.

If you select Chart as a View type, you need to configure the chart before you can preview it.

---

### View type: Table

You can view the results of your BigPicture search as a table, where you can select the displayed columns. Using the **table** view, you can display results as:

- Group of results
- Aggregation of results

![Screenshot 2023-11-24 at 13.34.25.png](/cms_trial/assets/46957877-a547-4223-9229-9933c7ae7969.png)

#### Group results

`Group results by selected columns`

If you are familiar with the `GROUP BY` statement in SQL, you can choose how to group the results of your BigPicture search.

If you choose to group the results from the previously selected columns, **the result rows are split into groups based on their values**. This means that only one row is displayed for each group.

**Example**

If we filter the previous list of work items by the **Status** column, the results show only two rows: one for the status *To Do* and the other for the status *Done*.

![Screenshot 2024-01-25 at 14.05.08.png](/cms_trial/assets/9be4b01a-bc54-4381-9dde-1346e725832c.png)

Selecting the columns **Status, Name,** and **ID**, the resulting list displays three rows.

Column grouping is typically combined with aggregations.

![Screenshot 2024-01-25 at 14.16.18.png](/cms_trial/assets/6cb2f92d-435c-467e-a74a-43d2b5334abf.png)

#### Aggregations

Aggregations are also common in the SQL domain. These functions take the values of grouped rows as input to return a calculated value.

This gadget supports five functions:

- **Count**. It returns the number of rows in that group.
- **Sum**. It returns the sum of the numbers in the group.
- **Min**. It returns the smallest value in the group's range of values.
- **Max**. It returns the largest value in the group.
- **Mean**. The arithmetic mean; sums the values of the grouped rows and divides the result by how many rows are averaged.

For example, if we want to view the number of Boxes with status, leader, and description:

![Screenshot 2024-01-25 at 15.15.25.png](/cms_trial/assets/90824bd4-e863-4247-bf7d-f2ed50b3595a.png)

---

### View type: Chart

#### Line chart

A line chart represents the results of your BigPicture search as a series of data points connected by a straight line. It’s used to visualize trends over periods or dates in the x-axis.

In the example, the line chart plots the work items created and closed date for a given date range.

![Screenshot 2024-01-17 at 11.32.58.png](/cms_trial/assets/8f0c8526-30e4-4e6a-a57a-7d12a5cb5330.png)

#### Multi line chart

The multiline chart is helpful when comparing data in a time series or trends.

The example chart shows the work items with an end date and description grouped weekly for a given data range.

![Screenshot 2024-01-17 at 11.38.50.png](/cms_trial/assets/2396321e-f663-456a-bbf0-c49d2349a51f.png)

#### Tile chart

This visual representation presents the information in a set of tiles. You can display the result of your BigPicture search and apply aggregations.

For example, you might want to find out the status of your team activities, view the progress, and count the number of boxes.

After you apply the filters to your query, the results are displayed in tiles showing both the number and the percentage; in the example, for the items `In Progress, Not Started, and Closed`.

![contentId-1918862370](/cms_trial/assets/7192181d-0bcb-47bc-9347-bcdbea0c58de.png)

#### Bar chart

A bar chart represents the results of your BigPicture search as a series of rectangular bars with the height proportional to the represented values. It’s helpful to compare results of different types or categories.

The Bar chart example shows the created and closed work items for the selected date range, displayed by quarter.

Note that you can select the bars to be horizontal or vertical, as in the example.

![Screenshot 2024-01-17 at 11.55.26.png](/cms_trial/assets/91bd9df4-1752-4d89-be3a-fc30118d677a.png)

#### Grouped bar chart

We can perform more complex comparisons of the information returned by our query grouping by specific fields.

![Screenshot 2023-11-24 at 13.34.51.png](/cms_trial/assets/7c78d5b2-55c9-4b42-990f-fab345b0abfc.png)

#### Stacked bar chart

The grouped bar chart is similar to the bar chart, with the combined results of the groups on top of each other. Thus, the height is the combined result, making it not applicable to cases with negative values.

In the illustrative example, the chart displays all the tasks organized by their respective Created Date and with a description. The output shows all Created Dates distributed each week in a month for the selected date range.

![Screenshot 2024-01-17 at 12.26.15.png](/cms_trial/assets/ad4ad1ee-3268-4714-b925-6ea0c9a575ae.png)

#### Pie chart

A pie chart is a visualization of your data in a circular graph, where each slice indicates the quantity of the result of your BigPicture search. When a pie chart has several sections or slices, it’s difficult to compare one with another. To overcome this inconvenience, the pie chart comes with a table indicating the values of each slice and the % it represents.

When the field selected in “Chart by” has a date format, for example, Created, a new selector allows grouping by day, week, month, quarter, or year, making the results easier to understand and communicate.

![Screenshot 2023-11-24 at 13.35.01.png](/cms_trial/assets/3101e640-41e6-441f-9a01-c4823d40e910.png)

#### Area chart

The area chart represents the results of your BigPicture search as a series of data points connected by a straight line and filled with a colored area. The colored area can help emphasize the magnitude of the presented values. An area chart is often used to show trends over time or categories, as well as to compare multiple data series.

In the example, the chart plots the work items by Created Date and Closed Date, organizing the Created Dates into monthly groupings for enhanced clarity and insight.

![Screenshot 2024-01-17 at 12.42.35.png](/cms_trial/assets/109d0113-5fd8-463c-853d-64a59cb597c6.png)

#### Stacked area chart

A stacked area chart is a variation of the area chart where the areas are stacked on top of each other instead of being overlaid. Each stack represents a category or a group, and the height of the stack represents the total value of the group. It's helpful in showing the relative contribution of each group to the total and tracking changes in the total over time. However, stacked area charts may not be suitable for displaying negative values, as they can become difficult to read.

![Screenshot 2023-11-24 at 13.34.36.png](/cms_trial/assets/9acf2c56-509e-4fca-951a-7e2f8b5347df.png)

---

### Custom colors

Within our organizations and teams, it’s common to associate concepts with specific colors, making it easier and quicker to share ideas and information.

When you use a chart, you can choose the color of each specific segment or value of it:

![contentId-1918862370](/cms_trial/assets/7072c2c4-a065-4dc3-8b41-2db5804e2112.png)

The color picker lets you select a color by hexadecimal code, RGB, or our pre-defined 24-color palette (selected for contrast and tone).

#### Hide segments

Not all the results are needed when communicating information in a chart, sometimes because one of those values or segments distorts the results or distracts attention. Click the 👁 **Eye** icon to show or hide the corresponding segment in the chart:

![contentId-1918862370](/cms_trial/assets/16e8eab0-be77-4682-b2ee-749f9ff4bddf.png)

#### Reorder segments

In the same way as hiding segments or customizing the colors of our charts, rearranging the position of the existing segments or values reinforces how we transmit information with our charts.

Just drag any segment or value from the six dots on the left side of the segments and move it upwards or downwards to the correct place, and the chart will be updated accordingly.

![contentId-1918862370](/cms_trial/assets/6c2f4c1f-a11f-4d58-9493-e6b0dda8647f.jpg)

## How to use the BigPicture OKRs gadget

**About the OKR gadget**

This gadget is supported **only** with [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). The OKR module is not available in the standard version of BigPicture.

The BigPicture OKRs gadget lets you display your BigPicture OKR progress directly in Dashboard Hub. Select the Objectives you want to track, filter by period, owner, team, or status, and view the results as a tree of Objectives and Key Results with customizable columns, or use Dashboard Hub’s charts and aggregations to analyze them, such as a pie chart of OKRs per team.

![BigPicture OKRs gadget rendered as a stacked bar chart](/cms_trial/assets/b790d8f6-5535-4093-a9ec-28650f5cadbe.png)

This gadget integrates with BigPicture. Make sure you have BigPicture installed and access to the **OKR module**.

### **Example use cases**

- **OKR Progress Tracking**: Monitor Objectives and their Key Results at a glance without leaving your dashboard.
- **Team OKR Overview**: Filter by team or owner to see which OKRs are assigned to specific people or groups.
- **Period Reviews**: Filter by period to focus on quarterly or annual OKRs during review cycles.
- **Stakeholder Reporting**: Share OKR progress with people outside Jira by embedding dashboards in Confluence pages.

### **Prerequisites**

To use this gadget, you need:

- A **BigPicture OKRs** datasource connected to Dashboard Hub. This requires a BigPicture OKR API token.
- An existing **Jira datasource** from the same Jira instance where BigPicture is installed.

### Create a BigPicture OKR API token

You must be a Jira administrator, an In-module administrator, or have the **API access** permission in your OKR role.

1. From the OKR module, go to **Settings** > **API**.
2. Click **+Generate new token**.
3. Enter a name for the token and click **Create**.
4. Copy the token and store it securely. You can’t retrieve it later.

For more information, see [OKR API](/cms_trial/space/SPM/3064169104/OKR+API/).

### Add a BigPicture OKRs datasource

1. In Dashboard Hub, go to **Datasources** and click **Add datasource**.
2. Select **BigPicture OKRs**.
3. Enter your BigPicture OKR module API token.
4. Select the linked Jira datasource from the same instance.
5. Click **Save**.

### **Configure the gadget**

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the **Search** bar to find and select the **BigPicture OKRs** gadget.
3. **Name** (optional): Edit the default name to make it meaningful to your team.
4. **Datasource**: Select a BigPicture OKRs datasource.
5. **Select OKRs**: Use the OKR selector to choose which Objectives to include, or apply a date range. Key Results are included automatically with their parent Objective.
6. (Optional) Use **OKR filters** to narrow the results.
7. **Columns**: Select the columns to display in the tree view and drag to reorder. At least one column must be present.
8. **Visualization**: Select a view type. See *View types*, below, to learn about the different options.
9. Preview the gadget, then click **Apply** to save it to your dashboard.

You can resize or reposition any gadget to prioritize specific data and improve the layout.

### OKR filters

All filters are populated dynamically from your BigPicture data.

|  |  |
| --- | --- |
| **Filter** | **Description** |
| Period | Filter by OKR period, for example, Q1 2026 or H1 2026. |
| Owner | Filter by the person responsible for the Objective or Key Result. |
| Team | Filter by team assignment. |
| Status | Filter by OKR status, for example, On Track, At Risk, or Off Track. |
| Collaborators | Filter by people contributing to the OKR. |
| OKR type | Filter by type, for example, Objective or Key Result. |
| Labels | Filter by labels applied to OKRs in BigPicture. |

### OKR rows

The **OKR rows** section lets you choose which levels of the OKR hierarchy to include. Use the selection field to include or exclude Objectives or Key Results from the display.

### **View types**

Select the view type that best visualizes your OKR data. A switch in the gadget header lets you display a chart or a table with the underlying data, available in the gadget’s main view when the dashboard is not in edit mode.

- **Nested Table (default)**: A hierarchical tree with Objectives as parent rows and their Key Results nested beneath, showing your selected columns. *Example: track quarterly Objectives with progress percentage, status, and owner for each.*
- **1D Pivot Table**: A single-dimension summary — select a field to group by and an aggregation (count, sum, min, max, or mean). *Example: count OKRs per owner to see workload distribution.*
- **2D Pivot Table**: Cross-tabulates two fields with an aggregation. *Example: OKR status by team.*
- **Pie and multi-pie charts**: Each segment’s share of the total, with a table of values and percentages; multi-pie adds a second dimension as an outer ring. *Example: proportion of OKRs by status.*
- **Bar charts (bar, grouped, stacked)**: Compare values across categories; grouped and stacked variants add a second dimension. *Example: OKRs per team, split by status.*
- **Line and multi-line charts**: Visualize trends over time. *Example: track OKR progress over a quarter.*

The visualization options work the same way as the BigPicture Custom Charts gadget, including customizations.