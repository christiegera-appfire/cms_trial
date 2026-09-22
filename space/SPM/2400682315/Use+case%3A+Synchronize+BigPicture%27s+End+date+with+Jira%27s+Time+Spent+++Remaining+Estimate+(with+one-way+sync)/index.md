# Use case: Synchronize BigPicture's End date with Jira's Time Spent + Remaining Estimate (with one-way sync)

|  |  |
| --- | --- |
| **Goal** | **Track tasks’ end dates in BigPicture by the time estimate field in Jira**  You want to synchronize the task’s End date in BigPicture with the task’s Time Spent and Remaining Estimate in Jira. |
| **Scenario** | In this scenario, a user learns how to map the End date field in BigPicture with the Time Spent + Remaining Estimate field in Jira.  As a result, the task’s end date is determined by the actual time spent on a task, coupled with the remaining days planned for that task.  Whenever the user logs their time in Jira, the respective values update in BigPicture’s Gantt column view, and the other way around.  The Jira/App Admin and the Box Admin can carry out this scenario as part of the custom field mapping. |
| **Key benefits** | - The sum of time spent and remaining estimate is a living metric. It reflects the adjustments made as the team gains a better understanding of the work. - It lets you give stakeholders an accurate and up-to-date completion date. If a task hits an unexpected roadblock and the remaining estimate is adjusted, the forecasted end date will automatically shift, providing a more realistic timeline. This prevents you from promising a delivery date that is no longer achievable. - This dynamic calculation helps you quickly identify when a task is at risk of being late. If the total time (Time Spent + Remaining Estimate) starts to exceed the Original Estimate, the end date will extend, signaling a potential delay. This lets you address issues early, either by reallocating resources or communicating a change in the schedule. - By using this metric to track progress, you have the data you need to make informed decisions. You can see which tasks are expanding in scope and where your team's time is being spent, which is crucial for making effective adjustments to your project plan. |

## Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture)
- BOX Admin You are a Box Admin of the box for which you want to customize the field mapping.
- The box scope consists of tasks from only one Jira project.

## Map the Start date field with the Original Estimate step-by-step

In this scenario, the Start date is field-mapped to the start date, while the end date is mapped to the Time spent + Remaining Estimate field.

1. Open a box for which you want to configure the field mapping.
2. Click the **plus icon** (**Add or edit columns**) in the column view (or the **wrench icon** (**App settings**)) **>** **Field mapping** button.
3. A **Field sync configuration modal** displays.
4. Open a dropdown for the End date Jira field, and select Time Spent + Remaining Estimate.
5. Open a dropdown for the **One-way sync end date field** and select Due date.
6. Click **Save**.

![End date field is custom field mapped to the Time Spent and Remaining Estimate field.](/cms_trial/assets/937475f6-2a0d-4ec6-84aa-fd5d5eae3d1e.png)

## Expected outcomes

- The task end date in BigPicture is based on the task estimate in Jira. Whenever a user logs time in Jira, the values in BigPicture’s Remaining Estimate and End Date columns change, too.
- Whenever the task estimate changes in BigPicture, the estimate value in the Jira work item changes, too.
- The one-way sync of the end date in BigPicture is synchronized with Jira’s Due date. Therefore, the change in the end date in BigPicture is also synchronized in Jira. However, the change in the end date on Jira’s side is not reflected in BigPicture.

## Additional resources

Map the start/end dates to different fields in Jira (video)

- [Progress field](/cms_trial/space/SPM/1918669957/Progress+field/)
- [Start/end date fields](/cms_trial/space/SPM/1918507050/Start%2Fend+date+fields/)
- [Synchronize task start and end dates with Jira](/cms_trial/space/SPM/2400780594/Synchronize+task+start+and+end+dates+with+Jira/)