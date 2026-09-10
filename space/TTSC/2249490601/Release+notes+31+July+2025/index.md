# Release notes 31 July 2025

**Release date**: July 31, 2025

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Import page optimization

We’ve implemented pagination for the **Import** page when retrieving projects. This improves performance and usability, especially for instances with a large number of projects.

### Status report clarity

We improved the Status report by removing the redundant *All SLAs* row when there's only one SLA configured. This eliminates duplicate results in single-SLA setups.

---

## Bug fixes

The following bugs are fixed in this release:

- SLA history was continuing to count time even after the SLA had ended. We’ve fixed this to ensure accurate tracking and historical data.
- Resolved an issue where audit logs sometimes displayed incomplete Account IDs and lacked user information. Audit logs are now more reliable and informative.
- Fixed a bug where contract extension requests were returning a 404 error. Users can now successfully extend SLA contracts without interruptions.
- Addressed an issue where JCMA was stuck at 0% due to a `Runtime.ImportModuleError`. The import process now functions as expected.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---