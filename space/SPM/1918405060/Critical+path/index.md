# Critical path

## About the critical path

The critical path is based on dependencies. It represents the longest sequence of tasks that determines the project duration.

This feature highlights all the tasks on the critical path with a red color. Tasks on the Critical path will also be listed in the Gantt Infobar.

To highlight the entire sequence, you must define dependency links between tasks. Only the strong links that impact scheduling will determine the tasks on the critical path.

See more about the critical path in the video.

Critical path is supported in own scope, sub-scope, and none-scope boxes.

Once you establish task dependencies, the App will automatically draw the Critical path.

To display it, click **View** > **Critical Path**.

![Visibility drop-down menu, Critical path option](/cms_trial/assets/4d16ca60-c54c-44f6-8c57-f033e6e8262f.png)

The critical path is drawn for:

- tasks with start and end dates
- tasks with one date (either start or end date)

When many tasks are linked by dependencies on the critical path, and one of the tasks loses start and end dates, the critical path may be disrupted. Once the task has dates assigned again, the critical path will appear.

![critical-path-row.png](/cms_trial/assets/f160c1f8-5752-4b0e-9e79-437eab130693.png)

### Dependency path calculation

Use strong dependenciesto determine the correct order of task**s**.

- The path is calculated from the end (the last task(s) in the project).
- The algorithm works backward, looking for strong links connecting tasks.
- The most direct path (without a time gap between tasks) is highlighted.
- A gap between tasks is allowed only if an ASAP link has the [lag time](/cms_trial/space/SPM/1918406747/Lag+time/) added.

![critical-path-diagram.png](/cms_trial/assets/e5a15791-2cde-4c9a-90f3-ed54e213183b.png)

## Non-working days

The non-working days do not affect the critical path calculation. This means that if there are two tasks with a dependency on the critical path and the predecessor ends before a non-working day, the App will move the successor to start on the first working day, and both will remain on the critical path:

![critical-path-dependencies.png](/cms_trial/assets/d59580b3-8ad4-40ec-b441-6a9cfc97b1a2.png)

## Critical path tab

Tasks that are a part of the critical path are listed in the **Infobar** > **Critical Path** tab.

![Critical path - Infobar tab.mov](/cms_trial/assets/6ea9da9b-3793-4f52-bb87-3c397f50260d.mov)

### Export

Requires [BigTemplate](https://appfire.atlassian.net/wiki/spaces/BTc).

The critical path can be exported to an XLSX file from the Infobar tab.

![image-20251119-182758.png](/cms_trial/assets/212baee2-2916-41df-9078-9c27279fd6e8.png)![image-20251119-183258.png](/cms_trial/assets/5b1c0e49-aec3-42df-897c-8ce2208db0a0.png)