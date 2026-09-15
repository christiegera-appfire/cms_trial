# Analyze a Workflow Intelligence report

After generating or opening a Workflow Intelligence report, use the report table to compare durations across work items. You can also summarize the results to identify broader trends or expand a work item to investigate its workflow and SLA data.

![image-20260914-234536.png](/cms_trial/assets/da880fe6-dc4e-4ab0-87fc-38e2495c3555.png)

## Review the report table

Each row represents a work item. The left side of the table shows the work item key, summary, and any fields added under **Work item columns**.

The remaining columns show how long each work item spent across the main and sub-columns selected during report configuration. For example, when **Assignee** is the main column and **Status** is the sub-column, each duration shows how long the work item spent in a status while assigned to that person.

A dash means that no tracked time is available for that combination.

If the report includes SLAs, the SLA indicator summarizes their overall state for each work item:

- **Breached** appears if at least one included SLA has breached.
- **Met** appears when all included SLAs are met.
- **In progress** appears when at least one included SLA is running and none have breached.
- **Not started** appears when the included SLAs have not started yet.
- **No SLA** appears when none of the included SLAs apply to the work item.

## Summarize the report

Click **Summarize** to display an overview above the report table. The summary is based on the current report configuration, so its labels and available cards change depending on the main column, sub-column, and included SLAs.

![Screenshot 2026-09-15 at 01.47.06.png](/cms_trial/assets/e450bfe8-3ede-4784-a0a0-46e6e847218f.png)

### Summary

The workflow summary can include:

| **Card** | **What it shows** |
| --- | --- |
| **Report statistics** | The number of work items and spaces, the number of distinct values for the selected report columns, and the date range. |
| **Work time distribution** | The main-column value that accounts for the largest share of tracked workflow time. |
| **Average elapsed time by** ***main column*** | The main-column values with the longest average elapsed time. Each result also shows the number of associated work items. |
| **Assignee work time** | The total tracked workflow time and number of work items for each assignee. This card appears only when **Assignee** is selected as the main or sub-column. |

### SLA insights

| **Card** | **What it shows** |
| --- | --- |
| **Overall SLA compliance** | The percentage and number of assessed SLAs that were met. |
| **Breached SLAs** | The percentage and number of assessed SLAs that breached, including where breaches are most concentrated. |
| **SLAs in progress** | The percentage and number of SLAs that are still running. |
| **Lowest compliance SLA** | If there are multiple SLAs in the configuration, this card shows the SLA with the lowest compliance rate. |

## Inspect a work item

Select the expand icon beside a work item to see how its time is distributed across the report columns.

The information shown depends on how the report was configured:

- When **Display SLA detail columns per work item** is selected, the report shows an **SLA breakdown**. When this option is cleared, the report shows a [**Workflow breakdown**](/cms_trial/space/TTSC/3638689841/Analyze+a+Workflow+Intelligence+report/).

  ![Untitled 2-20260915-000029.gif](/cms_trial/assets/b0fee637-743c-4d3b-8ed3-98b5f85c3dd9.gif)
- When **Time period** is selected as the main column, the expanded view lists the periods during which the work item was active. Each period shows its tracked time and percentage of the total.

  If a sub-column is included, the progress bars also show how the time within each period was distributed across the sub-column values.

  ![image-20260915-001517.png](/cms_trial/assets/9699157b-2a49-4f2e-a016-1522e27b8dfb.png)
- When **Break the main column down by a sub column** is selected, the breakdown includes both dimensions. When it is cleared, only the main-column values are shown.

### View the SLA breakdown

When SLA details are enabled, the expanded view shows each included SLA and its current status. Select an SLA to see its target, deadline, elapsed time, and exceeded time.

If a work item has several SLAs, the indicator in the report table summarizes their overall state. A work item is marked **Breached** when at least one included SLA has breached, even when another SLA is met or still in progress. It is marked **Met** only when all included SLAs are met. **In progress** appears when at least one included SLA is running and none have breached. **Not started** appears when the included SLAs have not started yet, and **No SLA** appears when none of the included SLAs apply to the work item.

The **SLA running time** section shows how long the selected SLA was active under each main-column value. When the report also uses a sub-column, the progress bars are divided into segments for the corresponding sub-column values. Hover over a segment to see its value, duration, and percentage of the SLA running time.

![Screenshot 2026-09-15 at 02.10.30.png](/cms_trial/assets/11f7b0ef-d36e-4a45-aa59-a309a3c21c56.png)

The durations in the report table and the SLA breakdown may be different. The table shows the work item’s tracked workflow time, while the expanded SLA breakdown includes only the periods when the selected SLA was active. Time recorded before the SLA starts or after it stops is not included in the SLA running time.

### View the Workflow breakdown

When **Display SLA detail columns per work item** is cleared, expanding a work item shows a **Workflow breakdown** instead.

![image-20260915-000829.png](/cms_trial/assets/54247a09-eaa3-468e-afd7-4fa9b38dafd9.png)

The breakdown shows the work item’s total tracked workflow time for each main-column value. It also shows the percentage of the work item’s total time associated with that value.

When a sub-column is included, each progress bar is divided according to the sub-column values. For example, with **Assignee** as the main column and **Status** as the sub-column, each row represents an assignee and the bar shows how that assignee’s time was distributed across statuses. Hover over a segment to see the status, duration, and percentage.

When **Break the main column down by a sub column** is cleared, only the main-column values are displayed. For example, a report grouped only by assignee shows the time for each assignee without a status breakdown.