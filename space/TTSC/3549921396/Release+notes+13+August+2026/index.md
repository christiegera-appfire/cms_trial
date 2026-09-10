# Release notes 13 August 2026

**Release date**: August 13, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## Bug fixes

The following bugs are fixed in this release:

- We fixed an issue where the **Reset SLA** endpoint could persist an SLA reset before verifying that the user had access to the issue. Issue access is now checked before the reset is applied.
- We fixed an issue where an SLA could remain paused when the same issue transition triggered both its resume and start conditions. When an issue now moves out of a pause condition and also meets the SLA start condition in the same action, the SLA resumes as expected.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!