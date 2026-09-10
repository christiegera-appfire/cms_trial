# Release notes 19 January 2026

**Release date**: January 19, 2026

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### More efficient issue fetching

We’ve switched to using a bulk fetch endpoint instead of individual issue requests, improving performance and reducing unnecessary API calls.

---

## Bug fixes

The following bugs are fixed in this release:

- We fixed a confusing warning on the work item view that appeared even when an SLA had already started. This happened for SLAs using the **No target** goal type, where the target date is intentionally empty. The warning is no longer shown in this case.
- Resolved visual rendering issues in Dark Mode for the **Time to SLA – Periodic Met vs Breached SLA** gadget.
- Improved how the Permissions page loads when there are many user groups, making it more responsive.
- Bulk recalculation requests now wait for any ongoing recalculation task to finish before starting, preventing conflicts and incomplete updates.
- Fixed an issue where SLA target dates were updating less frequently than the configured intervals.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!