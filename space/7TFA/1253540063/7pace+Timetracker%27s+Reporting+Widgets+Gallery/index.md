# 7pace Timetracker's Reporting Widgets Gallery

You can find a collection of custom widgets requested by our 7pace Timetracker users by copying the widget JSON definition and [importing](https://support.7pace.com/hc/en-us/articles/360035383932-Reporting-Overview#exporting-importing-definition) it to any of your existing reports.

## Postman collection

## Find a collection of the above custom widget queries and additional query examples for Postman

In order to be able to import our Postman collection, you must have a public Postman account. When importing, you should choose the "Fork" option, which will create a copy of the collection in your account, which you can then use its requests and make changes to without affecting the original. You can also choose to subscribe to updates to the original collection by checking "Watch original collection".

*How to fork the Postman collection data to your workspace:*

1. Open the following link:  
   <https://go.postman.co/workspace/Team-Workspace~36b01b3c-6ff9-4bd8-892a-1dd3367f07cc/collection/20406970-6c9f851b-19fb-40fc-9adb-d6cd0eded530?action=share&creator=20583389>
2. Click **OData collection**.
3. Click **Fork**.

   ![Fork_Option.png](/cms_trial/assets/475c15e5-d2f1-4021-b249-1d48cdbd19a4.png)
4. Choose the workspace where the collection should be stored.

   ![Fork_Collection.png](/cms_trial/assets/b9c36a0a-3483-45ca-9b1f-16c5ae91b001.png)

The current collection has several variables that you should change according to your chosen environment:

![Fork_Variables.png](/cms_trial/assets/336d30b3-fb74-4dd7-8d92-b041d5f24691.png)

## Reporting Widgets Gallery

## Work Items Activity

This donut widget displays work items' tracked time grouped by the DevOps' "Activity" field (Microsoft.VSTS.Common.Activity). To learn more about how this field is used, see [Capacity planning](https://docs.microsoft.com/en-us/azure/devops/boards/sprints/set-capacity?view=azure-devops).

![Work_Items_Activity.png](/cms_trial/assets/d62b5807-5fc9-47dd-9f6a-3a9140fc43b3.png)

`{"valueField":"PeriodLength","categoryField":"WorkItem.Microsoft_VSTS_Common_Activity","id":"","query":"$apply=groupby((WorkItem/Microsoft_VSTS_Common_Activity),aggregate(PeriodLength with sum as PeriodLength))&$orderby=WorkItem/Microsoft_VSTS_Common_Activity","endpoint":"workLogsWorkItems","type":"Pie","title":"Activity","subTitle":null,"w":4,"h":2,"chartSettings":{"backgroundColor":"#104547","showLegend":true,"name":"","innerRadius":30,"disableTicks":false,"disableTitle":false},"labelRadius":10,"autoSubtitle":true,"timeframeFilter":null,"y":20,"x":0,"valueFormat":"duration","":"","odataVersion":"v3.2"}`

## Work Items with Estimations

This drill-down table provides a list of work items (all levels) with estimations (Effort, Original Estimate, Completed Work, Remaining Work) as roll-up fields. To learn more about how roll-up fields work in reporting, see [Reporting API Overview](https://support.7pace.com/hc/en-us/articles/360035502332-7pace-Timetracker-Reporting-API-Version-3#rollupFields:~:text=To%20use%20our%20customFields/rollupFields%20parameters%20in%20Excel%20or%20Power%20BI%3A).

![Work_Items_with_Estimations.png](/cms_trial/assets/aabfe2fc-9604-49c9-b7a7-a89686db7d4f.png)

`{"type":"HierarchyTable","id":"","title":"Work Items with estimations","subTitle":"","w":8,"h":4,"endpoint":"workItemsHierarchy","query":"$select=System_Id,System_WorkItemType,System_TeamProject,System_Title,TrackedTotal,TrackedItself,RollupValue1,RollupValue2,RollupValue3,RollupValue4,System_State,System_AreaPath,System_AssignedTo,HasChildren&$filter=TrackedTotal gt 0&$orderby=TrackedTotal desc&rollupFields=Microsoft.VSTS.Scheduling.Effort, Microsoft.VSTS.Scheduling.OriginalEstimate, Microsoft.VSTS.Scheduling.RemainingWork, Microsoft.VSTS.Scheduling.CompletedWork","hierarchyField":"System_Id","childrenQuery":"({hierarchyField})/Children?{query}","columns":[{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-1,"expand":true},{"field":"System_State","title":"State","width":80},{"field":"System_AreaPath","title":"Area","width":100},{"field":"System_AssignedTo","title":"Assigned To","width":140},{"field":"TrackedTotal","title":"Tracked","width":100,"formatter":"TimeLength"},{"field":"RollupValue1","title":"Effort","width":60,"formatter":""},{"field":"RollupValue2","title":"Original Estimate","width":60},{"field":"RollupValue3","title":"RemainingWork","width":80,"formatter":"Number","format":"#.#"},{"field":"RollupValue4","title":"CompletedWork","width":80,"formatter":"Number","format":"#.#"}],"autoSubtitle":false,"timeframeFilter":null,"childrenEndpoint":"workItemsHierarchy","y":6,"x":0,"odataVersion":"v3.2"}`

## Work items filtered by tags

There is a possibility to tag work items:

![Work_Items_Filter_by_Tags.png](/cms_trial/assets/55d89083-f1a0-4a7d-940f-0d9f850ab572.png)

Our reporting feature supports filtration by these tags. Here is an example of the Work Item table filtered by the tag 'capex'.

![Work_Items_Month.png](/cms_trial/assets/a6c09dd6-b8de-44e2-8b19-c8d731d7033f.png)

`{"id":"","query":"$select=TrackedItself,System_Id,System_Title,System_TeamProject,System_WorkItemType,System_AreaPath,System_State,System_AssignedTo,CustomStringField1&customFields=System.Tags&$filter=contains(CustomStringField1, 'capex')&$orderby=TrackedItself desc&$top=30","endpoint":"workItems","type":"FlatTable","title":"Top 30 Work Items this Month","subTitle":null,"w":8,"h":3,"columns":[{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-100},{"field":"System_State","title":"State","width":100},{"field":"System_AreaPath","title":"Area","width":100},{"field":"System_AssignedTo","title":"Assigned To","width":150},{"field":"TrackedItself","title":"Tracked","width":100,"formatter":"TimeLength"},{"field":"CustomStringField1","title":"Tags","width":100,"formatter":""}],"autoSubtitle":false,"timeframeFilter":null,"y":23,"x":0,"odataVersion":"v3.2"}`

Here is also an example of a number widget. It contains the total tracking time count filtered by tag 'capex':

![Capex_Time_Month.png](/cms_trial/assets/0319bb52-680c-4fa5-ac5f-58db11c7b7d8.png)

`{"id":"","query":"$apply=filter(contains(CustomStringField1, 'capex'))/aggregate(TrackedItself with sum as PeriodLength)&customFields=System.Tags","endpoint":"workItems","type":"Number","title":"Capex time this month","subTitle":"","fieldName":"PeriodLength","formatter":"TimeLength","w":2,"h":1,"timeframeFilter":{"from":null,"to":null,"filterType":"Month"},"autoSubtitle":true,"y":27,"x":0,"odataVersion":"v3.2"}`

*For more information on capex reporting, check out our webinar:*[*Software Development Capitalization - Increasing Percentage of Work that is Capitalized & Reporting Tips*](https://www.youtube.com/watch?v=mQobvFiuH5k&ab_channel=7pace)

## Latest worklogs

This flat table provides a list of your latest 100 workLogs for the selected date period. It is recommended for the "Personal Overview" report.

![Latest_Worklogs.png](/cms_trial/assets/002a6304-82ac-484d-8486-73d39edabf00.png)

`{"type":"FlatTable","id":"","query":"$orderby=Timestamp desc&$top=100&$select=WorkItemId,Timestamp,PeriodLength,User,ActivityType,WorkItem/System_Title,WorkItem/System_WorkItemType,WorkItem/System_TeamProject,Comment","endpoint":"workLogsWorkItems","title":"My workLogs","subTitle":"Latest 100","w":8,"h":4,"columns":[{"field":"WorkItemId","title":"Work Item Id","formatter":"WorkItemId","width":100},{"field":["WorkItem.System_Title","WorkItem.System_WorkItemType","WorkItem.System_TeamProject"],"title":"Work Item Title","width":-200,"formatter":"WorkItemIndicator"},{"field":["Comment"],"title":"Comment","width":-100},{"field":"ActivityType.Name","title":"Activity Type","width":-100},{"field":"Timestamp","title":"Date","width":-100,"formatter":"DateTimeAgo"},{"field":"PeriodLength","title":"Tracked","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":29,"x":0,"odataVersion":"v3.2"}`

## Work Items with Pace

This drill-down table provides a list of work items (all levels) with a calculated pace based on Effort/Original Estimate/Story Point as the roll-up field.   
To learn more about how to add calculated columns with "MathExpression" formatter, see [Reporting Api Overview - MathExpression](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/)  
To learn more about how roll-up fields work in reporting, see [Reporting API Overview - rollup fields](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/).

![Work_Items_Pace.png](/cms_trial/assets/e26c9d6a-4532-4ef2-89b1-9745def479f2.png)

**Work Items with Pace based on Effort**

`{"type":"HierarchyTable","id":"","title":"Work Items Pace","subTitle":"","w":8,"h":4,"endpoint":"workItemsHierarchy","query":"$select=System_Id,System_WorkItemType,System_TeamProject,System_Title,TrackedTotal,TrackedItself,RollupValue1,System_State,System_AreaPath,System_AssignedTo,HasChildren&$filter=TrackedTotal gt 0&$orderby=TrackedTotal desc&rollupFields=Microsoft.VSTS.Scheduling.Effort","hierarchyField":"System_Id","childrenQuery":"({hierarchyField})/Children?{query}","columns":[{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-100,"expand":true},{"field":"System_State","title":"State","width":80},{"field":"System_AreaPath","title":"Area","width":80},{"field":"System_AssignedTo","title":"Assigned To","width":130},{"field":"TrackedTotal","title":"Tracked","width":80,"formatter":"TimeLength"},{"field":"RollupValue1","title":"Effort","width":80},{"field":["TrackedTotal","RollupValue1"],"title":"Pace","width":80,"formatter":"MathExpression","format":{"expression":"{0} / 3600 / {1}","resultFormat":"#.#"}}],"autoSubtitle":false,"childrenEndpoint":"workItemsHierarchy","y":34,"x":0,"odataVersion":"v3.2"}`

**Work Items with Pace based on Original Estimate**

`{"type":"HierarchyTable","id":"","title":"Work Items Pace","subTitle":"","w":8,"h":4,"endpoint":"workItemsHierarchy","query":"$select=System_Id,System_WorkItemType,System_TeamProject,System_Title,TrackedTotal,TrackedItself,RollupValue1,System_State,System_AreaPath,System_AssignedTo,HasChildren&$filter=TrackedTotal gt 0&$orderby=TrackedTotal desc&rollupFields=Microsoft.VSTS.Scheduling.OriginalEstimate","hierarchyField":"System_Id","childrenQuery":"({hierarchyField})/Children?{query}","columns":[{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-100,"expand":true},{"field":"System_State","title":"State","width":80},{"field":"System_AreaPath","title":"Area","width":80},{"field":"System_AssignedTo","title":"Assigned To","width":130},{"field":"TrackedTotal","title":"Tracked","width":80,"formatter":"TimeLength"},{"field":"RollupValue1","title":"Original Estimate","width":80},{"field":["TrackedTotal","RollupValue1"],"title":"Pace","width":80,"formatter":"MathExpression","format":{"expression":"{0} / 3600 / {1}","resultFormat":"#.#"}}],"autoSubtitle":false,"childrenEndpoint":"workItemsHierarchy","y":29,"x":0,"odataVersion":"v3.2"}`

**Work Items with Pace based on Story Points**

`{"type":"HierarchyTable","id":"","title":"Work Items Pace","subTitle":"","w":8,"h":4,"endpoint":"workItemsHierarchy","query":"$select=System_Id,System_WorkItemType,System_TeamProject,System_Title,TrackedTotal,TrackedItself,RollupValue1,System_State,System_AreaPath,System_AssignedTo,HasChildren&$filter=TrackedTotal gt 0&$orderby=TrackedTotal desc&rollupFields=Microsoft.VSTS.Scheduling.StoryPoints","hierarchyField":"System_Id","childrenQuery":"({hierarchyField})/Children?{query}","columns":[{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-100,"expand":true},{"field":"System_State","title":"State","width":80},{"field":"System_AreaPath","title":"Area","width":80},{"field":"System_AssignedTo","title":"Assigned To","width":130},{"field":"TrackedTotal","title":"Tracked","width":80,"formatter":"TimeLength"},{"field":"RollupValue1","title":"Story Points","width":80},{"field":["TrackedTotal","RollupValue1"],"title":"Pace","width":80,"formatter":"MathExpression","format":{"expression":"{0} / 3600 / {1}","resultFormat":"#.#"}}],"autoSubtitle":false,"childrenEndpoint":"workItemsHierarchy","y":27,"x":0,"odataVersion":"v3.2"}`

## Work Items Area Path

This donut widget displays work items' tracked time grouped by the DevOps "Area Path" field (System\_AreaPath).

![Work_Items_Area_Path.png](/cms_trial/assets/4c6e4be5-5d10-468f-840f-6d58baad8a46.png)

`{"valueField":"PeriodLength","categoryField":"WorkItem.System_AreaPath","id":"","query":"$apply=groupby((WorkItem/System_AreaPath),aggregate(PeriodLength with sum as PeriodLength))","endpoint":"workLogsWorkItems","type":"Pie","title":"Area Path","subTitle":null,"w":4,"h":2,"chartSettings":{"backgroundColor":"#104547","showLegend":true,"name":"","innerRadius":30,"disableTicks":false,"disableTitle":false},"labelRadius":10,"autoSubtitle":false,"timeframeFilter":null,"y":32,"x":0,"valueFormat":"duration","":"","odataVersion":"v3.2"}`

## Team Time per Project

This flat table provides daily tracked time summary per person per project.

![Team_Time_Per_Project.png](/cms_trial/assets/60b5a8f4-a839-4032-a4b2-9c692cbd74d2.png)

`{"id":"","query":"$apply=groupby((User/Name,WorkItem/System_TeamProject,WorklogDate/ShortDate),aggregate(PeriodLength with sum as PeriodLength))&$orderby=WorklogDate/ShortDate desc","endpoint":"workLogsWorkItems","type":"FlatTable","title":"Team Time per Project","subTitle":null,"w":5,"h":3,"columns":[{"field":"User.Name","title":"Person","width":-100},{"field":"WorkItem.System_TeamProject","title":"Project","width":-100,"formatter":"NullToComment"},{"field":"WorklogDate.ShortDate","title":"Date","width":-100,"formatter":"CustomDateTime","format":"DD.MM.YYYY"},{"field":"PeriodLength","title":"Tracked (h)","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":35,"x":0,"odataVersion":"v3.2"}`

## Time per Project

This flat table provides simple tracked time summary per project.

![Time_Per_Project.png](/cms_trial/assets/8024209b-b79c-4036-aa69-2a0bc180116e.png)

`{"id":"","query":"$apply=groupby((WorkItem/System_TeamProject),aggregate(PeriodLength with sum as PeriodLength))&$orderby=PeriodLength","endpoint":"workLogsWorkItems","type":"FlatTable","title":"Time per Project","subTitle":null,"w":3,"h":2,"columns":[{"field":"WorkItem.System_TeamProject","title":"Project","width":-100,"formatter":"NullToComment"},{"field":"PeriodLength","title":"Tracked (h)","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":39,"x":0,"odataVersion":"v3.2"}`

## Budgets

This flat table provides budgets information. It's not affected by any filtering.

![Budgets.png](/cms_trial/assets/a0abe92d-7d69-4ca8-a91e-e2456d7324e8.png)

`{"type":"FlatTable","id":"","query":" $orderby=BudgetName","odataVersion":"v3.2","endpoint":"budgets","title":"Budgets","subTitle":"","w":3,"h":2,"columns":[{"field":"BudgetName","title":"Name","width":-100},{"field":"Billed","title":"Billable","width":90,"formatter":"TimeLength"},{"field":"Tracked","title":"Tracked","width":90,"formatter":"TimeLength"},{"field":"Planned","title":"Planned","width":90,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":53,"x":0}`

## Time per Custom Work Item Field (InternalProject in this example)

This widget displays a pie chart of the time spent on any given project based on a custom field set by the user at the Work Item level. Each slice represents a value in such a field. For example, a user may want to add a new field to store project names, departments, or categories.

![My_Internal_Projects.png](/cms_trial/assets/f4719209-59de-46d4-b22e-15423886a9cc.png)

`{"type":"Pie","valueField":"PeriodLength","categoryField":"WorkItem.CustomStringField1","id":"","query":"$apply=groupby((WorkItem/CustomStringField1),aggregate(PeriodLength with sum as PeriodLength))&$orderby=WorkItem/CustomStringField1&customFields=Custom.InternalProject","odataVersion":"v3.2","endpoint":"worklogsWorkItems","title":"My Internal Projects","subTitle":null,"w":4,"h":3,"valueFormat":"duration","chartSettings":{"showLegend":true,"name":"","innerRadius":30,"disableTicks":true},"autoSubtitle":false,"timeframeFilter":null,"":"","y":20,"x":0}`

## Tracked Time per Person in a Bar Chart

This widget shows the total amount of time tracked by each person in an organization. The time range can be set using the filters on the Dashboard UI. It is possible to exclude the time logged against a specific Activity Type from the calculation, which is achieved by setting the parameter ***{$filter=(ActivityType/Name ne 'placeholder')}*** to the desired value. In this example, the time logged against ‘Testing’ is not displayed on the chart ($filter=(ActivityType/Name ne 'Testing')). Just remove the whole filter to display the total time tracked across all Activity Types.

![Track_Time_Person_Bar_Chart.png](/cms_trial/assets/c1caf2fc-7ba2-4618-8b06-7eaff42767d5.png)

`{"type":"Columns","title":"All activities except Testing by person","subTitle":"","id":"","query":"$apply=groupby((ActivityType/Name,User/Name),aggregate(PeriodLength with sum as PeriodLength))&$filter=(ActivityType/Name ne 'Testing')","odataVersion":"v3.2","endpoint":"workLogsWorkItems","w":8,"h":3,"chartSettings":{"showLegend":true,"name":""},"xAxis":{"type":"category","title":"Person","rotation":90,"granularity":"hour"},"yAxis":{"type":"duration","title":"Tracked, hours"},"series":{"fieldY":"PeriodLength","fieldX":"User.Name"},"dataAdapters":[{"name":"FillMissingDatePoints","params":"PeriodLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":36,"x":0}`

## Shortfalls per Person per Period

This table shows the difference (shortfall) between the total amount of hours a person is expected to log within a given date-range, minus the amount of hours they actually logged.

For example, if during a given week, a person logs time each day from Monday to Friday, the value of ‘Days Tracked’ for that week will be 5. If they only track 30 hours in total, their shortfall will be 10 hours (5 days tracked \* 8 hours a day - 30 hours logged) . If the shortfall value is negative, this means that the amount of time tracked exceeds the expected total (that person has logged more hours than they were expected). Note that in the example, the assumption is that a person is expected to log 8 hours a day, which amounts to 28800 seconds. This can be changed by changing "format":{"expression":"({0}\*28800 - {1}) to the desired value. The time-range can be set using the UI on the Dashboard.

![Shortfalls.png](/cms_trial/assets/ab8eb139-c9d4-47db-82f8-0bdc06e49e98.png)

`{"type":"FlatTable","id":"","query":"$apply=groupby((User/Name),aggregate(PeriodLength with sum as PeriodLength, WorklogDate/ShortDate with countdistinct as DaysTracked))","endpoint":"worklogsOnly","title":"Shortfalls","subTitle":null,"w":4,"h":3,"columns":[{"field":"User.Name","title":"Person","width":-100},{"field":"DaysTracked","title":"Days Tracked","formatter":"","width":120},{"field":"PeriodLength","title":"Tracked","formatter":"MathExpression","format":{"expression":"{0}/ 3600","resultFormat":"#.##"},"width":120},{"field":["DaysTracked","PeriodLength"],"title":"Shortfall","formatter":"MathExpression","format":{"expression":"({0}*28800 - {1}) / 3600","resultFormat":"#.##"},"width":120}],"autoSubtitle":false,"timeframeFilter":null,"y":16,"x":0,"odataVersion":"v3.2"}`

## Individual Shortfalls per Day

This table is similar to the one above; however, it shows the daily shortfall values for each individual person/day over a certain period, which can be defined via the Dashboard.

![Individual_Shortfalls_per_Day.png](/cms_trial/assets/6e74b6fb-db62-48d3-8771-290fa33e81d2.png)

`{"type":"FlatTable","id":"","query":"$apply=groupby((User/Name, WorklogDate/ShortDate),aggregate(PeriodLength with sum as PeriodLength))","endpoint":"worklogsOnly","title":"Shortfalls By Days","subTitle":null,"w":4,"h":3,"columns":[{"field":"User.Name","title":"Person","width":-100},{"field":"WorklogDate.ShortDate","title":"Date","formatter":"CustomDateTime","format":"DD.MM.YYYY","width":-100},{"field":"PeriodLength","title":"Tracked","formatter":"MathExpression","format":{"expression":"{0}/ 3600","resultFormat":"#.##"},"width":120},{"field":"PeriodLength","title":"Shortfall","formatter":"MathExpression","format":{"expression":"(28800 - {0}) / 3600","resultFormat":"#.##"},"width":120}],"autoSubtitle":false,"timeframeFilter":null,"y":19,"x":0,"odataVersion":"v3.2"}`

## Time Logged per Activity by Each Team Member

This table shows the total time logged per Activity by each team member for a given time period which can be set using the Dashboard UI.

![Team_Activity_Type_Time.png](/cms_trial/assets/07240897-431d-46fe-ba64-3bb04c2183c7.png)

`{"id":"","query":"$apply=groupby((User/Name,ActivityType/Name),aggregate(PeriodLength with sum as PeriodLength))&$orderby=User/Name,PeriodLength desc","endpoint":"worklogsOnly","type":"FlatTable","title":"Team Activity Type Time","subTitle":"","w":4,"h":3,"columns":[{"field":"User.Name","title":"Person","width":-100},{"field":"ActivityType.Name","title":"Activity Type","width":-100},{"field":"PeriodLength","title":"Tracked","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":44,"x":0,"odataVersion":"v3.2"}`

## Total Time Tracked per Iteration

This table shows the total time tracked against each Iteration, and compares it with the associated ‘Original Estimate’ and ‘Effort’ values as defined in DevOps. If such values are not displayed, this means that they were not set previously.

![Time_Track_by_Iteration.png](/cms_trial/assets/73707cfd-01c1-4aed-92a7-abc4e7265130.png)

`{"id":"","query":"$apply=groupby((System_IterationPath),aggregate(TrackedItself with sum as PeriodLength, Microsoft_VSTS_Scheduling_Effort with sum as Effort, Microsoft_VSTS_Scheduling_OriginalEstimate with sum as OriginalEstimate))&$orderby=System_IterationPath","endpoint":"workItems","type":"FlatTable","title":"By Iteration","subTitle":"","w":4,"h":3,"columns":[{"field":"System_IterationPath","title":"Iteration","width":-100},{"field":"PeriodLength","title":"Tracked","width":100,"formatter":"TimeLength"},{"field":"OriginalEstimate","title":"Original Estimate","width":100,"formatter":""},{"field":"Effort","title":"Effort","width":100,"formatter":""}],"autoSubtitle":false,"timeframeFilter":null,"y":22,"x":0,"odataVersion":"v3.2"}`

## Items Completed by Date Range

This widget shows a list of Product Backlog Items that were delivered (marked as ‘Done) within a given date-range. Information includes the person that each item is assigned to, the **total time tracked against each item**, as well as Effort and tags.

![Items_Complete_Date_Range.png](/cms_trial/assets/e450058a-ead7-4dc0-9cf1-3b1fbf28dc02.png)

`{"id":"","query":"$select=TrackedTotal,System_Id,System_Title,System_TeamProject,System_WorkItemType,System_State,System_AssignedTo,Microsoft_VSTS_Scheduling_Effort,CustomStringField1&$filter=TrackedTotal gt 0 and System_State eq 'Done'&$orderby=TrackedTotal desc&customFields=System.Tags&workItemsFilter=System_WorkItemType in ('Bug', 'Product Backlog Item')","endpoint":"workItemsHierarchyAllLevels","type":"FlatTable","title":"Items delivered (Done)","subTitle":"","w":6,"h":3,"columns":[{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-100},{"field":"System_AssignedTo","title":"Assigned To","width":150},{"field":"TrackedTotal","title":"Tracked","width":70,"formatter":"TimeLength"},{"field":"Microsoft_VSTS_Scheduling_Effort","title":"Effort","width":60},{"field":"CustomStringField1","title":"Tags","width":150,"formatter":""}],"autoSubtitle":false,"timeframeFilter":null,"y":0,"x":0,"odataVersion":"v3.2"}`

## Items Not Completed During a Given Date Range

This widget shows a list of items that have time tracked against them within a given period, however, have not yet been updated to the ‘Done’ state. The period can be defined using the date picker on the UI. The items can be expended to see the state of their children items.

![Items_Not_Complete_Date_Range.png](/cms_trial/assets/b289dfdd-972c-4cd4-815c-7eb8a4b0252a.png)

`{"type":"HierarchyTable","id":"","title":"Items not delivered (expand children)","subTitle":null,"w":7,"h":3,"odataVersion":"v3.2","endpoint":"workItemsHierarchyAllLevels","query":"$select=System_Id,System_Title,System_TeamProject,System_WorkItemType,System_State,System_AssignedTo,TrackedTotal,TrackedItself, Microsoft_VSTS_Scheduling_Effort,System_AreaPath,HasChildren, CustomStringField1&$filter=TrackedTotal gt 0 and System_State ne 'Done'&$orderby=TrackedTotal desc&customFields=System.Tags&workItemsFilter=System_WorkItemType in ('Bug', 'Product Backlog Item')","hierarchyField":"System_Id","childrenEndpoint":"workItemsHierarchy","childrenQuery":"({hierarchyField})/Children?{query}","columns":[{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-100,"expand":true},{"field":"System_State","title":"State","width":100},{"field":"System_AssignedTo","title":"Assigned To","width":150},{"field":"TrackedTotal","title":"Tracked","width":100,"formatter":"TimeLength"},{"field":"Microsoft_VSTS_Scheduling_Effort","title":"Effort","width":100,"formatter":""},{"field":"CustomStringField1","title":"Tags","width":150,"formatter":""}],"autoSubtitle":false,"timeframeFilter":null,"y":5,"x":0}`

## Total Story Points Delivered by Date Range

This widget shows the total amount of Story Points delivered within any given date range (the state of the associated Work Items should be set to ‘Done’). The date range should be set using the filters in the UI.

![Story_Points_Delivered_Date_Range.png](/cms_trial/assets/bf50a4ae-0eaf-424b-8c8d-55c0f5db6704.png)

`{"type":"Number","id":"","query":"$apply=filter(System_State eq 'Done' and TrackedTotal gt 0)/aggregate(Microsoft_VSTS_Scheduling_Effort with sum as Effort)&workItemsFilter=System_WorkItemType in ('Bug', 'Product Backlog Item')","odataVersion":"v3.2","endpoint":"workItemsHierarchyAllLevels","title":"SP delivered (Done)","subTitle":null,"fieldName":"Effort","w":2,"h":1,"timeframeFilter":null,"autoSubtitle":false,"y":0,"x":6}`

## Total Story Points Delivered by Date Range with a Tag

This widget is identical to the one above, however, only the Work Items with a specific tag are taken into consideration for this calculation. This is defined by the *contains(CustomStringField1, 'maintenance')* parameter, ‘maintenance’ being the value used in our example.

![Story_Points_Delivered_Date_Range_Tag.png](/cms_trial/assets/e051b789-298a-405d-9ad4-1cab1779866c.png)

`{"type":"Number","id":"","query":"$apply=filter(System_State eq 'Done' and TrackedTotal gt 0 and contains(CustomStringField1, 'maintainance'))/aggregate(Microsoft_VSTS_Scheduling_Effort with sum as Effort)&customFields=System.Tags&workItemsFilter=System_WorkItemType in ('Bug', 'Product Backlog Item')","odataVersion":"v3.2","endpoint":"workItemsHierarchyAllLevels","title":"SP delivered 'maintainance' (Done)","subTitle":null,"fieldName":"Effort","w":2,"h":1,"timeframeFilter":null,"autoSubtitle":false,"y":4,"x":6}`

## Total Time Spent on Bugs

This widget shows the total amount of time spent on bug-fixing (Work Item Type = Bug) within any given date-range.

![Time_Spent_Bugs.png](/cms_trial/assets/53615e6a-b499-4db2-945f-9e9505567777.png)

`{"type":"Number","id":"","query":"$apply=aggregate(TrackedTotal with sum as PeriodLength)&workItemsFilter=System_WorkItemType in ('Bug') and System_TeamProject ne 'Internal'","odataVersion":"v3.2","endpoint":"workItemsHierarchyAllLevels","title":"Bugs","subTitle":null,"fieldName":"PeriodLength","formatter":"TimeLength","w":2,"h":1,"timeframeFilter":null,"autoSubtitle":false,"y":3,"x":0}`

## Epics sum

This widget shows the sum of time for each epic by month and year.

`{"type":"HierarchyTable","id":"","title":"Epics By Month","subTitle":null,"w":8,"h":4,"endpoint":"workItemsHierarchy","query":" $select=System_Id,System_WorkItemType,System_TeamProject,System_Title,TrackedTotal,TrackedItself,HasChildren&$filter=TrackedTotal gt 0 and HasChildren eq true&$orderby=TrackedTotal desc","hierarchyField":"System_Id","childrenQuery":"({hierarchyField})/AllWorklogs?$apply=compute(concat(cast(year(Timestamp),Edm.String),concat(cast('-',Edm.String),cast(month(Timestamp),Edm.String))) as yearMonth)/groupby((yearMonth),aggregate(PeriodLength with sum as TrackedTotal))","hierarchyType":"workItems","columns":[{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-100,"expand":true,"child":{"field":"yearMonth"}},{"field":"TrackedTotal","title":"Tracked","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"childrenEndpoint":"workItemsHierarchy","y":19,"x":0,"odataVersion":"v3.2"}`

## Budgets by Activity Type

This widget shows the drill-down of Activity types per Budget. It has a custom hierarchyField usage and example of how to display values from different fields into 1 column (with aggregate/compute)

![Budgets_Activity_Type.png](/cms_trial/assets/9e578bc2-c2bb-43e5-a619-a7d4e2306692.png)

`{"type":"HierarchyTable","id":"","title":"Budget/Activity type","subTitle":null,"w":8,"h":4,"endpoint":"budgets","query":"$apply=groupby((Id,BudgetName,Tracked,Comment),aggregate(0 with sum as junk))/compute(Tracked as PeriodLength)","hierarchyField":"Id","childrenQuery":"({hierarchyField})/Worklogs?$apply=groupby((ActivityType/Name,Budget/Id),aggregate(PeriodLength with sum as PeriodLength))&$orderby=PeriodLength","columns":[{"field":"BudgetName","title":"Budget","expand":true,"width":-100},{"field":"Comment","title":"Comment","width":-100},{"field":"ActivityType.Name","title":"Activity","width":-100},{"field":"PeriodLength","title":"Budget Total","width":-100,"formatter":"TimeLength"}],"autoSubtitle":true,"timeframeFilter":null,"childrenEndpoint":"budgets","y":16,"x":0,"odataVersion":"v3.2","hierarchyType":"rootExpandable"}`

## Total Time Tracked by Month

This widget shows the sum total of all time tracked per each month for the selected time period.

![Time_Track_Month.png](/cms_trial/assets/b3f7cee2-585f-4c3f-901b-15a47b97bf76.png)

`{"title":"Total Time Tracked by Month","subTitle":"","id":"","query":"$apply=compute(concat(cast(year(Timestamp),Edm.String),concat(cast('-',Edm.String),cast(month(Timestamp),Edm.String))) as yearMonth)/groupby((yearMonth),aggregate(PeriodLength with sum as PeriodLength2))&$orderby=yearMonth","endpoint":"worklogsOnly","type":"Columns","w":6,"h":4,"chartSettings":{"backgroundColor":"#38ACEC","showLegend":true,"name":""},"xAxis":{"type":"date","title":"","rotation":90,"granularity":"month","minGridDistance":50},"yAxis":{"type":"duration","title":""},"series":{"fieldY":"PeriodLength2","fieldX":"yearMonth"},"autoSubtitle":false,"timeframeFilter":null,"y":13,"x":0,"dataAdapters":[{"name":"FillMissingDatePoints"}],"odataVersion":"v3.2"}`

## Filter by Custom Field value

![Filter_Custom_Field_Value.png](/cms_trial/assets/11393478-de3c-4cba-87cd-79711a77f089.png)

This widget shows an example of how to filter by the specific value of your DevOps custom field on a work item.

`{"type":"FlatTable","id":"","query":"$select=CustomStringField1,CustomStringField2,TrackedItself,System_Id,System_Title,System_WorkItemType,System_TeamProject&$filter=CustomStringField1 eq 'Demo1' and CustomStringField2 eq 'Demo2' and TrackedItself gt 0 &$orderby=TrackedItself desc&customFields=Custom.DemoField,Custom.DemoField2","odataVersion":"v3.2","endpoint":"workItems","title":"Filter by custom field value","subTitle":null,"w":4,"h":3,"columns":[{"field":"CustomStringField1","title":"DemoField","width":100},{"field":"CustomStringField2","title":"DemoField2","width":100},{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-100},{"field":"TrackedItself","title":"Tracked","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":18,"x":0}`

## Work items without tracked time

This widget only shows work items that do not have any time tracked on them.

![Work_Items_without_Tracked_Time.png](/cms_trial/assets/d9b37759-1add-4246-b485-e2519569c429.png)

`{"type":"FlatTable","id":"","query":"$select=System_TeamProject,System_WorkItemType,System_Title,System_Id,TrackedItself&$filter=TrackedItself eq 0&$orderby=TrackedItself desc&$top=10","odataVersion":"v3.2","endpoint":"workItems","title":"Workitems without tracked time","subTitle":null,"w":4,"h":3,"columns":[{"field":"System_Id","title":"ID","formatter":"WorkItemId","width":60},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"Title","formatter":"WorkItemIndicator","width":-100},{"field":"TrackedItself","title":"Tracked","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":22,"x":0}`

## Tracked time on each work item by person - individual worklogs

This widget allows you to see each individual time log by user on every work item and the total time tracked.

![Ttracked_Time_Individual_Worklog.png](/cms_trial/assets/22dfba4b-09a0-4fd6-99ce-3190352a2824.png)

`{"type":"HierarchyTable","id":"","title":"Tracked time on each work item by person","subTitle":null,"w":8,"h":4,"odataVersion":"v3.2","endpoint":"workItemsHierarchyAllLevels","query":"$select=System_Id,System_Title,System_WorkItemType,System_TeamProject,TrackedTotal,System_AreaPath,Microsoft_VSTS_Common_ActivatedDate,Microsoft_VSTS_Common_ClosedDate,System_AssignedTo,System_State,CustomStringField1,CustomStringField2,HasChildren,TrackedItself&workItemsFilter=System_TeamProject eq 'SuperProject'&$filter=TrackedTotal gt 0&$orderby=TrackedTotal desc&customFields=Custom.DemoField,Custom.DemoField,Custom.DemoField,Custom.DemoField,Custom.DemoField","hierarchyField":"System_Id","childrenEndpoint":"workItemsHierarchyAllLevels","childrenQuery":"({hierarchyField})/AllWorklogs?$apply=groupby((User/Name,WorklogDate/ShortDate),aggregate(PeriodLength with sum as TrackedTotal))&$orderby=User/Name,TrackedTotal desc","hierarchyType":"rootExpandable","columns":[{"field":"System_Id","title":"WorkItem ID","formatter":"WorkItemId","width":-50},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"WorkItem Title","formatter":"WorkItemIndicator","width":-150,"expand":true},{"field":"User.Name","title":"Name","width":150},{"field":"ActivityType.Name","title":"Activity Type","width":-100},{"field":"System_AreaPath","title":"Area","width":100},{"field":"CustomStringField1","title":"Custom Field 1","width":-100},{"field":"CustomStringField2","title":"Custom Field 2","width":-100},{"field":"WorklogDate.ShortDate","title":"Time Entry Date","width":-150},{"field":"System_AssignedTo","title":"Developer Assigned","width":150},{"field":"System_State","title":"State","width":80},{"field":"Microsoft_VSTS_Common_ActivatedDate","title":"Start Date","width":-150},{"field":"Microsoft_VSTS_Common_ClosedDate","title":"Closed Date","width":-150},{"field":"TrackedTotal","title":"Total Hours","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":194,"x":0}`

## Tracked time on each work item by person's total tracked time

This widget allows you to see the total tracked time by user on every work item.

![Person_Total_Tracked_Time_per_Work_Item.png](/cms_trial/assets/bccbf9a9-637a-4099-b55e-08be1db2bf6b.png)

`{"type":"HierarchyTable","id":"","title":"Tracked time on each work item by person's total tracked time","subTitle":null,"w":8,"h":4,"odataVersion":"v3.2","endpoint":"workItemsHierarchyAllLevels","query":"$select=System_Id,System_Title,System_WorkItemType,System_TeamProject,TrackedTotal,System_AreaPath,Microsoft_VSTS_Common_ActivatedDate,Microsoft_VSTS_Common_ClosedDate,System_AssignedTo,System_State,CustomStringField1,CustomStringField2,HasChildren,TrackedItself&workItemsFilter=System_TeamProject eq 'SuperProject'&$filter=TrackedTotal gt 0&$orderby=TrackedTotal desc&customFields=Custom.DemoField,Custom.DemoField,Custom.DemoField,Custom.DemoField,Custom.DemoField","hierarchyField":"System_Id","childrenEndpoint":"workItemsHierarchyAllLevels","childrenQuery":"({hierarchyField})/AllWorklogs?$apply=groupby((User/Name),aggregate(PeriodLength with sum as TrackedTotal))&$orderby=User/Name,TrackedTotal desc","hierarchyType":"rootExpandable","columns":[{"field":"System_Id","title":"WorkItem ID","formatter":"WorkItemId","width":-50},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"WorkItem Title","formatter":"WorkItemIndicator","width":-150,"expand":true},{"field":"User.Name","title":"Name","width":150},{"field":"System_AreaPath","title":"Area","width":150},{"field":"CustomStringField1","title":"Custom Field 1","width":-150},{"field":"CustomStringField2","title":"Custom Field 2","width":-150},{"field":"WorklogDate.ShortDate","title":"Time Entry Date","width":-150},{"field":"System_AssignedTo","title":"Developer Assigned","width":150},{"field":"System_State","title":"State","width":80},{"field":"Microsoft_VSTS_Common_ActivatedDate","title":"Start Date","width":-150},{"field":"Microsoft_VSTS_Common_ClosedDate","title":"Closed Date","width":-150},{"field":"TrackedTotal","title":"Total Hours","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":67,"x":0}`

## Tracked time on each work item by activity type

This widget allows you to see each individual time log by activity type on every work item and the total time tracked.

![Track_Time_Activity_Type.png](/cms_trial/assets/139d7dca-6164-48df-a6ba-e509507e2b32.png)

`{"type":"HierarchyTable","id":"","title":"Tracked time on each work item by activity type","subTitle":null,"w":8,"h":4,"odataVersion":"v3.2","endpoint":"workItemsHierarchyAllLevels","query":"$select=System_Id,System_Title,System_WorkItemType,System_TeamProject,TrackedTotal,System_AreaPath,Microsoft_VSTS_Common_ActivatedDate,Microsoft_VSTS_Common_ClosedDate,System_AssignedTo,System_State,CustomStringField1,CustomStringField2,HasChildren,TrackedItself&workItemsFilter=System_TeamProject eq 'SuperProject'&$filter=TrackedTotal gt 0&$orderby=TrackedTotal desc&customFields=Custom.DemoField,Custom.DemoField,Custom.DemoField,Custom.DemoField,Custom.DemoField","hierarchyField":"System_Id","childrenEndpoint":"workItemsHierarchyAllLevels","childrenQuery":"({hierarchyField})/AllWorklogs?$apply=groupby((ActivityType/Name),aggregate(PeriodLength with sum as TrackedTotal))&$orderby=ActivityType/Name,TrackedTotal desc","hierarchyType":"rootExpandable","columns":[{"field":"System_Id","title":"WorkItem ID","formatter":"WorkItemId","width":-50},{"field":["System_Title","System_WorkItemType","System_TeamProject"],"title":"WorkItem Title","formatter":"WorkItemIndicator","width":-150,"expand":true},{"field":"ActivityType.Name","title":"Activity Type","width":150},{"field":"System_AreaPath","title":"Area","width":150},{"field":"CustomStringField1","title":"Custom Field 1","width":-150},{"field":"CustomStringField2","title":"Custom Field 2","width":-150},{"field":"WorklogDate.ShortDate","title":"Time Entry Date","width":-150},{"field":"System_AssignedTo","title":"Developer Assigned","width":150},{"field":"System_State","title":"State","width":80},{"field":"Microsoft_VSTS_Common_ActivatedDate","title":"Start Date","width":-150},{"field":"Microsoft_VSTS_Common_ClosedDate","title":"Closed Date","width":-150},{"field":"TrackedTotal","title":"Total Hours","width":100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":62,"x":0}`

## Epics with their children items

This widget filters to only show Epic work items and their children, along with the total time tracked and time tracked individually on each work item. If your top work items are not Epics and you wish to see the top level work item with its children, then simply remove the *$filter=System\_WorkItemType eq 'Epic'* part of the widget definition.

![Epics_with_Children_Items.png](/cms_trial/assets/a2a30aa1-7425-421f-a037-d09e65139ec0.png)

`{"type":"HierarchyTable","id":"","title":"Epics with children","subTitle":"","w":8,"h":4,"odataVersion":"v3.2","endpoint":"workItemsHierarchyAllLevels","query":"$select=System_WorkItemType,System_Id,System_TeamProject,System_Title,System_State,System_AssignedTo,System_IterationPath,TrackedTotal,TrackedItself&$filter=System_WorkItemType eq 'Epic'&workitemsFilter=System_TeamProject eq 'SuperProject'","hierarchyField":"System_Id","childrenEndpoint":"workItemsHierarchy","childrenQuery":"({hierarchyField})/Children?filter=System_WorkItemType eq 'Task'","hierarchyType":"rootExpandable","columns":[{"field":["System_Id","System_WorkItemType","System_TeamProject"],"title":"ID","formatter":"WorkItemIdWithIndicator","width":-150},{"field":"System_Title","title":"Work Item Title","formatter":"","width":-400},{"field":"System_State","title":"Status","formatter":"","width":-100},{"field":"System_AssignedTo","title":"Assigned To","formatter":"","width":-200},{"field":"System_IterationPath","title":"Iteration Path","formatter":"","width":-250},{"field":"TrackedItself","title":"Tracked On This","width":-100,"formatter":"TimeLength"},{"field":"TrackedTotal","title":"Tracked Total","width":-100,"formatter":"TimeLength"}],"autoSubtitle":false,"timeframeFilter":null,"y":48,"x":0}`