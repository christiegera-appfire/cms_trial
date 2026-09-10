# Release notes 24 July 2026

**Release date**: July 24, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Report column preferences are now saved

Time to SLA now remembers the order of columns on the reports page, so you do not need to reorganize them each time you return.

### Faster filter selection in the Periodic Met/Breached SLA gadget

We improved the performance of the **Periodic Met/Breached SLA** gadget in Jira environments with a large number of issue filters. Instead of loading every filter when you edit the gadget, matching filters are now loaded when you start typing. This reduces loading times in large Jira instances.

### SLA information added to Global SLA action history

The execution history for **Global SLA** actions now includes an **SLA** column.

When an action contains multiple SLAs, you can use this column to identify which SLA was processed or caused an error.

### SLA configuration permission renamed

The **SLA configurations** permission has been renamed **SLAs/Actions** to clarify that users with this permission can access and manage both SLAs and actions.

### New time filter for reports

You can now use the **Days previously** option to limit report data to a recent period.

Applying this filter reduces the number of issues that need to be processed, helping reports load faster and reducing the likelihood of timeouts in large Jira environments.

### Switch between Single SLA and Global SLA actions

You can now change an existing action from **Single SLA** to **Global SLA**, or from **Global SLA** to **Single SLA**, without recreating the action.

---

## Bug fixes

The following bugs are fixed in this release:

### SLA panels now appear reliably on linked issues

Fixed an issue affecting SLAs configured with **Share this SLA on linked issues**.

When multiple linked issues were included in the same operation, the required issue properties were not always created or updated correctly. As a result, the SLA panel could be missing even though the SLA was active and the issues were linked. The properties are now updated correctly for all matching linked issues.

### Shared calendar entries are preserved

Fixed an issue where creating or updating a calendar through the REST API could delete its shared holidays and shared exceptions.

### Improved handling of the Data Center 24/7 calendar during imports

Fixed an issue that occurred when importing an SLA from Data Center that used the default **24/7 calendar** into Cloud, where that calendar is not available by default.

The import process now allows the calendar to be matched to an existing Cloud calendar or recreated during the matching step.

### Restricted access to SLA Fields

Fixed a permissions issue that allowed non-admin users to view the **SLA Fields** page and create SLA fields.

Only Jira administrators can now access and manage SLA fields.

### Improved field selection behavior

Fixed an issue where selecting a field moved the focus to the select list above it, making it difficult to select values.

### Correct SLA calculations during daylight saving time changes

Fixed an issue where SLA events occurring across a daylight saving time change could be processed using the wrong day or time zone.

This could cause incorrect calculations, such as displaying an SLA as breached when it should still be within its target.

### Invalid SLA goals no longer interrupt calculations

SLA goals that do not have a goal type or duration are now ignored during recalculation.

Previously, these invalid goals could cause SLA calculations to fail and prevent the SLA panel from being updated.

### Status reports display correctly

Fixed an issue where the **Status** report type was not displayed as the expected pie chart.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!