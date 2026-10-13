# Release notes 13 October 2026

**Release date**: October 13, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## New features

### **Live updates for SLA Indicator custom fields**

SLA Indicator custom fields can now update automatically in the background, without requiring users to open a Jira work item. This keeps SLA statuses up to date across Jira boards, filters, and automation rules.

To enable this feature, go to **Administration** > **SLA Fields** and turn on **Live updates** for the relevant custom field.

---

## Enhancements

### More reliable SLA notifications

Improved the execution order of SLA actions and notifications to ensure they are processed chronologically, including notifications triggered at the same time.

### Clearer SLA panel permissions

Updated the permission settings to clarify that everyone with access to a Jira work item can view its SLA panel unless access is restricted to specific users or groups.

### Improved time zone display

Updated how time zones are displayed to reflect standard time and daylight saving time, keeping them consistent with Jira.

### Cleaner email reports

Issue keys in subscription emails now link directly to their corresponding Jira work items. The separate Issue Link column has been removed to improve readability.

### Clearer Executive report limits

Updated the message displayed when a Jira site reaches the limit of 10 Executive reports, clarifying that the limit applies to the entire site rather than individual users.

### Improved report warnings

Refined warning messages for reports that exceed supported size limits to provide clearer guidance.

### Faster report filter loading

Optimized filter loading to reduce unnecessary requests and improve performance, particularly in Jira environments with many users, groups, and roles.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where SLA target dates were not postponed as expected when no calendar was configured.
- Fixed a crash that could occur when displaying disabled SLAs containing legacy or unsupported conditions.
- Fixed an intermittent issue where SLAs shared through the *Share this SLA on linked issues* option did not appear on some linked work items.
- Fixed an issue where resetting an SLA extension incorrectly displayed the **Extend** button instead of **Undo**.
- Fixed an issue where commas in SLA names caused exported report values to split across multiple columns.
- Removed the SLA Info button for users without the necessary permissions, preventing empty pop-ups from appearing.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!