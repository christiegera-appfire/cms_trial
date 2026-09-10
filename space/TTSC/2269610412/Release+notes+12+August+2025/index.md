# Release notes 12 August 2025

**Release date**: August 12, 2025

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Unified Slack channel for install/uninstall events

You can now set a single Slack channel for all app install/uninstall events across your instance. Plus, you can rename the channel for better alignment with your team workflows.

### Improved SLA accuracy for breached work items

The app now automatically updates the Target Date field when an SLA is breached, ensuring accurate tracking and reporting.

### Selective work item update ignoring

We’ve added the ability to ignore work item updates from a specific user, which is ideal for filtering out noisy bot activity or system users from triggering SLA recalculations.

---

## Bug fixes

The following bugs are fixed in this release:

- Updated our Content Security Policy (CSP) to include Atlassian-hosted assets for improved compatibility and security.
- Resolved a problem where some users encountered an AccessDeniedException during JCMA migrations. Migrations should now proceed more reliably.
- JCMA migration now handles SLAs with the Dynamic Duration goal type. A notification is provided if the required custom field is missing on Cloud.
- Removed the info button from the SLA panel in the Jira Service Management work item view for a cleaner and less cluttered interface.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---