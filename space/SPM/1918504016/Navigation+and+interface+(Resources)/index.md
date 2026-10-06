# Navigation and interface (Resources)

## Navigation and interface (Resources) (old navigation)

Click to expand the guide

The Resources module can display data essential to managing your resources in several views (swimlanes). The view customization options are under the **View** dropdown.

The following options are available:

![image-20241216-085637.png](/cms_trial/assets/188cffd2-2e96-40b0-ae1e-a3cf2d217907.png)

- Expand/ Collapse all rows (swimlanes)
- Show:

  - [Workload](/cms_trial/space/SPM/1918864229/Workload+details/) (adds the workload row to every swimlane)
  - Remaining capacity (adds the remaining capacity row to every swimlane)
  - [Capacity](/cms_trial/space/SPM/1918765081/Capacity+calculation/) (adds the capacity row to every swimlane)
  - Values on heatmap (displays values on the [colored bars](/cms_trial/space/SPM/1918636529/Workload%2C+capacity%2C+and+utilization+-+tile+coloring/) in every enabled row)
  - Tasks (displays tasks in respective swimlanes)
  - Overall assignment (shows all the tasks assigned to a resource across all the boxes the resource is assigned to)
  - [Timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) (if configured, displays timeboxes)
- Warnings:

  - Estimates
  - Assignment
  - Workload contour

## [Warnings](/cms_trial/space/SPM/1918538128/Task+warnings+(Resources+module)/)

Warnings highlight the misconfigured and potentially problematic tasks that need extra attention. Once enabled, you will see a red frame around the problematic tasks.

![contentId-1918504016](/cms_trial/assets/0f8ee551-46c8-48be-a6dc-e67ea6af5ccb.png)

## Show overall assignment

The **Show overall assignment** option displays all the tasks your resources are assigned to, even if those tasks belong to the scope of other boxes. This gives you a real insight into the resource's actual workload and remaining capacity, allowing you to quickly see if you can assign them more tasks from your project.

### Identify tasks in the scope of other boxes

The tasks in the scope of other boxes are translucent. Those tasks update the resource's workload and impact their remaining capacity.

When you mouse over such a task, a warning tooltip will inform you that it does not belong to the current box and that you cannot edit it.

![new-resource-grid.png](/cms_trial/assets/88a0d2d2-95ee-414a-a4a8-8831c1e0c5f5.png)

## Grid overview

The table below describes all the information presented on the resource grid. If you want to add or hide some information, use the **View** menu and uncheck the view options.

![grid-overview.png](/cms_trial/assets/20366a51-e391-48ad-bb2e-d157097778b9.png)

| **Feature** | **Description** |
| --- | --- |
| Timeboxes | Define consecutive timeframes used for work planning, such as sprints, iterations, increments, or stages. |
| Summary row | Shows the sum of all the data available in a selected time range. |
| Unassigned work | Show the sum of the unassigned work. |
| Allocation (workload) vs capacity | - Individuals, projects, and skills:    - Green - utilization under 100%   - Red - utilization is above 100% - Teams:    - Green - 0% to 80% utilization   - Yellow - 80 to 101% utilization   - Red - 101% or higher utilization   To learn more, see the [Coloring rules - workload vs capacity](/cms_trial/space/SPM/1918799470/Resource+coloring+rules/) page. |
| Overall assignment | This feature can show all the tasks to which the resource is assigned that do not fit the Program's scope. Those tasks will be transparent and can not be reassigned or moved. |
| [Capacity](/cms_trial/space/SPM/1918765081/Capacity+calculation/) | The availability of a resource derived from the Workload plans and reduced by the non-working days resulting from Holiday plans. |
| Remaining capacity | Remaining availability when the resource is assigned to a task in a given time period. |
| Non-working days | Non-availability period of the resource. |

## Working/ non-working days view

Modify the 'View' options (deselect items). The grayed-out grid days indicate time off for a given resource.

![view-options.png](/cms_trial/assets/957c1c37-9f61-428a-8de1-19b70a26922e.png)![days-grid.png](/cms_trial/assets/9704fd60-88dc-4d60-bf51-e8d1aacff525.png)

## [Timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/)

There is a graphical representation of timebox aggregation periods when no timeboxes are shown on a timeline.

There is also the possibility to right-click on a timebox and choose "go to earlier timeboxes”. It helps when timeboxes are enabled, but none are in the given period.

![timeboxes.png](/cms_trial/assets/227428e3-5516-4f9f-9867-11032ab82fc0.png)

## Time period and aggregation

To learn more, see the [Time period and aggregation](/cms_trial/space/SPM/1918702075/Time+period+and+aggregation/) page.

## Search and snipe to task

Use the **Snipe to result** option to highlight all tasks that fit the search criteria. It works similarly to the "Ctrl+F" feature in any web browser. The task is dynamically highlighted.

![Snipe to result - resources module.mov](/cms_trial/assets/45077fde-09a9-4354-a544-7e700d859b90.mov)

## Task dates visibility and resizing

As tasks are stretched and moved within the Resources timeline, their new dates are displayed on both sides of the taskbar. Additionally, tasks can be resized more intuitively, providing a clearer and more user-friendly interface for adjusting task durations.

![As you move or stretch a taskbar, you can see new task dates on the sides.](/cms_trial/assets/dd506483-41d1-480e-b7ac-a7e01b951bb8.png)

## Tooltips

Tooltips have been incorporated into the interface, offering quick access to additional information about tasks and other elements within the Resources module. This enhances user experience by providing relevant details without cluttering the main view.

![An example of the enhanced tooltip explaining the icon and its meaning.](/cms_trial/assets/6f6601db-94c3-4267-bcf8-f27ed7ef208d.png)

## Grid cells show units

The grid cells now display units, making it easier for users to understand the scale and timeframes of the tasks at a glance. This feature ensures that users can quickly grasp the duration and deadlines of tasks without needing to delve into detailed views.

![units displayed in the resources module.mp4](/cms_trial/assets/9a1f9800-b6fe-4be5-b115-04bf93b1e585.mp4)

## Jump to the nearest task in a swimlane

A new functionality allows users to quickly jump to the nearest task. This feature is particularly useful for large projects with numerous tasks, as it saves time and improves navigation efficiency.

![Snipe to a next or previous task.mov](/cms_trial/assets/e3396136-9f65-4fcf-95a5-92759cf10e2c.mov)

## Custom task colors on resources

Tasks can now be color-coded according to user preferences, making it easier to distinguish between different types of tasks or project phases at a glance. This customization enhances the visual organization and management of tasks within the chart. Task coloring is consistent across BigPicture - the same task colors can be seen in the Gantt module.

Image — asset pipeline pending  
task colors on teh resources module.mov

## Navigation and interface (Resources) (new navigation)

Click to expand the guide

The Resources module can display data essential to managing your resources in several views (swimlanes). The view customization options are under the **View** dropdown.

The following options are available:

![resources-navigation.png](/cms_trial/assets/af75c5ad-ca1f-4e99-a658-ee01da99bde1.png)

- Expand/ Collapse all rows (swimlanes)
- Show:

  - [Workload](/cms_trial/space/SPM/1918864229/Workload+details/) (adds the workload row to every swimlane)
  - Remaining capacity (adds the remaining capacity row to every swimlane)
  - [Capacity](/cms_trial/space/SPM/1918765081/Capacity+calculation/) (adds the capacity row to every swimlane)
  - Values on heatmap (displays values on the [colored bars](/cms_trial/space/SPM/1918636529/Workload%2C+capacity%2C+and+utilization+-+tile+coloring/) in every enabled row)
  - Tasks (displays tasks in respective swimlanes)
  - Overall assignment (shows all the tasks assigned to a resource across all the boxes the resource is assigned to)
  - [Timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) (if configured, displays timeboxes)
- Warnings:

  - Estimates
  - Assignment
  - Workload contour

## [Warnings](/cms_trial/space/SPM/1918538128/Task+warnings+(Resources+module)/)

Warnings highlight the misconfigured and potentially problematic tasks that need extra attention. Once enabled, you will see a red frame around the problematic tasks.

![resources-warnings-checkboxes.png](/cms_trial/assets/652e2c45-6b22-40ba-9683-444df5a1fa92.png)

## Show overall assignment

The **Show overall assignment** option displays all the tasks your resources are assigned to, even if those tasks belong to the scope of other boxes. This gives you a real insight into the resource's actual workload and remaining capacity, allowing you to quickly see if you can assign them more tasks from your project.

### Identify tasks in the scope of other boxes

The tasks in the scope of other boxes are translucent. Those tasks update the resource's workload and impact their remaining capacity.

When you mouse over such a task, a warning tooltip will inform you that it does not belong to the current box and that you cannot edit it.

![translucent-tasks.png](/cms_trial/assets/fd5dfe89-09fa-4778-ba76-088adb10fa7d.png)

## Grid overview

The table below describes all the information presented on the resource grid. If you want to add or hide some information, use the **View** menu and uncheck the view options.

![resources-view-options.png](/cms_trial/assets/99789651-9051-4099-96cd-17d42ac0086a.png)

| **Feature** | **Description** |
| --- | --- |
| Timeboxes | Define consecutive timeframes used for work planning, such as sprints, iterations, increments, or stages. |
| Summary row | Shows the sum of all the data available in a selected time range. |
| Unassigned work | Show the sum of the unassigned work. |
| Allocation (workload) vs capacity | - Individuals, projects, and skills:    - Green - utilization under 100%   - Red - utilization is above 100% - Teams:    - Green - 0% to 80% utilization   - Yellow - 80 to 101% utilization   - Red - 101% or higher utilization   To learn more, see the [Coloring rules - workload vs capacity](/cms_trial/space/SPM/1918799470/Resource+coloring+rules/) page. |
| Overall assignment | This feature can show all the tasks to which the resource is assigned that do not fit the Program's scope. Those tasks will be transparent and can not be reassigned or moved. |
| [Capacity](/cms_trial/space/SPM/1918765081/Capacity+calculation/) | The availability of a resource derived from the Workload plans and reduced by the non-working days resulting from Holiday plans. |
| Remaining capacity | Remaining availability when the resource is assigned to a task in a given time period. |
| Non-working days | Non-availability period of the resource. |

## Working/ non-working days view

The grayed-out grid days indicate time off for a given resource.

![non-work-days.png](/cms_trial/assets/af0b11b0-3063-4611-9ce1-25cd9317b80b.png)

## [Timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/)

There is a graphical representation of timebox aggregation periods when no timeboxes are shown on a timeline.

There is also the possibility to right-click on a timebox and choose "go to earlier timeboxes”. It helps when timeboxes are enabled, but none are in the given period.

![resources-timeboxes.png](/cms_trial/assets/316bb4ae-eb28-4bc0-8399-f83886355b46.png)

## Time period and aggregation

To learn more, see the [Time period and aggregation](/cms_trial/space/SPM/1918702075/Time+period+and+aggregation/) page.

## Search and snipe to task

Use the **Snipe to result** option to highlight all tasks that fit the search criteria. It works similarly to the "Ctrl+F" feature in any web browser. The task is dynamically highlighted.

![Snipe to result - resources module.mov](/cms_trial/assets/45077fde-09a9-4354-a544-7e700d859b90.mov)

## Task dates visibility and resizing

As tasks are stretched and moved within the Resources timeline, their new dates are displayed on both sides of the taskbar. Additionally, tasks can be resized more intuitively, providing a clearer and more user-friendly interface for adjusting task durations.

![new-dates.png](/cms_trial/assets/7ef55800-9817-4fea-84c2-1de864e172ed.png)

## Tooltips

Tooltips have been incorporated into the interface, offering quick access to additional information about tasks and other elements within the Resources module. This enhances user experience by providing relevant details without cluttering the main view.

![resources-tool-tips.png](/cms_trial/assets/cd205124-574f-45ec-a773-2e9a29d0b9ce.png)

## Grid cells show units

The grid cells now display units, making it easier for users to understand the scale and timeframes of the tasks at a glance. This feature ensures that users can quickly grasp the duration and deadlines of tasks without needing to delve into detailed views.

![grid-units.png](/cms_trial/assets/19fcf4dd-328c-44b7-adac-b6ebaf990f26.png)

## Jump to the nearest task in a swimlane

A new functionality allows users to quickly jump to the nearest task. This feature is particularly useful for large projects with numerous tasks, as it saves time and improves navigation efficiency.

![snape-task.png](/cms_trial/assets/a75b39d6-52ff-41ee-9d5d-a60fc4b2d08e.png)

## Custom task colors on resources

Tasks can now be color-coded according to user preferences, making it easier to distinguish between different types of tasks or project phases at a glance. This customization enhances the visual organization and management of tasks within the chart. Task coloring is consistent across BigPicture - the same task colors can be seen in the Gantt module.

![custom-task-color.png](/cms_trial/assets/50e7fa01-2a00-400f-b6bf-0f7c77ef2f96.png)