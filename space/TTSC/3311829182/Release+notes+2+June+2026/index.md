# Release notes 2 June 2026

**Release date**: June 2, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### SLA scope settings are now easier to manage

We re-implemented the **SLA Calculation Scope** page and reorganized SLA scope settings into a clearer layout.

![Time to SLA calculation scope](/cms_trial/assets/bd090a94-416d-4ac3-a603-de815f2aa936.png)

The existing **Exclude Automated Users** option, previously available under **Administration** > **Advanced**, has been moved to the new **Filter by events/webhooks** section. We also added a new webhook event **allowlist**, giving admins more control over which users’ events are processed.

Terminology has also been updated to use clearer naming:

- **Whitelist** is now **Allowlist**
- **Blacklist** is now **Blocklist**

### SLA field permissions are now restricted to Jira admins

Only Jira administrators can now edit the SLA fields permissions under **Administration** > **Permissions**.

### Configuration names are now kept unique across the app

Configuration name handling has been centralized across the frontend to ensure names remain unique throughout the app.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where old generated reports were not automatically deleted.
- Fixed an SLA creation failure during JCMA migrations when *Dynamic Duration* custom fields were created without associated screens.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!