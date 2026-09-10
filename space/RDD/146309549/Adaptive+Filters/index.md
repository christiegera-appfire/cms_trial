# Adaptive Filters

## Overview

This page explains how to use Adaptive Filters in Dashboard Hub. By default, the feature is available to all dashboard viewers, but dashboard editors can customize filters, and admins can disable them for external dashboards in Global Settings.

## Real-time data filters

Dashboards provide a centralized view of metrics for specific audiences, such as engineering, leadership, or support teams. **Adaptive Filters** allow you to refine this data in real-time. This ensures that a single dashboard can serve multiple purposes by allowing users to focus on specific subsets of data without modifying the underlying gadget configurations.

Dashboard Hub provides a default set of filters for dashboards configured with at least one Jira gadget with relevant data. The gadgets can be connected to any Jira instance, whether the current instance, an instance connected using a Connector app, or an instance accessed using an API token.

Adaptive Filters are dynamic by design. The values available in each filter reflect only the data already loaded in your dashboard, not every possible value in your Jira instance. This means the filter options remain relevant and do not expose data outside the current dashboard's scope.

Watch the Adaptive Filters overview video below, or continue reading to learn more.

Video transcript

In this video, you'll learn how to use Adaptive Filters in Dashboard Hub to refine your dashboard data in real time.

Adaptive Filters are a dynamic filter bar at the top of your dashboard that delivers focused reporting, flexible data exploration, and improved control and governance.

Rather than building a separate dashboard for every team, stakeholder, or use case, Adaptive Filters let anyone viewing the dashboard focus on what's relevant to them.

To get started, click **Filters** in the dashboard top bar to open the filter bar. The default filters appear at the top of the dashboard. These include: Project, Issue Type, Status, Assignee, and Created Date. Compatible Jira gadgets are highlighted with a blue border on your dashboard.

Select a value from a field drop-down to apply a filter. Every compatible Jira gadget on the dashboard updates to reflect your selection, and each affected gadget displays the Filtered status. There's also a Contains text field for keyword searches. Keep in mind, this only matches content in the Summary and Key fields. If a gadget has no matching results, it displays a No data to show message. You can broaden your selection, or click Clear to remove all active filters at once. The Filters button in the top bar always shows you how many filters are applied.

Filters apply to all relevant gadgets by default, but you can control this at the gadget level. Hold the pointer over the gadget name to reveal the filter toggle and turn it on for that gadget. Turn the toggle off, and that gadget ignores the dashboard filters and shows its full data set.

As a dashboard editor, you can remove or customize which fields appear in the filter bar. Click **Customize filters** to open the customization panel. From there, you can remove any of the five defaults and replace them with fields from 26 built-in Jira system fields, or custom fields pulled directly from your connected Jira instance. The maximum is five filters at any time, and your changes apply to everyone who views the dashboard.

As an admin, you can hide the filter bar on externally shared dashboards. Go to **App Settings**, then **Global Access Restrictions**, and turn on **Restrict use of adaptive filters for external users**. Once enabled, the filter bar won't appear on any dashboard shared using a public link or through the customer portal. Dashboards shared internally are not affected, and this setting applies globally.

To recap: Click **Filters** to open the filter bar and select values to narrow your gadget data in real time. Use the per-gadget toggle to control which gadgets respond to your filters. Editors can customize the available fields from the Customize filters panel, and admins can restrict the filter bar for external viewers through Global Access Restrictions in App Settings.

## Who can use Adaptive Filters?

| **Role** | **What you can do** |
| --- | --- |
| Viewer | Apply and clear filters on a dashboard and individual gadgets |
| Editor | Customize the fields that are available on a dashboard |
| Admin | Restrict filters on external dashboards |

## How to apply filters

To apply a filter, in the dashboard top bar, click **Filters** to open the filterbar. You can also use filters in dashboards embedded in Confluence pages with a dashboard macro. The filters are available whether you are the dashboard owner or viewing a shared dashboard.

![Dashboard top bar with the Filters button highlighted.](/cms_trial/assets/c5ebf1d6-71ed-44e8-8972-ea2f81ac4542.png)

### Default filters

Adaptive filters apply to dashboard Jira gadgets. The default filter options include **Projects**, **Work Item Types**, **Status**, **Assignee**, and **Created Date**.   
You can also use the free text, **Contains text** field to filter results for text matches.

The **Contains text** option only returns matches for the **Summary** and **Key** fields.

![The default Adaptive Filters bar in Dashboard Hub.](/cms_trial/assets/747060aa-b4c6-48f5-ab7b-40ef2de61b17.png)

### Select the values to display

To apply a filter, select a value from the field drop-down list, for example, a space name or a created date. The filters apply to all gadgets that retrieve relevant Jira data. Gadgets displaying filtered data are highlighted in a blue border. If the filter excludes matching data, the gadget displays the message, ℹ️ `No data to show`.

The **Filters** button displays the number of filters currently applied to the dashboard. In the example below, two filters are applied. To clear all filters, click **Clear**.

![Dashboard with two selected filters in Dashboard Hub.](/cms_trial/assets/10ac552d-dad1-4aef-ae09-bffff78b41b2.png)

### Manage filtered gadgets

The selected filters apply to all relevant Jira gadgets in the dashboard. To manage the filters for each gadget, hover over the gadget name to display the filter toggle, then turn the filter on or off. When a filter is on, the filtered status is displayed. If you disable it, the content of that gadget won’t be affected by the selected dashboard filters.

![Example gadget displaying the Filter toggle.](/cms_trial/assets/168a3b74-5a54-406f-8486-c020b1585943.png)

![Example gadget displaying the Filtered status.](/cms_trial/assets/b0ac0b18-14a6-488c-8db7-bb7920a954e1.png)

## How to customize the filter bar

Dashboard editors can customize which filters are available or restrict filtering altogether. This ensures that viewers only see the most relevant fields and are not overwhelmed by unnecessary options. The customized filter bar applies to the dashboard regardless of who is viewing it.

**To change the dashboard filters:**

1. Click **Customize filters**. The current filters display at the top of the *Customize dashboard filters* page. Dashboard editors can remove any of the default filters and add fields from 26 built-in Jira fields and supported custom fields.

![Customize dashboard filters page with three selected fields.](/cms_trial/assets/65f8e16a-c160-4b04-9d30-7be7252bb604.png)

1. Select the required fields from the selection list. You can add up to 10 filters in the filter bar.
2. To remove a selected field, click the corresponding **X**. To remove all selected filters at once, click **Clear all**.
3. To change the order of the filters, drag them to the desired position. This is the order in which they appear on the dashboard.

## Supported products

Adaptive Filters supports data connections to:

- Jira Software
- Jira Service Management
- Jira Work Management

## Supported fields

Only supported fields are available in the *Customize dashboard filters* selection list.

### Jira built-in system fields

Expand to view full list of built-in fields 

|  |  |
| --- | --- |
| **Jira built-in field** | **Supported in Adaptive Filters** |
| Assignee | ✅ |
| Attachment | ❌ |
| Comment | ❌ |
| Components | ✅ |
| Created | ✅ |
| Creator | ✅ |
| Description | ✅ |
| Due date | ✅ |
| Environment | ✅ |
| Fix versions | ✅ |
| Images | ❌ |
| Issue Type | ✅ |
| Key | ✅ |
| Labels | ✅ |
| Last Viewed | ❌ |
| Linked Issues | ❌ |
| Log Work | ❌ |
| Original estimate | ✅ |
| Parent | ❌ |
| Priority | ✅ |
| Progress | ❌ |
| Project | ✅ |
| Remaining Estimate | ✅ |
| Reporter | ✅ |
| Resolution | ✅ |
| Resolved | ✅ |
| Restrict to | ❌ |
| Security Level | ✅ |
| Status | ✅ |
| Status Category | ✅ |
| Status Category Changed | ❌ |
| Sub-tasks | ❌ |
| Summary | ✅ |
| Time Spent | ✅ |
| Time tracking | ❌ |
| Updated | ✅ |
| Votes | ✅ |
| Watchers | ✅ |
| Work Ratio | ❌ |
| Σ Original Estimate | ❌ |
| Σ Progress | ❌ |
| Σ Remaining Estimate | ❌ |
| Σ Time Spent | ❌ |

### Field types

The list of available fields is pulled directly from your connected Jira instance. Only supported field types appear in the selection menu.

Expand to view supported custom field types

## Work item panel

| **Field type** | **Schema** | **Supported in Adaptive Filters** |
| --- | --- | --- |
| checkbox | option | ✅ |
| date | date | ✅ |
| dropdown | option | ✅ |
| formula | number | ✅ |
| labels | string | ✅ |
| number | number | ✅ |
| paragraph | string | ✅ |
| people multi | user | ✅ |
| people single | user | ✅ |
| short text | string | ✅ |
| timestamp | datetime | ✅ |
| url | string | ✅ |

## Standard

| **Field type** | **Schema** | **Supported in Adaptive Filters** |
| --- | --- | --- |
| checkboxes | option | ✅ |
| Date Picker | date | ✅ |
| Date Time Picker | datetime | ✅ |
| Labels | string | ✅ |
| Number Field | number | ✅ |
| Paragraph | string | ✅ |
| Radio Buttons | option | ✅ |
| Select List (cascading) | option-with-child | ❌ |
| Select List (multiple choices) | option | ✅ |
| Select List (single choice) | option | ✅ |
| Short text (plain text only) | string | ✅ |
| URL Field | string | ✅ |
| User Picker (single user) | user | ✅ |

## Other

| **Field type** | **Schema** | **Supported in Adaptive Filters** |
| --- | --- | --- |
| Assets objects | cmdb-object-field | ❌ |
| Date of First Response | datetime | ✅ |
| Days since last comment | any | ❌ |
| Domain of Assignee | any | ❌ |
| Domain of Reporter | any | ❌ |
| Global Rank | any | ❌ |
| Group Picker (multiple groups) | group | ❌ |
| Group Picker (single group) | group | ❌ |
| Last commented by a User Flag | any | ❌ |
| Last public comment date | any | ❌ |
| Message Custom Field (for edit) | string | ✅ |
| Message Custom Filed (for view) | string | ✅ |
| Number of attachments | any | ❌ |
| Number of comments | any | ❌ |
| Participants of an issue | user | ✅ |
| Project Picker (single project) | project | ✅ |
| Text Field (read only) | string | ✅ |
| Time in Status | any | ❌ |
| User Picker (multiple users) | user | ✅ |
| User Property Field (< 255 characters) | string | ✅ |
| Username of last updater or commenter | user | ✅ |
| Version Picker (multiple versions) | version | ✅ |
| Version Picker (single version) | version | ✅ |

## Jira Product Discovery

| **Field type** | **Schema** | **Supported in Adaptive Filters** |
| --- | --- | --- |
| Checkbox | number | ✅ |
| Connection | any | ❌ |
| Custom formula | number | ✅ |
| Rating | number | ✅ |
| Reactions | string | ✅ |
| Slider | number | ✅ |
| Time interval | string | ✅ |

## Atlassian (built-in)

| **Field name** | **Schema** | **Supported in Adaptive Filters** |
| --- | --- | --- |
| Sprint (Atlassian) | json | ✅ |

## How to restrict Adaptive Filters

By default, the Adaptive Filters bar is available to all dashboard viewers whether you share a dashboard internally or externally with a public link.

Admins can disable the filter bar for externally shared dashboards.

**To restrict filters for external users:**

1. Go to **App settings** > **Global Access Restrictions**.
2. Turn on **Restrict use of adaptive filters for external users**.

Once disabled, the filter bar does not appear on any dashboard shared via a public link or through the customer portal. This setting applies globally and can’t be overridden at the individual dashboard level. Dashboards shared internally are not affected. See [Global Settings](/cms_trial/space/RDD/146309685/Manage+Global+Access+Restrictions/) to learn more about global access restrictions.

![Dashboard Hub Adaptive Filters restriction in Global Settings.](/cms_trial/assets/279ef0b8-d2d2-4331-a6ef-908222972efb.png)