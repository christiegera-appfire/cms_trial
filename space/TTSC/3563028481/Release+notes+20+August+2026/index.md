# Release notes 20 August 2026

**Release date**: August 20, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## New features

### Require a reason for SLA extensions

Admins can now require users to provide a reason when extending an SLA.

Enable this option in **Time to SLA** > **Administration** > **General** to make the extension reason mandatory in the **Extend SLA** dialog. When enabled, users must enter a reason before they can extend an SLA.

This setting is off by default, so existing SLA extension workflows remain unchanged unless an admin enables it.

### Schedule Durations and Status reports

You can now schedule [**SLA Durations**](/cms_trial/space/TTSC/36077648/Durations+report/) and [**SLA Status**](/cms_trial/space/TTSC/44761089/Status+report/) reports as periodic reports.

Set a schedule, choose recipients, and use either a saved filter or the current report configuration. Each scheduled run creates a downloadable report on the [**Periodic reports**](/cms_trial/space/TTSC/36012105/Periodic+reports/) page and sends the standard notification email.

### Track SLA time by specific Team values

You can now use **Changed to a value** and **Changed from a value** with the **Team** field in SLA conditions. This lets you start or track an SLA when a work item is assigned to a specific team, useful when tickets move between teams that follow different working calendars.

---

## Bug fixes

The following bugs are fixed in this release:

- Saved report settings are now retained when switching report types. Previously, changing the report type of a saved report could clear its JQL, SLA, and other settings. You can now switch between Summary, Status, Durations, and Details reports without re-entering your configuration.
- Fixed project role search during import match. You can now search for project roles when configuring matches during an import.
- Updated the calendar timezone name from Kiev to Kyiv.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!