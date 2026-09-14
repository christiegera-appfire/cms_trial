# Release notes 11 September 2026

**Release date**: September 11, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Use request participants in Comment made conditions

You can now select **Request participants** as a user field when configuring a **Comment made** SLA condition.

This lets the condition match comments made by any request participant on the work item, giving you more flexibility when defining SLA start, stop, pause, or resume conditions.

### Simplified Executive report sharing text

Removed redundant informational text from the **Share** dialog in Executive reports.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue affecting SLAs that use a Negotiation date goal. When an SLA reached its negotiation date while paused, it could appear as breached without recording the breach in SLA history or running actions configured for *Is breached*. Breach events in this state are now recorded correctly and trigger the configured breach actions.
- Fixed an issue where an **All remaining issues** goal that was disabled in Data Center could become enabled after migration to cloud. Jira Cloud Migration Assistant migrations and imports now preserve the disabled state of these goals, so you no longer need to disable them again after migration.
- Fixed an issue that could prevent SLA-related issue properties from being set during a Jira Cloud Migration Assistant migration, even when the SLA and issue SLA data migrated successfully. Issue properties are now handled more reliably during migration.
- Fixed an issue that could cause issue SLA data to be skipped during Jira Cloud Migration Assistant migrations when a corresponding SLA mapping entry was unavailable. Migration now handles these cases more reliably and reduces unnecessary migration warnings.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!