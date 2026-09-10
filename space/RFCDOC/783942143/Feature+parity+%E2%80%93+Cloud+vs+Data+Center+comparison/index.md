# Feature parity – Cloud vs Data Center comparison

Last updated onFebruary 11, 2026.

This page compares the functional coverage of the Cloud and Data Center (DC) versions of the Rich Filters for the Jira Dashboards app. Below, we list the major functional blocks and their current availability status. Note that some features were added on Cloud first and don't yet exist on DC.

We will continue to update this page as we progress. If you plan to migrate from the DC to the Cloud, please check this page regularly, in addition to the release notes.

| **Feature** | **Cloud** | **DC** | **Notes** |
| --- | --- | --- | --- |
| **Rich Filters configuration** |
| **Static filters** | ✅ | ✅ |  |
| **Dynamic filters** |  |  |  |
| - Option dynamic filters | ✅ | ✅ |  |
| - Text dynamic filters | ✅ | ✅ |  |
| - Number dynamic filters | ✅ | ✅ |  |
| - Date dynamic filters | ✅ | ✅ |  |
| **Smart filters** | ✅ | ✅ | On Cloud, a smart filter can contain up to **10 smart clauses**, compared to **15 on Data Center**. This limit is not enforced during migration, so all clauses from migrated smart filters will be preserved. |
| **Views** |  |  |  |
| - Display support for Jira fields, special columns, smart filters, and custom values | ✅ | ✅ |  |
| - Show totals | ✅ | ✅ | With user-defined aggregation formula (sum, average, minimum, or maximum). |
| - Customizable column heading | ✅ | ✅ |  |
| - Customizable smart filters display | ✅ | ✅ |  |
| **Queues** | ✅ | ✅ |  |
| - Static and fixed-order queues | ✅ | ❌ |  |
| **Custom values** |  |  |  |
| - Custom values based on issue count | ✅ | ✅ |  |
| - Custom values based on numeric fields | ✅ | ✅ |  |
| - Custom values based on time-tracking fields | ✅ | ✅ |  |
| - Custom values based on durations | ✅ | ✅ |  |
| **Custom ratios** | ✅ | ✅ |  |
| **Time series** | ✅ | ✅ |  |
| **Management of rich filter objects** |  |  |  |
| - Trash (soft delete) | ✅ | ❌ |  |
| - Automatic archive | ✅ | ❌ |  |
| - Bulk operations | ✅ | ❌ |  |
| - Export/import | ✅ | ❌ |  |
| **Rich Filter Gadgets** |
| **Rich Filter Controller** | ✅ | ✅ |  |
| - Support for dashboard quick filters | ✅ | ✅ |  |
| - Additional filtering modes for option dynamic filters (AND/NOT) | ✅ | ✅ |  |
| - Custom additional JQL | ✅ | ✅ |  |
| - Collapsible sections for quick filters | ✅ | ✅ |  |
| - Dashboard state permalinks | ✅ | ✅ |  |
| - Auto-refresh | ❌ | ✅ |  |
| - Presets | ✅ | ❌ |  |
| - Navigate between filter states | ✅ | ❌ |  |
| **Rich Filter Results** | ✅ | ✅ |  |
| - Queues & views display | ✅ | ✅ |  |
| - Issue actions | ✅ | ✅ | On Cloud, this functionality is provided by the Issue Actions Dialog. |
| - Bulk change issues | ✅ | ✅ |  |
| - Export to Excel | ✅ | ✅ |  |
| - Timeline / Gantt chart view | ✅ | ❌ |  |
| - Freeze columns | ✅ | ❌ |  |
| **Rich Filter Issue Activity Stream** | ✅ | ❌ |  |
| **Rich Filter Simple Counter** | ✅ | ✅ |  |
| **Rich Filter Smart Counters** | ✅ | ✅ |  |
| **Rich Filter Simple Gauge** | ✅ | ✅ |  |
| **Rich Filter Smart Gauges** | ✅ | ✅ |  |
| **Rich Filter Statistics (1D)** | ✅ | ✅ |  |
| - Statistics on Jira option fields | ✅ | ✅ |  |
| - Statistics on date fields | ✅ | ✅ |  |
| - Statistics on text fields and numeric fields | ✅ | ❌ |  |
| - Statistics on time series | ✅ | ✅ |  |
| - Statistics on smart filters | ✅ | ✅ |  |
| - Quick charts | ✅ | ✅ |  |
| **Rich Filter Two dimensional Statistics (2D)** | ✅ | ✅ |  |
| - Statistics on Jira option fields | ✅ | ✅ |  |
| - Statistics on date fields | ✅ | ✅ |  |
| - Statistics on text fields and numeric fields | ✅ | ❌ |  |
| - Statistics on smart filters | ✅ | ✅ |  |
| - Quick charts | ✅ | ✅ |  |
| **Rich Filter Flexi Charts** | ✅ | ✅ | On DC, starting with version 2.2 this gadget replaces the deprecated gadgets *Rich Filter Pie Chart* and *Rich Filter Date Bar Chart*. |
| - One dimensional charts (pie, donut, gauge, sliced bar, bar, line, treemap, word cloud) | ✅ | ✅ |  |
| - Two dimensional charts (clustered bar, stacked bar, multi-line) | ✅ | ✅ |  |
| - Charts based on dates | ✅ | ✅ |  |
| **Rich Filter Created vs. Resolved Chart** | ✅ | ✅ |  |
| **Rich Filter Time Series Chart** | ✅ | ✅ |  |
| **Rich Filter Text Panel** | ✅ | ❌ | On DC, this is covered by the native Jira gadget *Rich Text*. |
| **Rich Filters::Service Management Dashboards** | On Data Center, Jira Service Management-specific functionality is available through an extension - Rich Filters::Service Management Dashboards. On Cloud, the same functionality is delivered directly through the main Rich Filters for Jira Dashboards app. |
| - Dynamic filtering on Customer Request Type and Organizations | ✅ | ✅ |  |
| - Statistics based on Customer Request Type and Organizations | ✅ | ✅ |  |
| - Advanced statistics, charts, and metrics based on SLA fields | ✅ | ✅ |  |
| **Rich Filters::Time Tracking Dashboards** | On Data Center, time tracking specific functionality is available through an extension – *Rich Filters::Time Tracking Dashboards*. The same functionality is not yet available on Cloud. |
| - Dynamic filtering on worklogs | ❌ | ✅ |  |
| - Statistics based on worklogs | ❌ | ✅ |  |
| - WQL (Worklog Query Language) support | ❌ | ✅ |  |
| **Rich Filters::PDF Reports for Jira** | This functionality is available on the Data Center through an extension – *Rich Filters::PDF Reports for Jira*. On the Cloud, the same functionality is delivered directly through the main Rich Filters for the Jira Dashboards app. |
| - Export gadgets to PDF | ✅ | ✅ |  |
| - Export dashboards to PDF | ✅ | ✅ |  |
| **Rich Filters Global Functionality** |
| - Maximum number of issues supported by one rich filter | **50,000** | **Unlimited** | On Cloud, the base Jira filter of a rich filter must return no more than **50,000 issues**. If this limit is exceeded, rich filter gadgets will display an error. |
| - Maximum number of rich filters on an instance | **7,500** | **Unlimited** | By default, a Jira Cloud site can contain up to **7,500 rich filters**. This limit is not enforced during migration, so all migrated rich filters will be imported. If necessary, you can request an increase of this limit by [contacting our support team](http://appf.re/support). |
| - Support for working queries in all rich filter gadgets | ✅ | ✅ |  |
| - JQL auto-complete | ✅ | ✅ | This applies to all JQL inputs in rich filters and rich filter gadgets. |
| - Support for wallboard mode | ✅ | ✅ |  |
| - Support for themes (dark mode) | ✅ | ✅ |  |
| - Availability of rich filter gadgets in Confluence | ✅ | ✅ | This functionality is available on Cloud through this feature provided by Atlassian:  [Embed Jira dashboards & gadgets in Confluence with Smart Links](https://community.atlassian.com/t5/Confluence-articles/Embed-Jira-dashboards-amp-gadgets-in-Confluence-with-Smart-Links/ba-p/2717630) |