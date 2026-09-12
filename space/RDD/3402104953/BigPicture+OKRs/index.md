# BigPicture OKRs

## Overview

Dashboard Hub’s **BigPicture OKRs** gadget lets you display your BigPicture OKR progress directly in Dashboard Hub. Select the Objectives you want to track, filter by period, owner, team, or status, and view the results as a tree of Objectives and Key Results with customizable columns. Or, use Dashboard Hub’s charts and aggregations to analyze them, such as a pie chart of OKRs per team.

You can use this gadget in Dashboard Hub and native Jira dashboards.

This gadget integrates with [BigPicture Advanced](https://support.appfire.com/space/SPM/3451617346). Make sure you have BigPicture Advanced installed and access to the OKR module.

![The BigPicture OKRs gadget in Dashboard Hub showing a stacked bar chart grouped by Team](/cms_trial/assets/35dc1983-94e4-438d-9a8d-ac8849338f15.png)

## Example use cases

Use this gadget to answer questions about your OKR progress, such as:

- **OKR Progress Tracking**: Monitor the progress of Objectives and their Key Results at a glance without leaving your dashboard.
- **Team OKR Overview**: Filter by team or owner to see which OKRs are assigned to specific people or groups.
- **Period Reviews**: Filter by period to focus on quarterly or annual OKRs during review cycles.
- **Stakeholder Reporting**: Share OKR progress with people outside Jira by embedding dashboards in Confluence pages.

Watch the overview video, or follow the steps below to get started.

Click to view transcript

The team that delivered dashboard snapshots straight to your inbox now brings you a single place to manage all your subscriptions, at once.

To view your subscriptions, open the More actions menu in the top bar of any dashboard and select My subscriptions. Here, you'll see every in one list, the last run status, next scheduled date, who's receiving it, and any restrictions all at a glance.  
If you manage several subscriptions, you can filter your view to see all subscriptions, just the ones you own, or the ones you're subscribed to. Or, use the search field to quickly find a subscription for a specific dashboard.

Each has its own actions menu. If you're the dashboard editor, you can select edit, to update the schedule details, recipient list, or delete the subscription for everyone. Or select run now to send an ad hoc snapshot email right away. So you don't need to wait for an update or open individual dashboards.

Anyone on the list can unsubscribe to remove their name from the recipient list. If you need to subscribe again later, just reach out to a dashboard editor.

With my subscriptions, there's no more digging through dashboards or inboxes. Keep track of everything you follow, own, and send with ease.

## Prerequisites

To use this gadget, you need:

- A **BigPicture OKRs** datasource connected to Dashboard Hub. This requires a BigPicture OKR API token.
- An existing **Jira datasource** from the same Jira instance where BigPicture is installed.

### How to create a BigPicture OKR API token

Before you can add the datasource, you need an API token from the BigPicture OKR module. You must be a Jira Admin, an In-module Admin, or have the **API access** permission in your OKR role.

1. From the OKR module, go to **Settings** > **API**.
2. Click **+Generate new token**.
3. Enter a name for the token and click **Create**.
4. Copy the generated token and store it securely. You will not be able to retrieve it later.

For more information, see [OKR API](https://appfire.atlassian.net/wiki/spaces/SPM/pages/3064169104) in the BigPicture documentation.

### How to add a BigPicture OKRs datasource

1. In Dashboard Hub, go to **Datasources** and click **Add datasource**.
2. Select **BigPicture OKRs**.
3. Enter your BigPicture OKR module API token.
4. Select the linked Jira datasource from the same instance.
5. Click **Save**.

To learn more about datasource types and management, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).

## How to configure the gadget

This section explains how to add and configure the gadget.

**To add the gadget to a dashboard:**

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the **Search** bar in the *Add gadget* page to find the required gadget.
3. Select the **BigPicture OKRs** gadget.
4. **Name** (*optional*): The name field is completed by default. You can edit the name to make it more meaningful to your team.
5. **Datasource**: Select a BigPicture OKRs datasource. To learn more about datasource types, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).
6. **Select OKRs**: Use the OKR selector to choose which Objectives to include. Select Objectives or apply a date range. Key results are included automatically with their parent objective.

   ![The BigPicture OKRs configuration page showing the objective selector](/cms_trial/assets/f0eadc9c-e026-4d7f-a16f-23d029abb5a3.png)

Only selected objectives are automatically updated in the dashboard.

1. (Optional) Use **OKR filters** to narrow the results. See the next section for details.
2. **Columns**: Select the columns to display in the tree view, and drag to reorder. At least one column must be present.
3. **Visualization**: Select a view type. See [View types](/cms_trial/space/RDD/3402104953/BigPicture+OKRs/) for the available options.
4. A preview of the gadget displays on the configuration page. When you are ready, click **Apply** to save the configuration and add the gadget to your dashboard.

You can resize or reposition any gadget in a dashboard to prioritize specific data and enhance the dashboard layout.

### OKR filters

Use the following **OKR filters** section to refine which OKRs appear in the gadget. All filters are populated dynamically from your BigPicture data.

| **Filter** | **Description** |
| --- | --- |
| Period | Filter by OKR period, for example, Q1 2026 or H1 2026. |
| Owner | Filter by the person responsible for the Objective or Key Result. |
| Team | Filter by team assignment. |
| Status | Filter by OKR status, for example, On Track, At Risk, or Off Track. |
| Collaborators | Filter by people contributing to the OKR. |
| OKR type | Filter by type, for example, Objective or Key Result. |
| Labels | Filter by labels applied to OKRs in BigPicture. |

### OKR rows

The **OKR rows** section lets you choose which levels of the OKR hierarchy to include in the gadget. Use the selection field to include or exclude Objectives or Key Results from the display.

## View types

Select the view type that best visualizes your BigPicture OKR data. For more examples of BigPicture visualizations, and gadget customizations, see [BigPicture Custom Charts](https://support.appfire.com/space/RDD/629873831/BigPicture+Custom+Charts). The options work the same way for both gadgets.

A switch in the gadget header lets you display a chart or a table with the underlying data. This option is available in the gadget’s main view when the dashboard is not in edit mode.

### Nested Table (default)

The default view displays your OKRs as a hierarchical tree, with Objectives as parent rows and their Key Results nested beneath. Each row shows the values for your selected columns.

*[Screenshot placeholder: Tree view showing Objectives with nested Key Results and column values]*

**Example:** Track quarterly Objectives with their Key Results, showing progress percentage, status, and owner for each.

### 1D Pivot Table

The 1D Pivot Table view provides a single-dimensional perspective on your OKR data. Select a field to group by, and apply an aggregation (count, sum, min, max, or mean) to summarize the data.

**Example:** Count the number of OKRs per owner to see workload distribution.

### 2D Pivot Table

The 2D Pivot Table view adds a second dimension by cross-tabulating two fields. Select row and column dimensions and an aggregation to analyze OKR data across both dimensions simultaneously.

**Example:** Cross-tabulate OKR status by team to see how each team’s OKRs are progressing.

### Pie and multi-pie charts

A pie chart shows each segment’s share of the total, with an accompanying table of values and percentages. A multi-pie chart adds a second dimension as an outer ring.

**Example:** Show the proportion of OKRs by status.

![Pie chart showing OKRs grouped by status.](/cms_trial/assets/ac5effda-bfcb-46c7-a35f-3101b0c4257d.png)

### Bar charts (bar, grouped, stacked)

Bar charts compare values across categories. Use grouped or stacked variants to add a second dimension.

**Example:** Compare the number of OKRs per team, split by status.

![Stacked bar chart comparing the number of OKRs by team, grouped by status.](/cms_trial/assets/7d2f3a93-018d-44d4-a673-4a7f9ce38d47.png)

### Line and multi-line charts

Line charts visualize trends over time. Use the multi-line variant to compare several series.

**Example:** Track OKR progress over a quarter.

## Integrations

- BigPicture Advanced (OKR module)

## Related pages

- [BigPicture Custom Charts](https://support.appfire.com/space/RDD/629873831/BigPicture+Custom+Charts)