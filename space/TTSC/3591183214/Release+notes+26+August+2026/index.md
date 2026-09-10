# Release notes 26 August 2026

**Release date**: August 26, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## New features

### Add a reason when manually resetting an SLA

You can now add a reason when manually resetting an SLA, making it easier to understand why a reset was performed when reviewing past activity.

Admins can also require users to provide a reason for manual resets from the app settings. This requirement is off by default and applies only to manual resets.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where an SLA start event could be missing from the SLA history when stop, reset, and start conditions were triggered at the same time.
- Resolved several UI issues in SLA condition dialogs that could cause fields to appear incorrectly when editing conditions.
- Fixed an issue where actions created through Data Center imports could be assigned IDs starting from the same value on every import. Imported actions now receive the correct unique IDs.
- Fixed an issue where SLA actions could remain disabled after their owner became inactive, even after an admin assigned a new user. Updating the owner now correctly re-enables the affected actions so they can run again.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!