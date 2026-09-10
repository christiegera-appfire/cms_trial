# SLA History tab

The **SLA History** tab provides detailed insights into the lifecycle of SLAs. It organizes SLA states into cycles, allowing you to track performance, identify trends, and pinpoint areas for improvement.

To access the SLA History tab:

1. Navigate to a work item.
2. Click the **SLA History** tab.
3. Use the dropdown menu to view all SLAs associated with the work item and select one to explore its details.  
   You can check the **Overall Details** box to display time details.

   ![Time to SLA History tab](/cms_trial/assets/661b7af0-a1b5-4a52-a737-9f7bf65d34d7.png)

### SLA cycles

Each cycle consists of a start and an end condition. By examining your SLA history, you can easily see how long people spent between those conditions.

- The time between these start and end conditions shows how long it takes to complete a cycle (that is, elapsed time).
- When an SLA is stopped, its current cycle is marked as Met or exceeded based on its completion status.
- If a work item is reopened after an SLA cycle ends, a new cycle automatically starts.

The reset function isn’t a start condition, which means it cannot start a new cycle. If you want a reset to trigger a new cycle, the SLA’s end and reset conditions should be the same. If you reset an SLA that has already been completed, you will be able to start a new cycle with a reset condition.