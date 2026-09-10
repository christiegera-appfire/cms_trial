# Release notes 24 June 2025

**Release date**: June 24, 2025

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### SLA target date behavior post-breach aligned with contractual logic

We’ve updated how Time to SLA handles target dates after an SLA breach to ensure consistency, transparency, and contractual compliance.

Going forward, once an SLA has been breached, any subsequent pause condition will no longer postpone the SLA target date. This change applies across all components of the app:

- **SLA panel and custom fields:** SLA target dates will remain fixed after breach, even if a pause is triggered later. This ensures the panel and custom field values reflect accurate SLA behavior.

This change reinforces clear SLA tracking and aligns Time to SLA’s behavior with legal best practices, ensuring that post-breach actions do not alter contractual deadlines.

For more details, you can refer to the [SLA goals](/cms_trial/space/TTSC/35390901/SLA+goals/) and [SLA custom field](/cms_trial/space/TTSC/35684678/SLA+custom+field/) pages.

---

## Bug fixes

The following bugs are fixed in this release:

- Improved the performance of background reports by preventing unnecessary SLA configuration fetches for every issue SLA conversion. This optimization reduces processing time and enhances efficiency when running reports.
- Resolved an issue where the `sla-configuration-helper` could cause timeouts, particularly when handling large volumes of SLA data. The SLAs page now loads more reliably and quickly.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---