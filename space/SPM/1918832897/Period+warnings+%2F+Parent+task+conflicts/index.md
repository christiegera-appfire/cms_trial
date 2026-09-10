# Period warnings / Parent task conflicts

Period warnings have been renamed to **Parent task conflicts** as part of the new navigation rollout.

Both names refer to the same functionality. You may see either term depending on whether you’re using the previous navigation or the new navigation that is currently being rolled out in BigPicture.

## Period warnings (old navigation)

Click to expand the guide

Period warnings occur when a parent task cannot be recalculated due to a constraint, such as a blocking task (for example, a task in Locked mode), a non-working day, or when you use the manual period mode.

See the video about period warnings.

## Showing Period Warnings

The warning is displayed as a yellow box with a dashed-line frame and shows the position of the parent tasks calculated based on its children.

![Gantt view with period warning displayed](/cms_trial/assets/e775916f-7e8f-401d-8a1e-f0016c281287.png)

Period warnings **do NOT** consider tasks without start and end dates (tasks without dates are ignored by period warnings).

Period warning considers tasks with one date, only considering the existing date.

For more details, see the table below.

| **Case** | **Outcome** |
| --- | --- |
| The child task has no dates, and the parent has no dates | No period warning |
| The child task has no dates, but its parent has dates | No period warning |
| The child task only has a start date, and this is within the parent dates | No period warning |
| The child task only has a start date, and this is before the parent starts | The period warning is displayed |
| The child task only has a start date, and this is after the parent ends | The period warning is displayed |
| The child task only has an end date, and this is within the parent dates | No period warning |
| The child task only has an end date, and this is before the parent starts | The period warning is displayed |
| The child task only has an end date, and this is after the parent ends | The period warning is displayed |
| The parent has only one date | No period warning |

The warning can only be displayed using the Gantt module. To show the warnings, click on View > Period warnings.

![View options, Layout, Period warnings checked](/cms_trial/assets/f3b21eba-5b49-4209-bf89-423d924e4d12.png)

## Rescheduling Tasks Manually

Parent tasks in manual mode can be manually rescheduled so the task period is calculated based on children tasks. To reschedule the task manually, click on the task to show the tasks' details and click Reschedule:

![Period warning details displayed](/cms_trial/assets/07ffae99-a44b-48d8-9b17-b98bfa73849e.png)

## Bulk Rescheduling

Switch to one of the Auto period modes to fix all the warnings.

## Parent task conflicts (new navigation)

Click to expand the guide

Parent task conflicts occur when a parent task cannot be recalculated due to a constraint, such as a blocking task (for example, a task in locked mode), a non-working day, or when you use the manual period mode.

See the video about parent task conflicts.

## Show parent task conflicts

The warning is displayed as a yellow box with a dashed-line frame and shows the position of the parent tasks calculated based on their children.

![Screenshot of parent task conflicts in the Gantt module.](/cms_trial/assets/404078c9-b527-41a1-a482-fc6b50f36a2f.png)

Parent task conflicts **do NOT** consider tasks without start and end dates (tasks without dates are ignored by parent task conflicts).

Parent task conflicts consider tasks with a single date, using only the existing date.

For more details, see the table below.

| **Case** | **Outcome** |
| --- | --- |
| The child task has no dates, and the parent has no dates. | No parent task conflict |
| The child task has no dates, but its parent has dates. | No parent task conflict |
| The child task only has a start date, and this is within the parent dates. | No parent task conflict |
| The child task only has a start date, and this is before the parent starts. | The parent task conflict is displayed |
| The child task only has a start date, and this is after the parent ends. | The parent task conflict is displayed |
| The child task only has an end date, and this is within the parent dates. | No parent task conflict |
| The child task only has an end date, and this is before the parent starts. | The parent task conflict is displayed |
| The child task only has an end date, and this is after the parent ends. | The parent task conflict is displayed |
| The parent has only one date. | No parent task conflict |

The warning can only be displayed using the Gantt module. To show the warnings:

1. Click **Indicators** > **Parent task conflicts**.

   ![Screenshot of enabling the parent task conflicts option in the Gantt module.](/cms_trial/assets/fd1f1f9e-39ff-45d4-86a7-910d8860f83f.png)

## Reschedule tasks manually

Parent tasks in manual mode can be manually rescheduled so the task period is calculated based on child tasks.

To reschedule the task manually, click on the task to show the task’s details and click **Reschedule**.

![Screenshot of the Parent task conflict message in the Gantt module.](/cms_trial/assets/ecbf311d-478c-4fe3-8e5c-c4b50f227c99.png)

## Bulk rescheduling

Switch to one of the [auto-scheduling modes](/cms_trial/space/SPM/1918831395/Scheduling+mode/) to fix all the warnings.