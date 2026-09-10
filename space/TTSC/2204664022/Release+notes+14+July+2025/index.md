# Release notes 14 July 2025

**Release date**: July 14, 2025

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Pause conditions no longer delay overdue SLAs

Previously, if an SLA had already been breached, applying a pause condition would still postpone the target date, leading to inaccurate timing and reporting. With this fix, Time to SLA now correctly prevents any changes to the target date once the SLA has been exceeded, even if pause conditions apply afterward.

### Enhanced Pendo integration for CSAT Guide support

We've updated our Pendo implementation to enable support for the new Customer Satisfaction (CSAT) Guide. This ensures a smoother experience for users as we roll out guided help and feedback collection directly in the Time to SLA interface.

---

## Bug fixes

The following bugs are fixed in this release:

- A bug was causing SLAs that rely on JQL filters to produce incorrect results when recalculated. This issue has been resolved, and recalculations now respect the original SLA configuration, including any filters applied.
- When exporting SLA reports, negative SLA durations (indicating a breach) used to appear aligned to the right side of the cell, making the data hard to scan and inconsistent with other values. We've fixed this so that all values, including negative ones, are now properly aligned for better readability.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---