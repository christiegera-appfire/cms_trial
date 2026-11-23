# Display SLA reports on Jira dashboards

Time to SLA lets you display saved SLA reports as gadgets or widgets on Jira dashboards. This makes it easier to monitor SLA performance and share reporting insights without opening Time to SLA.

You can display the following report types:

| **Report type** | **What it displays** |
| --- | --- |
| **Duration** | SLA duration trends using line or bar charts. |
| **Status** | SLA results using a pie chart and legend. |
| **Summary** | SLA performance across work items. |
| **Detail** | Detailed SLA information for work items. |

## Save a report as a gadget

You can add a report to a Jira dashboard when saving its configuration.

1. In Time to SLA, go to **Reports**.
2. Select a supported report type and configure its filters and display options.
3. Click **Save report configuration as**.
4. Enter a **Report configuration name**.
5. Enable **Save as gadget**.
6. Select the **Dashboard** where you want to display the report.
7. Enter a **Gadget title**.
8. Click **Save**.

The gadget is added to the selected dashboard using your saved report configuration.

## Add a saved report to a dashboard

You can also add a previously saved report configuration directly from Jira.

1. Open the Jira dashboard where you want to display the report.
2. Edit the dashboard and click **Add widget**.
3. Find and select the Time to SLA report widget.
4. Click **Edit widget**.
5. Select the **Report configuration** you want to display.
6. Click **Add**.
7. Click **Done** to finish editing the dashboard.

## Report permissions and data visibility

**Important:** Report gadgets and widgets display data using the report configuration owner's permissions, not the dashboard viewer's permissions.

This means dashboard viewers may see Jira data they wouldn't normally have access to.

Before sharing a dashboard, make sure everyone with access is authorized to view the report data. The person creating the gadget or widget is responsible for preventing unintended exposure of sensitive information.

## Understanding dashboard views

The information displayed depends on the report type and the space available on the dashboard.

### Compact view

Compact views display essential information for monitoring SLA performance at a glance.

For example:

- **Status reports** display a pie chart and legend without the detailed table.
- **Summary reports** display an SLA performance overview and up to five work items.

### Expanded view

Expanded views provide additional report details and interactions where supported.

For example:

- **Status reports** display the pie chart and a paginated summary table. You can select chart segments to explore the underlying data.
- **Summary reports** display the full report table, including saved column preferences, pagination, and sorting.

Dashboard reports use their saved configurations and refresh automatically. Dashboard tables are read-only. To change a report configuration or export its results, open the report in Time to SLA.

For more information about each report type, see [Summary report](/cms_trial/space/TTSC/36044860/Summary+report/), [Detail report](/cms_trial/space/TTSC/36143159/Detail+report/), [Durations report](/cms_trial/space/TTSC/36077648/Durations+report/), and [Status report](/cms_trial/space/TTSC/44761089/Status+report/).