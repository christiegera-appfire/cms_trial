# Release notes 23 November 2026

**Release date**: November 23, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Display SLA reports on Jira dashboards

You can now display **Duration, Status, Summary, and Detail reports** as gadgets on Jira dashboards.

![image-20261123-173529.png](/cms_trial/assets/6cc0239f-557f-4569-b8fc-6454c8d8990e.png)

Save a report configuration as a gadget or add a saved configuration directly from your dashboard. This lets you monitor SLA performance and share reporting insights without opening Time to SLA.

For setup instructions and important information about report permissions, see [Display SLA reports on Jira dashboards](/cms_trial/space/TTSC/3869049192/Display+SLA+reports+on+Jira+dashboards/).

### Manage SLAs by JSM Organization

You can now use Jira Service Management (JSM) Organizations to configure SLA goals and analyze performance for individual customers.

- **Filter SLA goals by JSM Organization:** Apply different SLA targets to work items associated with specific customer organizations.

  ![image-20261123-172758.png](/cms_trial/assets/93491cf1-f8b4-4f0f-af40-ccddc39b84bd.png)
- **Group Executive reports by JSM Organization:** Compare SLA performance across customers, including work item counts, average SLA durations, and success rates.

  ![image-20261123-172935.png](/cms_trial/assets/745fc325-879d-4c89-afdf-af6e03ed09f5.png)

You can also combine JSM Organization with other grouping fields in Executive reports for a more detailed breakdown.

For more information, see [SLA goals](/cms_trial/space/TTSC/35390901/SLA+goals/) and [Executive reports](/cms_trial/space/TTSC/3404431363/Executive+reports/).

### Extend SLA contracts through REST API

You can now extend SLA contracts through the Time to SLA REST API. This feature lets you manage contract extensions programmatically, reducing manual updates. You can:

- Preview an SLA deadline extension for a specific work item.

  ![Screenshot 2026-11-23 at 20.30.32.png](/cms_trial/assets/af0ac098-6265-43e3-a42a-7438cca7f4ba.png)
- Extend an SLA deadline for a specific work item.
- Undo an existing SLA extension.

For more information, refer to the [SLA contract extension](/cms_trial/space/TTSC/2001470255/SLA+contract+extension/) and [REST APIs](/cms_trial/space/TTSC/36209134/REST+APIs/). For endpoint details and request examples, see the [Work item SLA API](https://docs.timetosla-appfire.com/).

### Clone calendars

You can now clone existing calendars in Time to SLA instead of creating similar configurations from scratch.

![image-20261123-173159.png](/cms_trial/assets/a4053d05-e304-408d-9617-95fa120b3180.png)

Calendar cloning helps you reuse business hours and holiday settings when setting up calendars with similar schedules. You can then customize the cloned calendar to meet your requirements.

### Improved custom field values in SLA History

The SLA History tab now displays the actual values of supported custom fields instead of their internal IDs.

For example, when a custom field contains values such as *Customer Commented* or *Agent Replied*, SLA history displays these values instead of numeric identifiers, making SLA events easier to understand and troubleshoot.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where the SLA Indicator field displayed inconsistent statuses. Previously, breached SLAs could appear as *In progress* in Jira queues or display different statuses after refreshing the page.
- Fixed an issue where pausing and resuming an SLA could result in an incorrect breach calculation when the associated calendar had different working hours on certain days.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!