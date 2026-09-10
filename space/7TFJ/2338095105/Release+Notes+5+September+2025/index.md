# Release Notes 5 September 2025

**Release date**: September 5, 2025

Our team is thrilled to announce the latest release of 7pace Timetracker for Jira.

---

## Enhancements

## Time approvals for Managers

**7pace for Jira** now includes time approvals for submitted worklogs! This feature improves accuracy and accountability, leading to more accurate reporting and billing. Managers can quickly review, approve, or reject team members’ timesheets directly within Jira. See [Time approvals for Managers](/cms_trial/space/7TFJ/2290122780/Time+approvals+for+Managers/) for more information.

## 'Show items' added to Timesheet view

The Timesheet view has been updated to include the option to show work items from previous weeks. Worklogs for the previous time period are displayed within the Timesheet alongside the current time period. Options include showing the previous week, previous two weeks, and previous month of worklogs. See [Timesheet view](/cms_trial/space/7TFJ/1828782116/Timesheet+view/) for more information.

## API version 2.0 updates

Version 2.0 of the 7pace API has been updated. Changes include improved error codes when creating or updating worklogs and updates to the structure of worklog responses. The updated worklogs endpoint now returns more complete data on custom fields. See [API version 2](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=7tfj&title=API%20version%202&linkCreation=true&fromPageId=2338095105) for more information.

## Bug Fixes

- **Worklogs endpoint returns incorrect error code when trying to update a deleted or non-existent worklog** - The `/worklogs` endpoint returns a 500 error when trying to update a deleted or otherwise non-existent worklog when it should return a 404 error. This has been resolved.
- **Creating worklogs with an invalid externalItemID logs an error even when the worklog is created** - The `/worklogs` endpoint logs an error when creating a new worklog with an invalid value for `externalItemId`. This has been resolved - worklogs will still be created, but no error will be logged.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1235398/7pace-timetracker-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](mailto:support@7pace.com).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support inspires us to improve our apps continually. We appreciate your trust in 7pace Timetracker for Jira!