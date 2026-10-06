# Dashboard Hub audit log

This page explains how to use the audit log in Dashboard Hub to track changes to datasources, dashboards, permissions, and gadgets.

## Overview

The audit log records changes to your datasources, dashboards, and gadgets, including sharing and permissions. Each entry shows the user who made the change, when it happened, and which object was created, updated, or deleted. Entries are retained for 365 days.

Only Jira or Confluence administrators can view the audit log. It records actions taken inside Dashboard Hub and doesn’t replace your site administrator audit log.

## How to view the audit log

Jira administrators can access the audit log in Dashboard Hub’s App Settings.

To open the log in Jira:

Option A:

1. In the Jira navigation bar, select **Settings** > **Marketplace** **apps**.
2. Under *Dashboard Hub*, select **Audit log**. The *Audit log* page displays.

Option B:

1. In the left sidebar in Jira, click **Apps** > **Dashboard Hub** > **More actions** (**…**) > **App settings**.
2. Under Dashboard Hub, select **Audit log**. The *Audit log* page displays.

Confluence administrators can access the audit log from **Confluence administration** > **Apps** > **Dashboard Hub** > **Audit log**.

## What gets recorded

The audit log tracks 18 events related to five object types. Each entry is tagged with the object type it relates to:

| **Object type** | **Recorded changes** | **Example** |
| --- | --- | --- |
| **Datasource** | Changes to datasource access and configuration. | `UPDATE DATASOURCE ACCESS` |
| **Dashboard** | Sharing and public-link changes, and when dashboards are created, updated, or deleted. | `DISABLE PUBLIC LINK` |
| **Gadget** | Creating, updating, and removing gadgets. | `CREATE GADGET` |
| **Config** | Site configuration changes, such as enabling the customer portal. | `ENABLE CUSTOMER PORTAL` |
| **Ops** | Operational actions, such as a manual tenant purge performed by support. | `MANUAL PURGE TENANT` |

## Read the audit log

![The Audit Log in Dashboard Hub Pro](/cms_trial/assets/8fa12613-7c96-4815-8b4f-3591f7c2af37.png)

A row of quick filter cards at the top of the page shows how many events have been recorded, grouped by object type. Below the summary cards, the audit log table lists each event in six columns.

| Column | Description |
| --- | --- |
| **Timestamp** | The date and time the event occurred. |
| **User** | The user who performed the action. |
| **Event** | The action performed, for example `CREATE GADGET` or `UPDATE DATASOURCE ACCESS`. |
| **Event object** | The type of object affected: Datasource, Dashboard, Gadget, Config, or Ops. |
| **Object name** | The name of the affected object, for example a gadget or datasource name. Shows `--` when there is no specific object. |
| **Summary** | A brief description of the change. To view the complete record for an individual event, click the **Details** icon. |

### Filtering and searching

Use the filter bar above the table to narrow down entries. You can:

- Filter by **Date**, **User**, **Object**, or **Event** using the dropdown menus.
- **Search** by date range, user, object, or action using the search box.
- Use the quick filter cards to see log entries for a specific object type: datasource, dashboard, gadget, config, or ops.
- Select **Clear** to remove all filters and show the full log again.

### Export the log

Select **Export as CSV** to download a .csv file of the log if you need to perform further analysis or share the log details.