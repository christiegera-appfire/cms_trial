# Automations

## About automations in BigPicture

BigPicture provides several automation mechanisms that help you save time and keep hundreds of tasks under control and within deadlines.

## Structure builders and field sync

BigPicture automatically updates fields in Jira (or another platform) once you edit a task or [create a dependency](/cms_trial/space/SPM/1918800164/Create+dependencies/). Changes to tasks can be made also by automation based on modifications to the task position in the task structure.

If you move a task to an appropriate place in the task structure, BigPicture can automatically perform the following actions:

- Assign a task to the correct sprint, version, or epic.
- Unlink a task from the correct sprint, version, or epic.
- Create links between tasks in Jira.
- Delete links between tasks in Jira.

Find out more the [Manage task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) page.

![contentId-1918535176](/cms_trial/assets/e6b63374-74db-41a5-ae82-4998d89573be.png)

### Scheduling rules - priorities

According to multiple rules, the auto-scheduling function aims to calculate the task's period (start and end dates). Those rules are applied simultaneously, but each has its priority. Depending on the implemented rules, you can end up with different setups of scheduling functions for each task.

The table below lists the rules according to the following priority:

| **Priority** | **Applicable rule** |
| --- | --- |
|  | Scheduling mode applied to a task |
|  | Parent-child relation |
|  | Calendar (non-working days) |
|  | Dependencies |

| **Examples** |
| --- |
| - When a task is in [manual scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/), start/end dates **are unaffected** by dependencies and the calendar. |
| - When a task is in auto top-down scheduling mode, start/end dates **are unaffected** by dependencies if dependencies were to move children of such a task outside the date range of the parent task. |

## Dependencies

Dependencies are relationships between tasks, milestones, and other items. The mechanism can simultaneously move one or more tasks linked to a moving task. By defining dependencies, task dates and other initiatives are updated automatically due to changes made to a project.

You can also define dependencies between initiatives such as versions or projects.

If you **do NOT** want dependencies to affect tasks, you can turn off automation by setting an appropriate scheduling mode.

![contentId-1918535176](/cms_trial/assets/64ec65f6-464d-4107-984e-76f8027d62f6.png)

Find out more on the [Dependencies](/cms_trial/space/SPM/1918536086/Dependencies/) page.

## Scheduling mode

The scheduling mode is a task parameter in BigPicture that determines what automation mechanisms impact task dates. There are four scheduling modes explained further below:

- Auto basic

- Auto bottom-up
- Auto top-down
- Manual
- Locked

| **Scheduling mode** | **Description** |
| --- | --- |
| Auto basic auto-basic.png | Auto basic mode is the default scheduling mode in **BigPicture**.  Tasks in Auto basic mode react to automation based on non-working days, dependencies, and parents in Auto top-down and Locked mode.  Tasks set to Auto basic mode do **NOT** affect children’s dates (as tasks in Auto bottom-up mode) and do **NOT** shift children’s tasks when tasks are moved. gantt-auto-basic.png |
| Auto bottom-up contentId-1918535176 | Parent task dates are adjusted to match the period of their children’s tasks.  **Use case:** You want the end date of the epic to be defined by the latest task that belongs to the epic. contentId-1918535176 |
| Auto top-down contentId-1918535176 | A parent task repositions its children tasks to fit within a parent task period.  **Use case:** You want tasks to be moved back in time so that they do not exceed the end date of a version or project. contentId-1918535176 |
| Manual contentId-1918535176 | Automation mechanisms such as dependencies, calendars, and parent-child relations **do NOT** work on such tasks.  **Use case:** You want a task to be completed on the weekend or **unaffected** by any automation mechanism (task dates have to be manually changed). contentId-1918535176 |
| Locked contentId-1918535176 | The mode blocks the possibility of changing the duration and position of tasks by automation and other users.  Children tasks dates **do NOT** exceed the end date of a parent task (as in the auto top-down mode).  **Use case:** You want a task to be necessarily scheduled on specified dates.  To change the start/end dates of a locked task, you have to change the scheduling mode first. contentId-1918535176 |

Find out more on the [Scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/) page.

## Calendar (non-working days)

You can mark days in the calendar as non-working days by setting schedules or assigning a day off to an employee. BigPicture recognizes non-working days and adjusts a task period accordingly. If you plan a task or part of your task's period on a non-working day, it will be moved or extended, or shortened.

Find out more on the [Non-working days](/cms_trial/space/SPM/1918504137/Non-working+days/) page.

If you **do NOT** want non-working days to affect the duration of tasks, you can turn off automation by setting an appropriate scheduling mode.

## Calculate task dates based on estimates or logged time

Another solution that helps you manage and monitor tasks more efficiently is the possibility to automatically calculate task dates based on estimates or the time logged on tasks.

Activating the mechanism modifies the way of editing the “Start Date” field. Entering a new “Start Date” moves a task. The duration of a task **is NOT** changed, and its “Original Estimate” remains unchanged.

Automatic calculation of task dates based on estimates proves helpful when:

- The “Original Estimate” field contains estimates for a task. If you enter the “Start Date”, the “End Date” is calculated automatically based on an estimate.
- You monitor the project estimate based on the sum of the “Original Estimate” for all tasks in that project. If you update task dates, task estimates, along with the final project estimate, are updated automatically.
- You want task dates adjusted to the time logged on a task. As a result, you can track in real-time how tasks match the dates to the actual progress of work logged by other employees.

Find out more on the [Task dates based on estimates](/cms_trial/space/SPM/1918539473/Task+dates+based+on+estimates/) page.

## Align task dates with iteration dates

BigPicture offers the possibility to align task dates with iteration dates automatically. With such a solution, you can see a visualization of tasks in the Gantt module, or it is possible to automatically set expected end dates for tasks (e.g., bug type) that are assigned to a given sprint.

![contentId-1918535176](/cms_trial/assets/241ff743-dce6-4e4c-ba59-c5ab29da9f1b.png)

Find out more on the [Define task period alignment](/cms_trial/space/SPM/1918830096/Define+task+period+alignment/) page.

## Changing absences for assignee

Task is re-scheduled when absence is added or removed from the assignee. For more details, check the [Calculate tasks automatically based on assignee's working days](/cms_trial/space/SPM/1918638098/Calculate+tasks+automatically+based+on+assignee%27s+working+days/) option.

## Constraints

### Task in multiple boxes

If you make changes to a task in multiple boxes, the changes are automatically implemented in other boxes. When each box is configured differently, the resulting task's period is 'evenly shaped' by the rules of each box. **The task's position and duration on the timeline remain the same in all boxes.**

### Automation vs. tasks with the Done status

Tasks with the **Done** status are excluded from any scheduling automation rules. Such tasks aren’t affected by dependencies, scheduling mode of other tasks (parent and children).

Only manual changes to the dates and/or duration affect those tasks.