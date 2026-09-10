# Release Notes 7 October 2025

**Release date**: October 7, 2025

Our team is thrilled to announce the latest release of 7pace Timetracker for Jira.

---

## Enhancements

## Improved Calendar integration - Smart suggestions!

Tired of searching for the same item for every daily meeting? The system will make the connection for you!

Calendar integrations have been improved with smart suggestions. When you connect a calendar, 7pace Timetracker will now automatically suggest work items to which a new worklog will be linked when converting a calendar entry into a worklog. These suggestions are based on matching event titles, Jira item keys included in titles or descriptions, and recurring items that were included in previous worklogs.

![7pace Timetracker for Jira release note screenshot for October 2025 update](/cms_trial/assets/6f1a6be9-99ef-499a-b720-abc242a7b59d.png)

## Additional filters on 'Show items' option

The Timesheet view has been updated to include the option to show work items from previous weeks. Worklogs for the previous time period are displayed within the Timesheet alongside the current time period. Options include showing the previous week, previous two weeks, and previous month of worklogs. See [Timesheet view](/cms_trial/space/7TFJ/1828782116/Timesheet+view/) for more information.

## Updated error reporting for APIs

The 7pace API has been updated to provide better error messages when users encounter an issue with the API. These updates currently apply only to [version 2](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=7tfj&title=API%20version%202&linkCreation=true&fromPageId=2430206009) of the API.

## Bug Fixes

- **Calendar unlinking requires confirmation** - In some instances, unlinking a calendar from integration encountered an error. Additionally, unlinking did not require a confirmation. The errors have been resolved, and unlinking has been updated to require confirmation before completing the update.
- **Order of properties causes errors when creating or updating worklogs through the API** - Version 2 of the API encounters errors when the properties of custom fields are submitted in the wrong order. This has been resolved and worklogs should be created successfully no matter what order properties are included.
- **Calendar titles are not copied to worklog comments** - In some instances, particularly when a calendar event is not generally visible, the title of the event is not correctly copied to the worklog comment. This has been resolved.
- **Users added to 7pace do not have access** - In some instances, users who have been added to 7pace Timetracker explicitly still do not have access to the app. This has been resolved.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1235398/7pace-timetracker-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](mailto:support@7pace.com).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support inspires us to improve our apps continually. We appreciate your trust in 7pace Timetracker for Jira!