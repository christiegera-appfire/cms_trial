# 7pace Timetracker's Reporting Page

If you require additional assistance or training or are interested in having a custom report created for you, consider enlisting our [support team](https://appfire.atlassian.net/servicedesk/customer/portals).

Webinar: [Software Development Capitalization - Increasing Percentage of Work that is Capitalized & Reporting Tips](https://www.youtube.com/watch?v=mQobvFiuH5k)

## Default Reports

All reports are personal and cannot be shared with other team members within a project or organization at this time.

![Reports_Overview.png](/cms_trial/assets/da987990-2f40-4f89-8be2-3cef904ceba9.png)

The Reporting page of 7pace Timetracker comes with the following default reports for your convenience. Depending on the report, you may have the option to change the date range of data that displays.

![Reports_Overview_Change_Date_Range.png](/cms_trial/assets/848c98d8-58e0-4d0c-94d6-990316c60203.png)

## Personal Overview

This report shows an individual progress line chart, as well as a breakout of the days you worked, total time worked, average time worked per day, and time worked during the current day, during the selected time period. It also shows a time tracked per day bar chart, a details panel of the work items you tracked on, and projects and activity types pie charts for that period.

## Team Overview Report

This report shows all time tracked by the team for the current day, current week, current month, and current year. It also shows a period summary line chart, a projects pie chart, team time per day bar chart, activity types line chart and pie chart, team time tracked per person breakout list, team time tracked per person pie chart, and top 30 work items tracked for the current month details panel.

## Team Overview Report (Date Period)

You can select the time period of data you’d like to see for this report. It shows a period summary line chart, a projects pie chart, a team time per day bar chart, activity types line and pie charts, activity types line and pie charts, a team time tracked per person breakout list, a team time tracked per person pie chart, the top 30 work items tracked for the selected time period details panel, and an Iterations bar chart.

## Backlog Report

For this report, you can select the time period of data you’d like to see. It includes a team work item details panel with their children, time tracked per Work Item Type, and time.

## Epics Report

For this report, you can select the time period of data you’d like to see. It includes a team work item details panel, time tracked per person list, time tracked per project and per activity type pie charts, total tracked time for the selected period line chart, and daily time bar chart.  Please note that this report features data from the work item and its children.

## Last Tracks

This report shows time tracked on the current day and the previous day.

## Report properties

Every report has several configurable properties:

- Name
- Prefilter - The option to limit data displayed on the report by current user or current project. These filters are dynamic and depend on the current user who opened the report or on the project.
- Type - The option to enable or disable the Date filter on the report.  
  ℹ️ You can't change this option after a report has been created; you have to create a new report and copy the Widgets into it.
- Filters have two types: Work item filter and worklog filter. For technical reference, check [this](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) section.

  - Projects - Work item filter that provides a list of projects that can be used to filter data on the report
  - Area - Work item filter that provides the ability to filter by the area path of work items
  - Iteration - Work item filter that provides the ability to filter by the iteration path of work items
  - State - Work item filter that provides the ability to filter by work item state
  - Work Item Type - Work item filter that provides the ability to filter by the type of work items
  - Person - Worklog filter that provides the ability to filter by specific team members (**Important**: To see the Person filter, the user must have at least the "Product" role assigned. This filter is not available for "Team" role users. To check on your users' permissions, you can go to the "Settings" page of Timetracker -> User Management ).
  - Activity Type - Worklog filter that provides the ability to filter by the Activity Type of worklogs
- Work Item Filters Type - These define how the filters, above, marked as w*ork Item* filters, areapplied to work items:

  - Apply to only top-level work items—filters are applied only to work items that do not have parents (e.g., Epics) and are not applied to the children of those work items. This can be helpful with reports that have drill-down tables that present data for high-level work items.
  - Apply on the whole hierarchy - filters are applied on all the items that are present in the backlog and only leave items matching the specific condition.

## About privacy

By default, because reporting operates under [Service Account](/cms_trial/space/7TFA/1253540778/7pace+Timetracker+Service+Account/) permissions, users have access to all worklogs and work items within reporting. If privacy issues are a concern and you'd like to restrict access to only those projects to which your users currently have access, disable the "Allow access to DevOps data from restricted projects in Reporting" checkbox in [Service Account Settings](/cms_trial/space/7TFA/1253540778/7pace+Timetracker+Service+Account/).

## Widget types

- **Line Chart** - Visually presents a series of data points over intervals of time as a linear graph. It is often used to show trend data.
- **Column / Bar Chart** - Compares values by visualizing data as vertical bars with height being proportional to the values.
- **Pie / Donut Chart** - Shows proportions and percentages between categories by dividing a circle into  proportional segments.
- **Number  Chart** - Shows concrete values from a series of data and is often used to display a summary, average values or other results of data aggregation.
- **Table** - Shows a detailed set of flat data.
- **Drilldown Table -** Presents a detailed data set in which every entity can be expanded to display related information.
- **Stacked Bars -** Compares data by categories, dividing each category into smaller pieces to compare each. Similar to a column chart, categories are displayed as vertical bars with height being proportional to the totals, and each bar divided into smaller rectangles to represent the values.
- **Pivot table -** Is used to quickly summarize large amounts of data. You can use a PivotTable to analyze numerical data in detail, and answer unanticipated questions about your data. A PivotTable is especially designed for querying large amounts of data in many user-friendly ways. We have created a pivot table template which can be downloaded from the following link: [Pivot table](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/)

Pivot table is **not available out of the box in the 7pace UI currently**, but we have created a workaround that utilizes our API to achieve pivot table functionality.

## Working with reports

## How to: Add a report

1. From the Reporting page, select the default reports list dropdown and then click “New Report”.

![Add_Report.png](/cms_trial/assets/dd37ce51-9897-4b7c-8d96-09c569b2982e.png)

2. Type in a report “Name”, select a “Pre-filter dashboard” (“None”, “Me” or “CurrentProject”), select “Type” (“Date Period” or “No Date Period”), check relevant “Enabled Filters”, and select “Work Item Filters Type” (“Apply on whole hierarchy” or “apply only on top level work items”).

3. Click **Save**. “Create Widgets for your report” page displays.

Click [here](https://appfire.atlassian.net/wiki/spaces/7TFA/pages/edit-v2/1253539934#How-to%3A-Add-new-Widget) for how to add a widget.

## How to: Edit a report

1. To edit an existing report, click **Edit**.

![Edit_Report.png](/cms_trial/assets/429ccc5d-b299-4277-b053-d57429c707d0.png)

The "Edit report" window displays.

2. Make changes to any of the fields within the window and click **Save**.

## How to: Delete a report

1. To delete an existing report, click the dropdown icon by the “Edit” button.

![Delete_Report.png](/cms_trial/assets/576f5488-f295-410a-8fa2-5d42ddc22670.png)

2. On the “Are you sure” popup window, select “Yes”. The report is deleted.

For the time being, if you delete all default reports, you must also delete any user-created reports for the default reports to return.

## How to: Reorder Widgets

1. Click the dropdown arrow icon next to the “Edit” button and select “Reorder Widgets”.

![Reorder_Widgets.png](/cms_trial/assets/69fa23c3-128d-4cb8-a496-3bcd810cc3db.png)

2. With your mouse or keypad, move the Widget or Widgets to the preferred placement on the page.

3. Click **Done Reorder** at the top-center of the page. The new placement of Widget or Widgets is saved.

## How to: Export data to Excel

1. With the report of your choice selected, hover your mouse over an individual Widget until the “Export Data” icon displays.

![Export_Data_to_Excel.png](/cms_trial/assets/86215e1f-8d88-4276-b1d9-5c8dd7e0a8d0.png)

2. Click **Export Data**. Data from the Widget is exported to an Excel file.

Only visible data will be exported. If you export data from tables, only the items that are present in the table will be exported.

## How to: Zoom in and zoom out of Widgets

On the Widget of your choice, hover over it until dotted grid lines display on it. You can then zoom in or zoom out to the level of detail you require.

![Zoom_In_Out_Widgets.png](/cms_trial/assets/6a0f0430-8210-49aa-a679-9b17175800ab.png)

## How to: Add a new Widget

1. Choose a report where you want to add a Widget.

2. Click the **Add Widget**.

3. Choose the Widget type you need. For this example, let's create a Drilldown Table.

![Add_Widget.gif](/cms_trial/assets/18995a16-06ec-4e3c-94c1-ebfa5a7c7a0c.gif)

4. When you click "Drilldown Table", you'll see the table configuration.

5. Fill in the title.

6. Add subtitle (optional). If you check the Auto title checkbox, it will be automatically filled by the widget pre-filter value.

7. Choose the Widget size.

8. Choose the OData endpoint where you need to pull data (all endpoints described [here](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/)).

For this example, let's say we want to show all work items on which the team tracked time with all hierarchy levels.

9. Therefore, choose "[workItemsHierarchyAllLevels](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/)".

You now need to construct an OData Query (for more information, see [OData documentation](http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part2-url-conventions.html)):

In this case, we'll need this query:

`$select=System_Id,System_WorkItemType,System_TeamProject,System_Title,TrackedTotal,TrackedItself,System_State,System_AssignedTo,HasChildren&$filter=TrackedTotal gt 0`

The "children" endpoint and "children" query will be filled automatically.

The other settings should be filled in the Console field as JSON:

- Our table will have a hierarchy, so fill the field so our table can show this hierarchy.

`"hierarchyField": "System_Id"`

- The only one we need to now fill is the columns field:

```text
"columns": [
 {
   "field": "System_Id",
   "title": "ID",
   "formatter": "WorkItemId",
   "width": 60
 },
 {
   "field": [
     "System_Title",
     "System_WorkItemType",
     "System_TeamProject"
   ],
   "title": "Title",
   "formatter": "WorkItemIndicator",
   "width": -100,
   "expand": true
 },
 {
   "field": "System_State",
   "title": "State",
   "width": 100
 },
 {
   "field": "System_AreaPath",
   "title": "Area",
   "width": 100
 },
 {
   "field": "System_AssignedTo",
   "title": "Assigned To",
   "width": 150
 },
 {
   "field": "TrackedTotal",
   "title": "Tracked",
   "width": 100,
   "formatter": "TimeLength"
 },
 {
   "field": "Microsoft_VSTS_Scheduling_Effort",
   "title": "Effort",
   "width": 100,
   "formatter": ""
 }
 ]
```

Each field can be formatted using formatter. The full Console input will look like this:

```text
{
 "hierarchyField": "System_Id",
 "childrenQuery": "({hierarchyField})/Children?{query}",
 "columns": [
   {
     "field": "System_Id",
     "title": "ID",
     "formatter": "WorkItemId",
     "width": 60
   },
   {
    "field": [
      "System_Title",
      "System_WorkItemType",
      "System_TeamProject"
     ],
     "title": "Title",
     "formatter": "WorkItemIndicator",
     "width": -100,
     "expand": true
   },
   {
     "field": "System_State",
     "title": "State",
     "width": 100
   },
   {
     "field": "System_AreaPath",
     "title": "Area",
     "width": 100
   },
   {
     "field": "System_AssignedTo",
     "title": "Assigned To",
     "width": 150
   },
   {
     "field": "TrackedTotal",
     "title": "Tracked",
     "width": 100,
     "formatter": "TimeLength"
   },
   {
     "field": "Microsoft_VSTS_Scheduling_Effort",
     "title": "Effort",
     "width": 100,
     "formatter": ""
   }
 ],
 "childrenEndpoint": "workItemsHierarchy"
}
```

10. Click **Save**.

11. Click **Refresh**.

![Refresh.png](/cms_trial/assets/0acafedb-863f-4bfd-bd47-a940f879f440.png)

## How to: Export/Import Widget definitions

To **export** a Widget definition to share with anyone:

1. Choose the Widget you need to copy or share with someone.

2. Click **Settings** on the Widget.

3. Select **Export definition**. Copy, close, and share that JSON definition with any user or import on one of your reports.

To **import** a Widget definition:

1. Click **Add Widget**.

2. Select **Import now**.

3. Insert Widget code.

4. Click **Import**.

## How to: Add columns to a Widget table

A common scenario is to modify a Widget table to display additional fields required by your team.

Example: Add additional columns: "Created Date" and "Billable Hours":

First, change the query to add the new fields:

`$select=System_Id,System_CreatedDate,TrackedItselfBillable,System_WorkItemType,System_TeamProject,System_Title,TrackedTotal,TrackedItself,System_State,System_AssignedTo,HasChildren&$filter=TrackedTotal gt 0`

Second, add new columns so the table can show the new fields:

```text
 {
   "field": "System_CreatedDate",
   "title": "Created Date",
   "width": 100,
   "formatter": "LocaleSettingsDateTime"
 },
 {
   "field": "TrackedItselfBillable",
   "title": "Billable hours",
   "width": 100,
   "formatter": "TimeLength"
 }
```

System\_CreatedDate column is added with the "Created Date" title and formatter [LocaleSettingsDateTime](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) that displays the date in a users preferred format.

## How to: Change time granularity in Column chart Widget

Default reports come with several line/column charts that show time displayed over a specific period. All of them use "day" as the time granularity. If you are interested in using "month" instead, it can be accomplished with the following steps:

1. Click **Settings** on the Widget.

2. Click **Reconfigure**.

3. Find xAxis definition.

```text
"xAxis": {
   "type": "date",
   "title": "",
   "rotation": 0,
   "granularity": "day",
   "minGridDistance": 50
 },
```

 4. Change "granularity" value to "month" and click **Save**. The Widget should now display data in month granularity.

![Change_Time_Granularity_Column_Chart_Widget.gif](/cms_trial/assets/a1e037f2-8602-4171-819f-61cfce00861d.gif)

## Troubleshooting and common issues

## Service Account is not configured for your organization

![Service_Acc_Not_Configured.png](/cms_trial/assets/a0f4bbd9-d9e1-48db-85a8-91a3ad84d53e.png)

For Reporting to work, the [Service Account](https://support.7pace.com/hc/en-us/articles/15425349557778-7pace-Timetracker-Service-Account) must be [configured](https://support.7pace.com/hc/en-us/articles/15425349557778-7pace-Timetracker-Service-Account). To do this, the Service Account page should be opened by a user from the Collection Admin group.

## How to restart reporting

If you are experiencing reporting issues, our support team recommends that you restart reporting. To do this, navigate to **Settings** > **Reporting & REST API** and click **Restart Reporting**.

![Restart_Reporting.png](/cms_trial/assets/0cfac874-6c0d-4ed5-97c6-94950705c542.png)