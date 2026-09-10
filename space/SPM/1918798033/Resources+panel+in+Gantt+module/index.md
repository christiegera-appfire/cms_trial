# Resources panel in Gantt module

## Resources panel in Gantt module (old navigation)

The **Resources panel** offers a user-friendly method to monitor the workload assigned to individuals and teams. By opening the panel, you can easily view each assignee's and team’s workload, which can be displayed in hours, man-days, percent, or Story Points, and is color-coded to reflect capacity.

Workload information is filter-specific, focusing solely on tasks visible in the current view. To customize tasks and analyze different situations, use quick filters or the search box.

While workload distribution is typically uniform within a task, you have the flexibility to adjust it in the Resources module. For more in-depth information, visit the [Workload contouring](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297046379) page.

See the video about the Resources panel below.

## Enable Resources panel

To enable the Resources panel in the Gantt module:

1. Click the **Show/Hide Resources** button in the top menu.
2. The Resources panel appears at the bottom of the page.

See an interactive demo below.

## Customize Resources panel

All panel settings are available above the panel:

- Workload - Individuals, Teams
- Effort mode - Original estimate, Remaining estimate, Story Points
- Display in - Hours, Man-days, Percent, Story Points
- Aggregations - Daily, Weekly, Monthly, Quarterly, Yearly, By timeboxes

![Screenshot of the Resources panel settings in the Gantt module.](/cms_trial/assets/a00aa434-3454-489e-be6a-3803b20da1b1.png)

### Resize

To resize the Resources panel, click the line and resize as needed.

[Unmapped block: nestedExpand]

### Workload details dialog

Thanks to the workload details dialog, you can better understand what data is presented in the panel.

Click a colored tile to open the dialog:

![Screenshot of the Workload details window in the Gantt module.](/cms_trial/assets/9adef6f6-64dc-4127-a899-87ae610e195f.png)

### Individual and team capacity

You can switch between the individual’s and the team’s capacity.

![Screenshot of the Resources panel in the Gantt module with the possibility to switch between the Individual's and Team's view.](/cms_trial/assets/37e81cd3-6bb3-4085-901c-4208d6c0fabd.png)

### Effort modes

The general rule is that effort is evenly distributed over the duration period. You can switch between three effort modes.

See the table to learn more about each mode.

| **Effort mode** | **Description** |
| --- | --- |
| Original Estimate | Use this mode during the planning phase, as the Original Estimate of time tracking is used, and it is assumed that assignees did not start logging work at this point. |
| Remaining Estimate | Use this mode to monitor the project's execution. In this case, the Remaining Estimate of time tracking is used. The remaining effort is evenly distributed starting from the current date.  In this mode, the Remaining duration is evenly distributed over the remaining task duration, starting from the current date, and the Spent time is evenly distributed over the past duration. |
| Story Points | This mode monitors the project’s execution in Story Points. To use this mode, ensure the story points value has been specified for tasks. |

![Screenshot of the effort modes available in the Resources panel in the Gantt module.](/cms_trial/assets/0c7dce64-e704-4b53-bc30-93ed859e8ac9.png)

### Display settings

The capacity can be displayed in:

- Hours
- Man-days
- Percent (the ratio of workload to capacity, expressed as a percentage)
- Story Points

The available display settings depend on the selected effort mode. Not all display settings are available for every effort mode.

![Screenshot of the display settings in the Resources panel in the Gantt module.](/cms_trial/assets/e7a5ac0a-ccd7-496f-96ed-5a037f4579d8.png)

### Aggregations

Display the workload as aggregated values in the following intervals:

- Daily
- Weekly (weeks count starting from Monday through Sunday)
- Monthly
- Quarterly
- Yearly
- By timeboxes

![Screenshot of the aggregation settings available in the Resources panel in the Gantt module.](/cms_trial/assets/a28746fd-42b1-4007-9f3a-2d56e4425783.png)

If a box contains multiple levels of timeboxes, you can choose which level is used to calculate the aggregations. Click a timebox name above the Gantt chart to view the aggregations calculated only for that specific timebox level.

![Screenshot of the Resources panel in the Gantt module.](/cms_trial/assets/97e5549a-65f2-4b5b-a324-07149b1e2eac.png)

By default, the longest aggregation is yearly. However, in a portfolio box, you can have timeboxes that are own-scope boxes, which can span longer than one year. This lets you achieve aggregations beyond a single year, covering the full date range of the timebox and enabling long-term planning.

![Screenshot of the portfolio box with timeboxes under it.](/cms_trial/assets/887702e5-0fa9-44e7-8b9b-a3beb5496aeb.png)

### Switch to the Resources module

Click the **Switch to Resources** button to be redirected to the Resources module.

![Screenshot of the Switch to Resources button in the Resources panel in the Gantt module.](/cms_trial/assets/764b018e-62fa-48a3-84b8-ef2680f29c43.png)

## Workload vs capacity thresholds

The same rules for calculating and [displaying resources workload](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298028177) apply to the Resources panel in the Gantt module as in the Resources module.

Factors such as issue type (for example, an epic) and issue relationships (links, dependencies) have no impact on resource workload and capacity.

### Coloring rules

The coloring thresholds can differ between teams and individuals.

The coloring settings are defined on the **Administration** > **Box types** > **click on a selected box type** > **Resources** >[**Coloring rules**](/cms_trial/space/SPM/1918799470/Resource+coloring+rules/) page.

## Capacity = 0

To learn more about the capacity calculation, see the [Capacity calculation](/cms_trial/space/SPM/1918765081/Capacity+calculation/) page.

[Unmapped block: nestedExpand]

When the total availability of a resource exceeds 100%, a warning is displayed.

![Pop-up in the user workoad panel](/cms_trial/assets/f876fe64-d17c-4af2-9c20-e3057cc513d6.png)

## Resources panel in Gantt module (new navigation)

The **Resources panel** offers a user-friendly method to monitor the workload assigned to individuals and teams. By opening the panel, you can easily view each assignee's and team’s workload, which can be displayed in hours, man-days, percent, or Story Points, and is color-coded to reflect capacity.

Workload information is filter-specific, focusing solely on tasks visible in the current view. To customize tasks and analyze different situations, use quick filters or the search box.

While workload distribution is typically uniform within a task, you have the flexibility to adjust it in the Resources module. For more in-depth information, visit the [Workload contouring](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297046379) page.

See the video about the Resources panel below.

<https://appfire.wistia.com/medias/oazasrlyh9>

## Enable Resources panel

To enable the Resources panel in the Gantt module:

1. Click the **Show/Hide Resources** button in the top menu.
2. The Resources panel appears at the bottom of the page.

See an interactive demo below.

<https://app.arcade.software/share/AMK3wsVnhy6gPqdUKVUg>

## Customize Resources panel

All panel settings are available above the panel:

- Workload - Individuals, Teams
- Effort mode - Original estimate, Remaining estimate, Story Points
- Display in - Hours, Man-days, Percent, Story Points
- Aggregations - Daily, Weekly, Monthly, Quarterly, Yearly, By timeboxes
- Switch to Resources - selec this option to switch to the Resources module

![resources-panel-options.png](/cms_trial/assets/44f08d2f-1931-49dd-8fc3-4da47b4b6440.png)

### Resize

You can resize the panel by clicking and dragging the line between the panel and the Gantt module.

### Workload details dialog

Thanks to the workload details dialog, you can better understand what data is presented in the panel.

Click a colored tile to open the dialog:

![Screenshot of the Workload details window in the Gantt module.](/cms_trial/assets/9adef6f6-64dc-4127-a899-87ae610e195f.png)

### Individual and team capacity

You can switch between the individual’s and the team’s capacity.

![resources-panel-individuals.png](/cms_trial/assets/60fc6d1d-d94d-4b84-8b5d-db3c57c97569.png)

### Effort modes

The general rule is that effort is evenly distributed over the duration period. You can switch between three effort modes.

See the table to learn more about each mode.

| **Effort mode** | **Description** |
| --- | --- |
| Original Estimate | Use this mode during the planning phase, as the Original Estimate of time tracking is used, and it is assumed that assignees did not start logging work at this point. |
| Remaining Estimate | Use this mode to monitor the project's execution. In this case, the Remaining Estimate of time tracking is used. The remaining effort is evenly distributed starting from the current date.  In this mode, the Remaining duration is evenly distributed over the remaining task duration, starting from the current date, and the Spent time is evenly distributed over the past duration. |
| Story Points | This mode monitors the project’s execution in Story Points. To use this mode, ensure the story points value has been specified for tasks. |

![resources-panel-effort-modes.png](/cms_trial/assets/d55873cb-81b3-4bc9-818a-c6e649b6f262.png)

### Display settings

The capacity can be displayed in:

- Hours
- Man-days
- Percent (the ratio of workload to capacity, expressed as a percentage)
- Story Points

The available display settings depend on the selected effort mode. Not all display settings are available for every effort mode.

![resources-module-time.png](/cms_trial/assets/c5a72e42-0fea-413d-9918-a27cd33061c6.png)

### Aggregations

Display the workload as aggregated values in the following intervals:

- Daily
- Weekly (weeks count starting from Monday through Sunday)
- Monthly
- Quarterly
- Yearly
- By timeboxes

![resources-module-weekly.png](/cms_trial/assets/8f49607b-7085-49a6-8b6c-e332eef660d3.png)

If a box contains multiple levels of timeboxes, you can choose which level is used to calculate the aggregations. Click a timebox name above the Gantt chart to view the aggregations calculated only for that specific timebox level.

![resources-panel-levels.png](/cms_trial/assets/a4f772a8-c65c-4b2d-83e5-76eaf85bfedf.png)

By default, the longest aggregation is yearly. However, in a portfolio box, you can have timeboxes that are own-scope boxes, which can span longer than one year. This lets you achieve aggregations beyond a single year, covering the full date range of the timebox and enabling long-term planning.

![tasks-longer-than-year.png](/cms_trial/assets/abc30341-d369-43bb-9213-b4d2aedb3d37.png)

### Switch to the Resources module

Click the **Switch to Resources** button to be redirected to the Resources module.

![switch-to-resources.png](/cms_trial/assets/e9a13519-fc6b-4f61-b779-179e309c5d57.png)

## Workload vs capacity thresholds

The same rules for calculating and [displaying resources workload](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298028177) apply to the Resources panel in the Gantt module as in the Resources module.

Factors such as issue type (for example, an epic) and issue relationships (links, dependencies) have no impact on resource workload and capacity.

![overloaded-resources.png](/cms_trial/assets/2c3a1f24-9c7a-4529-a28d-e058a1273f8a.png)

### Coloring rules

The coloring thresholds can differ between teams and individuals.

The coloring settings are defined on the **Administration** > **Box types** > **click on a selected box type** > **Resources** >[**Coloring rules**](/cms_trial/space/SPM/1918799470/Resource+coloring+rules/) page.

## Capacity = 0

To learn more about the capacity calculation, see the [Capacity](/cms_trial/space/SPM/1918765081/Capacity+calculation/) page.

[Unmapped block: nestedExpand]

When the total availability of a resource exceeds 100%, a warning is displayed.

![resources-panel-warning.png](/cms_trial/assets/c812dbab-fe7f-4563-8528-86b58418f74f.png)