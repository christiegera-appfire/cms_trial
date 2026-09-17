# Release Notes 17 September 2026

**Release date**: September 17, 2026

Our team is thrilled to announce the latest release of 7pace Timetracker for Jira.

## New features

### Worklogs Audit Log

Track complete history for created, edited, and deleted worklogs, including support for custom fields, saved filters, and affected users.

### Additional Custom Rules

You can now forbid logging time by work item type and status.

## Fixes

### Google Calendar Read-Only Calendars Missing

Fixed an issue where Google Calendars with readonly permissions (such as shared team or national holiday calendars) were excluded from the calendar integration.

### Public API: Custom Fields Returning Null

Fixed a bug in the public API where custom fields returned `null` instead of their values on the `/api/v2/worklogs/views/incrementalChanges` endpoint.

### Weekly View Suggestions Timeout

Resolved an issue where worklog suggestions timed out when loading the Weekly view.

### Smart Suggestions for Newly Created Issues

Fixed an issue where work items were not suggested if an assignee was set during issue creation.

### Custom Project Avatars in Times Explorer

Fixed broken image rendering for custom project avatars in Times Explorer.

### Monthly View Auto-Opening Daily Panel

Corrected behavior in Monthly view so the daily detail panel no longer automatically opens upon switching months

### Custom Rules Filter Toggle Retention

Fixed a UI glitch in Custom Rules where search filter toggles were unintentionally disabled when leaving the configuration menu quickly.

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1235398/7pace-timetracker-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](mailto:support@7pace.com).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support inspires us to continually improve our apps. We appreciate your trust in 7pace Timetracker for Jira!