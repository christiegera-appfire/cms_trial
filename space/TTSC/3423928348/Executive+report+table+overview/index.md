# Executive report table overview

The Executive report outputs data into a wide-format, dynamic matrix. Each row represents a grouped segment of work items, and columns expand horizontally to display discrete time intervals alongside overall totals.

Watch this video for a quick overview of the Executive reports results.

## Report access

Executive reports can be shared with other users with **Viewer** or **Editor** access.

| **Access** | **What you can do** |
| --- | --- |
| **Viewer** | Open the report, review aggregated data, and open detailed views. |
| **Editor** | Do everything a Viewer can do, plus change display and report settings, regenerate the report, manage saved Detailed Reports, update sharing settings, and delete the report. |
| **Owner** | The report owner always has full access. |

Report permissions override Jira permissions. Anyone with access to an Executive report can see the work items included in the report, regardless of their individual Jira permissions. Share reports with caution.

## Overview

The structural components of the Executive report table page operate as follows:

Image — asset pipeline pending  
Executive report table showing grouped rows, time-based columns, performance metrics, and summary totals.

## 1. Top action buttons

The actions available at the top right of the report depend on your access level.

- **Display:** Opens the *Display settings* dialog, where you can change the time interval and success rate thresholds used to display the report. This action is available to Editors and the report owner. Viewers can review the report but can't change Display settings.

  Image — asset pipeline pending  
  Display settings dialog with options for time interval and success rate thresholds.

  - **Time interval**: Allows you to choose how the report data is divided: *Daily*, *Weekly*, *Monthly*, and *Quarterly*.
  - **Success rate threshold**: Define the percentage ranges used to classify SLA performance. Success rate thresholds determine how the report highlights performance:

    - **Critical** performance (red)
    - **Warning** performance (yellow)
    - **Successful** performance (green)
  - Update the threshold values, then select **Apply** to update the report display.
- **Edit (Pencil icon):** Opens the report configuration, where you can change the date range, SLAs, filters, or groups. This action is available to Editors and the report owner.
- **Share:** Opens the sharing settings for the Executive report. Editors and the report owner can use these settings to control who can view or edit the report and whether saved Detailed Reports are shared.

## 2. Table controls

For *Daily* and *Weekly* time intervals, a **Focus period** dropdown and directional buttons appear at the top to let you slide through the report's timeline.

*Monthly* and *Quarterly* intervals display all available periods at once (up to 12 months or 4 quarters), so the focus layout switcher is hidden.

Image — asset pipeline pending  
Executive report showing the Focus period selector and navigation controls for Daily or Weekly views.

## 3. Space column (Data grouping)

The leftmost column displays the report’s configured Group by fields in order. For example, if the report is grouped by Space, Priority, and Assignee, the column header appears as Space/Priority/Assignee.

If you configured multiple grouping tiers, this column functions as an interactive, expandable tree hierarchy using the expand arrow (>).

This multi-level hierarchy transforms the table from a flat summary into an active root-cause analysis tool. If the overall SLA success rate is low, expanding the rows allows managers to pinpoint where the bottleneck resides.

## 4. Horizontal time period segmentation

The matrix lays out chronological trends and long-term aggregates side-by-side across a continuous horizontal view:

- **Period totals:** Moving left to right, columns are segmented by your chosen time interval (for example, columns for `2026-06` and `2026-07`). This makes trend tracking and month-over-month performance comparisons immediate.
- **Grand totals:** Pinned to the far-right section of the wide table is the **Total of "Past X Days"** block. This column aggregates all metrics across the entire report timeframe, summarizing the periodic buckets that precede it.

## 5. Key performance metrics

Within every time period and total column, the table populates three core metrics:

- **Issue count:** The total number of completed SLA items belonging to that specific row segment within that timeframe.
- **Average SLA duration:** The average time spent in specific SLAs (for example, *L3 - Time to Assign*, *L3 - Time to Resolve*, *L3 - Time in Triage*), formatted in `Hours:Minutes`.
- **SLA success rate:** The percentage of completed cycles that met their target goals. This metric is color-coded based on your configured thresholds for instant visual health checks:

  - **Red (Critical):** Low SLA adherence / high breach rates.
  - **Yellow (Warning):** Borderline or intermediate performance.
  - **Green (Successful):** Healthy performance / target compliance (for example, 100%).

Table headers include tooltips that explain what each value represents, such as issue count, average duration, and success rate.

Image — asset pipeline pending  
Tooltip explaining the meaning of a report table column or metric.

Hover over the headers to learn more about each.

Image — asset pipeline pending  
Tooltip explaining the meaning of a report table column or metric.

## 6. Aggregate totals (Bottom row)

Pinned permanently to the bottom of the table is the **Total** row. This row displays calculated averages and sums across *all* combined primary groups, offering executives an overall health index of the entire ecosystem for each period.

## 7. Detailed view

Most data cells within the periodic columns are interactive and clickable, serving as shortcuts to a deep-dive breakdown called detailed view. This view surfaces the underlying records represented by that specific cell and automatically inherits its exact filtering parameters.

Most data cells in the summary table are clickable and open the detailed view with the relevant filters applied. This includes cells in the Total row at the bottom of the table.

Empty cells are not clickable.

Image — asset pipeline pending  
Detailed view showing filtered work items and SLA results for a selected report cell.

The detailed view includes:

1. **Filters –** Active dropdowns populated automatically based on the selected report cell (e.g., *SLAs*, *Spaces*, *Product*, *Priority*, etc.). You can manually refine this view at any time by clicking Add filter or removing active pills.
2. A list of matching work items and their SLA outcomes.
3. **Focus period –** The corresponding focus period window.
4. **Save –** Once you have refined the filters inside a detailed view, you can preserve it as a dedicated, easily accessible child report.

   - Configure your detailed view filters, focus periods, and columns to your liking.
   - Click **Save**. The *Save report* modal appears.

     Image — asset pipeline pending  
     Save report dialog for creating a saved detailed view.
   - Enter a unique, recognizable name for the view.
   - Click **Save** again.

   Saved detailed views are nested directly beneath their parent Executive report on the main **Executive reports** page, indented and marked with an arrow icon. Opening a saved detailed view bypasses the primary matrix table and launches you straight into the filtered work item records list.

   Image — asset pipeline pending  
   Executive reports page showing saved detailed reports nested beneath a parent report.

   When you open a saved detailed view report, you can freely experiment with its fields to run temporary ad-hoc investigations. If you decide you want to discard your changes, click **Reset**. This instantly wipes your unsaved filter changes and reverts the view back to its previously saved baseline configuration state.   
   When editing a detailed report, you can also save your changes as a new detailed report. Click **Save**, enter a unique, recognizable name, and save the new version.

   Image — asset pipeline pending  
   Detailed view toolbar showing the Reset and Save controls.

In the detailed view, you can hover over each cell to learn more about it:

Image — asset pipeline pending  
Tooltip displayed for a value in the detailed view table.

## 8. Report scope summary

Displayed below the report title, the report scope summary shows the main configuration used to generate the report, such as the date range, selected SLAs, and selected spaces.

These values are read-only on the report results page and help you quickly confirm which completed SLA data the report is based on.

If you have Editor access or own the report, click the pencil button (see [Top action buttons](/cms_trial/space/TTSC/3423928348/Executive+report+table+overview/)), update the report configuration, and generate the report again to change the report scope. Viewers can review the report scope but can't change the report configuration.

## Executive reports page overview

The **Executive reports** landing page acts as your central control dashboard, indexing all pre-generated reports available in the environment.

Image — asset pipeline pending  
Executive reports page listing generated reports with their status, owner, and available actions.

| **Column** | **Description** |
| --- | --- |
| **Report Name** | The designated title assigned when the configuration was generated. Saved detailed view reports are nested directly underneath the parent Executive reports, indented with an arrow. |
| **Status** | The processing state of the report data generation (*Complete*, *In Progress*, or *Failed*). |
| **Request Date** | The exact timestamp showing when the report execution was run. |
| **Owner** | The user who owns the report. The report owner always retains full access. Reports can also be shared with Viewers and Editors. |
| **Actions** | Available actions depend on your access level. Editors can edit the report, generate it again, manage saved Detailed Reports, update sharing settings, and delete the report. Viewers have read-only access. |

Click on a report name to open it. When you open a generated report, Time to SLA shows the report results from the last generation. The report is not generated again automatically.

For example, if a report was generated using the **Last 30 days** timeframe, the report shows the 30-day period that applied when it was generated. It does not automatically update each day to show the latest rolling 30-day period.

To refresh a report, edit the report configuration and click **Generate** again. When you generate the report again, Time to SLA updates the results using the latest matching completed SLA data and the current report configuration. Results may change if new SLA cycles were completed, existing data changed, or the report timeframe now covers a different period.

Changes made to Executive reports are recorded in audit logs. To review Executive report updates, go to the [audit log page](/cms_trial/space/TTSC/36110718/Audit+logs/) and check the related entries.