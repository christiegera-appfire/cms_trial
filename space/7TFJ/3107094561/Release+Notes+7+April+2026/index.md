# Release Notes 7 April 2026

**Release date**: April 7, 2026

Our team is thrilled to announce the latest release of 7pace Timetracker for Jira.

---

## **New Features**

- **Limit logging option**  
  Administrators can configure custom rules to limit logging and modifying time on closed Jira issues, with pre-set options for limiting changes to the last 3, 7, or 30 days.
- **Extended Worklog Approval Reporting API**  
  For advanced reporting, we've extended the worklog API. A new parameter, *include approval*, now allows you to pull approval attributes consistent with the data displayed in the time period explorer UI.
- **Pre-Scheduled Period for Historical Data Migration**  
  A new capability has been introduced during the initial period setup to add a pre-scheduled period. This feature is designed to aid migration and allows for the review and locking of historical worklogs.

## Improvements

- **Faster User Approval Fetching**
- **Enhanced Capacity and Approval Views**

  - Approval columns have been renamed to *approval period from* and *approval period to* to ensure they are correctly exportable and sortable as dates in Excel.
  - A new capacity source display clarifies that capacity calculations are based on BigPicture integration.
  - The *Total* column in the worklog table is now sticky, remains visible on narrow screens, and visually indicates capacity fulfillment by turning green when capacity is met.
- **Improved Worklog Suggestions and Calendar Handling**

  - A fix was implemented to ensure that Google Calendar events display correctly on the weekly calendar by properly handling discrepancies between the Google Calendar time zone and the user's configured time zone.
  - Worklog suggestion visuals and wording have been updated for better clarity, including more descriptive text and a toast notification that appears when a suggestion is successfully added.
- **Worklog Card UI Refinements**

  - The front-end rendering of worklog cards has been adjusted. The action bar panel now moves above the card if space is limited, and tooltips reposition to the right or left to avoid being cut off on small worklog cards.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1235398/7pace-timetracker-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](mailto:support@7pace.com).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support inspires us to improve our apps continually. We appreciate your trust in 7pace Timetracker for Jira!