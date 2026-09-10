# 7pace Timetracker's Reporting API "This set of parameters is not allowed" error

## Problem

Why do I get a *This set of parameters is not allowed* in the request error in 7pace Timetracker's Reporting API and how do I avoid it?

## Probable cause

The Odata library used for the Odata API has been updated because the new version contains important improvements. However, some of the improvements lead to broken compatibility.

Since the 7.5.0 version, the Odata library does not allow users to select the whole object – only specific properties. Currently, work is being done to find a workaround to fix that and to allow queries to keep working, but unfortunately, according to this [information from GitHub](https://github.com/OData/WebApi/pull/2320), it is not possible. Given that the Odata library developers are unlikely to change this back, it is only possible to provide ways to modify the query.

## Solution

The most likely answer is that you are trying to use the **Budget** or **Work Item** field in the `$select` filter of your OData request.

For example: `api/odata/v3.0/workLogsWorkItems?$select=WorkItem`

Currently, you cannot put **Work Item** or **Budget** fields in a select statement to get the whole Work Item or Budget objects with all their fields. You can only select certain fields of these objects by putting them in the select statement.

For example: `api/odata/v3.0/workLogsWorkItems?$select=WorkItem/System_Id`

If you need more than one property, please type them out, separated by commas.

For example: `api/odata/v3.0/workLogsWorkItems?$select=WorkItem/System_Id,WorkItem/BudgetAssignmentType,WorkItem/System_AreaId`

If you need to see all fields, please remove the `$select` statement from the query to see the full object in the response.

**Fix standard widgets**

Go to the widget configuration panel and replace OData Query.

**Tracks of today** widget

| Before:  `$orderby=Timestamp desc&$top=100&$select=WorkItemId,Timestamp,PeriodLength,User,ActivityType,WorkItem,Comment` | After:  `$orderby=Timestamp desc&$top=100&$select=WorkItemId,Timestamp,PeriodLength,User,ActivityType,WorkItem/System_Title,WorkItem/System_WorkItemType,WorkItem/System_TeamProject,Comment` |
| --- | --- |

**Tracks of yesterday** widget

| Before:  `$orderby=Timestamp desc&$top=100&$select=WorkItemId,Timestamp,PeriodLength,User,ActivityType,WorkItem,Comment` | After:  `$orderby=Timestamp desc&$top=100&$select=WorkItemId,Timestamp,PeriodLength,User,WorkItem/System_Title,WorkItem/System_WorkItemType,WorkItem/System_TeamProject,Comment` |
| --- | --- |

**Latest Worklogs** widget

| Before:  `$orderby=Timestamp desc&$top=100&$select=WorkItemId,Timestamp,PeriodLength,User,ActivityType,WorkItem,Comment` | After:  `$orderby=Timestamp desc&$top=100&$select=WorkItemId,Timestamp,PeriodLength,User,ActivityType,WorkItem/System_Title,WorkItem/System_WorkItemType,WorkItem/System_TeamProject,Comment` |
| --- | --- |

If you require additional assistance or have any remaining questions, please contact us at support@7pace.com and let us know your specific use case.