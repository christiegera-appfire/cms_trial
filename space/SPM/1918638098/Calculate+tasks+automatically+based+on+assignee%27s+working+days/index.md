# Calculate tasks automatically based on assignee's working days

Calculating the task period based on the assignee's working days does not apply to parent tasks in the WBS structure. The reason for this limitation is that parent tasks can be automatically recalculated based on their children's tasks, which may be in contradiction with the working days of a resource assigned to the task.

You can enable the 'Calculate tasks automatically based on assignee's working days' option in the App's Configuration (you need to be a Jira administrator to access this page) to show non-working days when you click a task and allow the scheduling mechanism to reschedule your task taking into account the non-working days.

The scheduling mechanism performs the following:

- Checks the assignee's working days (individual resource)that allow the assignee to complete the task based on:

  - resource's Holiday, Workload, and Absence plans,
  - task start date,
  - task duration.
- Calculates the start date of the task, and in case a task's start date is a non-working day, the task will be updated to start on the earliest possible working day that comes after the task's start date.
- Calculates the end date of the task and checks the assignee's working days consecutively that fit the task duration until the task can be fully completed.

When this toggle is switched on, rescheduling is also triggered when absences are added or removed for a person assigned to the task. This rule applies to tasks that:

- are in Not Started or In Progress status
- are not in Manual or Locked scheduling mode
- are not parent tasks for Auto bottom-up scheduling mode.

If it is not possible to determine a correct task period because the assignee has no working days in the future, the task will not be rescheduled. In that case, the task will be marked with a red frame if warnings are enabled.

When you change the task's assignee, it might cause automatic rescheduling of the task. This will occur if the new assignee's schedule differs from the previous one. The only exception to this rule is when a task is in the **Locked** mode, as its position will not be recalculated.

![image-20250325-094534.png](/cms_trial/assets/fc0449b5-07fb-4b26-96c8-b781d6bd43ba.png)