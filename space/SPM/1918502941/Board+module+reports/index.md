# Board module reports

## Board module reports (old navigation)

Click to expand the guide

## About the reports in the Board module

Using the Board module, you can generate reports at two levels

- Upper level – e.g., Program Increment or a Project phase
- Lower level – e.g., Iteration or a sub-phase

You can generate separate reports for each team and see the summary for all teams combined in the top row. Click on the Reports button to enable the reporting functionality. Once you do, an additional configuration button will show up right next to it. Use the drop-down menu to change chart settings.

![contentId-1918502941](/cms_trial/assets/ace64942-f682-4d28-8dfe-8158fb99cfed.png)

## Reporting using the full scope

When you enable the Report functionality, charts will be generated for each Timebox. But, since some of your tasks might have already been planned on the lower level, they will not be included as the source data. To capture the entire scope of the upper-level Timebox, enable the "Show full scope" feature.

Use the "Show full scope" feature to generate reports for the whole PI, including the Iteration level.

![contentId-1918502941](/cms_trial/assets/c5ec30ee-c006-4035-aaa1-abf6ca201daa.png)

## Edit Charts

After generating the chart, you can exclude different categories from it by clicking on the legend.

The example below shows how to filter out the Craftsman Team from the first chart:

![contentId-1918502941](/cms_trial/assets/f165c3da-a99c-4b85-8f66-229f3f483f3f.png)

## Chart Types

### Pie Chart

Pie charts show percentage distribution across different categories defined as groups. Hover over a segment of a pie chart to display the details.

In the example below, you can see we've checked Cameron's capacity, and it's exactly 25% or 10/40 Story points. Again, Cameron's capacity is presented in red to match the colors in the legend.

![contentId-1918502941](/cms_trial/assets/d8247ce0-d5ba-474c-a264-7d10b854bfe1.png)

### Bar Chart

Bar charts will adjust the scale depending on the values presented and show data source categories as bars. Hover over the bar to display a tooltip with details.

![contentId-1918502941](/cms_trial/assets/b71ec8f7-011e-4211-af16-ffd233551aad.png)

## Data Source

You can select Tasks or Capacities as the data source for your charts. Tasks include additional counting and grouping options listed below.

### Capacities

Generate charts based on the capacities resulting from workload, holiday, and absence plans. Capacity can be expressed using story points or man-days.

The example below shows how you can check if your teams' capacity is increasing over time. As you can see below, the Craftsman Team is losing its capacity. For Iteration 1, it was 55 story points, while for Iteration 2, it's 50 story points. So if you take a closer look at the Craftsman Team, you can see that it's because of Lesley.

![contentId-1918502941](/cms_trial/assets/08cf7663-b928-43cf-b610-1e4ca9171fca.png)

### Tasks

Generate charts based on the number of tasks presented on the Board. This option allows further grouping of tasks and counting all available units.  
When you select the tasks as a data source, you can group data by:

- Status
- Assignee
- Priority
- Status category

And count data by the number of:

- Tasks
- Story Points
- Remaining Estimate
- Original Estimate
- Man-days

The example below shows how to create a bar chart using Tasks as the data source, group these tasks by the Assignee field, and count the number of tasks assigned to each Assignee. For example, if you hover over the bar representing Eric, you can see there are currently 2 tasks assigned to him.

![contentId-1918502941](/cms_trial/assets/d0b41d10-6ffa-42b6-a28a-746652a7f905.png)

## Troubleshooting

### Report information

Reports are generated correctly **only when** **all the information is available.**

For example:

- if reports are based on Story Points, the tasks must have a Story Point value assigned to them.
- if reports are based on capacities, the teams must have a capacity value (teams must have members, and the availability of the members has to be above zero)

### Work Progress

Work progress depends on the "totals" settings:

![image-20250226-082410.png](/cms_trial/assets/54eec32c-7c34-49e2-8460-376f64a7d4c7.png)![image-20250226-082431.png](/cms_trial/assets/cc800659-795d-4c4d-af40-8e16ded8ad53.png)

## Board module reports (new navigation)

Click to expand the guide

## About the reports in the Board module

Using the Board module, you can generate reports at two levels

- Upper level – e.g., Program Increment or a Project phase
- Lower level – e.g., Iteration or a sub-phase

You can generate separate reports for each team and see the summary for all teams combined in the top row.

Click **Board** > **Reports view** to enable the reporting functionality. Under the **View** menu, you can change report type and aggregation settings.

![Screenshot of the Reports view in the Board module. ](/cms_trial/assets/c0fac878-7a1c-4329-933c-f01dddf8fe05.png)

## Reporting using the full scope

When you enable the **Reports view**, charts will be generated for each timebox. But since some of your tasks might already have been planned at the lower level, they will not be included as source data. To capture the entire scope of the upper-level timebox, enable the **Show full scope** feature.

Use the **Show full scope** feature to generate reports for the whole PI, including the Iteration level.

![Screenshot of the Show full scope button in the Backlog tab in the Board module.](/cms_trial/assets/0ac788a5-8910-4189-9dc8-250043b58fd7.png)

## Edit charts

After generating the chart, you can exclude different categories from it by clicking on the legend.

![Video of the report and its legend in the Board module.](/cms_trial/assets/450b9171-3482-4eae-b6b6-fd207cfa3d31.mp4)

## Chart types

### Pie chart

Pie charts show the percentage distribution across different categories defined as groups. Hover over a segment of a pie chart to display the details.

### Bar chart

Bar charts will adjust the scale depending on the values presented and show data source categories as bars. Hover over the bar to display a tooltip with details.

![Screenshot of the Reports type option in the Board module.](/cms_trial/assets/af3f0207-3ef0-4bb0-b056-f78fba312cd9.png)

## Data source

You can select Tasks or Capacities as the data source for your charts. Tasks include additional counting and grouping options listed below.

### Capacities

Generate charts based on the capacities resulting from workload, holiday, and absence plans. Capacity can be expressed using story points or man-days.

### Tasks

Generate charts based on the number of tasks presented on the Board. This option allows further grouping of tasks and counting all available units.  
When you select the tasks as a data source, you can group data by:

- Status
- Assignee
- Priority
- Status category

And count data by the number of:

- Tasks
- Story Points
- Remaining Estimate
- Original Estimate
- Man-days

## Troubleshooting

### Report information

Reports are generated correctly **only when** **all the information is available.**

For example:

- If reports are based on Story Points, the tasks must have a Story Point value assigned to them.
- If reports are based on capacities, the teams must have a capacity value (teams must have members, and the availability of the members has to be above zero)

### Work progress

Work progress depends on the [Aggregation](/cms_trial/space/SPM/1918666880/Aggregations/) settings.

![Screenshot of the Work progress Aggregation type selected in the Board module. ](/cms_trial/assets/56ae7776-b1eb-412f-9067-3ed1dc15f109.png)