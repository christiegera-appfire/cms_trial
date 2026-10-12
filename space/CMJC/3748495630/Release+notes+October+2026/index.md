# Release notes October 2026

**Release date**: October 12, 2026

Our team is thrilled to announce the latest release of Configuration Manager for Jira (CMJ) Cloud.

---

## New features

### Slack notifications

You can now receive Slack notifications about your CMJ Cloud operations without having to check their progress manually. Configure notifications to stay informed about snapshot creation, deployment analysis, transformations, and snapshot deployments.

Each notification reports whether the operation succeeded, failed, or was canceled. You can select notifications for individual snapshots and deployments or set a default notification for a snapshot scope to stay updated on future snapshot versions.

[Read more about notifications](/cms_trial/space/CMJC/3749347329/Notifications/)

---

## Enhancements

### App upgrade notifications

CMJ Cloud now displays a notification banner when a newer app version requires a manual upgrade. The banner informs Jira administrators that an update is available and prompts them to approve the upgrade to the latest version.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue that could cause snapshot creation to fail when resolving project role references in workflows.
- Fixed an issue that caused snapshot creation to fail when a Jira project had no assigned project lead.
- Fixed an issue that prevented JSM Knowledge Base links from being migrated from Server to Cloud when the migrating user lacked administrator permissions in Confluence.
- Fixed an issue that could cause deployments to fail when adding custom fields to Jira boards.
- Fixed an issue that caused deployments to fail when creating Jira forms with empty names.
- Fixed an issue that could cause snapshot creation to fail when JSM forms contained unrecognized question types.
- Fixed an issue that incorrectly allowed scheduled snapshots to be configured for snapshot groups uploaded from Jira Data Center.
- Fixed an issue where CMJ Cloud incorrectly reported that JMWE was not installed on the destination site during deployment analysis.
- Fixed an issue that could cause deployment analysis to fail when processing configuration identifiers for JSM projects.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Configuration Manager for Jira (CMJ) Cloud!