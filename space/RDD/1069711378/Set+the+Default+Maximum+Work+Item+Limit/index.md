# Set the Default Maximum Work Item Limit

## Overview

This help document guides users through setting the default maximum work item limit in Jira's administration settings.

### How to set the default maximum work item limit

1. Go to **App settings** > **Global Settings**.
2. Select **Performance options**.
3. Under **Set work item limit**, pick the maximum number of work items.
4. Click **Save**.

![Dashboard Hub default maximum work item limit setting](/cms_trial/assets/c4f90c0c-6ac2-41fe-87a9-e2c41c344d69.png)

| **Host** | **Gadget** | **Limit** |
| --- | --- | --- |
| data center | All (Jira) | - Default 2,500 - Up to limit set by admin [500 - 10,000] |
| cloud | [Jira Custom Charts](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) | - Default 2,500 - Up to limit set by admin [500 - 10,000] |

[Jira Custom Charts](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/): Previews of tables are limited to 100 work items and to 1,000 work items to avoid hindering Jira performance.

### Number of work items processed

The system is optimized to process up to 2,500 work items per gadget for optimal performance. While it is possible to set a higher maximum work item limit (as indicated above), the **effective processing capacity may not exceed** this number due to several factors (see table above):

- The gadget is designed to support up to a specific number of results.
- The data is displayed in a table rather than a chart (charts allow more work items).
- Certain data, such as custom fields from other applications, may not be supported in large volumes.
- Queries have fields that are not currently supported.

### Supported fields

- **Built-in Jira system fields**

Expand to view full list of built-in fields 

|  |  |
| --- | --- |
| **Jira Built-in Field** | **Supported** |
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
| Status Category Changed | ✅ |
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

- **Custom field types**

The list of available custom fields is pulled directly from your connected Jira instance. Only supported custom field types appear in the selection menu.

Expand to view supported custom field types

## Work item panel

| **Custom field type** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| checkbox | ✅ | ✅ |
| date | ✅ | ✅ |
| dropdown | ✅ | ✅ |
| formula | ✅ | ✅ |
| labels | ✅ | ✅ |
| number | ✅ | ✅ |
| paragraph | ✅ | ✅ |
| people multi | ✅ | ✅ |
| people single | ✅ | ✅ |
| short text | ✅ | ✅ |
| timestamp | ✅ | ✅ |
| url | ✅ | ✅ |

## Standard

| **Custom field type** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| checkboxes | ✅ | ✅ |
| Date Picker | ✅ | ✅ |
| Date Time Picker | ✅ | ✅ |
| Labels | ✅ | ✅ |
| Number Field | ✅ | ✅ |
| Paragraph | ✅ | ✅ |
| Radio Buttons | ✅ | ✅ |
| Select List (cascading) | ❌ | ✅ (has `option-with-child` ) |
| Select List (multiple choices) | ✅ | ✅ |
| Select List (single choice) | ✅ | ✅ |
| Short text (plain text only) | ✅ | ✅ |
| URL Field | ✅ | ✅ |
| User Picker (single user) | ✅ | ✅ |

## Other

| **Custom field** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| Assets objects | ❌ | ✅ (has `cmdb-object-field` renderer) |
| Date of First Response | ✅ | ✅ |
| Days since last comment | ❌ | ✅ (Dashboard Hub calculated field) |
| Domain of Assignee | ❌ | ❌ |
| Domain of Reporter | ❌ | ✅ (Dashboard Hub calculated field) |
| Global Rank | ❌ | ❌ |
| Group Picker (multiple groups) | ❌ | ✅ (has `group` rendered) |
| Group Picker (single group) | ❌ | ✅ (has `group` rendered) |
| Last commented by a User Flag | ❌ | ❌ |
| Last public comment date | ❌ | ❌ |
| Message Custom Field (for edit) | ✅ | ✅ |
| Message Custom Filed (for view) | ✅ | ✅ |
| Number of attachments | ❌ | ❌ |
| Number of comments | ❌ | ❌ |
| Participants of an issue | ✅ | ✅ |
| Project Picker (single project) | ✅ | ✅ |
| Text Field (read only) | ✅ | ✅ |
| Time in Status | ❌ | ❌ |
| User Picker (multiple users) | ✅ | ✅ |
| User Property Field (< 255 characters) | ✅ | ✅ |
| Username of last updater or commenter | ✅ | ✅ |
| Version Picker (multiple versions) | ✅ | ✅ |
| Version Picker (single version) | ✅ | ✅ |

## Jira Product Discovery

| **Custom field type** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| Checkbox | ✅ | ✅ |
| Connection | ❌ | ❌ |
| Custom formula | ✅ | ✅ |
| Rating | ✅ | ✅ |
| Reactions | ✅ | ✅ |
| Slider | ✅ | ✅ |
| Time interval | ✅ | ✅ |

## Atlassian (built-in)

| **Field name** | **General support in Custom Charts** | **Supported for dynamic filters and > 2,500 work items** |
| --- | --- | --- |
| Sprint (Atlassian) | ✅ | ✅ |