# Release notes 18 May 2026

**Release date**: May 18, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## New features

### Set when SLA notifications start applying

You can now set an **Effective from** date for SLA notifications.

![Time to SLA release notes May 2026 showing redesigned SLA view](/cms_trial/assets/c43318ff-0359-4a8b-97ef-b8ffa6d48760.png)

This helps prevent notifications from being sent for older work items that already match your notifier rules, such as breached SLAs, upcoming breaches, or SLA threshold changes. Set a date to apply notification changes from that point forward, or leave the field empty to apply them to all existing work items retrospectively.

This gives admins more control when enabling notifications and helps reduce the risk of sending messages for historical backlog items.

---

## Bug fixes

The following bugs are fixed in this release:

- We fixed an issue where large reports redirected users to background report generation, but the downloaded file was empty even after the report status changed to *Generated*. Background reports now generate and download the expected data, including reports with more than 100,000 work item-SLA results.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---