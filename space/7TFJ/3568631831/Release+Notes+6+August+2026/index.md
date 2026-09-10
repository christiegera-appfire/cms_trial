# Release Notes 6 August 2026

**Release date**: August 6, 2026

Our team is thrilled to announce the latest release of 7pace Timetracker for Jira.

---

### Improvements

**Improved month navigation in the date range picker** — The date range component now uses a single pair of left/right arrows that advances both calendars together, with the right calendar always showing the next month relative to the left.

**Suggestions now propose custom fields and comments even without duration** — Item View Suggestions no longer skip items that lack enough data for duration prediction; they will still suggest comment-only or custom-field-only entries.

**Item is mandatory by default for new accounts** — New accounts are now created with the "Item is mandatory" setting enabled, promoting more complete and accurate reporting data from the start. Existing accounts are unaffected.

**Smoother Add Time Dialog in Issue Context** — Opening and closing the ATD on the Issue Context page now features an expand/collapse animation instead of a jarring layout jump.

### Bug Fixes

**View active timer button no longer blocked in sandboxed frame** — The "View active timer" button now correctly opens the linked issue. Previously it was blocked by browser sandbox permissions.

**Times Explorer filters — correct item removed from multi-value list** — Deleting a single value from a multi-value filter no longer removes the wrong entry.

**ATD no longer resets fields when clearing a suggested external item** — The Add Time Dialog now preserves user-entered field values instead of resetting to initial suggestions when the suggested work item is cleared.

**Date format consistency fix** — Worklog dates are now displayed and accepted in a consistent format, resolving a long-standing issue where European-format dates had to be entered in American format.

**BigPicture workday boundaries corrected** — The WorkdayBoundaries calculation now uses actual capacity values from BigPicture instead of deriving capacity solely from start/end dates, ensuring accurate suggestions and daily views for BP-integrated users.

**Custom fields at space level no longer conflict with "Require a work item"** — Fixed an issue where having space-level custom fields together with the "Require a work item" setting caused duplicate field errors.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1235398/7pace-timetracker-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](mailto:support@7pace.com).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support inspires us to continually improve our apps. We appreciate your trust in 7pace Timetracker for Jira!