# 7pace Timetracker API's

## What kind of API's does 7pace Timetracker have and what are they used for?

7pace has three sets of API's:

- [REST CRUD API](/cms_trial/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3/)
- [Client (Tracking) API](/cms_trial/space/7TFA/1253540758/7pace+Timetracker+Client+(Tracking)+API/)
- [Reporting API](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/)

The [REST CRUD API](/cms_trial/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3/) allows you to perform standard time tracking operations such as tracking time, submitting time for approval, approving time, etc. Any operation that you perform from the UI is available through the REST CRUD subset of API's.

The REST CRUD API also allows you to get information about the following:

- Active and inactive Timetracker users
- User roles and assigned licenses (and to manage them)
- Activity types
- Approval state of weeks

For example, you can [export a list of all licensed users](/cms_trial/space/7TFA/1253539939/How+to+export+a+list+of+all+licensed+users/) by using the *users/roles* endpoint of the REST CRUD API, or you can fetch the approval state from a specific date with the *timeApproval* endpoint, and also use the same endpoint to send weeks for approval or revoke approval with a POST REST API call.

There is also the *workLogs* endpoint that can be used to see a list of worklogs for the current user or from all of the users, and it can also be used to create worklogs either for just one user or multiple users, or even a batch of worklogs all at once.

With the *activityTypes* endpoint you are able to see the state of the activity types in your system, their names and ID's.

The [Client (Tracking) API](/cms_trial/space/7TFA/1253540758/7pace+Timetracker+Client+(Tracking)+API/) is used by the 7pace Timetracker web interface, as well as our downloadable desktop app. Our web client and desktop app offer a user friendly UI with several options to track time. The Client API allows you to perform the same actions as the web client and the desktop app, by utilizing a REST call. Although this may not be something that you would use on a daily basis, it allows integration and communication with third-party tools and apps. It can be used to build an integration of Timetracker with other applications.

The [Reporting API](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) allows you to get a combined output from both 7pace Timetracker’s own data as well as Azure DevOps’ proprietary data.

This API encompasses Timetracker data such as worklogs, the work items linked to worklogs, and the ability to build queries to work items and their hierarchy.

The Timetracker Reporting API and most of the syntax supported is based on the OData framework.

We have extensive [documentation and tutorials](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/) on how to use the Reporting API to achieve your reporting needs. We also have a [Widgets Gallery](/cms_trial/space/7TFA/1253540063/7pace+Timetracker%27s+Reporting+Widgets+Gallery/) that we continuously update with new reporting widgets that address the needs of our users.

The main thing that can be achieved with the Reporting API is to create reports which can help Timetracker users in their day to day reporting needs.

For instance you can have a report that tells you all the time that has been tracked on your work items between two dates, who tracked it, what is the work item ID, its name and the work item status it is in, and also to which budget it belongs to. For this purpose you would use the *workLogsWorkItems* endpoint as it provides data both from DevOps work items as well as Timetracker worklogs (tracked time).

To get just the Timetracker data about tracked time that you can export to be used use somewhere else, you should use the *workLogsOnly* endpoint, which is a simple and fast endpoint.

If you wish to see total tracked time rolled up to the root work item, the *workItemsHierarchy* endpoint is designed for this purpose. It will show time that has been tracked on all of the children work items rolled up and summed to the root item level.

However, to see the entire hierarchy and what was tracked on each individual work item within the hierarchy, you will need to use the workItemsHierarchyAllLevels endpoint.