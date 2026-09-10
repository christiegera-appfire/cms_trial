# SLA Accomplishment

## Overview

Service management teams work on organizations' service level agreements (SLAs) basis, and the ability to easily spot SLA breaches is required. We already saw gadgets for the two most common SLA metrics: [Time to resolution](/cms_trial/space/RDD/146309230/Time+to+resolution/) and [Time to first response](/cms_trial/space/RDD/146309393/Time+to+first+response/), but different teams have different SLA metrics.

This gadget is **multi-project**, so you can report across your whole portfolio of projects

## How it works

This gadget displays the average time of a given completed SLA over a period of time. It highlights the breached (and met) percentage of those requests over the selected period of time. Hover the graph series line to see the average time for all issues for each day. This gadget includes only work items for which the SLA has been **completed,** meaning the SLA cycle has reached a final state (met or breached). Work items where the SLA is still running or paused are excluded.

## How to add and configure the gadget

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the **Search** bar in the *Add gadget* page to find the required gadget.
3. Click **Add** on the **SLA Accomplishment** gadget. The configuration page displays.
4. **Name** (*optional*): Edit the gadget name to make it meaningful to your team.
5. **Datasource**: Select a datasource where **Current** indicates the Jira Service Management instance where the app is installed.
6. **Specify the work items to include**:Select a JSM project and queue, or select the JQL toggle to display a JQL input field. For example, to list all the issues of the project Teams in Space, use the clause `project = "TIS`. To ensure only completed work items are reported on, Dashboard Hub runs the query by prepending `<selected SLA field>=completed()`. Remember that the gadget dynamically returns query results that can change over time as the resolution changes.
7. **Priorities**: Select the priorities that you want to differentiate from the rest of the work items. You can also customise the colour of the line segments for both series.
8. Select the SLA to display data from.
9. **Period to retrieve**: Select a number of days weeks or months.
10. Click **Add**, then save the dashboard.

## Integrations

- Jira Service Management

## Dashboards

This gadget appears in the following dashboard: [IT Service Management team template](/cms_trial/space/RDD/146309962/IT+Service+Management+team+template/).