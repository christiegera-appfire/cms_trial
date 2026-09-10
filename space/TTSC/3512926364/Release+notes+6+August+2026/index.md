# Release notes 6 August 2026

**Release date**: August 6, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

**Upgrade recommended**

If you’re currently using **16.0.0-FORGE**, we recommend upgrading to version 17.

This upgrade needs to be completed manually from your Jira site. Upgrading ensures you have the latest version of Time to SLA and can continue receiving the newest improvements and fixes.

---

## New features

### Smoother updates with rolling releases

Time to SLA now supports rolling releases. App code updates and permission changes are versioned separately, helping us deliver new features and improvements more smoothly.

### Run SLA actions when an SLA starts

You can now trigger SLA Actions as soon as an SLA starts. Use the new **is started** trigger to perform actions such as:

- Assigning an issue to a manager when an escalation SLA begins
- Saving the SLA start date to a Jira field
- Updating an SLA indicator field to **IN PROGRESS**

Resuming an SLA after a pause does not count as a new start. The trigger also supports reset SLAs, multiple cycles processed during the same calculation, and configurations that use [**All of the following conditions**](/cms_trial/space/TTSC/35456221/SLA+conditions/).

### Run SLA actions every time an SLA is met

You can now run configured actions each time an SLA is completed before its target date.

For example, you can:

- De-escalate an issue when the SLA is met
- Update an SLA indicator field to **MET**
- Change issue fields, add comments, reassign the issue, or trigger a Jira automation rule

Previously, determining whether an SLA was met required additional fields and automation rules to distinguish met SLAs from breached ones. The new trigger lets you handle this directly through SLA actions.

---

## Enhancements

### SLA history performance

Improved SLA history processing for issues with large numbers of changelog entries, comments, and event indexes. This also resolves delays and timeout errors that could occur when SLAs used the **All of the following conditions** logic.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue that prevented users from selecting an SLA when the **Invalidate current SLA (SLA is not active anymore)** reset type was selected.
- Periodic reports can now be created only for **Details** and **Summary** reports. The application prevents users from creating a periodic report when its selected filter uses an unsupported report type.
- Prevented invalid **Fire event** notifications with an empty action type from being created during JCMA migrations or through export and import.
- Fixed an issue that prevented SLAs from being exported when they contained the following SLA Actions: Set Jira field, Add comment, Change assignee, and Change priority.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!