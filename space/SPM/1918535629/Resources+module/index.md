# Resources module

## Resources module (old navigation)

Click to expand the guide

## About the Resources module

**The Resources module** provides essential information for managing resources at the project and portfolio levels and can also provide insight into resource utilization during a sprint.

You can use this view to manage resources across the whole organization.

You can analyze resource consumption, currently utilized resources, and forecasted availability using different effort modes.

The [**Find the perfect match**](/cms_trial/space/SPM/1918405181/Find+the+perfect+match/) feature will help you allocate resources more effectively by suggesting available assignees at the individual and team levels.

## Available swimlanes

![image-20240909-074940.png](/cms_trial/assets/eec60fc2-aa92-4296-9840-818bf44f3eea.png)

Organize data into the following swimlanes:

| **Swimlane** | **Result** |
| --- | --- |
| **Individuals** | People assigned to tasks (assignees) |
| **Teams** | BigPicture teams (go to the [Teams module](/cms_trial/space/SPM/1918829775/Teams+module/) to review the teams) |
| **Projects** | Sub-boxes (for a project box, that would be lower-level boxes, such as Program Increments, Iterations, Stages, Sprints, etc.; for a portfolio box, those would be project boxes in a portfolio) |
| **Skills** | BigPicture skills assigned to tasks |

## Main features

| **Feature** | **Description** |
| --- | --- |
| Individuals, Teams, Projects, and Skills swimlanes | Switch between differentswimlanes to see the total workload, remaining capacity, and total capacity for the selected swimlane.  If you want tasks assigned to an individual to be automatically assigned to their team, enable the [Tasks assigned to an individual are auto-assigned to their team](/cms_trial/space/SPM/1918408224/Automatic+assignment/) option in the **App Configuration** > **Modules** >[**Resources**](/cms_trial/space/SPM/1918636014/Resources+(App+configuration)/) tab.  This option is switched on by default for all new instances. |
| [Group swimlanes](/cms_trial/space/SPM/1918701793/Swimlanes+and+grouping/) | You can group the swimlanes on two levels. For example, a grouping by the Skills and then Individuals will display all the skills assigned to the box along with the users who have them. |
| [Add tasks](/cms_trial/space/SPM/1918800322/Create+tasks/) | Use the **Add task +** button to create new tasks. |
| [Resource filters](/cms_trial/space/SPM/1918503449/Filters+and+search/) | Filter resources using the resource filters. Depending on the current view (individual or team view). |
| [Effort mode](/cms_trial/space/SPM/1918764313/Effort+modes/) | The workload allocation can be expressed using the following source data of Time tracking fields:   - [Original estimate](/cms_trial/space/SPM/1918407058/Original+estimate+(Effort+mode)/) - [Remaining estimate](/cms_trial/space/SPM/1918863764/Remaining+estimate+(Effort+mode)/) - [Story points](/cms_trial/space/SPM/1918506126/Story+points+(Effort+mode)/)   The module distributes the workload evenly over the duration period.  You can choose the unit you want the capacity to be displayed in:   - Hours (for Original and Remaining Estimate only) - Man-days (for Original and Remaining Estimate only) - Percent (for Original, Remaining Estimate, and Story points) - Story points (for Story points only) |
| View options | Show the tasks for each resource or team   - Expand all rows - Collapse all rows   Show additional information for each reporting period:   - Allocation - Remaining capacity - Capacity - Values on heatmap - Tasks (when tasks are visible, you can click a task and see a dialog with the task details) - [Timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) (and representations of timebox aggregation periods when timeboxes haven't been created for a given period) - Show overall assignment - Warnings - [Task color](/cms_trial/space/SPM/1918636160/Task+color/) |
| Task details dialog | View and inline edit the details of assigned tasks.  Search for the perfect match using the [**Find the perfect match**](/cms_trial/space/SPM/1918405181/Find+the+perfect+match/) button(assignee and team).  Enhance the process and assign tasks to a respective team by inline editing. Screenshot of a task details pop-up in the Resources module of BigPicture. |
| [Export](https://appfire.atlassian.net/wiki/spaces/BTc) | To unlock the export features, install the [BigTemplate App](https://appfire.atlassian.net/wiki/spaces/BTc) from the Atlassian Marketplace.   - XML - PDF image  Screenshot of the Export icon in the Resources module of BigPicture.Screenshot of the Export data window in the Resources module of BigPicture. |
| Scale options | Select how to display available data using the time period and aggregation options. When looking at the date using the quarter and half-year view, only colors are displayed unless the weekly or monthly aggregation is selected.  Time period:   - Week - Month - Quarter - Half-year - Year   Aggregation   - Daily - Weekly - Monthly - Quarterly - Yearly - By timeboxes |
| Navigation | Navigate through the calendar using the buttons. |
| [Quick filters](/cms_trial/space/SPM/1918635901/Quick+filters/) | Add your favorite filters to the header and filter tasks from the resource grid. When the filter is applied, the workload will be calculated solely based on the tasks that match the filter. |
| [Resource filters](/cms_trial/space/SPM/1918503449/Filters+and+search/) | Filter resources using the in-built resource-specific filters to zoom in on a particular Team or its team members. |
| Summary row | Total capacity, allocation, and remaining capacity of all resources in the current view. |
| [Backlog panel](/cms_trial/space/SPM/1918405862/Backlog+panel/) | Manage all unscheduled tasks easily from the sidebar. Screenshot of the Unscheduled tasks panel available in the Resources module of BigPicture. |
| [Add absence](/cms_trial/space/SPM/1918764834/Absences/) | To add an absence directly from the Resources module, right-click on the resource name and choose **Add absence**. Screenshot of adding an absence to a resource in the Resources module of BigPicture. |
| Redirect to the Administration > Resources > [Individual's details page](/cms_trial/space/SPM/1918637190/Individual%27s+details+page/) | When you click the resource name, you will be redirected to the **Individuals** page of that resource. Screenshot of a resource name that is a link to the Individuals page. |

## “You can’t edit this task…” (tooltip)

When a task can't be edited, the reason is provided in the tooltip:

![Screenshot of a message that a user can't edit a task in the Resources module of BigPicture.](/cms_trial/assets/33d2bb54-dc18-4b89-a0d2-e3db755d77d6.png)

- Missing permissions:

  - In integration (connected tool), Jira (a user doesn't have sufficient Jira permissions to edit tasks).
  - In a box (a user is a viewer only - can't edit tasks).
- The box is closed or archived:

  - The box you're in is closed/archived.
  - You are in a portfolio box, but one of its children is closed/archived (the resources module of the portfolio aggregates tasks from all child boxes).
- Show overall assignment - a task from a different box (overall assignment shows all tasks assigned to a resource. Tasks in the scope of the box you are in can be edited normally. Tasks assigned to the resource in other boxes can't be edited.

## Resources (new navigation)

Click to expand the guide

## About the Resources module

**The Resources module** provides essential information for managing resources at the project and portfolio levels and can also provide insight into resource utilization during a sprint.

You can use this view to manage resources across the whole organization.

You can analyze resource consumption, currently utilized resources, and forecasted availability using different effort modes.

The [**Find the perfect match**](/cms_trial/space/SPM/1918405181/Find+the+perfect+match/) feature will help you allocate resources more effectively by suggesting available assignees at the individual and team levels.

See the video to learn more.

## Available swimlanes

![resources-swim-lane.png](/cms_trial/assets/47e00cb1-5c8c-4c5e-b948-8d595837f309.png)

Organize data into the following swimlanes:

| **Swimlane** | **Result** |
| --- | --- |
| **Individuals** | People assigned to tasks (assignees) |
| **Teams** | BigPicture teams (go to the [Teams module](/cms_trial/space/SPM/1918829775/Teams+module/) to review the teams) |
| **Projects** | Sub-boxes (for a project box, that would be lower-level boxes, such as Program Increments, Iterations, Stages, Sprints, etc.; for a portfolio box, those would be project boxes in a portfolio) |
| **Skills** | BigPicture skills assigned to tasks |

## Main features

| **Feature** | **Description** |
| --- | --- |
| Individuals, Teams, Projects, and Skills swimlanes | Switch between differentswimlanes to see the total workload, remaining capacity, and total capacity for the selected swimlane.  If you want tasks assigned to an individual to be automatically assigned to their team, enable the [Tasks assigned to an individual are auto-assigned to their team](/cms_trial/space/SPM/1918408224/Automatic+assignment/) option in the **App Configuration** > **Modules** >[**Resources**](/cms_trial/space/SPM/1918636014/Resources+(App+configuration)/) tab.  This option is switched on by default for all new instances. |
| [Group swimlanes](/cms_trial/space/SPM/1918701793/Swimlanes+and+grouping/) | You can group the swimlanes on two levels. For example, a grouping by the Skills and then Individuals will display all the skills assigned to the box along with the users who have them. |
| [Add tasks](/cms_trial/space/SPM/1918800322/Create+tasks/) | Use the **Add task +** button to create new tasks. |
| [Resource filters](/cms_trial/space/SPM/1918503449/Filters+and+search/) | Filter resources using the resource filters. Depending on the current view (individual or team view). |
| [Effort mode](/cms_trial/space/SPM/1918764313/Effort+modes/) | The workload allocation can be expressed using the following source data of Time tracking fields:   - [Original estimate](/cms_trial/space/SPM/1918407058/Original+estimate+(Effort+mode)/) - [Remaining estimate](/cms_trial/space/SPM/1918863764/Remaining+estimate+(Effort+mode)/) - [Story points](/cms_trial/space/SPM/1918506126/Story+points+(Effort+mode)/)   The module distributes the workload evenly over the duration period.  You can choose the unit you want the capacity to be displayed in:   - Hours (for Original and Remaining Estimate only) - Man-days (for Original and Remaining Estimate only) - Percent (for Original, Remaining Estimate, and Story points) - Story points (for Story points only) |
| View options | Show the tasks for each resource or team   - Expand all rows - Collapse all rows   Show additional information for each reporting period:   - Allocation - Remaining capacity - Capacity - Values on heatmap - Tasks (when tasks are visible, you can click a task and see a dialog with the task details) - [Timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) (and representations of timebox aggregation periods when timeboxes haven't been created for a given period) - Show overall assignment - Warnings - [Task color](/cms_trial/space/SPM/1918636160/Task+color/) |
| Task details dialog | View and inline edit the details of assigned tasks.  Search for the perfect match using the [**Find the perfect match**](/cms_trial/space/SPM/1918405181/Find+the+perfect+match/) button(assignee and team).  Enhance the process and assign tasks to a respective team by inline editing. resources-task-details.png |
| [Export](https://appfire.atlassian.net/wiki/spaces/BTc) | To unlock the export features, install the [BigTemplate App](https://appfire.atlassian.net/wiki/spaces/BTc) from the Atlassian Marketplace.   - XML - PDF image  export-option.pngresources-export-data.png |
| Scale options | Select how to display available data using the time period and aggregation options. When looking at the date using the quarter and half-year view, only colors are displayed unless the weekly or monthly aggregation is selected.  Time period:   - Week - Month - Quarter - Half-year - Year   Aggregation   - Daily - Weekly - Monthly - Quarterly - Yearly - By timeboxes |
| Navigation | Navigate through the calendar using the buttons. |
| [Quick filters](/cms_trial/space/SPM/1918635901/Quick+filters/) | Add your favorite filters to the header and filter tasks from the resource grid. When the filter is applied, the workload will be calculated solely based on the tasks that match the filter. |
| [Resource filters](/cms_trial/space/SPM/1918503449/Filters+and+search/) | Filter resources using the in-built resource-specific filters to zoom in on a particular Team or its team members. |
| Summary row | Total capacity, allocation, and remaining capacity of all resources in the current view. |
| [Backlog panel](/cms_trial/space/SPM/1918405862/Backlog+panel/) | Manage all unscheduled tasks easily from the sidebar. Screenshot of the Unscheduled tasks panel available in the Resources module of BigPicture. |
| [Add absence](/cms_trial/space/SPM/1918764834/Absences/) | To add an absence directly from the Resources module, right-click on the resource name and choose **Add absence**. resources-add-absance.png |
| Redirect to the Administration > Resources > [Individual's details page](/cms_trial/space/SPM/1918637190/Individual%27s+details+page/) | When you click the resource name, you will be redirected to the **Individuals** page of that resource. Screenshot of a resource name that is a link to the Individuals page. |

## “You can’t edit this task…” (tooltip)

When a task can't be edited, the reason is provided in the tooltip:

![resources-warning.png](/cms_trial/assets/7b4f7da6-b189-447d-8249-e9bb14f54b24.png)

- Missing permissions:

  - In integration (connected tool), Jira (a user doesn't have sufficient Jira permissions to edit tasks).
  - In a box (a user is a viewer only - can't edit tasks).
- The box is closed or archived:

  - The box you're in is closed/archived.
  - You are in a portfolio box, but one of its children is closed/archived (the resources module of the portfolio aggregates tasks from all child boxes).
- Show overall assignment - a task from a different box (overall assignment shows all tasks assigned to a resource. Tasks in the scope of the box you are in can be edited normally. Tasks assigned to the resource in other boxes can't be edited.