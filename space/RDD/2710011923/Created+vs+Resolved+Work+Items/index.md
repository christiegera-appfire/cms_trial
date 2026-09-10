# Created vs Resolved Work Items

## Overview

The Created vs Resolved Work Items gadget provides a clear view of work item creation and resolution over time using two debt metrics alongside a stacked area chart, helping stakeholders understand not just how many work items are being created, but whether overall technical or operational debt is growing or shrinking.

The area chart visualizes the work items across a selected time period, using color-coded areas to clearly indicate whether the team is accumulating new debt or reducing existing debt at a specified point. The **Created** value represents all issues; **Resolved** shows the number of resolved issues in the selected time period.

![Dashboard Hub Dashboard Hub Created vs Resolved Work Items](/cms_trial/assets/974a475d-ed27-4a1e-9da6-dc8989974010.png)

The gadget combines two key metrics using the number of items created and resolved within the defined date range. Current Period Accumulated Debt shows how work is accumulating right now, while Historical Debt shows what has carried over unresolved from previous periods. Both trending downward over time is a strong indicator of a team successfully managing its workload.

### **Current Period Accumulated Debt**

This metric shows how many work items created during the *current* time period (day, week, or month, depending on your selected date range) have not yet been resolved. It provides a real-time view of whether your team is keeping pace with incoming work.

**Calculation:** `Created this period − Resolved this period`

A higher number means new work is arriving faster than it's being completed. A number at or near zero means your team is keeping pace with incoming work within the period. The gadget also displays the resolution rate for the current period as a percentage.

**Calculation:** `Resolved in period/Created in period x 100`

**Example**: If 5 work items were created this month and 1 was resolved, the current period’s accumulated debt is 4. The resolution rate is 20%. This calculation doesn’t include work items created in previous periods.

### **Historical Debt**

This shows how many work items created in *previous* periods were resolved in the *current* period, revealing the total unresolved deficit accumulated across all previous periods.

Periods where the team resolved more than was created do not offset deficits from other periods — each period's shortfall is counted independently. This ensures the metric accurately reflects the full weight of unresolved work carried forward over time, rather than allowing strong periods to obscure ongoing backlog pressure.

**Calculation:** `SUM of MAX(0, Created − Resolved) for each previous period`

**Example:** If previous periods result in a shortfall of 6, the current period adds 5, and resolves 1, then the redemption ratio is 6% using `1 / (11 + 6) × 100 = 1 / 17 × 100 = 5.9%`

---

## Interactive demo

Watch the interactive demo to learn how to add the gadget to your dashboard, or follow the steps under *Configure the gadget*.

<https://app.arcade.software/share/6o1FuhsXYzXr11mfWSAM>

## Configure the gadget

To add the gadget to a dashboard:

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the *Search* bar in the *Add gadget* page to find the required gadget.
3. Select the **Created vs Resolved Work Items** gadget.
4. Configure the gadget:

   1. **Name**: The name field is completed by default. You can edit the name to make it more meaningful to your team.
   2. **Datasource**: Select the Jira datasource from where you want to retrieve work item statistics. To learn more about datasource types, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).
   3. **Filter** (optional): Use this option to limit the work items to compare. Select a Jira filter or enter a JQL query and click **Load**. If you change the JQL filter, click **Load** again to refresh the work items used for the report.
   4. **Date range**: Select a date range for the work items. The dates provided filter the results of any applied filters.
   5. **Group by** (optional): Select an option from Day, Week, Month, Quarter or Year to aggregate work into a single data point. Day is the default selection.
5. Click **Add** to save the configuration and add the gadget to your dashboard.

You can resize or reposition any gadget in a dashboard to prioritize specific data and enhance the dashboard layout.