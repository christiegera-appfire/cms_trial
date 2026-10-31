# Tips and tricks

![A decorative image featuring a big cauldron that overflows with a magic mixture.](/cms_trial/assets/c96bd58f-4625-49c5-a695-c55af1117fd3.png)

Maximize your BigPicture productivity, regardless of your experience level. These smart shortcuts, tips, and notable features will help you work efficiently in the Gantt, Scope, Reports, and Resources modules.

## Gantt module

A Gantt chart is excellent for visualizing Waterfall and Hybrid projects and Agile or SAFe® roadmaps. To make the most of it, you must ensure you have correctly configured your Gantt chart. Then, it might be helpful to learn a trick or two about how to move around the timeline efficiently.

### Add hierarchy to the task list

In BigPicture, [structure builders](/cms_trial/space/SPM/1918536846/Automatic+task+structure+(structure+builders)/) are responsible for the hierarchy of your project components, such as Jira work items. They determine parent and child elements.

You can use one of the pre-defined built-in template structures or choose a Jira link-based structure. You can also define a custom structure for your box.

You can find the task structure configuration page in the box settings.

![Task structure page in the box configuration.](/cms_trial/assets/c8ba5812-f583-4aca-8493-da6cd33a5d72.png)

To further customize your project structure, you can use [basic tasks](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Basic%20tasks&linkCreation=true&fromPageId=2484568389) as parents to group child tasks that belong to, for example, a Waterfall project phase. Basic tasks are an excellent grouping element and can aggregate data on their children.

### Track data with custom column views and aggregations

The Gantt and Scope modules feature a hierarchical task list (WBS) alongside columns that display various data on your project components. For example, start/end dates for phases and individual tasks.

Add as many columns as you need and aggregate data on them to help you track your project. Then, save your setup as a [column view](/cms_trial/space/SPM/1918404907/Column+views/). You can create many different column views, star them to keep them at the top of the list, and then switch between them on the fly.

![Column view dropdown.](/cms_trial/assets/ef92cce1-299c-47ac-af7a-b2f11eb448d9.png)

### Schedule tasks using different modes

[Scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/) determines how a task (or a group of tasks) will behave in relation to each other’s schedules. There are five scheduling modes: auto basic, auto bottom-up, auto top-down, manual, and locked. Each has a different scheduling property and can impact the schedule of another task.

For example, in the auto bottom-up mode, the children determine the duration of the parent task on the Gantt timeline. If you change the start date of the earliest child (a task that starts first) or the end date of the latest child (a task that finishes last), the parent’s end/start dates will adjust accordingly.

![A context menu listing all available task scheduling modes.](/cms_trial/assets/41104719-7604-404e-bae7-ad1ee65cef61.png)

Task period mode, especially when coupled with [strong dependencies](/cms_trial/space/SPM/1918701700/Strong+dependencies/), impacts how your tasks behave. Therefore, knowing what scheduling modes you apply to your respective tasks is important.

### Enable timeboxes on the Gantt chart

A timebox in BigPicture represents any consecutive work timeframe, such as a Sprint or iteration, a Program Increment, and a project stage. Even though the Gantt chart is typically associated with Waterfall projects, you can [enable timeboxes on a Gantt chart](/cms_trial/space/SPM/1918539612/Timeboxes+(Gantt+chart)/).

Such an option lets you happily marry Classic and Agile projects, allowing you to visualize and manage them on the Agile board and the Gantt chart.

![Timeboxes enabled on the Gantt chart.](/cms_trial/assets/eba03670-6d1d-4d31-bd88-f019034d207f.png)

### Enhance taskbar visibility with colors

On the Gantt chart, by default, [taskbar colors](/cms_trial/space/SPM/1918636160/Task+color/) come from their respective task statuses (gray for “To do,” blue for “In progress,” and green for “Done”). You can overwrite that status-based coloring code and customize it.

Right-click on the task or milestone (on the WBS side) or taskbar (on the Gantt timeline side) and pick the color from the color palette. Confirm when the app asks you whether you want to set colors on the timeline to manual.

![A set of colorful taskbars on the Gntt chart.](/cms_trial/assets/6a22d8c2-921b-40fe-bc60-1c454f7e994a.png)

If you’re a visual person, such custom color coding might help you recognize and track respective project elementsmore quickly. For example, you can assign a color to MoSCoW-based priority tasks or color a group of tasks according to some theme.

### Use shortcuts for faster Gantt timeline navigation

You can comfortably navigate from one point to another on the Gantt timeline using a mouse (or touchpad). Click and hold the mouse left-click button to drag the entire timeline and drop it on the date range you want.

![A video showing how a Gantt timeline can be dragged in all four directions.](/cms_trial/assets/d61d6f2c-297b-46e7-bae6-8aceaea4a1c3.mp4)

To move the timeline only sideways, hold Shift and use the mouse scroll wheel to scroll left or right along the timeline. (This shortcut works on the WBS side, too.)

You can also quickly adjust the timeline’s zoom level to increase/decrease the project view granularity level. Press and hold the Ctrl/Cmd button and use the mouse scroll wheel to zoom in/out.

If you want to focus the entire timeline on a specific task or tasks, press F on your keyboard to trigger the **Scale to fit** option. If no task is selected, this option will scale the entire project (box) to fit your view.

### Synchronize task dates between BigPicture and Jira

BigPicture can calculate a task’s start or end date based on the [task’s estimate](/cms_trial/space/SPM/1918539473/Task+dates+based+on+estimates/).

By field mapping the Start Date/End Date in BigPicture to the Original Estimate in Jira, the task’s start/end date and the length of the taskbar automatically update whenever you change its estimate (or duration).

Visit the [Synchronize task start and end dates with Jira](/cms_trial/space/SPM/2400780594/Synchronize+task+start+and+end+dates+with+Jira/) course and [Use cases](/cms_trial/space/SPM/2401107989/Use+cases/) pages to learn more about task date synchronization.

## Scope module

The scope module is an extensive list of all the project components, including tasks and epics. It’s your project WBS, like in the Gantt module, but without a timeline. The Scope module, therefore, gives you more space to work on the scope of your project. But there’s more to it.

### View Jira work item details directly in BigPicture

In other modules, to see issue details, you need to click the issue to open it on a separate Jira page.

In the Scope module, you no longer need to do that.

The [Detail View panel](/cms_trial/space/SPM/1918503360/Detail+view+panel/) lets you see all the Jira issue details right next to your task list. Select the task you want to inspect, and its details will appear in the Detail View.

The panel shows the same data as a Jira work item details page. If you have Skills and WBS [widgets](/cms_trial/space/SPM/1918832064/Widgets/) enabled, you’ll also see them in the Detail View.

![Detail view panel in BigPicture Cloud.](/cms_trial/assets/0ed10571-9433-4545-8c21-3c68d80a4a75.png)

## Reports module

Project reports help you communicate the status to your stakeholders, sponsors, and team. You can generate unlimited reports that you can customize and add to your report dashboard. In particular, the [Task report](/cms_trial/space/SPM/1918863921/Task+report/) that supports JQL lets you get the granular data you need.

### Gain more insights into tasks

The Task report provides comprehensive data related to your project tasks. You can build your report according to multiple different parameters, including counting or summing formulas, Jira and BigPicture fields, date filters, and date ranges.

You can also filter the report using JQL statements, allowing the results to be as detailed as you need. For example, you might want to focus your report on high-priority tasks assigned to a specific person or team.

![Task report configuration modal.](/cms_trial/assets/0a26bebd-0e68-46b3-9790-d72129b7cdc3.png)

## Resources module

The Resources module offers many interesting ways to help you effectively manage people’s workloads, absences, and task assignments.

### Lay the groundwork for resource management

The pillars of the Resource module are the [Workload plan](/cms_trial/space/SPM/1918506352/Workload+plans/) and [Holiday plan](/cms_trial/space/SPM/1918505164/Holiday+plans/) you define for your team members.

A Holiday plan covers holidays and days off observed in your country and organization. The Workload plan defines which days are considered business days in your organization and how long they typically take. You can also create separate workload plans for, for example, part-time contractors.

Keeping those two plans up to date will make your assignments more accurate. You'll know who is off and when, and you’ll also see how many more hours (or story points) someone can still take on in a given period.

![An overview of the default workload plan in the App Administration.](/cms_trial/assets/97b4a088-eec3-48ea-84db-b5d43cd40cd4.png)

### Add an absence on the fly

Jira and App Admins can [manage absences](/cms_trial/space/SPM/1918633840/Manage+absences/) on the Administration page. But there’s another, much faster way to add an absence to a person.

In the Resources module, right-click the tile with the person’s name and click **Add absence** on the context menu. The next screen lets you provide details for an absence, including the type of absence dates, and leave a comment (optional). You can also select a half-day.

![Add absence contex menu on the resource's tile.](/cms_trial/assets/99fd45b9-e246-4548-9e58-75464f1515d9.png)

Alternatively, click the workload or capacity bar in the resource’s swimlane on a specific day or week and select the **Add absence** modal. On the next screen, you'll notice that the absence dates are already defined.

For this method, you’ll need to adjust the time period and aggregation to make the timeline display the proper period. This will help you ensure you can click the bar on the exact date the resource will be away.

![Add absence contex menu on the resource's workload bar.](/cms_trial/assets/38842d12-a34e-4c79-bea6-c5c925d71b3d.png)

### Find a perfect assignee with just one click

You can find the perfect person to assign to a task based on their skills and capacity in a few seconds. How? The [**Find the perfect match**](/cms_trial/space/SPM/1918405181/Find+the+perfect+match/) feature matches up to three suitable people you can assign to a selected task. You can find this feature on the [Task details](/cms_trial/space/SPM/1918766626/Task+details+(Resources)/) dialog.

The app matches individual resources or teams (depending on the view) with tasks based on their workload, holiday plans, skills, and tasks you have defined and assigned earlier.

![Find the perfect match option on the task details.](/cms_trial/assets/4e023b7e-76b1-41ae-b9da-6a8aae960582.png)

### Quickly look up the detailed resource workload and capacity

The [color-coded capacity bars](/cms_trial/space/SPM/1918636529/Workload%2C+capacity%2C+and+utilization+-+tile+coloring/) indicate, by default, when someone has too much (red), just about enough (orange), or too little work (green) on their plate. The numbers on those bars indicate a person’s workload in a given period. But you might need more than those quick-glance details.

First, switch to the more granular timeline aggregation, for example, weekly or daily.Next, click the capacity or workload bar in the resource’s swimlane to open the [Workload details modal](/cms_trial/space/SPM/1918864229/Workload+details/). It will provide a detailed breakdown of the person’s or team’s workload for a selected period.

![Workload details modal.](/cms_trial/assets/1a476f20-7aa0-4f3a-99b1-3880412dc6df.png)

To display capacity details, click the capacity bar for a specific day, week, or other period, as defined by the selected aggregation set. The Capacity details modal displays information on whether a given day is a working or non-working day (if the daily aggregation is set), and the Workload plan details the resources assigned to.

Make sure you have **Capacity** enabled under the **View** options.

![Capacity details modal.](/cms_trial/assets/9b177faa-cdc8-4b25-95aa-4c99161907b5.png)

### Edit and assign tasks

Resource workload and capacity are not the only information pieces that you can open by clicking on the respective bars. You can get extra information on tasks, too.

Click the task you want to inspect to open the Task details modal. This modal displays the start/end dates, assignee, original estimate, scheduling mode, and other information about the task.

In addition, you can [edit most of those details inline](/cms_trial/space/SPM/1918637324/Inline+edit/).

For example, you can re-assign the task and change its dates, estimates, [workload contouring](/cms_trial/space/SPM/1918767273/Workload+contouring/), and status. Click the field you want to edit and change values as you see fit. To fit more details on the screen, expand the modal or manually stretch it.

![Task details modal.](/cms_trial/assets/817e0020-ba82-41e4-96d1-7ba3eadb40f0.png)

### Aggregate data by timeboxes

If you work in Agile and have already defined [timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) for your project (sub-boxes like PIs and iterations), you can display them on the resource grid. Change the timeline aggregation to **By timeboxes** to aggregate data by individual timeboxes instead of periods, such as months or weeks.

Make sure you have **Timeboxes** enabled under the **View** options.

![tTimeboxes enabled o nthe resources grid.](/cms_trial/assets/d4d6823f-93ba-455c-b803-dca28d20a072.png)