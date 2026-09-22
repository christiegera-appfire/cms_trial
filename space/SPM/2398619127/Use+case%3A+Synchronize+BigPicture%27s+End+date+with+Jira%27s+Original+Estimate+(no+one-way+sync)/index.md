# Use case: Synchronize BigPicture's End date with Jira's Original Estimate (no one-way sync)

|  |  |
| --- | --- |
| **Goal** | **Track tasks’ end dates in BigPicture by the time estimate field in Jira**  You want to synchronize the task end date in BigPicture with the task’s Original Estimate in Jira. |
| **Scenario** | In this scenario, a user learns how to map the End date field in BigPicture with the Original Estimate field in Jira.  As a result, the task’s end date is determined by its duration.  Whenever the task’s end date changes in Jira, the respective values update in BigPicture’s Gantt column view, and the other way around.  The Jira/App Admin and the Box Admin can carry out this scenario as part of the custom field mapping. |
| **Key benefits** | - Tracking tasks by the Original Estimate is helpful because it provides a baseline for comparison and helps with future planning. It lets you measure the accuracy of your initial predictions against the actual time spent on a task. - The original estimate represents your team's initial commitment to the work. By using it to calculate a planned end date, you create a clear, visual schedule of when the task is expected to be completed. This is essential for communicating realistic timelines to stakeholders. - If the forecasted end date starts to move past the original planned end date, it's a clear signal that the project is slipping. This early warning allows project managers to intervene, reallocate resources, or adjust the project scope before the delay becomes critical. |

| **Contents:**   - [Preconditions](#preconditions) - [Map the End date field with the Original Estimate step-by-step](#map-the-end-date-field-with-the-original-estimate-step-by-step) - [Expected outcomes](#expected-outcomes) - [Additional resources](#additional-resources) |
| --- |

## Preconditions

- app user You were granted the [App User role](/cms_trial/space/SPM/1918535770/App-level+permissions/) (to open BigPicture)
- BOX Admin You are a Box Admin of the box for which you want to customize the field mapping.
- The box scope consists of tasks from only one Jira project.

## Map the End date field with the Original Estimate step-by-step

In this scenario, the end date is field-mapped to the time estimate, while the start date remains mapped to the Start date field.

1. Open a box for which you want to configure the field mapping.
2. Click the **plus icon** (**Add or edit columns**) in the column view (or the **wrench icon** (**App settings**)) **>** **Field mapping** button.
3. A **Field sync configuration modal** displays.
4. Open a dropdown for the Start date Jira field, and select Start date.
5. Open a dropdown for the End date Jira field, and select Original Estimate
6. Leave the **One-way sync start date field** as Not synchronized.
7. Click **Save**.

![End date is mapped to the original estimate on the custom field mapping modal.](/cms_trial/assets/d8c7a147-89fb-44dc-8db0-e31db260fd11.png)

## Expected outcomes

- The task end date in BigPicture is based on the task estimate in Jira. Whenever the task estimate changes in Jira, the values in BigPicture’s Original Estimate and End Date columns change too.
- In addition, for better visibility, you can observe the impact of the change in the Original Estimate in BigPicture’s duration columns (Duration Calendar Days and Duration Working Days), as well as in the taskbar’s length.
- Whenever the task estimate changes in BigPicture, the estimate value in the Jira work item changes, too.
- The one-way sync of the end date in BigPicture is not synchronized. Therefore, the change in the end date in BigPicture is not synchronized with the due date in Jira.

In the video below, you can see how the Original Estimate changes bi-directionally in BigPicture and Jira. Note the change in the taskbar length and the end date in BigPicture; the task due date remains the same on the work item details screen in Jira.

![A demonstration of how the change of the original estimate value is reflected in Jira and BigPicture.](/cms_trial/assets/c1398c92-bcf1-4d3e-a995-e8771a873ac7.mp4)

## Additional resources

Map the start/end dates to different fields in Jira (video)

- [Progress field](/cms_trial/space/SPM/1918669957/Progress+field/)
- [Start/end date fields](/cms_trial/space/SPM/1918507050/Start%2Fend+date+fields/)
- [Synchronize task start and end dates with Jira](/cms_trial/space/SPM/2400780594/Synchronize+task+start+and+end+dates+with+Jira/)