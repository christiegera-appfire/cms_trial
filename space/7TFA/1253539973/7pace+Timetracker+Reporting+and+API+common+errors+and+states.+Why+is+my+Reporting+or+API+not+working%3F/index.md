# 7pace Timetracker Reporting and API common errors and states. Why is my Reporting or API not working?

The most common issue faced with Reporting is with the Service Account losing authorization. You can find the resolution for this in the section of this article here: [Service account has lost authorization](/cms_trial/space/7TFA/1253539973/7pace+Timetracker+Reporting+and+API+common+errors+and+states.+Why+is+my+Reporting+or+API+not+working%3F/)

## **Question 1**

I’m getting a message that says "*Reporting restart has been initiated"* and that "*this can take some time depending on the number of work items in DevOps and worklogs in 7pace Timetracker.*" Why is my reporting page being restarted?

![FAQ_TimeTracker_Reporting.png](/cms_trial/assets/1c709eff-e0eb-4f27-b510-981bebe451b9.png)

### Answer

Please refer to the answer listed for Question 2. It also works for the issue described in Question 1.

## **Question 2**

7pace Timetracker Reporting or API  (and therefore Excel, PowerBi, etc.) is not working and I am seeing "*Current Report State is Being processed"* (for more than a day now) / "*Error Calling DevOps API"* / "API call returns *Unauthorized* message." Why is my Reporting or API not working?

### Answer

The Reporting page may be restarting or processing due to the following reasons:

- The Reporting page was accessed for the very first time by someone in your DevOps organization and is being refreshed.  
  *SOLUTION:* This is normal behavior and no action is necessary. Please wait for Reporting to build.
- Reporting & API were not used for six (6) months or more.  
  SOLUTION: This is normal behavior and no action is necessary. Please wait for Reporting to rebuild.
- Reporting was restarted manually by someone from Settings -> Reporting & API.  
  *SOLUTION:* Please wait for the restart to complete in order to use 7pace Timetracker Reporting.
- Your [Service Account](/cms_trial/space/7TFA/1253540778/7pace+Timetracker+Service+Account/) has lost authorization.  
  *SOLUTION:* The user who is set as your Service Account user needs to log in and access any 7pace Timetracker page, where they will be prompted to authorize 7pace Timetracker. It is required for the Service Account user to [authorize Timetracker by using a DevOps PAT](/cms_trial/space/7TFA/1253540459/Use+a+Personal+Access+Token+to+authorize+7pace+Timetracker+for+ADO+Cloud/).  
  In order to check which user is set as the Service Account, please navigate to 7pace Timetracker Settings -> Reporting and API -> Service Account.

The time necessary for Reporting to process all data depends on the amount of data you have both in 7pace Timetracker and in Azure DevOps. It can take from 30 minutes to several hours in some cases (up to 4 hours).  
If the reporting restart is taking longer, you will need to check the reporting health state error message by navigating to 7pace Timetracker *Settings -> Reporting & API* and click on the Details button:

![FAQ_TimeTracker_Reporting_Settings_Details.png](/cms_trial/assets/e8e2da99-6bf7-40c9-b6eb-0f2f8ddf178c.png)

COMMON REPORTING AND API ERRORS FOUND UNDER CURRENT REPORT STATE / API ERROR MESSAGES

**Problem**: Error with Service Account authorization/permissions:

- You will find keywords like ***Token, authorize, Service Account*** in the reporting state error details

Examples:

- *Could not perform request to DevOps Services. Token may be invalid. Refresh token or check AAD Settings.*
- *7pace Timetracker is not authorized. Personal Access Token (PAT) has expired or has been revoked.*
- *Error occurred calling the DevOps API. Please click Details for more info.*
- *Token for Service Account … is empty*

**Solution:** Your Service Account user needs to log in and access any 7pace Timetracker page, where they will be prompted to authorize 7pace Timetracker. It is required for the Service Account user to [authorize 7pace Timetracker by using a DevOps PAT](/cms_trial/space/7TFA/1253540459/Use+a+Personal+Access+Token+to+authorize+7pace+Timetracker+for+ADO+Cloud/).

**Problem**: *Cannot insert the value NULL into column 'System\_State', table 'tfstimetracker\_db.dbo.WorkItemCacheEntry'; column does not allow nulls. UPDATE fails.*

**Solution:** This issue can only be solved with the help of the 7pace team, so please contact 7pace Timetracker Support at support@7pace.com.

## **Question 3**

I'm receiving an error saying “Not allowed parameter in request” when I try to execute an Odata request on the workitem-related endpoint with $select=WorkItem. What should I do?

### Answer

Worklogs can be tracked via comments only, and for those worklogs, the complex property WorkItem is null. Odata can't process null for complex types on workitem-related endpoints. Add a filter to exclude the workitem with the null value, e.g.

$filter=WorkItem ne null

and the error message should disappear.

## **Question 4**

**Why do I get a timeout expired error from the Timetracker Reporting API and how do I avoid it?**

### Answer

Some fields that the Reporting API endpoints return are not just stored in our database as values, but calculated every time that users make requests. These are referred to as calculated fields.

Calculating these fields - "**TrackedItself**", "**TrackedTotal**", "**TrackedItselfBillable**", "**TrackedTotalBillable**" - is a heavy operation, so retrieving them can take a considerable amount of time. This might lead to a "timeout expired" exception if a user requests a large amount of data. In this case, we suggest decreasing the amount of data by using more filters or removing calculated fields from the select statement if you don't need them.

### How to sort and filter by calculated fields

Usually, it's relatively easy to sort or filter data by some value, but with calculated fields, their values should be calculated first and then filtered or sorted. For example, let's say a user runs a query that returns the first 100 rows ordered by *TrackedItself* field. Only 100 rows are requested, but the application has to calculate *TrackedItself* for the whole organization's work items based on all worklogs that were ever tracked to just sort them.

The same approach is true for filtering by calculated fields - both operations are extremely heavy and there's a good chance that it could lead to a timeout exception. That's why we've made additional filtering required.

Right now, it's impossible to sort or filter by a calculated field based on all data for all times. If such a filter or order is added to query, then using *worklogsFilter* becomes required to limit the number of worklogs for calculation. Learn more about *worklogsFilter* [here](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/).

Here are some examples:

// this query is allowed because it doesn't use sorting or filtering by a calculated field  
https://your\_org\_name.timehub.7pace.com/api/odata/v3.0/workitems?$select=System\_Id,System\_WorkItemType,TrackedItself&$filter=System\_TeamProject eq 'My project'  
  
// following queries will throw an exception   
// because worklogsFilter is not used and values are calculated basing on all worklogs  
https://your\_org\_name.timehub.7pace.com/api/odata/v3.0/workitems?$select=System\_Id,System\_WorkItemType,System\_TeamProject,TrackedItself&$filter=System\_TeamProject eq 'My project'&$orderby=TrackedItself desc  
https://your\_org\_name.timehub.7pace.com/api/odata/v3.0/workitems?$select=System\_Id,System\_WorkItemType,System\_TeamProject,TrackedItself&$filter=System\_TeamProject eq 'My project' and TrackedItself ge 3600  
  
// these queries are allowed -   
// although they use filtering or sorting by a calculated field   
// those calculations are based on worklogs filered by dates,   
// so TrackedItself would contain sums of worklogs from a specified month only  
https://your\_org\_name.timehub.7pace.com/api/odata/v3.2/workitems?$select=System\_Id,System\_WorkItemType,System\_TeamProject,TrackedItself&$filter=System\_TeamProject eq 'My project'&$orderby=TrackedItself desc&worklogsFilter=Timestamp ge 2023-05-01 and Timestamp lt 2023-09-01  
https://your\_org\_name.timehub.7pace.com/api/odata/v3.2/workitems?$select=System\_Id,System\_WorkItemType,System\_TeamProject,TrackedItself&$filter=System\_TeamProject eq 'My project' and TrackedItself ge 3600&worklogsFilter=Timestamp ge 2023-05-01 and Timestamp lt 2023-09-01

### Sort and filter by other fields

Most work item fields can be used in any statement without any issues, but some of them are not really expected to be used for filtering or sorting, so queries are slow in such cases.

You can find the list of fields available to sort by in your 7pace [Timetracker Reporting API Reference](https://timehub.7pace.com/api_reference/index.html?urls.primaryName=7pace%20Timetracker%20API%20documentation%20v3.2), at the very end of the bottom of the Reference page in the ReportingWorkItem model schema.

Below you can find a list of some of the available fields:

System\_AreaId  
System\_CreatedBy  
System\_NodeName  
System\_Reason  
System\_RevisedDate  
Microsoft\_VSTS\_CMMI\_Blocked  
Microsoft\_VSTS\_CMMI\_FoundInEnvironment  
Microsoft\_VSTS\_CMMI\_HowFound  
Microsoft\_VSTS\_CMMI\_Probability  
Microsoft\_VSTS\_CMMI\_RequirementType  
Microsoft\_VSTS\_CMMI\_RequiresReview  
Microsoft\_VSTS\_CMMI\_RequiresTest  
Microsoft\_VSTS\_CMMI\_RootCause  
Microsoft\_VSTS\_CMMI\_TargetResolveDate  
Microsoft\_VSTS\_CMMI\_TaskType  
Microsoft\_VSTS\_CMMI\_UserAcceptanceTest  
Microsoft\_VSTS\_Common\_ActivatedBy  
Microsoft\_VSTS\_Common\_ActivatedDate  
Microsoft\_VSTS\_Common\_BacklogPriority  
Microsoft\_VSTS\_Common\_BusinessValue  
Microsoft\_VSTS\_Common\_ClosedBy  
Microsoft\_VSTS\_Common\_ClosedDate  
Microsoft\_VSTS\_Common\_Discipline  
Microsoft\_VSTS\_Common\_Issue  
Microsoft\_VSTS\_Common\_Priority  
Microsoft\_VSTS\_Common\_Rating  
Microsoft\_VSTS\_Common\_ResolvedBy  
Microsoft\_VSTS\_Common\_ResolvedDate  
Microsoft\_VSTS\_Common\_ResolvedReason  
Microsoft\_VSTS\_Common\_ReviewedBy  
Microsoft\_VSTS\_Common\_Risk  
Microsoft\_VSTS\_Common\_Severity  
Microsoft\_VSTS\_Common\_StackRank  
Microsoft\_VSTS\_Common\_StateChangeDate  
Microsoft\_VSTS\_Common\_TimeCriticality  
Microsoft\_VSTS\_Common\_Triage  
Microsoft\_VSTS\_Common\_ValueArea  
Microsoft\_VSTS\_Scheduling\_CompletedWork  
Microsoft\_VSTS\_Scheduling\_DueDate  
Microsoft\_VSTS\_Scheduling\_Effort  
Microsoft\_VSTS\_Scheduling\_FinishDate  
Microsoft\_VSTS\_Scheduling\_OriginalEstimate  
Microsoft\_VSTS\_Scheduling\_RemainingWork  
Microsoft\_VSTS\_Scheduling\_Size  
Microsoft\_VSTS\_Scheduling\_StartDate  
Microsoft\_VSTS\_Scheduling\_StoryPoints  
Microsoft\_VSTS\_Scheduling\_TargetDate

## **Question 5**

How to solve "Response 406.0 from Timetracker server" error?

I'm trying to use the reporting API Odata endpoint from Excel, but I'm getting a HTTP 406 error: "Response 406.0 from Timetracker server". My coworker, who is using a different version of Excel gets a different error along the lines of "Unexpected error. Cannot access a disposed object ..." etc. Can you help?

### Answer

These are known issues in the latest versions of Excel and Power BI\* that have already been reported to Microsoft.

Here is a [related topic in Power BI.](http://community.powerbi.com/t5/Issues/After-upgrade-Odata-functions-are-missing-in-connector/idi-p/453753)  
  
If you receive “Error 406” when connecting Excel to 7pace Timetracker’s reporting API, please check the query details through the Advanced Editor:

![FAQ_TimeTracker_Response_406.png](/cms_trial/assets/69afa3aa-bdd2-48e8-844f-7f8f000284c6.png)

If you find the Implementation=”2.0” setting, please remove it from the query and check if the issue persists:

![FAQ_Work_Items.png](/cms_trial/assets/5bdad1a1-7272-499a-976e-985765bb2172.png)

If you were not able to resolve your issues by following the steps described, please contact 7pace Timetracker Support at support@7pace.com.