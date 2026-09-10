# Historical Insights

## **Overview**

Dashboard Hub’s Historical Insights gadget lets you visualize how specific Jira field values or numeric totals have changed over time. Unlike standard gadgets that display the current state of your data, this gadget samples historical data at defined intervals to show you exactly what your space looked like on a specific date.

## **Example use cases**

Use this gadget to answer critical historical questions, such as:

- **Volume Trends:** See how many High Priority work items were in your backlog at the start of every month.
- **Workload Snapshots:** View the total sum of story points sitting in in progress at the beginning of each week.
- **Historical Distribution:** Compare how field values like **Assignee** or **Space** were distributed across a specific date range.
- **Migration path for Dataplane Historical Values reports:** See the [Migrations from Dataplane](/cms_trial/space/RDD/3058532407/Historical+Insights/) section below.

## How to configure the gadget

This section explains how to add and configure the gadget.

**To add the gadget to a dashboard:**

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the **Search** bar in the *Add gadget* page to find the required gadget.
3. Select the **Historical** **Insights** gadget.
4. **Name** (*optional*): The name field is completed by default. You can edit the name to make it more meaningful to your team.
5. **Datasource**: Select the datasource from where you want to retrieve work item statistics. To learn more about datasource types, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).
6. Use the filter options to limit the data you analyze. Select a Jira filter or enter a JQL query.
7. Select a date range for the work items you want to track. For example, Last 4 months, Weekly, or define a custom date range.
8. Select how to group the results of the date range. You can group by Day, Week, Month, Quarter, or Year.
9. **Field tracking**

   1. **Value Of**: Select the work item field that you want to track, for example, **Resolution** or **Story Points**.
   2. **Aggregation mode**: Select **Snapshot** or **Cumulative**.
   3. **Status filter** (optional): Select one or more statuses to filter work items. You can choose to include or exclude the resulting work items.
10. **Chart type**

    1. Select a view type to visualize data best. The options are table view, pie charts, bar charts, area charts, or line charts.
    2. (*optional*) Depending on the view type you select, choose one or more segments to group the data.
11. Click **Add** to save the configuration and add the gadget to your dashboard. The gadget displays the configured data. In the example below, the gadget uses a stacked bar chart to display story points for work items grouped by day.

    ![Dashboard Hub Historical Insights gadget with a stacked bar chart visualization of story points grouped by day.](/cms_trial/assets/8eca38ed-9e6f-492e-9621-4ade093bbe1b.png)

You can resize or reposition any gadget in a dashboard to prioritize specific data and enhance the dashboard layout.

## **Migrations from Dataplane Reports**

If you are migrating from Dataplane to Dashboard Hub, the Historical Insights gadget consolidates three of your most-used legacy reports into a single, flexible report.

The table below shows you the default setting for the value mode in the Historical Insights gadget based on the existing Dataplane reports when migrated:

|  |  |
| --- | --- |
| **Legacy Dataplane Report** | **Dashboard Hub Configuration** |
| Issue Values Snapshots by Date | Ensurevalue mode is set to **Snapshot** |
| Issue Values Snapshots Sum by Date | Ensurevalue mode is set to **Cumulative** |
| Issue Values by Date | Ensurevalue mode is set to **Snapshot** |

While Dataplane requires separate report templates for snapshots (counts) vs. cumulative (sums), the Historical Insights gadget value mode options lets you configure these reports in a single gadget. See the [Feature comparison](/cms_trial/space/RDD/438796304/Feature+comparison+for+Dataplane+Data+Center+vs+Dashboard+Hub+Pro+Cloud/) page for more information on how your Dataplane reports are supported in Dashboard Hub.