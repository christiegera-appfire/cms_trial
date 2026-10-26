# Release notes 26 October 2026

**Release date**: October 26, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## New features

### View SLA information directly in Salesforce

We've introduced a new integration with **Connector for Salesforce & Jira**, allowing Salesforce users to view Time to SLA information for associated Jira work items directly on Salesforce record pages.

With the **Time to SLA for Jira** component, teams can keep track of SLA performance without switching between Salesforce and Jira.

To get started, connect Time to SLA to Connector for Salesforce & Jira, configure your integration, and add the component to your Salesforce record pages.

[Learn how to set up the integration](/cms_trial/space/TTSC/3742760964/Connector+for+Salesforce+%26+Jira/).

### Customize SLA Indicator fields

You can now customize the appearance of SLA Indicator fields to better distinguish between **Breached**, **At Risk**, and **Within Target** states.

Choose from seven colors, add custom labels for each state, and select rounded or square badges. A live preview shows how your indicators will appear as you make changes.

### Set SLA targets relative to a date field

We've introduced a new **Relative to Date Field** target type, allowing you to calculate SLA deadlines based on a Jira date field rather than the SLA start time.

Configure a target to fall a specified number of hours, days, or working days before or after a selected date. For example, you can set an SLA target to seven days before an agreed delivery date, ensuring the deadline stays tied to that commitment.

### Start SLAs relative to a date field

SLAs can now start automatically at a calculated time before or after a date stored in a Jira field.

For example, you can configure an SLA to start 14 days before an agreed delivery date. The start time is calculated from the selected date field, rather than when the SLA is processed.

---

## Enhancements

### More control over SLA Date fields

You can now choose which SLA determines the date displayed in an SLA Date field. Select the earliest or latest SLA based on whether it has been completed or is still incomplete.

### Stop failed or stuck imports

You can now stop imports that fail or become stuck directly from the Time to SLA interface.

### JQL search support for SLA Duration fields

We've improved Jira Query Language (JQL) support for SLA Duration custom fields. You can now use supported SLA values, including state, elapsed duration, remaining duration, and target date, to filter and search for work items.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where user fields were not searchable when configuring the **Comment is made** condition.
- Fixed an issue where SLA panels continued to appear on work items moved outside the project scope of their SLA configuration.
- Summary report exports now include all SLAs specified in the report filters, even when no matching work items contain those SLAs. When no specific SLAs are selected, the export includes columns for all SLAs.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!