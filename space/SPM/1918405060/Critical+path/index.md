# Critical path

## About the critical path

The critical path is based on dependencies. It represents the longest sequence of tasks that determines the project duration.

This feature highlights all the tasks on the critical path in red. Tasks on the Critical path will also be listed in the Gantt Infobar.

To highlight the entire sequence, you must define dependency links between tasks. Only the strong links that impact scheduling will determine the tasks on the critical path.

See more about the critical path in the video.

Critical path is supported in own scope, sub-scope, and none-scope boxes.

Once you establish task dependencies, the App will automatically draw the Critical path.

To display it, click **View** > **Critical Path**.

![Visibility drop-down menu, Critical path option](/cms_trial/assets/bd822c71-6369-45f1-9c93-4bcba8a90686.png)

The critical path is drawn for:

- tasks with start and end dates
- tasks with one date (either start or end date)

When many tasks on the critical path are linked by dependencies and one of the tasks loses its start and end dates, the critical path may be disrupted. Once the task has dates assigned again, the critical path will appear.

![critical-path-row.png](/cms_trial/assets/9407672b-adf1-4210-bd61-a4f5f10f620c.png)

### Dependency path calculation

Use strong dependenciesto determine the correct task order.

- The path is calculated from the end (the last task(s) in the project).
- The algorithm works backward, looking for strong links connecting tasks.
- The most direct path (without a time gap between tasks) is highlighted.
- A gap between tasks is allowed only if an ASAP link includes the [lag time](/cms_trial/space/SPM/1918406747/Lag+time/).

![critical-path-diagram.png](/cms_trial/assets/dbc4971a-b053-4234-ac61-68a476d1967f.png)

## Non-working days

The non-working days do not affect the critical path calculation. This means that if there are two tasks with a dependency on the critical path and the predecessor ends before a non-working day, the App will move the successor to start on the first working day, and both will remain on the critical path:

![critical-path-dependencies.png](/cms_trial/assets/a9244454-353f-4e65-8128-0640e717816a.png)

## Critical path tab

Tasks that are a part of the critical path are listed in the **Infobar** > **Critical Path** tab.

![Critical path - Infobar tab.mov](/cms_trial/assets/1563707d-24b5-4219-8778-d5e2832cd234.mov)

### Export

Requires [BigTemplate](https://appfire.atlassian.net/wiki/spaces/BTc).

You can export the critical path to an XLSX file from the Infobar tab.

![image-20251119-182758.png](/cms_trial/assets/b9e0b918-86af-45fb-ab5c-44fc9f631929.png)![image-20251119-183258.png](/cms_trial/assets/0e9effeb-206c-4378-b1e3-5bd178c9ac4f.png)