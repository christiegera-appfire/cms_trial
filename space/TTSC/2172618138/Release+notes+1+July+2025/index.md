# Release notes 1 July 2025

**Release date**: July 1, 2025

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## Bug fixes

The following bugs are fixed in this release:

#### Migration and import

- Fixed an issue where importing calendars from on-premise instances to Cloud failed with an error. Calendar data now transfers smoothly.
- Resolved an error during Jira Cloud Migration Assistant (JCMA) operations. SLA contexts will now correctly include only projects, preventing unexpected migration failures.
- Fixed an issue where `slaErrors` related to `migrationWarnings` were incorrectly stored in the `TTS_CLIENTS` table. These warnings are now handled properly without polluting client data.
- Addressed a case where basic SLA setups appeared as successfully migrated from on-premises, but no SLAs were saved in the Cloud. SLAs are now preserved as expected.
- Resolved import issues specific to a unique Data Center to Cloud migration scenario. Migration stability has been improved for similar large-scale environments.

#### SLA performance improvements

- Optimized performance for instances with a high number of Issue SLAs. Users should notice faster response times and reduced load-related issues.
- Enhanced the import process to automatically match unique status values during the *Import Match* step, reducing manual intervention and increasing accuracy.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---