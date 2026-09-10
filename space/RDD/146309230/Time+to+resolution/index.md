# Time to resolution

## Overview

Graphical representations help us to understand valuable and actionable information. Service management teams need to easily confirm whether they are meeting their organizations' service level agreements (SLAs), so they can take action before any breach occurs.

One key SLA is the **time to resolution**: How long it takes from the moment a request is logged in the system until it is resolved.

This gadget displays the average time to resolution for all resolved requests within a specified period. It covers all request types in your service desk, and highlights the average time for all work items, and for work items of the highest priority (or any other priority you decide to include).

This gadget is **multi-project**, so you can report across your whole portfolio of projects

If you hold the pointer over the graph series line, it indicates the average time to resolution for all work items for each day.

![Dashboard Hub Time to resolution gadget](/cms_trial/assets/be7457ed-a69d-4d93-bb62-d586ed35af72.png)

## How work items are selected

This gadget includes only work items for which the Time to Resolution SLA has been **completed**, meaning the SLA cycle has reached a final state (met or breached). Work items where the SLA is still running or paused are excluded.

## How to add and configure the gadget

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the **Search** bar in the *Add gadget* page to find the required gadget.
3. Click **Add** on the **Time to resolution** gadget. The configuration page displays.
4. **Name** (*optional*): Edit the gadget name to make it meaningful to your team.
5. **Datasource**: Select a datasource where **Current** indicates the Jira Service Management instance where the app is installed.
6. **Specify the work items to include**:Select a JSM project and queue, or select the JQL toggle to display a JQL input field. For example, `project = "SD" AND priority = High`. To ensure only completed work items are reported on, Dashboard Hub runs the query by prepending `<selected SLA field>=completed()`. Remember that the gadget dynamically returns query results that can change over time as the resolution changes.
7. **Priorities**: Select the priorities that you want to differentiate from the rest of the work items. You can also customise the colour of the line segments for both series.
8. **Period to retrieve**: Select a number of days weeks or months.
9. Click **Add**, then save the dashboard.

## Integrations

- Jira Service Management

## Dashboards

This gadget appears in the following dashboard: [IT Service Management team template](/cms_trial/space/RDD/146309962/IT+Service+Management+team+template/).