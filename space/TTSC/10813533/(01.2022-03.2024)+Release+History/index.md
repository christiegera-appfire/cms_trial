# (01.2022-03.2024) Release History

This page lists the release notes from every production version of Time to SLA for Jira Cloud.

### **2.1.17.7-AC-2024-03-08**

- Recalculation wasn’t working correctly for some customers using Request Type within their SLA configurations.

### **2.1.17.7-AC-2024-03-04**

- Unmasked some non-free text items.
- Implemented pagination on the SLAs page to avoid timed-out issues.

### **2.1.17.7-AC-2024-02-22**

- Applied hashing for free text items such as SLA name, descriptions, and goal name.

### **2.1.17.6-AC-2024-02-22**

- Fixed an issue where the Periodic SLA detail report had an empty column when downloaded or sent via email.

### **2.1.17.5-AC-2024-02-16**

- Applied hashing for free text items such as SLA name, descriptions, and goal name.

### **2.1.17.4-AC-2024-02-14**

- Enhanced the loading performance of the SLA Panel.
- Implemented microcopy changes for improved clarity.
- Resolved an issue where the calendar was not displayed next to the SLA goal.
- Fixed a blank page error that occurred when editing the SLA goal due to amplitude.

### **2.1.17.3-AC-2024-02-09**

- Implemented a fix to ensure SLAs stop as expected when users specify an end condition.
- Addressed the issue causing the ECONNRESET error.
- Pausing SLAs using the "All of the conditions" in a group was not working correctly. Fixed the issue to ensure proper pausing of SLAs.
- Implemented a fix to prevent the creation of redundant pause condition components during the switch between ANY and All conditions.
- Fixed the 401 error occurring during SLA recalculation.

### **2.1.17.2-AC-2024-02-01**

**Improvements:**

- Implemented Amplitude analytics for Time to SLA's REST APIs to track contributors of 429 errors.

**Bug Fixes:**

- Resolved issue where gadgets were not displayed in full-screen size.
- Fixed "Unsaved Changes" error in SLA view mode on the SLA configuration page.
- Fixed an issue causing error 400 or timeouts on the report page, impacting users' ability to retrieve reports.
- Removed old SLA Reports from S3 and DynamoDB.

### **2.1.16.5-AC-2023-12-29**

**Bug Fixes:**

- Resolved an issue where the migration completion message was not displayed in certain cases regarding data residency.
- Fixed the SLA calculation failure when the request type is present in the SLA context.
- Addressed an authentication problem occurring on the Reports page.
- Rectified the issue where exporting a detailed SLA report to Excel resulted in empty SLA state data.
- Ensured consistency of INACTIVE Issue SLAs across gadgets.
- Resolved a bug where SLA calculation did not produce the correct value.

**Improvements:**

- Removed the SLA prefix just before the configuration name in the SLA Panel.
- The app now assigns a default goal order number when none is specified to alleviate confusion.
- The pause condition in the summary section has been improved.

### **2.1.16.4-AC-2023-12-25**

- Introducing SLA Conditions based on another SLA. (Note: This feature is available exclusively on the new SLA Page.)

### **2.1.16.3-AC-2023-12-22**

- Resolved permission migration problems when utilizing JCMA.

### **2.1.16.1-AC-2023-12-19**

- Fixed dark mode background in the SLA Panel in board view.
- Added support for custom domains in the app.
- Set progress above 100% for breached date field goals if elapsed time is less than 100%.
- Stopped the app for DR migration and displayed appropriate flags.
- Updated description for common options in SLA conditions.
- Re-engineered the SLAs page in the customer portal.
- Implemented Amplitude.
- Resolved issue where goal context cannot be changed to default context.

### **2.1.13.0-AC-2023-11-17**

**Enhancements:**

1. Introducing a brand-new SLA Condition creation experience that allows you to group conditions using 'All of the following conditions' and 'Any of the following conditions' operations, providing better control over your SLAs.
2. Better recalculation structure on the backend for enhanced performance.

**Bug Fixes:**

1. Resolved an issue where the "User" field in group conditions was not triggered during issue creation.
2. Fixed inaccuracies in the counts displayed by the Periodic Met vs Breached gadget for some edge cases.
3. Resolved a bug where periodic reports were not created correctly for some users within their selected period.

### **2.1.12.0-AC-2023-10-19**

- Resolved an issue where users were facing SLA triggering post functions error.
- Users without permission to view a page were receiving unauthorized errors when attempting to view a page. Now, they will be directed to the appropriate page based on their access permission.
- Integrated Pijen for notifications and updates.
- Updated Readme for a better onboarding experience for new engineers.
- Replaced issue glance for TTS with issue context.

### **2.1.11.1-AC-2023-09-27**

- Resolved an issue where the target date custom field was not being properly imported.
- Fixed an issue where the SLA scope was not being imported correctly.

### **2.1.11-AC-2023-09-22**

- With the new dynamic calendar selection feature, you can now utilize the "Dynamic Calendar" option within SLA goals to individually select each issue's calendar using the "TTS - Dynamic Calendar" custom field.
- Fixed an issue where the import of SLA configurations from a backup was failing in specific cases.

### **2.1.9.5-AC-2023-08-28**

- Resolved an issue related to Cloud migration error.
- Fixed an issue where the target date custom field was being updated for disabled SLAs.
- Added dark mode support to the Get Started page.
- Resolved a bug that prevented filtering by Project or Workflow on the SLA Recalculation page.

### **2.1.9.4-AC-2023-08-21**

- Improved the token validation mechanism for our REST API.
- Resolved a bug related to importing default goals.
- Default page is now the SLAs page. If a user lacks permission for this page, they will see the Getting Started page.
- Fixed a bug related to transferring filters from gadgets to reports.
- Resolved an issue where the settings menu content was displayed behind other contents.
- Fixed a bug related to percentage calculations for negotiation goals.
- Resolved an issue where too many periodic reports were being generated.

### **2.1.9.3-AC-2023-08-15**

- Say hello to Dark Mode! Now you can enjoy using our app with a sleek and stylish dark color scheme.
- The “Number field changed” condition has been fixed in SLAs.

### **2.1.9.2-AC-2023-08-09**

- SLA Panel was not showing up on some custom portals.
- Fix for the Advanced Settings page save error.
- Retrying mechanism has been added for some connection errors.
- Recalculation requests older than one month will now be deleted.
- Bug fix for adding recipients to filter subscriptions.

### **2.1.9.1-AC-2023-06-13**

- SLA History information can now be retrieved using the REST API.
- SLA durations on the SLA Report page can now be formatted in milliseconds.
- Recalculation was failing in some cases where there was no SLA data.
- Some periodic reports weren't created when they should have been.

### **2.1.9-AC-2023-05-31**

- Periodic report was failing if the issue filter was used in JQL.
- Some REST API calls were reachable using JWT tokens instead of TTS API Tokens.

### **2.1.7.4-AC-2023-04-03**

- Postponed event handling service has been enabled. If an SLA event is entered in the future, such as the SLA end date, it will be handled according to the event’s date.
- SLA Panel now auto-refreshes. If there is a change in the SLA Panel while the issue is open in the browser, updated SLA data will be fetched automatically.
- The ‘Hide disabled SLAs’ option is added to SLA selections in the SLA History panel and SLA Reports page.
- JCMA Migration was giving errors in some cases.
- Asynchronous report was failing in some cases where the data is too large.
- The Duration report was failing to load.
- SLA notifier was failing to send notifications in some cases.
- The ‘Clear Filter’ option was not clearing some filters correctly on the SLA Reports page.
- Filter selection in SLA Reports was not loading all filters of the users.
- The chart interval default value has been changed to the past last month.
- The SLA Details report was missing some columns.
- Users were unable to edit SLA conditions with group selections.

### **2.1.7.3-AC-2023-05-16**

- The “SLA History” tab now displays each cycle and its success results separately.
- Clicking on columns in the “Periodic Met vs. Exceeded” gadget now redirects to the SLA Report.
- Issue summary containing commas was causing problems with Report subscriptions.
- The SLA select field in the Reset SLA post function was not working correctly.
- Users who didn’t have permission were able to view the SLA panel.
- The export/import feature was not working properly for SLA configurations using the security level field.
- Server to Cloud migration was problematic for SLA configurations that use certain system fields.
- The “SLA History” tab panel was failing to display when SLA Panel is not visible on the issue.
- The API Token copy button was not working in Google Chrome.

### **2.1.7.2-AC-2023-03-06**

- Ability to generate background reports via REST Services.
- The security level field was not working as expected.
- ‘No Target’ SLA goal types were not correctly displayed in the SLA info pop-up.
- All filters were not retrieved for the SLA/Assignee Performance gadget.

### **2.1.7.1-AC-2023-02-27**

- The target date for the "Next Business Day" goal type was not calculated correctly in some cases.
- The SLA name was displayed incorrectly in the SLA panel in some cases.

### **2.1.6-AC-2023-02-09**

- Ability to stop notifications after a specific percentage or duration
- Ability to share SLA configuration with linked issues that do not have SLA
- Ability to sort SLA date and duration columns in SLA Report page
- Ability to ‘Never expire’ API Tokens
- ‘Save as default’ option was not working
- Auto refresh option and cancel button is added to ‘Met and Exceeded SLAs’ gadget
- SLA Columns were empty for existing SLA Report configurations

### **2.1.5-AC-2023-01-31**

- SLA/Assignee Performance Gadget is added.
- Ability to edit default issue and SLA columns in SLA Reports.
- Ability to get multiple issues' SLA information via REST API.
- Getting background reports via REST API was not generating URLs correctly.
- The Remaining duration filter in SLA Reports was calculating days as 24 without considering the calendar’s business day hours.

### **2.1.4.1-AC-2023-01-13**

- Cascading select list custom fields was breaking SLA reset conditions and recalculation
- Target date calculation was problematic for calculations with different start and end years.
- Calculation error was not correctly saved.

### **2.1.4-AC-2023-01-06**

- The ability to download background reports via REST API has been added.
- Holidays in time zones with a large time difference from GMT+0 were not correctly calculated by SLA computations.
- The overdue duration calculation was incorrect for paused SLAs.

### **2.1.3-AC-2022-12-16**

- Ability to mute SLA notifications is added.
- Ability to group the results of the SLA Status Pie Chart Report.
- The Recalculation page was giving an error in some cases.
- In some cases, holidays were not considered in the SLA calculation.
- Overdue calculation was wrong in some cases.

### **2.1.2.2-AC-2022-11-25**

- The custom field match problem during importing has been fixed.
- The Calendars page was failing when the holiday icon was clicked.

### **2.1.2.1-AC-2022-11-18**

- Target date update was failing to update in some cases.
- SLA Report generation was giving time out in some cases.
- Calendar calculations were not correct in some cases.

### **2.1.2-AC-2022-11-07**

- SLA History PDF exporting did not fit the page sometimes.
- Recalculation started by inactive users was preventing the recalculation page from loading.
- Importing on-premise export files was not working in some cases.
- SLA Report was displaying dates in the GMT timezone only.
- Calculation problems related to calendars have been fixed.
- SLA History was not displaying correctly sometimes.
- The Delete Old Reports task was not working.

### **2.1.1.2-AC-2022-10-25**

- Status Pie Chart Report is added.
- Periodic report generation is fixed.
- Background report date formatting is fixed.

### **2.1.1.1-AC-2022-10-21**

- Improved Calendar UI design
- Importing with same status names was causing error.
- Recalculate SLA Issue Operation was not working in some instances.
- Importing was failing for some field change types.
- More understandable Recalculation error messages.
- The SLA clock did not pause if multiple holidays were present for a given day.
- Some users were encountering an error due to deleted custom fields on SLA configurations.

### **2.1.1-AC-2022-09-29**

- Ability to export SLA and Calendar configurations from cloud instances has been added.
- Ability to import SLA and Calendar configurations from cloud and on-premise instances has been introduced. Simply use the export tool to export your configurations.
- Issue SLA Operations: Users can now use issue menu actions such as Reset, Undo Reset, Recalculate, and Where is my SLA.
- The ‘Security Level’ field has been added to the available fields in SLA conditions.
- Group names containing the '&' character were causing recalculations to fail.
- Improved handling of Jira REST API results.
- The recalculation page was displaying an error for the new customers and customers without a recalculation task.

### **2.1.0.2-AC-2022-09-05**

- Users were unable to use their email addresses in notifications.
- SLA migration for SLAs with "No Target" was not working.
- The legacy SLA Report filter's ownership problems have been fixed.
- Personal subscriptions were not sending emails.
- Audit logs were not displaying dates correctly.
- Background reports were stuck in the progress state.

### **2.1.0.1-AC-2022-08-25**

- SLAs were missing from the SLA Report if the users did not have permission for SLA Configurations.
- “Team” type custom field values were missing from the SLA Report.
- The time offset for date field conditions was inaccurate for some users.

### **2.1.0-AC-2022-08-24**

- SLA Report improvements
- Ability to share SLA Report filters with other users.  
  SLA Report subscriptions have been added. Users can now create periodic reports.  
  Users can see all issues in the UI without any limits.  
  Users can get reports asynchronously.
- Recalculation for specific issues was not working.

### **2.0.6.7-AC-2022-08-19**

- Gadgets were failing to load in some cases.
- Receiving a pause event while the SLA was already paused was causing calculation problems.
- CurrentUser, currentLogin, and other user-specific JQL functions were not working correctly for the recalculation task.
- Some users were unable to access the Permissions page.
- SLA Report generation with state selection was not working as expected.
- The Group Picker custom field was not working for event generation.
- The SLA state was inconsistent if the SLA goal and end condition were set to the same date in a custom field.
- Negotiation Date SLA goals were not displayed with the correct title in the SLA panel.

### **2.0.6.6-AC-2022-07-26**

- What’s New dialog has been added as well as the ability to give feedback directly from within Time to SLA.
- SLA Report was not working correctly with the SLA State Filter.
- SLA Target Date update was not working for some customers.
- Last Cycle calculation method was not showing the current status.
- SLA Recalculation page was not loading in some instances.

### **2.0.6.5-AC-2022-07-04**

- Ability to whitelist/blacklist projects and issue types has been added.
- SLA Reports now respect Jira Date format
- SLA Notifier parameters were not considering Jira time formats
- SLA title box was too small to fit long SLA names
- SLA Reset was malfunctioning when used with statuses

### **2.0.6.2-AC-2022-05-24**

- SLA Durations Line/Bar Chart Report has been added to SLA Reports.
- SLA History Panel was not showing an icon when loading which was not intuitive.

### **2.0.6.1-AC-2022-05-10**

- Brand new SLA Recalculation design. More reliable and clearer recalculation experience.
- Ability to exclude finished SLAs from recalculation.
- Ability to cancel a recalculation task once it’s started.
- Better issue event handling.
- Report was not filtering SLA records according to a user’s timezone.
- REST API now supports issue key as well as issue id.
- Disabled SLAs were displayed in the SLA panel.
- Customer request type was not displayed correctly on SLA Reports.

### **2.0.6-AC-2022-03-29**

- SLA History tab panel can be exported to Excel/PDF
- Rest API has now been made public. You can learn about API [here](https://documenter.getpostman.com/view/15299464/UVyoXJMy).

### **2.0.5.6-AC-2022-03-24**

- Users were unable to create SLAs with both start and end conditions as a comment, due to an issue with the validation when configuring the SLA.
- Notifier associated goals were disappearing in some instances.

### **2.0.5.5-AC-2022-03-18**

- SLAs were showing in the Customer Portal even once they had been disabled, in some cases.
- User select fields were not showing the correct authorization header.

### **2.0.5.4-2022-03-10**

- Audit log page was not loading in some cases

### **2.0.5.3-AC-2022-03-04**

- SLA History tab panel was not running properly in some cases.
- ‘No Target’ goal type calculation problem has been fixed.

### **2.0.5.2-AC-2022-02-15**

- SLA Panel for met SLAs had wrong tooltip message.

### **2.0.5.1-2022-02-14**

- Creating SLAs with comment rule was failing.
- Saving SLAs with reset conditions was failing.
- Target date custom field was not set in some cases.

### **2.0.5-AC-2022-02-11**

- Added JCMA support
- Added 'No Target' goal type

### **2.0.4-AC-2022-02-03**

- SLA History Tab Panel has been added.
- Audit logging has been applied to plugin. Configuration changes will be logged from now on.
- Async reports will be deleted after a given time period which can be set in the Settings page.
- Date field selection was causing issues in some instances.

### **2.0.3.1-AC-2022-02-01**

- User selection inputs were not searching for users correctly if users didn't reload the page in 15 minutes.
- JQL inputs weren’t working if users didn't reload the page in 15 minutes.
- SLAs were not saving when users selected a date field as an SLA goal.
- SLA working duration was showing different results for Summary and Detail Reports.

### **2.0.3.0-AC-2022-01-27**

- Host Check for incoming requests have been added.
- Issue SLA notifier was logged as sent even if it was not successfully sent.
- Logging Issue SLA Notifier logs were not working if an issue had multiple notifications.
- Negotiation date calculation was incorrect in some time zones.