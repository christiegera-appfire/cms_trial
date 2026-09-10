# 7pace Timetracker Reporting API Version 3

With 7pace Timetracker 5, we introduce the Reporting API v3. This API encompasses Timetracker data such as worklogs, the work items linked to worklogs, and the ability to build queries to work items and their hierarchy.

## 7pace Timetracker API & Reporting Tutorial

## How to compose a 7pace Timetracker API call

In addition, you could check our tutorial video about the Reporting page, where we also utilize our API: [7pace Timetracker's Reporting Page](/cms_trial/space/7TFA/1253539934/7pace+Timetracker%27s+Reporting+Page/).

## Timetracker Reporting API Overview

The Timetracker Reporting API and most of the syntax supported is based on the OData framework. For an overview on OData query language, please follow these pages: [OData documentation](http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part2-url-conventions.html) and [Aggregation Extension](http://docs.oasis-open.org/odata/odata-data-aggregation-ext/v4.0/cs01/odata-data-aggregation-ext-v4.0-cs01.html). If you see something that's not working, please let us know.

For the entire API reference, please see [API reference](https://timehub.7pace.com/apireference/?urls.primaryName=7pace%20Timetracker%20API%20documentation%20v3.0-preview#/OData%20Reporting%20API).

To find your Reporting API URL, navigate to the *Settings* tab of **Timetracker** > **Reporting & REST API** section.

![Reporting_API_Overview.png](/cms_trial/assets/b6427a57-41b0-40db-b9ea-b1e287ffe30d.png)

## Reporting and API Limits

When Reporting is enabled, there are several things of which you should be aware. First, the [Service Account should be enabled](/cms_trial/space/7TFA/1253540778/7pace+Timetracker+Service+Account/) to make the Reporting API work.

All data displayed in 7pace Timetracker related to work items switches to using the Reporting API internally. This means that changes to work items in DevOps might not be reflected immediately in the interface but may take between two minutes and an hour to display. To force an update, please navigate to **Settings** > **Reporting and API—API** and click **Schedule update now**.

The API returns data as paged:

- Worklogs endpoints return data by 1000 items per page
- All endpoints related to work items return data by 100 items per page

When data is paged, the response object presents a "@odata.nextLink" property with a link to the next page.

Abuse or excessively frequent requests to GitHub via the API may result in the temporary or permanent suspension of your Account's access to the API. GitHub, in our sole discretion, will determine abuse or excessive usage of the API. We will make a reasonable attempt to warn you via email prior to suspension.

You may not share API tokens to exceed GitHub's rate limitations.

## WorkItem Fields Naming Convention

## Complex Field Names

Due to OData specifics, we can’t use a standard DevOps delimiter for field references, and therefore, we use “\_” in complex field names instead of “.” everywhere.

If the DevOps field name is “[System.Id](http://System.Id)”, it will be “System\_Id” in Timetracker Reporting API responses.

## Object and Sub-Object Access

In 7pace Timetracker Reporting widgets, when viewing or reconfiguring the OData Query and Console fields within a widget, please note that the **OData Query** field requires a forward slash ("/"), and the **Console** field requires a dot ("."). Therefore, the same data would be displayed as in the examples, below:

*OData Query:* **WorkItem/Microsoft\_VSTS\_Common\_Activity**  
*Console:* **WorkItem.Microsoft\_VSTS\_Common\_Activity**

Keep in mind that for custom field parameters, you must provide the original DevOps field reference, so if you have “Some.CustomField”, you should pass it to the customFields parameter unchanged. Please refer to [this section](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) for additional details on [custom fields](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/).

Also, if an object contains other objects as a part of it, you must split the objects with a forward slash. For example: WorkItem.Microsoft\_VSTS\_Common\_Activity - Here, the **WorkItem** is the object and the field (**Microsoft\_VSTS\_Common\_Activity**) is another object, so we separate it with a forward slash "/": **Microsoft/VSTS\_Common\_Activity**.

Finally, a note on pulling data related to **Activity Types**: You will need to use an endpoint that contains the 7pace Timetracker-specific field ActivityType, like the WorkLogsWorkItems or WorkLogsOnly endpoints. The field **Microsoft.VSTS.Common.Activity** is a **DevOps field**, and **ActivityType** is a**7pace Timetracker** **field**.

## API endpoints overview

This overview details the purpose and intended use of every Reporting endpoint that 7pace Timetracker provides.

In addition to the standard OData parameters that Timetracker provides, there are also several extending options to the query; please see the links, below, for more detail.

Worklog time is provided in *seconds*; if you require *hours* in your environment, please divide PeriodLength (and all similar properties in the API) by 3600.

### worklogsOnly

This endpoint is the fastest one; it only provides data related to worklogs without joining workloads to related work items.

This is the endpoint you should choose if you need to integrate with other systems based on work item IDs only.

Usage scenarios:

1. Report: "How many hours did every user add into the system during a specific period?"

   `/workLogsOnly?$apply=filter(Timestamp ge 2019-11-01T00:00:00Z and Timestamp lt 2019-12-01T00:00:00Z)`  
   `/groupby((User/Name),aggregate(PeriodLength with sum as PeriodLength))`  
   `&$orderby=User/Name`
2. "Sum of time for the whole team during specific date range"

   `/workLogsOnly?$filter(Timestamp ge 2019-11-01T00:00:00Z and Timestamp lt 2019-12-01T00:00:00Z)`  
   `/aggregate(PeriodLength with sum as PeriodLength)`
3. Scenarios with aggregating worklogs by User, Activity Type, Budget, Date, and others

### worklogsWorkItems

This endpoint provides data on all worklogs, but also includes information on the work item that the worklog linked to in the work item property.

The workItem field contains all standard fields that DevOps has itself and additional fields CustomStringField1-CustomStringField5, CustomNumericField1-CustomNumericField5, CustomBooleanField1-CustomBooleanField5. 

Use these fields to load data from fields you created for work items manually that are not a part of any DevOps standard template.

**Note**: There is no way to load HTML or text fields over Timetracker's Reporting API.

[Check full reference here.](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/)

Usage scenarios:

1. Report: "Team personal time per Project"  
   Sample query:

   `/workLogsWorkItems?$apply=groupby((User/Name,WorkItem/System_TeamProject,WorklogDate/ShortDate),`  
   `aggregate(PeriodLength with sum as PeriodLength))`  
   `&$orderby=WorklogDate/ShortDate desc`
2. Report: "Distribution of time per project"

   `/workLogsWorkItems?$apply=groupby((WorkItem/System_TeamProject),`  
   `aggregate(PeriodLength with sum as PeriodLength))`  
   `&$orderby=WorkItem/System_TeamProject`
3. Scenarios with aggregating worklogs by Project, Area Path, Iteration, Assigned To and others

### workItems

As opposed to the *worklogsOnly* and *worklogsWorkItems* endpoints*,* this endpoint (and workItemsHierarchy, workItemsHierarchyAnyLevel) provides you with a way to retrieve time data already aggregated by work items.

The workItems endpoint displays all the standard fields of work items and the ability to get [any custom field](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) created in work items.

Further, this endpoint provides information as a flat object with combined information from DevOps and Timetracker, extending work item objects with the following fields from Timetracker:

- TrackedItself - the sum of time for all worklogs directly assigned to this work item
- TrackedItselfBillable - sum of Billable time for all related worklogs
- BudgetAssignmentType - type of budget assignment for this work item
- Budget - budget or empty
- Optional property containing parent work item (if present) or first work item in the hierarchy, click [here](https://appfire.atlassian.net/wiki/spaces/7TFA/pages/edit-v2/1253540266#%5BhardBreak%5DExpanding-%2F-Retrieving-linked-objects) on how to retrieve linked optional properties in Timetracker Reporting API
- CustomStringField1-5, CustomNumericField1-5 and CustomBooleanField1-5 can be used to retrieve non-standard fields from work items, please click [here](https://appfire.atlassian.net/wiki/spaces/7TFA/pages/edit-v2/1253540266#customFields) for details.

Usage scenarios:

1. Get all work items that have time tracked on them:

   `/workItems?$filter=TrackedItself gt 0`
2. Get a summary on an Iteration: how many hours tracked on a specific iteration:

   `/workItems?$filter=TrackedItself gt 0 and System_IterationPath eq 'Project Name/Iteration Path'`

### workItemsHierarchy / workItemsHierarchyAllLevels

Both workItemsHierarchy and workItemsHierarchyAllLevels provide information similar to the workItems endpoint but allow you to also get information on Parent-Children.

The key differences between *workItemsHierarchy* and *workItemsHierarchyAllLevels* are the following:

- *workItemsHierarchy,* by default, returns only items that do not have parents (e.g., Epics), and it is possible to navigate to children through parents.
- *\*workItemsHierarchyAllLevels* returns data irrelevant of the Parent-Children hierarchy, so it can return the Parent and its Child in the same response, on the same level, if the user doesn’t apply the correct filtering. It is up to the API consumer to provide the correct filtering, e.g., by work item type (see samples below).

For this endpoint, workitemsFilter may be required for some actions. If you see an error, it may be because your query doesn't contain the required workItemsFilter parameter. To add that parameter, follow these steps:

1. Select workItemsHierarchyAllLevels and click the **Load**button.
2. Double-click on the query to open the Power Query Editor.
3. Click **Advanced Editor** on the top-left part of the window.
4. Change the script by adding the workItemsFilter field.

Similar to the workItems object, the work item is extended with fields from Timetracker. It has all the fields that workItems provides, along with the following additions:

- TrackedTotal - summary of all tracked time against the item and all children work items
- TrackedTotalBillable - summary of all billable time against the item and all children work items
- HasChildren - flag identifying that specific work item has children items
- Parent - optional property containing parent work item, if present
- Root - optional property containing the first work item in the hierarchy
- RollupValue1-RollupValue5 - set of up to 5 fields allowing to roll-up numeric values to the work item from all children, e.g. rollup Effort or Story Points. Click [here](https://appfire.atlassian.net/wiki/spaces/7TFA/pages/edit-v2/1253540266#To-use-our-customFields%2FrollupFields-parameters-in-Excel-or-Power-BI%3A) for more details.

To identify whether the item has children items, HasChildren is used as a call to the Children path:

`/workItemsHierarchy(x)/Children`

Sample usage:

1. Get a report for Epic work items that have time within a specific period, add a summary for Effort as an additional field, and order by tracked time, descending:

   `/workItemsHierarchy?$select=System_Id,System_WorkItemType,System_TeamProject,`  
   `System_Title,TrackedTotal,TrackedItself,RollupValue1,`  
   `System_State,System_AreaPath,System_AssignedTo,HasChildren`  
   `&$filter=TrackedTotal gt 0&$orderby=TrackedTotal desc`  
   `&rollupFields=Microsoft.VSTS.Scheduling.Effort`
2. Get a report for all Product Backlog Items and Bugs for a specific period (from 3.2 API version):

   `/v3.2/workItemsHierarchyAllLevels?$select=System_Id,System_WorkItemType,System_TeamProject,System_Title,TrackedTotal,TrackedItself,System_State,`  
   `System_AreaPath,System_AssignedTo,HasChildren,Microsoft_VSTS_Scheduling_Effort`  
   `&$filter=TrackedTotal gt 0&workItemsFilter=System_WorkItemType eq 'Product Backlog Item' or System_WorkItemType eq 'Bug'`

### Budgets

This endpoint provides data related to Timetracker budgets. If you need to integrate with other systems based on Budgets, including related Work Items and Worklogs, you should choose this endpoint.

Usage scenarios:

1. Get overview of all budgets

   `/budgets`

### Expanding / Retrieving linked objects

Some properties or linked objects can be retrieved by requesting specific paths or providing $expand parameters. This applies to *workItems / workItemsHierarchy / workItemsHierarchyAllLevels* endpoints, so in essence to all work item related endpoints.

**Object expanding**

*Parent* field - retrieves the Parent item of all work items returned by the API.

(In old API versions it might be called ParentItem)

Sample:

`/workItems?$expand=Parent&$select=System_Id,Parent`

*Root* field - retrieves the root item of all work items returned by the API, it is the first work item in the hierarchy.

Sample:

`/workItems?$expand=Root&$select=System_Id,Root`

When expanding the Parent or Root field, if you wish to only have certain properties expanded from the field, you will need to specify which properties you want returned by using $select along with the $expand command, as in the example below where we are only selecting the System\_Id from the Root field.

`/workItems?$expand=Root($select=System_Id)&$select=System_Id,Root`

When expanding objects within Excel and Power BI, even though it is possible to manually expand objects and fields in these apps, due to their logic, the query should always contain the expand command for the Parent and Root fields. When it is not possible to adjust your query you can get the Parent or Root field values by calling the field itself - endpoint(id)/expandablefield. An example for this is given below:

`/workItems(id)/Parent`

**Parent endpoint**

Retrieves the Parent of specific work items (x is the ID of work item). The endpoint is available in API v3.1 and later:

workItems(x)/Parent

**Root endpoint**

Retrieves the first work item in the hierarchy of specific work items (x is the ID of work item).  
The endpoint is available in API v3.2 and later:

workItems(x)/Root

**Children**

Endpoint provides access to the information of direct children work items.

Sample:

/workItems(x)/Children

**DirectWorklogs / AllWorklogs**

Returns worklogs related only to that specific work item (*DirectWorklogs*) or all worklogs from the item itself and all children (*AllWorklogs*). *AllWorklogs*endpoint is available in API v3.1 and later:  
Sample:

`/workItems(x)/DirectWorkLogs`  
`/workItems(x)/AllWorklogs`

**worklogsOnlyWithDeleted** / **workLogsWorkItemsWithDeleted**

Only available in 3.3-beta

Usage scenarios:  
See all changed worklogs during a specific period.

`/workLogsWorkItemsWithDeleted?$filter(EditedTimestamp lt 2023-09-01T00:00:00Z and EditedTimestamp ge 2023-08-11T00:00:00Z)&$orderBy=Timestamp desc&$select=Id,IsDeleted,Comment`

## Timetracker OData Query Extended Parameters

- [worklogsFilter](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) for filtering worklogs before executing queries
- [workItemsFilter](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) for filtering work items before executing queries
- [customFields](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) for including own fields into response
- [rollupFields](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) for adding summary of specific fields
- [prefilter (filter by Me)](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/)

We covered topics, above, that detailed how to get information on work items and pure worklogs.

When retrieving data by work items, you might need to get work items time tracked to those work items, during a specific timeframe and/or by a specific person, Activity Type, etc.

Timetracker provides extension syntax for filtering worklogs and work items in any of the endpoints listed above. As additional parameter types are not part of the OData syntax, they do not have $-sign prefix.

All filters use OData syntax; see the syntax description [here.](http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part2-url-conventions.html)

### worklogsFilter

Use this filter to limit worklogs returned by the API. This filter should be applied first in the processing of the query, with all other filters applied after it, including workItemsFilter.

![Worklogs_Filter.png](/cms_trial/assets/0dc053f7-5cf7-447a-9a32-79e17ee26962.png)

How worklogsFilter is applied, only green Worklogs will be processed

Example

Let’s assume we need to pull a report on "How much time was spent on an Epic during a specific timeframe?". The following query will return all Epics, but it will not filter worklogs by date:

`/workItemsHierarchy/?$select=System_Id,System_WorkItemType,System_TeamProject,System_Title,`  
`TrackedTotal,TrackedItself`  
`&$filter=System_WorkItemType eq 'Epic'`

To achieve our goal we should define worklogsFilter in the request:

`/workItemsHierarchy/?$select=System_Id,System_WorkItemType,System_TeamProject,System_Title,`  
`TrackedTotal,TrackedItself`  
`&$filter=System_WorkItemType eq 'Epic'`  
`&worklogsFilter=Timestamp ge 2019-09-30T00:00:00Z and Timestamp lt 2019-11-05T00:00:00Z`

The filter parameter ...

`worklogsFilter=Timestamp ge 2019-09-30T00:00:00Z and Timestamp lt 2019-11-05T00:00:00Z`

... will make the API return *TotalTracked* and *TrackedItself* for work items computed only by workLogs between 30 September and 5 November 2019.

### workItemsFilter

Similar to worklogsFilter, this filter applies to the work items that will be processed by the API call. The filter is applied after worklogsFilter.

![WorkItems_Filter.png](/cms_trial/assets/c53b85bc-e438-42e9-a9ab-24bd8da4087d.png)

How workItemsFilter is applied, only green Worklogs and Work Items will be processed

This filter is applied after the *worklogsFilter*.

Example

We want to build a report on “How much time was spent on Project A”.  
The following query may help:

`/worklogsOnly?$apply=aggregate(PeriodLength with sum as PeriodLength)`

This will return the sum of all projects, not just Project A, so to filter by Project A \_before\_ aggregating, we should use a workItemsFilter:

`/worklogsOnly?$apply=aggregate(PeriodLength with sum as PeriodLength)`  
`&workItemsFilter=System_TeamProject eq 'Project A'`

Now, the number will be computed only by work items from Project A.

*workItemsFilter* has an additional parameter: *workItemFilterApplyTarget*

This parameter accepts following values:

- AllWorkItems (default value): when this value is provided, the *workItemsFilter* will be applied to all work items
- RootWorkItems: when this value is provided, the *workItemsFilter* will be applied only to top-level work items (items that do not have parents)

### customFields

Displays any custom string field for workItems  
**Endpoints:** workItems; workItemsHierarchy  
**How to use:** Specify up to five (5) custom field names for each data type (string, numeric, boolean), *separated by a comma in the select part of your query or the OData field in our Reporting Widget.* They will appear in:  
*CustomStringField1...CustomStringField5* fields in result objects for string fields  
*CustomNumericField1...CustomNumericField5* fields in result objects for numeric fields  
*CustomBooleanField1...CustomBooleanField5* fields in result objects for boolean fields

7pace Timetracker detects the type of passed field and puts the value in accordingly. All fields are sequentially numbered (e.g. when you select custom fields with different data types, as described in the example below).

Please note that it takes up to 24 hours for DevOps custom fields to appear in Timetracker reporting.

Also, only the OData $filter can be used with custom fields, the Timetracker prefilters (worklogsFilter,workItemsFilter) will not work with them.

Example

Let's say you have 'ProjectCode', 'Custom.Finance' and 'AdditionalField.Order' custom fields in your work items. You can add a parameter this way:

`/workItemsHierarchy?$select=System_Id,System_Title,TrackedTotal,CustomStringField1,CustomStringField2,CustomNumericField3&customFields=ProjectCode,Custom.Finance,AdditionalField.Order`

To find the correct name of your custom field you will have to navigate to your Organization Settings Processes and open the Process where the custom field is located. Once there, select the field you wish to use and check Field Reference Name under the field Options.

`"CustomStringField1": "648521",`  
`"CustomStringField2": "Finance 2",`  
`"CustomNumericField3": 3`

### To use our customFields/rollupFields parameters in Excel or Power BI:

1. Double-click the query to open Power Query Editor.

![Power_Query_Editor.png](/cms_trial/assets/32f02059-2523-4a90-be5e-172d496722ad.png)

2. Click **Advanced Editor** in the top-left part of the window.

![Advanced_Editor.png](/cms_trial/assets/1eed8b2a-57c4-4f1c-84fd-98bb3852f9f9.png)

3. Add customFields/rollupFields parameter using "Query" statement with the syntax from the following screenshot and save the query.

![Work_Items.png](/cms_trial/assets/4b5b6dc0-7fcf-479e-b8a3-07ceb97a199a.png)

Field reference name for pt.3, above, can be found when editing a field in process customization settings in DevOps (**Organization Settings** > **Process** > **Select process** > **Select Work Item Type** > **Edit field**).

![Edit_Field_Effort_Epic.png](/cms_trial/assets/6d50f7bc-e8fd-4154-aca0-4b41c4f2f7bf.png)

### rollupFields

Allows you to get roll-up summary fields that contain the sum of specified **numeric** field values from all children items, including the current item.  
**endpoints:** workItemsHierarchy  
**How to use:** specify up to five (5 ) roll-up field name,s *separated by comma*. They will appear in  
*RollupValue1 ... RollupValue5* fields in result objects.

Example

Let's say you use the 'Effort' field in work items. If you'd like to sum efforts of an item and all its child items, you can add a parameter this way:

`/workItemsHierarchy?rollupFields=Microsoft.VSTS.Scheduling.Effort`

You'll get work items with fields such as:

`"RollupValue1": 47,`

### prefilter (filter by Me)

If you'd like to see just data related to your account only, you can use the query parameter **prefilter=Me**.  
In this case, all data will be filtered by an authorized account that performs a query.  
Default parameter value is **prefilter=NoFilter** (not required).

### Using POST Requests

The query options part of an OData URL can be quite long, potentially exceeding the maximum length of URLs supported by components involved in transmitting or processing the request.

For POST requests append /$query to the resource path of the URL and pass the query options part of the URL in the request body. The request body must use the content-type text/plain.

Usage scenarios:

1 Report: "How many hours did every user add into the system during a specific period?"

Sample query for GET request:

`/workLogsOnly?$apply=filter(Timestamp ge 2019-11-01T00:00:00Z and Timestamp lt 2019-12-01T00:00:00Z)`  
`/groupby((User/Name),aggregate(PeriodLength with sum as PeriodLength))`  
`&$orderby=User/Name`

Sample query for POST request:

`/workLogsOnly/$query`

Headers:

`Content-Type: text/plain`

Body:

`apply=filter(Timestamp ge 2019-11-01T00:00:00Z and Timestamp lt 2019-12-01T00:00:00Z)`  
`/groupby((User/Name),aggregate(PeriodLength with sum as PeriodLength))`  
`&$orderby=User/Name`

2 Report: "Team personal time per Project"

Sample query for GET request:

`/workLogsWorkItems?$apply=groupby((User/Name,WorkItem/System_TeamProject,WorklogDate/ShortDate),`  
`aggregate(PeriodLength with sum as PeriodLength))`  
`&$orderby=WorklogDate/ShortDate desc`

Sample query for POST request:

`/workLogsWorkItems/$query`

Headers:

`Content-Type: text/plain`

Body:

`$apply=groupby((User/Name,WorkItem/System_TeamProject,WorklogDate/ShortDate),`  
`aggregate(PeriodLength with sum as PeriodLength))`  
`&$orderby=WorklogDate/ShortDate desc`

## Budget Information in Worklogs and Work Items

The Reporting API follows the same behavior as Budgets, described [here](/cms_trial/space/7TFA/1253540085/Budgets/).

Every work item or worklog in the API has the following fields: *BudgetId*, *Budget* and *BudgetAssignmnetType*. Budgets can be either inherited or directly assigned; the *BudgetAssignmnetType* field indicates what kind of assignment every item has.

The following BudgetAssignmentType values are possible in the ReportingAPI v3.x:

- `NotComputed`: Budget is not yet computed and has an undefined state. Due to the nature of Budget computation in ReportingAPI 3, it runs asynchronousley and has delays between creating work items in DevOps and proper budget assignment computation in Timetracker.
- `NoBudget`: Budget was not set for either this item, for its parents or iterations of the item.
- `DirectlyAssigned`: Budget was assigned directly to the work item.
- `InheritedFromParent`: Budget was assigned to one of the parent work items. The closest parent is the defining budget.
- `InheritedFromIteration`: Budget assigned to the iteration or any parent iteration of the work item. Closest parent iteration is the defining budget.

## Widget Chart Parameter Options

Below, you will find the six (6) available widget types found on the Reporting page of 7pace Timetracker.  We have listed the various parameters available within each widget chart type so that you can create your own widget or edit existing widgets and what fields you need to accomplish this.

To see our separate article with custom widgets gallery, please click [here](/cms_trial/space/7TFA/1253540063/7pace+Timetracker%27s+Reporting+Widgets+Gallery/).

![Widget_Chart_Parameter_Options.png](/cms_trial/assets/b643e43b-75a9-4c72-a495-b428670eca41.png)

## Line Chart Fields

![Line_Chart_Fields.png](/cms_trial/assets/9bfcc2de-96e4-48ed-93f9-eec4733b3e03.png)![Activity_Types.png](/cms_trial/assets/4096a063-01e0-4910-aa01-0e5a5a300c8f.png)

```text
{
   "chartSettings": {
       "strokeWidth": number,
       "strokeColor": string, - //for example "#38ACEC"
       "backgroundColor": string, - //for example "#38ACEC"
   },
   "xAxis": {
       "type": "date" or "value" or "category" or "duration",
       "title": string,
       "rotation": number, - //Rotation of the axis title in degrees
       "granularity": "minute" or "hour" or "day" or "week" or "month" or "year", - //Used to indicate what are the base units of your data.
       "toolTipDisabled": boolean,
       "minGridDistance": number, - //Minimum distance in pixels between grid elements.
       "durationFormat": string,
       "minValue": number, - //A minimum value for the axis scale. (Only for "duration" axios type)
   },
   "yAxis": {
       "type": "date" or "value" or "category" or "duration",
       "title": string,
       "rotation": number, - //Rotation of the axis title in degrees
       "granularity": "minute" or "hour" or "day" or "week" or "month" or "year", - //Used to indicate what are the base units of your data.
       "toolTipDisabled": boolean,
       "minGridDistance": number, - //Minimum distance in pixels between grid elements.
       "durationFormat": string,
       "minValue": number, - //A minimum value for the axis scale. (Only for "duration" axios type)
   },
   "series": {
       "fieldY": string,
       "fieldX": string
   },
   "colorField": string, - //field name where stored color value
   "dataAdapters": [
{
           "name": "NullToComment" or "YearMonthToDate" or "NotSetActivityTypeFormat" or "StrokeForLightColor" or "SumOverPeriod", "FillMissingDatePoints", "AggregateDataSetsByMutualField"
           "params": string
         }
   ]
}
```

## Column Chart fields

![Column_Chart_Fields.png](/cms_trial/assets/782876a9-5066-4be2-a4b6-ff2f49795491.png)

```text
{
   "chartSettings": {
       "backgroundColor": string, - //for example "#38ACEC"
   },
   "xAxis": {
       "type": "date" or "value" or "category" or "duration",
       "title": string,
       "rotation": number, - //Rotation of the axis title in degrees
       "granularity": "minute" or "hour" or "day" or "week" or "month" or "year", - //Used to indicate what are the base units of your data.
       "toolTipDisabled": boolean,
       "minGridDistance": number, - //Minimum distance in pixels between grid elements.
       "durationFormat": string,
       "minValue": number, - //A minimum value for the axis scale. (Only for "duration" axios type)
   },
   "yAxis": {
       "type": "date" or "value" or "category" or "duration",
       "title": string,
       "rotation": number, - //Rotation of the axis title in degrees
       "granularity": "minute" or "hour" or "day" or "week" or "month" or "year", - //Used to indicate what are the base units of your data.
       "toolTipDisabled": boolean,
       "minGridDistance": number, - //Minimum distance in pixels between grid elements.
       "durationFormat": string,
       "minValue": number, - //A minimum value for the axis scale. (Only for "duration" axios type)
   },
   "series": {
       "fieldY": string,
       "fieldX": string
   },
   "colorField": string, - //field name where stored color value
   "dataAdapters": [
         {
           "name": "NullToComment" or "YearMonthToDate" or "NotSetActivityTypeFormat" or "StrokeForLightColor" or "SumOverPeriod", "FillMissingDatePoints", "AggregateDataSetsByMutualField"
           "params": string - //parameters depends on adapter type
         }
   ]
}
```

## Stacked Bar Chart fields

![Stacked_Bar_Chart_Fields.png](/cms_trial/assets/d007c395-8928-4071-bbf2-ea96fc06c975.png)

```text
{
   "chartSettings": {
      "backgroundColor": string, - //for example "#38ACEC"
  },
   "xAxis": {
       "type": "date" or "value" or "category" or "duration",
       "title": string,
       "rotation": number, - //Rotation of the axis title in degrees
       "granularity": "minute" or "hour" or "day" or "week" or "month" or "year", - //Used to indicate what are the base units of your data.
       "toolTipDisabled": boolean,
       "minGridDistance": number, - //Minimum distance in pixels between grid elements.
       "durationFormat": string,
       "minValue": number, - //A minimum value for the axis scale. (Only for "duration" axios type)
       "opposite": boolean - //Indicates whether Axis should be drawn on the opposite side of the plot area than it would normally be drawn based on chart's settings.
   },
   "yAxes": [{
       "type": "date" or "value" or "category" or "duration",
       "title": string,
       "rotation": number, - //Rotation of the axis title in degrees
       "granularity": "minute" or "hour" or "day" or "week" or "month" or "year", - //Used to indicate what are the base units of your data.
       "toolTipDisabled": boolean,
       "minGridDistance": number, - //Minimum distance in pixels between grid elements.
       "durationFormat": string,
       "minValue": number, - //A minimum value for the axis scale. (Only for "duration" axios type)
  }],
   "series": {
       "fieldY": string, - //field name for category in X axis
       "fieldX": string, - //field name for category in Y axis
       "seriesFields": [
         {
           "field": string,
           "stacked": boolean,
           "axis": string,
           "title": string
         }
       ]
  },
  "dataAdapters": [
         {
           "name": "NullToComment" or "YearMonthToDate" or "NotSetActivityTypeFormat" or "StrokeForLightColor" or "SumOverPeriod", "FillMissingDatePoints", "AggregateDataSetsByMutualField"
           "params": string - //parameters depends on adapter type
         }
   ]
}
```

## Pie/Donut Chart fields

![Pie_Chart_Fields.png](/cms_trial/assets/ff05fe69-5752-4bed-850f-ab8596abcb55.png)

```text
{
   "chartSettings": {
      "name": string, - //series name
      "innerRadius": number, - //donut circle inner radius,
      "radius": number, - //donut circle outer radius
      "disableTitle": bool, - //define if show title in chart for each segment
      "disableTicks": bool, - //should ticks be disabled
      "disableLabels": bool, - //define if show labels
      "labelsMaxWidth": number - //maximum label width in chart
      "tooltip": string, - //tooltip text
      "showPercent": bool, - //if show percent or just values
      "units": string - //units name
  },
   "categoryField": string, - //field name where to put data from for category
   "valueField": string, - //field name where to put data from for value
   "valueFormat": string - //format string
   "colorField": string, - //field name where stored color value
   "dataAdapters": [
         {
           "name": "NullToComment" or "YearMonthToDate" or "NotSetActivityTypeFormat" or "StrokeForLightColor" or "SumOverPeriod", "FillMissingDatePoints", "AggregateDataSetsByMutualField"
          "params": string - //parameters depends on adapter type
         }
   ]
}
```

## Number Chart fields

![Number_Chart_Fields.png](/cms_trial/assets/bd70e14b-88c2-4ac8-a2d1-3de18dfec867.png)

```text
{
   "showCount": boolean, - //if true widget will show not the data itself, but their number
   "formatter": string, - //formatter name to format number
   "fieldName": string - //field name where to get data from
}
```

## Table fields

![Table_Fields.png](/cms_trial/assets/22689b36-a010-4d9f-a6e2-eccdc312aa7e.png)

```text
{
  "columns": [{
        "field": string || string[], - //field name can be as just string as array.
        "title": string, - //column title
        "formatter": string, - //formatter name to format column
        "width": number - //column width
     }
  ]
}
```

## Drilldown Table fields

![Drilldown_Table_Fields.png](/cms_trial/assets/56cd8d13-f529-4a43-8340-372ab46aac52.png)

```text
{
"hierarchyField": string, -// parentId to filter children query
"hierarchyType": string, -// criteria to expand children items
  "columns": [{
       "field": string || string[], - //field name can be as just string as array.
       "title": string, - //column title
       "formatter": string, - //formatter name to format column
       "width": number - //column width
       "expand": true, - //if column expandable
       "child": {
        "field": "yearMonth" //expand field to show
      }
    }
 ]
}
```

### hierarchyType

The hierarchyType field in the reporting widget console is used to identify criteria to expand children items in Drill-down table widgets:

- *workLogs*- always expandable on any level
- *workItems* - expandable when *HasChildren == true* and something is tracked on children (*TrackedTotal - TrackedItself > 0*)
- *rootExpandable*- root level is expandable, child level isn't
- *byHasChildrenField*- expandable if *HasChildren == true*

Default "Epics by person" hierarchyType has been updated to *rootExpandable*. To see time spent by persons on all workitems (even if there are only direct worklogs, with no tracks on children), update the *hierarchyType* field in the reporting console manually.

## Data Formatters

Data formatters allow modifications to be made in how data is presented in Widgets.

For example, worklogs time is saved in seconds and the API also returns it in seconds. However, most people want to see time displayed in hours or in "HH:MM" format. This is where data formatters come in.

## TimeLength formatter

**Purpose:** displays number field (number of seconds) in TimeLength format (for Example 69 seconds = 00:01:09)  
**How to use:** add field "formatter": "TimeLength" to the column

**Example:**

```text
{
 "columns": [
 ...,
 {
   "field": "TrackedItself",
   "title": "Tracked",
   "width": 100,
   "formatter": "TimeLength"
 },
 ...
 ]
}
```

## NullToComment formatter

**Purpose:** if a cell's value is null or empty, then view text "(No Work Item)"  
**How to use:** add field "formatter": "NullToComment" to the column

**Example**

```text
{
 "columns": [
 ...,
 {
   "field": "System_AssignedTo",
   "title": "Assigned To",
   "formatter": "NullToComment",
   "width": 150
 },
 ...
 ]
}
```

## Number formatter

**Purpose:** displays the number field in the desired format  
**How to use:** add field "formatter": "Number" and "format": "#.#" to the column.

**Example**

```text
{
 "columns": [
 ...,
 {
   "field": "System_Id",
   "title": "ID",
   "formatter": "Number",
   "format": "#,###.00",
   "width": 100
 },
 ...
 ]
}
```

## String formatter

**Purpose:** displays field in string format  
**How to use:** add field "formatter": "String" to the column

**Example**

```text
{
 "columns": [
 ...,
 {
   "field": "System_AssignedTo",
   "title": "Assigned To",
   "formatter": "String",
   "width": 150
 },
 ...
 ]
}
```

## WorkItemId formatter

**Purpose:** displays the work item id as a link that opens the work item  
**How to use:** add field "formatter": "WorkItemId" to the column

**Example**

```text
{
 "columns": [
 ...,
 {
   "field": "System_Id",
   "title": "ID",
   "formatter": "WorkItemId",
   "width": 100
 },
 ...
 ]
}
```

## WorkItemType formatter

**Purpose:** displays the typeof work item  
**How to use:** add field "formatter": "WorkItemType" and "field": ["System\_WorkItemType", "System\_TeamProject"] to the column

**Example**

```text
{
 "columns": [
 ...,
 {
   "field": [
     "System_WorkItemType",
     "System_TeamProject"
 ],
 "title": "Type",
 "formatter": "WorkItemType",
 "width": 100
 },
 ...
 ]
}
```

## WorkItemIndicator formatter

**Purpose:** displays the title of the work item and its type  
**How to use:** add field "formatter": "WorkItemIndicator" and "field": ["System\_Title", "System\_WorkItemType", "System\_TeamProject"] to the column

**Example**

```text
{
 "columns": [
 ...,
 {
   "field": [
     "System_Title",
     "System_WorkItemType",
     "System_TeamProject"
 ],
 "title": "Title",
 "formatter": "WorkItemIndicator",
 "width": 100
 },
 ...
 ]
}
```

## WorkItemIdWithIndicator formatter

**Purpose:** displays the title of the work item with its type as a link that opens the work item  
**How to use:** add fields "formatter": "WorkItemIndicator" and "field": ["System\_Title", "System\_WorkItemType", "System\_TeamProject"] to the column

**Example**

```text
{
 "columns": [
 ...,
 {
 "field": [
    "System_Title",
    "System_WorkItemType",
    "System_TeamProject"
 ],
 "title": "Title",
 "formatter": "WorkItemIdWithIndicator",
 "width": 100
 },
 ...
 ]
}
```

## LocaleSettingsDateTime formatter

**Purpose:** displays DateTime value in format that is defined in Timetracker Locale Settings  
**How to use:** add field "formatter": "LocaleSettingsDateTime" to the column

**Example**

```text
{
 "columns": [
 ...,
 {
   "field": "System_CreatedDate",
   "title": "Date",
   "formatter": "LocaleSettingsDateTime",
   "width": 200
 },
 ...
 ]
}
```

## CustomDateTime formatter

**Purpose:** displays DateTime value in the format that is defined in "format" field DateTime formatting article  
**How to use:** add fields "formatter": "LocaleSettingsDateTime" and "format": "DD.MM.YYYY H:mm" to the column

**Example**

```text
{
 "columns": [
 ...,
 {
   "field": "System_CreatedDate",
   "title": "Date",
   "formatter": "CustomDateTime",
   "format": "DD.MM.YYYY H:mm",
   "width": 200
 },
 ...
 ]
}
```

## DateTimeAgo formatter

**Purpose:** displays DateTime value in DevOps Azure format (for example: "Today at 2:30 PM")  
**How to use:** add field "formatter": "DateTimeAgo" to the column

**Example**

```text
{
 "columns": [
 ...,
 {
   "field": "System_CreatedDate",
   "title": "Date",
   "formatter": "DateTimeAgo",
   "width": 200
 },
 ...
 ]
}
```

## MathExpression formatter

**Purpose:** performs math expressions on desired fields  
**How to use:** add

"field": ["Field\_0", "Field\_1", "Field\_N"],  // any fields from the model

"formatter": "MathExpression",

"format": {

   "expression": "( {0} + {1} ) \* {N}", // (any math expression using selected fields) to the column  
   "resultFormat": "#.##" // see [Number Formatter](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/)

}

**Supported operations:**see [this](https://www.npmjs.com/package/math-expression-evaluator#supported-symbols) reference

**Example**

```text
{
 "columns": [
 ...,
 {
    "field": [
       "TrackedTotal", // {0}
       "Microsoft.VSTS.Scheduling.Effort" // {1}
     ],
    "title": "Pace",
    "width": 80,
    "formatter": "MathExpression",
    "format": {
       "expression": "{0} / 3600 / {1}",
       "resultFormat": "#.#"
    }
},
 ...
 ]
}
```

## How Reporting works

The Reporting API is based on the asynchronous building of data in the background when Reporting is enabled for your organization.

As soon as the API is enabled and the Service Account is configured, 7pace Timetracker queues the DevOps API and fetches information about work items. This information is temporarily stored in an encrypted database hosted by 7pace. To build a relationship between work items and hierarchies, Timetracker also processes work item links and temporarily stores Parent-Child relations.

Information on work items and string, decimal and boolean field types are only stored temporarily; HTML and text fields such as "Description" are never stored, even temporarily.

The background job runs periodically within a two-minute-to-24-hour time-range, depending on changes made in work items within your DevOps organization. Information about when reporting was last processed, when it will run next, and the option to schedule an update is located in Settings -> Reporting and API -> API.

After a period 60 days of inactivity in the Reporting API, all data is removed from our databases, and Reporting becomes disabled. To reactivate the Reporting API, please navigate to the Reporting section in Timetracker or click "Schedule update now".

The Reporting API is based on OData and provides multiple endpoints. The full overview is located [here](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/).

## Connecting to API (Excel, C#, python, javascript)

To connect to the API, you must first [generate a Timetracker API token](/cms_trial/space/7TFA/1253539983/7pace+Timetracker+API+Important+Information/). This can be done in **Settings** > **Reporting & REST API** section > click **Create New Token**. Use the generated token to connect to the API from any application. For on-premise, you must use NTLM authentication to connect to the API.

## Postman

## Excel / Power BI

1. To connect to the API with Excel, navigate to the *Data* tab, click *Get Data*, and select **From Other Sources** > **From OData Feed**.
2. On the resulting new window, insert "Your API Root" value.
3. Use "Basic" authorization, keep the username field empty, and use the token generated earlier as the password.
4. Select the endpoint you are interested in and click **Load**. You can also modify the data before it is loaded, like expanding properties or applying additional filtering or grouping.

See the following recording for reference:

![Excel_Power_BI.gif](/cms_trial/assets/97e0c3a8-a115-489a-a3d9-6a000e4ae3cc.gif)

## Pivot table example using Excel

![Pivot_Table_Example_Excel.png](/cms_trial/assets/fd0adccd-8a50-4ab7-a60a-80c3ecbcdbab.png)

We have created a pivot table template which can be downloaded here: ▢   
In this example, we are merging results from requests from two endpoints into two different tables and then summarizing this in a pivot table.

Instructions on how to use

1. On the *Parameters* tab, specify your organization name and the Epic ID you want to drill down to
2. Switch to the *PivotReport* tab, click on **Data**, and select **Refresh All**.

On the first launch of the table, you will also need to provide your credentials. Select *Basic* and input your API token (which is issued at **7pace Timetracker Settings** > **Reporting and REST API**) into the password field (you can keep the Username field blank or simply enter “user”).

This table can be used as is or it can be customized to your needs.

## Find users and work items without tracked time

We have composed Excel spreadsheets which connect to the Timetracker API and the DevOps API and fetch data on users who have not tracked time during a time period, and work items without tracked time during a time period.  
The instructions along with the downloadable files can be found here: ▢

## Filtering data / expanding work item columns

To get filtered worklogs, you can use a standard OData Feed **$filter** query parameter:  
<https://docs.microsoft.com/en-us/graph/query-parameters>

It can be done in Excel by Power Query. Select the *Data* tab > **Queries & Connections** and click **Edit**.

![Filter_Data_Work_Item_Columns.png](/cms_trial/assets/f5106d8e-480a-4ee4-bc36-c9245b553364.png)

You can filter values there using column filters. All changes will appear in the Advanced Editor query, which means that data is filtered on the server side.

![Advanced_Editor_Date_Timezone.png](/cms_trial/assets/7f12b445-a587-4b1b-afac-d3ae21e32667.png)

To get the work item title, the **worklogsWorkItems**endpoint can be used to get the worklogs list with work items assigned. This endpoint returns the WorkItem column as a record - it can be expanded with all the DevOps fields that you need.

![Search_By.png](/cms_trial/assets/e307e2df-73b0-4ef2-aae0-09ac7bbb8090.png)

## C#

There is sample code available on [GitHub](https://github.com/7pace/timetracker-api-samplecode) for a console application connecting to the API. Please check the application and source code to configure a connection to 7pace Timetracker.

## Python

This module accesses the 7pace time tracking Reporting API.  
Example usage:

```python
.. code-block:: python
​
 7pace_time_test.py
"""
import argparse
import base64
import json
import requests
​
​
def main(options):
 authentication = ('', '<your API token>')
 headers = {'$select': 'System_Id,System_WorkItemType,System_TeamProject,System_Title,TrackedTotal,TrackedItself,RollupValue1,System_State,System_AreaPath,System_AssignedTo,HasChildren', '$filter': 'TrackedTotal gt 0', '$orderby': 'TrackedTotal desc', 'rollupFields': 'Microsoft.VSTS.Scheduling.StoryPoints'}
 response = requests.get('<YOUR API ROOT>/workItemsHierarchy', auth=authentication, headers=headers).json()
 print (response)
if __name__ == '__main__':
 # pylint: disable=invalid-name
 parser = argparse.ArgumentParser(description='Access the 7pace time tracking REST API')
​
 main(parser.parse_args())
```

## JavaScript

```javascript
var request = require('request');

var options = {
 'method': 'GET',
 //this is sample request, use your query here
 'url': 'https://%ORG_NAME%.timehub.7pace.com/api/odata/v3.2/worklogsWorkItems?$top=1&$select=WorkItem/System_Id,Id',
 'headers': {
 'Authorization': 'Bearer %TOKEN%' //token is generated on Settings -> Reporting & REST API
 }
};
request(options, function (error, response) { 
 if (error) throw new Error(error);
 console.log(response.body);
});
```

### Accessing 7pace Timetracker with Node.js

*T*o use 7pace Timetracker REST/SignalR API in the DevOps Server environment, you don’t need tokens. All requests must be authorized with Negotiate authorization.

*To connect via node, this library allows for Kerberos authentication and returns the body correctly:* <https://www.npmjs.com/package/kerberos> *.*

Examples are available here:

1. Common example - <https://stackoverflow.com/questions/53302948/ntlm-api-access-with-node-js>

2. Working example for getting data from our API:

```javascript
import fetch from 'node-fetch';
import kerberos from 'kerberos';

async function getKerberosToken(servicePrincipal) {
  return new Promise((resolve, reject) => {
    kerberos.initializeClient(servicePrincipal, { }, (err, client) => {
      if (err) return reject(err);

      client.step('', (err, token) => {
        if (err) return reject(err);
        resolve(token);
      });
    });
  });
}

async function callProtectedApi() {
  try {
    const servicePrincipal = '<SPN>';
    const apiUrl = '<your url>';

    const kerberosToken = await getKerberosToken(servicePrincipal);

    const response = await fetch(apiUrl, {
      method: 'GET',
      headers: { 'Authorization': `Negotiate ${kerberosToken}` }
    });

    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}`);
    }

    const data = await response.text();
    console.log('API Response:', data);
  } catch (error) {
    console.error('Error:', error);
  }
}

callProtectedApi();
```

### 7pace Timetracker Reporting API: Using Dynamic Parameters in Excel Power Query

7pace Timetracker's reporting API feature that allows you real-time access to 7pace Timetracker data secured by OAuth, available in the format OData via REST in Microsoft Excel. Once accessed, it is just a couple of extra clicks to add the data from DevOps Server in the same way, dynamically, from DevOps Server itself. Your application for analysis will allow you to merge the data on your platform so that you have a much more flexible, dynamic experience than before.

Below, you'll find the steps on how you can dynamically use the parameters in Excel Power Query and load DevOps Server data based on the specified parameter values.

Remember to wrap the parameter values in your query into single (' ') quotes.

1. Open Microsoft Excel.

2. In a new worksheet, click **Insert** > **Table** and create a table of two (2) columns and two (2) rows, including the header row. You can name the first column header "Parameter" and the second column header "Parameter Value".

3. In the table, set up the parameters list as shown in the first screenshot, below (the Reporting API uses a specific parameters format; therefore, make sure to use these parameter values - see also, second screenshot):

![Insert_Table_Parameters.png](/cms_trial/assets/a4dbcd74-7713-488c-9621-5aba33dd9fda.png)

You must format the parameter values for "**Start Date**" and "**End Date**" in the **Parameters** column to **Text**.

4. Open a new Excel sheet and access the 7pace Timetracker data as OData feed.

5. For more information, see [7pace Timetracker Reporting API Version 3](https://support.7pace.com/hc/en-us/articles/360035502332-7pace-Timetracker-Reporting-API-Version-3#user-content-customfields).

6. Click the **Query** tab and then click the **Edit** button to open the original query text.

![Query_Edit.png](/cms_trial/assets/2d6a86f4-62ee-43d0-aee5-0d52ab52ba7b.png)

7. Click the **Advanced Editor** menu.

![Advanced_Editor_Menu.png](/cms_trial/assets/7b8950e1-3789-4397-b6df-1155a2a415e7.png)

The system displays the query in the advanced query editor. Below is the actual query text:

```text
let

    Source = OData.Feed("https://[your_organization_name].timehub.7pace.com/api/odata/v3.2/workLogsWorkItems?$orderby=Timestamp desc&$top=100&$select=EditedTimestamp,WorkItemId,Timestamp,PeriodLength,User,ActivityType,WorkItem/System_Title,WorkItem/System_WorkItemType,WorkItem/System_TeamProject,Comment", null, [Implementation="2.0"])

in 
```

8. Update the query as shown below.

Add the variables for the parameters and replace the actual values with these parameter variables.

The bold highlighted text below, represents the changes made to the original query.

![Query1.png](/cms_trial/assets/9432230d-758e-4517-b829-a5d939efa1f3.png)

```javascript
let

Parameter = Excel.CurrentWorkbook(){[Name="Parameters"]}[Content], // Report parameters table name

Param_StartDate = Parameter{0}[Parameter Values], // First table row: Start Date

Param_EndDate = Parameter{1}[Parameter Values], // Second table row: End Date

Source = OData.Feed("https://[your_organization_name].timehub.7pace.com/api/odata/v3.2/workLogsWorkItems?$select=WorkItemId,Timestamp,PeriodLength,User,ActivityType,WorkItem/System_Title,EditedTimestamp&workLogsFilter=EditedTimestamp gt "& Param_StartDate & " and EditedTimestamp lt "& Param_EndDate, null, [Implementation="2.0"])
in
Source
```

9. Click **Done** and go to the sheet where you accessed the OData feed.

10. Click the **Query** tab and select **Refresh**. You can also right-click within the sheet and select **Refresh**.

![Refresh.png](/cms_trial/assets/cddb8809-cf03-4496-b751-18a541445de1.png)

The data is loaded as per the changed parameter values. Afterwards, you can update the values in the Parameters table and refresh the query to reload the updated data.

#### Example of using Dynamic Parameters:

```javascript
let
       base = https://[your_organization_name].timehub.7pace.com/api/odata/v3.2/workItems?$select=System_Id,Parent,Budget/BudgetName&$expand=Parent($select=System_Id),
       mybudget = BudgetSelected,
       myfilter = "&workItemsFilter=Budget/BudgetName eq '" & mybudget & "'",
       uri = base & myfilter,
       Source = OData.Feed(uri, null, [Implementation="2.0"]),
       #"Expanded Budget" = Table.ExpandRecordColumn(Source, "Budget", {"BudgetName"}, {"Budget.BudgetName"}),
       #"Expanded Parent" = Table.ExpandRecordColumn(#"Expanded Budget", "Parent", {"System_Id"}, {"Parent.System_Id"})
in
       #"Expanded Parent"
```

### 7pace Timetracker Reporting API: CURL example

Since CURL does not accept spaces, they need to be replaced with "%20" in a CURL query. We also suggest using double quotes "" for the query URL. Please see example below:

`curl --location --request GET "https://{your-organization}.timehub.7pace.com/api/odata/v3.2/workLogsWorkItems?apply=filter(Parent%20ne%20null)/groupby((Parent,Timestamp,User/Name,WorkItem/System_Id,WorkItem/System_Title,WorkItem/System_TeamProject,ActivityType/Name,WorkItem/System_WorkItemType,Budget/BudgetName),aggregate(PeriodLength%20div%203600%20with%20sum%20as%20PeriodLength))&workItemsFilter=System_Id%20ne%20null&workLogsFilter=Timestamp%20ge%202022-09-01T00:00:00Z%20and%20Timestamp%20lt%202022-10-31T00:00:00Z&$expand=Parent($select=System_Id)" --header 'Authorization: Basic {your-token}'`