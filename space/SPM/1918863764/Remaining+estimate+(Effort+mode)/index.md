# Remaining estimate (Effort mode)

## Remaining estimate (Effort mode) (old navigation)

## About the Remaining estimate mode

When you select this mode, the 'Remaining estimate' and 'Time spent' are evenly distributed over the task's duration, counting the working days only.

You can define the working and non-working days by editing the [Workload plans](/cms_trial/space/SPM/1918506352/Workload+plans/), [Holiday Plans](/cms_trial/space/SPM/1918505164/Holiday+plans/) and [Absence Plans](/cms_trial/space/SPM/1918764834/Absences/).

The Remaining Estimate and Spent Time are  'Time tracking' fields. To add it to your issue screen add the 'Time tracking' field which included the Original Estimate, Remaining Estimate and Spent Time.

The Remaining estimate reflects the time remaining to complete a task or an issue. The Time Spent is the sum of time-log entries, which you logged while working on a task.

When you enable the 'Remaining Estimate' mode, both the Remaining estimate and Spent Time are evenly distributed over the task's duration.

The Remaining Estimate, if available, will be evenly distributed starting from today and onward, the Spent Time will be evenly distributed starting from yesterday and going backward.

If the Remaining estimate is not available, the Original estimate will be displayed instead when available.

![contentId-1918863764](/cms_trial/assets/261178a5-c30d-475d-85bf-cba9e66c0a00.png)

## How is workload calculated?

The Total workload presented for a given time period is calculated using the following formula:

***Total workload = Sum of all estimates of the assigned tasks***

*\*Workload values are presented in hours*

For individuals, the formula takes into account tasks that have the Assignee set to this specific individual.

For Teams, the formula takes into account only tasks that have a label (or another mapped single-line field) set to this specific team. The tool does not check whether an Assignee of the task belongs to the Team created in Big Picture.

Calculated estimates might change depending on the selected aggregation. There are some additional rules.

**Work has been logged:**

Past duration (start date until yesterday) - the allocation is displayed as Logged Work evenly distributed over the past duration of the task.

Current date (today) to End date - The allocation for the remaining duration is displayed as Remaining Estimate evenly distributed over the remaining duration.

**Work has not been logged:**

Start date until yesterday - The allocation on the past days is displayed as '0'

Remaining duration (current date (today) to end date ) - the Remaining estimate is evenly distributed over the remaining duration:

![contentId-1918863764](/cms_trial/assets/ddac7929-670a-4cde-9691-261d3d63bc40.png)

There are also some additional rules related to special cases:

1. If the Task's Remaining Estimate value is not set (--) then the Original Estimate is used when available.

1. If the Task is scheduled entirely in the future (Start Date > = Today) then only the Remaining Estimate is shown (evenly distributed over Task's duration)

2.1) If there is no Logged Work a warning will appear. To enable go to View > Warnings

1. Task is entirely in the past (Today > End Date) only Logged Work is used in the report.

[Unmapped block: nestedExpand]

## Warnings

If the Task does not have a Remaining Estimate value you will see a warning, a red line that contours the Task.

Warnings can help you in resolving the most common problems. To enable go to 'View > Warnings.

![contentId-1918863764](/cms_trial/assets/72864b91-353c-4ab5-8cf1-2e73bdf81dc5.png)

## Remaining estimate (Effort mode) (new navigation)

## About the Remaining estimate mode

When you select this mode, the 'Remaining estimate' and 'Time spent' are evenly distributed over the task's duration, counting the working days only.

You can define the working and non-working days by editing the [Workload plans](/cms_trial/space/SPM/1918506352/Workload+plans/), [Holiday Plans](/cms_trial/space/SPM/1918505164/Holiday+plans/) and [Absence Plans](/cms_trial/space/SPM/1918764834/Absences/).

The Remaining Estimate and Spent Time are  'Time tracking' fields. To add it to your issue screen add the 'Time tracking' field which included the Original Estimate, Remaining Estimate and Spent Time.

The Remaining estimate reflects the time remaining to complete a task or an issue. The Time Spent is the sum of time-log entries, which you logged while working on a task.

When you enable the 'Remaining Estimate' mode, both the Remaining estimate and Spent Time are evenly distributed over the task's duration.

The Remaining Estimate, if available, will be evenly distributed starting from today and onward, the Spent Time will be evenly distributed starting from yesterday and going backward.

If the Remaining estimate is not available, the Original estimate will be displayed instead when available.

![remaining-calculation.png](/cms_trial/assets/a567bc1b-0ca8-43ce-baac-b669a5b366b4.png)

## How is workload calculated?

The Total workload presented for a given time period is calculated using the following formula:

***Total workload = Sum of all estimates of the assigned tasks***

*\*Workload values are presented in hours*

For individuals, the formula takes into account tasks that have the Assignee set to this specific individual.

For Teams, the formula takes into account only tasks that have a label (or another mapped single-line field) set to this specific team. The tool does not check whether an Assignee of the task belongs to the Team created in Big Picture.

Calculated estimates might change depending on the selected aggregation. There are some additional rules.

**Work has been logged:**

Past duration (start date until yesterday) - the allocation is displayed as Logged Work evenly distributed over the past duration of the task.

Current date (today) to End date - The allocation for the remaining duration is displayed as Remaining Estimate evenly distributed over the remaining duration.

**Work has not been logged:**

Start date until yesterday - The allocation on the past days is displayed as '0'

Remaining duration (current date (today) to end date ) - the Remaining estimate is evenly distributed over the remaining duration:

![remaining-calculation-2.png](/cms_trial/assets/7ba77b5e-a684-4484-b94f-d1e6239dc06a.png)

There are also some additional rules related to special cases:

1. If the Task's Remaining Estimate value is not set (--) then the Original Estimate is used when available.

1. If the Task is scheduled entirely in the future (Start Date > = Today) then only the Remaining Estimate is shown (evenly distributed over Task's duration)

2.1) If there is no Logged Work a warning will appear. To enable go to View > Warnings

1. Task is entirely in the past (Today > End Date) only Logged Work is used in the report.

[Unmapped block: nestedExpand]

## Warnings

If the Task does not have a Remaining Estimate value you will see a warning, a red line that contours the Task.

Warnings can help you in resolving the most common problems. To enable go to 'View > Warnings.

![example-warning.png](/cms_trial/assets/ac69a589-fb1d-45c1-98de-37c4f99e593c.png)