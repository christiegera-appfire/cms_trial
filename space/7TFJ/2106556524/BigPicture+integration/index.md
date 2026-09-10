# BigPicture integration

![TryItButton (2).png](/cms_trial/assets/0c5a8de7-c3d4-4021-ba97-e296fb7d316f.png)

## Introduction

With the 7pace Timetracker and BigPicture integration, you can leverage time tracking information and:

- View tracked time in BigPicture using custom 7pace Timetracker fields.
- Gain insight into team member capacity.

## Watch a video

The following video takes you through the process of:

- Activating the 7pace Timetracker and BigPicture integration.
- Adding custom fields, Billable, and the R&D Activity type, to BigPicture’s Gantt chart.
- Tracking time in 7pace.
- Gaining insights into team member capacity.

## Turn on the integration

Use the following steps to activate the 7pace integration in BigPicture:

1. Click **Settings** > **Integrations**.
2. Select the **7pace Timetracker** tab and use the slider to **Enable 7pace Timetracker integration**.

   ![Turn on the 7pace Timetracker integration.](/cms_trial/assets/39ba262c-0bde-4b67-8471-7755c64c2887.png)
3. Save the change.

## Track billable R&D time in BigPicture

In this example, we’ll display two custom time tracking fields in BigPicture, **Activity Type** and **Billable**, which allow us to learn more about how team members track time.

To begin, open a BigPicture project in the Gantt chart. Here, epics and work items display along with original time estimates and actual time spent. At the highest level, we see that we planned to spend about 19 1/2 weeks on the sample project, and so far, the team has worked about 12 1/2 weeks.

![Compare budgeted time to actual time in BigPicture.](/cms_trial/assets/1c0d6955-849f-45c9-bde2-1e0988022b9f.png)

Now, let’s drill down to each epic and view time tracking data at a more granular level.

![Drill down to see how time is spent on each epic](/cms_trial/assets/7c22b1d8-dab7-44f9-b249-bb795a5a30e4.png)

Next, let’s add custom time tracking information from 7pace to the BigPicture Gantt chart. First, we’ll add the custom field for **Activity type: R&D**.

![Add 7pace Timetracker fields to BigPicture](/cms_trial/assets/157794b1-aad9-4194-b3d1-88e9ba700e90.png)

Then, **Billable** hours.

![Include billable hours in the Gantt chart.](/cms_trial/assets/c97a56c4-da6d-45c3-8008-954937da7890.png)

Now, we see additional information from 7pace Timetracker on the Gantt chart, illustrating how the team tracked billable research and development time in the project.

![Display columns in the Gantt chart from 7pace Timetracker.](/cms_trial/assets/9fe0204e-024f-4d51-b52e-1ae5f29d2ff3.png)

If necessary, we can aggregate the R&D time on the Gantt chart and gain insight into how these activities influence the overall project.

![image-20250610-220445.png](/cms_trial/assets/2bd8a36b-9d78-466c-bcf0-2a8c5ad31151.png)

## Track time in 7pace

7pace Timetracker strives to provide users with a seamless, integrated tool for [tracking time](/cms_trial/space/7TFJ/1202159710/Add+worklogs/). There’s no context-switching with 7pace Timetracker; everything you need to track time exists in Jira. The steps below illustrate how a software engineer adds time to a Jira work item.

1. In the right-hand pane, click the option in 7pace Timetracker for **+ Add Time**.

   ![Click the Add Time button.](/cms_trial/assets/d7db4f56-9379-412a-aadb-6d19dbe3c3e7.png)
2. Select the date, enter the duration, a comment (if necessary), and complete any custom fields, **Billable** and **Activity type** in this example.

   ![Complete the fields in the Add Time window.](/cms_trial/assets/9fa3ac19-0bc4-4eeb-a55e-a773dad7e05d.png)
3. **Save** the worklog.

After saving the worklog, view Timetracker insights, which display the original estimate and the actual time logged. You can also view the time tracked on the work item by user.

![Gain insight into estimates vs actuals in 7pace Timetracker.](/cms_trial/assets/31e1b315-43b0-4080-95f0-d548aa40487e.png)

## Gain insight into team member capacity

With BigPicture, you can define resource capacity based on workload plans, holidays, and individual absences. Now, with the 7pace Timetracker integration, you can view capacity information by team member.

### Access

The BigPicture capacity is displayed in many places across 7pace:

#### Times Explorer

From the 7pace [**Times Explorer**](/cms_trial/space/7TFJ/1920729127/Times+Explorer+view/), click the BigPicture and 7pace integration button, and filter for a time period to view capacity notes (**On Track**, **Below Capacity**, **Above Capacity**) for each team member.

![Get a birds-eye view of team member capacity.](/cms_trial/assets/0d538fb6-be33-4895-a1b5-c983e33004bd.png)

Or, group the *Times Explorer* view by a custom field, such as **activity type,** to see where team members are spending their time.

![image-20250610-224345.png](/cms_trial/assets/cb6d5914-d5ed-4c52-a012-ce024d85b28e.png)

#### Approval periods

In [**Approval Periods**](/cms_trial/space/7TFJ/2651455520/Approval+periods/), capacity is displayed next to specific user in period This allows managers to determine if users are on track with their tasks. The warning icon appears when logged hours do not match capacity.

![capacity-approval-periods.png](/cms_trial/assets/ed145fc4-06dd-4ec7-98dd-1da504f2e861.png)

#### Monthly view

Total capacity for of a current user for a specific month is displayed in [**Monthly view**](/cms_trial/space/7TFJ/1202094136/Monthly+view/):

![capacity-monthly-view.png](/cms_trial/assets/c4d3f264-c33c-4d5a-ab00-08c0282f24d2.png)

#### Weekly view

Total capacity for of a current user for a specific week is displayed in [**Weekly view**](/cms_trial/space/7TFJ/1201930328/Weekly+view/):

![weekly-view.png](/cms_trial/assets/2e90407c-4246-4f97-9757-a222fffce00c.png)

#### Timesheet view

Total capacity is displayed in [**Timesheet view**](/cms_trial/space/7TFJ/1828782116/Timesheet+view/).

![capacity-timesheet-view.png](/cms_trial/assets/fbec345f-647e-4ed4-8994-c11633b499dc.png)

#### Add Time

In [**Add Time**](/cms_trial/space/7TFJ/1202159710/Add+worklogs/)a user can check the remaining time (capacity - logged time), which provides context for individual contributors to submit accurate hours.

![capacity-add-time.png](/cms_trial/assets/c9918840-a21a-43dc-b96d-2bd61816221d.png)

## Summary

The BigPicture and 7pace Timetracker integration leverages time tracking data to assist your team in keeping projects on track on both manager and individual contributors level.