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

![Screenshot of the Resources panel settings in the Gantt module.](/cms_trial/assets/621b7ab3-2ab7-49ef-b1e7-0aa1b2271f74.png)

### Resize

To resize the Resources panel, click the line and resize as needed.

[Unmapped block: nestedExpand]

### Workload details dialog

Thanks to the workload details dialog, you can better understand what data is presented in the panel.

Click a colored tile to open the dialog:

![Screenshot of the Workload details window in the Gantt module.](/cms_trial/assets/6d4ab6e5-271c-4aa0-a5f7-5a78dbc98feb.png)

### Individual and team capacity

You can switch between the individual’s and the team’s capacity.

![Screenshot of the Resources panel in the Gantt module with the possibility to switch between the Individual's and Team's view.](/cms_trial/assets/327ee712-17fb-4d0b-b037-be62667816e5.png)

### Effort modes

The general rule is that effort is evenly distributed over the duration period. You can switch between three effort modes.

See the table to learn more about each mode.

| **Effort mode** | **Description** |
| --- | --- |
| Original Estimate | Use this mode during the planning phase, as the Original Estimate of time tracking is used, and it is assumed that assignees did not start logging work at this point. |
| Remaining Estimate | Use this mode to monitor the project's execution. In this case, the Remaining Estimate of time tracking is used. The remaining effort is evenly distributed starting from the current date.  In this mode, the Remaining duration is evenly distributed over the remaining task duration, starting from the current date, and the Spent time is evenly distributed over the past duration. |
| Story Points | This mode monitors the project’s execution in Story Points. To use this mode, ensure the story points value has been specified for tasks. |

![Screenshot of the effort modes available in the Resources panel in the Gantt module.](/cms_trial/assets/572f8c8f-4fba-4b14-a407-93b4ff34c1f0.png)

### Display settings

The capacity can be displayed in:

- Hours
- Man-days
- Percent (the ratio of workload to capacity, expressed as a percentage)
- Story Points

The available display settings depend on the selected effort mode. Not all display settings are available for every effort mode.

![Screenshot of the display settings in the Resources panel in the Gantt module.](/cms_trial/assets/1a7c1792-e269-4ef5-8480-ad1e9ed9b471.png)

### Aggregations

Display the workload as aggregated values in the following intervals:

- Daily
- Weekly (weeks count starting from Monday through Sunday)
- Monthly
- Quarterly
- Yearly
- By timeboxes

![Screenshot of the aggregation settings available in the Resources panel in the Gantt module.](/cms_trial/assets/9a6fd649-c3d5-48bd-8499-47e6dd5d78d5.png)

If a box contains multiple levels of timeboxes, you can choose which level is used to calculate the aggregations. Click a timebox name above the Gantt chart to view the aggregations calculated only for that specific timebox level.

![Screenshot of the Resources panel in the Gantt module.](/cms_trial/assets/eb9704c1-0988-4746-af1e-2afcfcdf52c5.png)

By default, the longest aggregation is yearly. However, in a portfolio box, you can have timeboxes that are own-scope boxes, which can span longer than one year. This lets you achieve aggregations beyond a single year, covering the full date range of the timebox and enabling long-term planning.

![Screenshot of the portfolio box with timeboxes under it.](/cms_trial/assets/ee685364-f138-40bd-a873-fd0f5956f330.png)

### Switch to the Resources module

Click the **Switch to Resources** button to be redirected to the Resources module.

![Screenshot of the Switch to Resources button in the Resources panel in the Gantt module.](/cms_trial/assets/fe608e62-27ad-4fe6-8197-7cbdadfcf5b6.png)

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

![Pop-up in the user workoad panel](/cms_trial/assets/e5982160-078c-49ca-90f6-b48e5dbf7847.png)

## Resources panel in Gantt module (new navigation)

The **Resources panel** offers a user-friendly method to monitor the workload assigned to individuals and teams. By opening the panel, you can easily view each assignee's and team’s workload, which can be displayed in hours, man-days, percent, or Story Points, and is color-coded to reflect capacity.

Workload information is filter-specific, focusing solely on tasks visible in the current view. To customize tasks and analyze different situations, use quick filters or the search box.

While workload distribution is typically uniform within a task, you have the flexibility to adjust it in the Resources module. For more in-depth information, visit the [Workload contouring](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297046379) page.

See the video about the Resources panel below.

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

![resources-panel-options.png](/cms_trial/assets/7eaf650e-2160-4b9a-a21d-fe5670d14c23.png)

### Resize

You can resize the panel by clicking and dragging the line between the panel and the Gantt module.

### Workload details dialog

Thanks to the workload details dialog, you can better understand what data is presented in the panel.

Click a colored tile to open the dialog:

![Screenshot of the Workload details window in the Gantt module.](/cms_trial/assets/6d4ab6e5-271c-4aa0-a5f7-5a78dbc98feb.png)

### Individual and team capacity

You can switch between the individual’s and the team’s capacity.

![resources-panel-individuals.png](/cms_trial/assets/21ef46f9-99a6-4f11-8d54-9901e3856409.png)

### Effort modes

The general rule is that effort is evenly distributed over the duration period. You can switch between three effort modes.

See the table to learn more about each mode.

| **Effort mode** | **Description** |
| --- | --- |
| Original Estimate | Use this mode during the planning phase, as the Original Estimate of time tracking is used, and it is assumed that assignees did not start logging work at this point. |
| Remaining Estimate | Use this mode to monitor the project's execution. In this case, the Remaining Estimate of time tracking is used. The remaining effort is evenly distributed starting from the current date.  In this mode, the Remaining duration is evenly distributed over the remaining task duration, starting from the current date, and the Spent time is evenly distributed over the past duration. |
| Story Points | This mode monitors the project’s execution in Story Points. To use this mode, ensure the story points value has been specified for tasks. |

![resources-panel-effort-modes.png](/cms_trial/assets/e91defbe-fdfe-4273-bafc-4354526f2225.png)

### Display settings

The capacity can be displayed in:

- Hours
- Man-days
- Percent (the ratio of workload to capacity, expressed as a percentage)
- Story Points

The available display settings depend on the selected effort mode. Not all display settings are available for every effort mode.

![resources-module-time.png](/cms_trial/assets/c43e92f5-cdfd-4c06-a985-bfa31b96ddae.png)

### Aggregations

Display the workload as aggregated values in the following intervals:

- Daily
- Weekly (weeks count starting from Monday through Sunday)
- Monthly
- Quarterly
- Yearly
- By timeboxes

![resources-module-weekly.png](/cms_trial/assets/519e4949-f7d5-44b9-bad0-30baa7343d80.png)

If a box contains multiple levels of timeboxes, you can choose which level is used to calculate the aggregations. Click a timebox name above the Gantt chart to view the aggregations calculated only for that specific timebox level.

![resources-panel-levels.png](/cms_trial/assets/0a60ddc7-5695-4e3a-87c7-de187d8dc01b.png)

By default, the longest aggregation is yearly. However, in a portfolio box, you can have timeboxes that are own-scope boxes, which can span longer than one year. This lets you achieve aggregations beyond a single year, covering the full date range of the timebox and enabling long-term planning.

![tasks-longer-than-year.png](/cms_trial/assets/8a596f4b-0129-455e-ae5d-fca2563a5666.png)

### Switch to the Resources module

Click the **Switch to Resources** button to be redirected to the Resources module.

![switch-to-resources.png](/cms_trial/assets/f894846e-32a2-4e29-b76e-32073b997a60.png)

## Workload vs capacity thresholds

The same rules for calculating and [displaying resources workload](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298028177) apply to the Resources panel in the Gantt module as in the Resources module.

Factors such as issue type (for example, an epic) and issue relationships (links, dependencies) have no impact on resource workload and capacity.

![overloaded-resources.png](/cms_trial/assets/3c057e88-08cb-4eb9-8db2-1529efc1aada.png)

### Coloring rules

The coloring thresholds can differ between teams and individuals.

The coloring settings are defined on the **Administration** > **Box types** > **click on a selected box type** > **Resources** >[**Coloring rules**](/cms_trial/space/SPM/1918799470/Resource+coloring+rules/) page.

## Capacity = 0

To learn more about the capacity calculation, see the [Capacity](/cms_trial/space/SPM/1918765081/Capacity+calculation/) page.

[Unmapped block: nestedExpand]

When the total availability of a resource exceeds 100%, a warning is displayed.

![resources-panel-warning.png](/cms_trial/assets/8f95725f-3142-4b84-abc4-ce6c9d1ba585.png)