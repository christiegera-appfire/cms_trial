# Release notes 4 September 2026

**Release date**: September 4, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## New features

### Share Executive Reports with others

You can now share Executive Reports with other users and control whether they can **view** or **edit** them.

- **Viewers** can access the report, explore aggregated data, open drill-downs, and adjust display settings.
- **Editors** can also update report settings, regenerate reports, manage associated Detailed Reports, change access settings, and delete the report.
- Report owners always retain full access.

You can also choose whether saved Detailed Reports are shared with everyone who has access to the Executive Report or remain private to their creator and the report owner.

---

## Enhancements

### Improved DC-to-Cloud migration handling for unsupported notification recipients

Migration now handles notification recipients that are not supported in Jira Cloud more safely. Actions that rely on unsupported **Project role** or **email address** recipients are no longer created with incomplete or invalid configurations.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where opening a report from a dashboard gadget automatically applied a **Work item created** filter, causing the report results to differ from the gadget.
- Fixed an issue where a running SLA could incorrectly display a **Paused** icon in SLA History.
- Fixed an issue where linked SLAs could fail to appear in the SLA panel even when the SLA configuration, scope, and permissions were correct.
- Fixed an issue that could prevent SLA History from loading.
- Fixed an issue where status conditions without labels could interrupt SLA processing.
- Fixed an issue during DC-to-Cloud migration where notification actions using **Repeat every** were not created.
- Fixed an issue during DC-to-Cloud migration where notification actions could fail when recipient fields were mapped using **Define new**.
- Fixed an issue with migration mappings that could prevent SLA data from being saved for some migrated issues.
- Fixed an issue where options for select lists, checkboxes, radio buttons, and other custom fields did not load in the **Filter by** field.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!