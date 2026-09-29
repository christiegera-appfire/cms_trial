# Bulk change

## About bulk change

The bulk edit option applies only to the [**own-scope**](/cms_trial/space/SPM/1918765868/Own-scope/) and [**sub-scope**](/cms_trial/space/SPM/1918799715/Sub-scope/) [boxes](/cms_trial/space/SPM/1918799715/Sub-scope/). You cannot bulk edit tasks in the [none-scope](/cms_trial/space/SPM/1918537743/None+(aggregations+only)/) types of boxes, like Portfolio.

Tasks bulk change in the Gantt module lets you modify multiple tasks simultaneously instead of editing them one by one. This feature can streamline your workflow and save time, especially if you manage large projects consisting of hundreds of tasks. Bulk changes also help you ensure uniformity across similar tasks by applying the same changes, reducing the risk of errors.

You can carry out the following actions on the group of tasks (including [basic tasks](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Basic%20tasks&linkCreation=true&fromPageId=1918506627)) and apply one bulk change at a time:

- add/change the assignee
- change the color
- change the start date
- change the end date
- change status
- add/change a team

![The overview of the bulk change tab in the Gantt Infobar.](/cms_trial/assets/9ce76001-1245-4453-ab5b-819d68002b0d.png)

## Edit tasks in bulk

### Select multiple tasks

You can select and bulk edit up to **50 tasks** in one go. The bulk change options in the Infobar appear only for tasks selected with the checkboxes.

Select individual tasks for editing by checking them in the checkbox column in your [column view](/cms_trial/space/SPM/1918404907/Column+views/). Use the **top checkbox** in the column header to clear your selections.

Once you check at least one task, a **bottom bar** with a counter will appear.

![Bottom bar with a task counter appears after you have checked at least one task.](/cms_trial/assets/0644e5e3-8a8f-413a-8933-0bb462e2a2df.png)

### Apply bulk change

Once you have your tasks selected, apply a bulk change:

1. Click the **Bulk change** button on the counter bar or open the [**Infobar**](/cms_trial/space/SPM/1918799264/Infobar+(Gantt)/) > **Bulk change** tab to access additional fields for bulk edit.
2. Select the field you want to edit and the value.
3. Click the **Apply changes** button.

![Selecting and applying task bulk changes in the Infobar.](/cms_trial/assets/e965bb31-a560-4a89-8f14-74de9947dee0.mp4)

## Task schedule conflicts in bulk changes

Bulk change actions let you change task dates. However, you will not be allowed to bulk edit task dates if there is a conflict in the tasks you selected, resulting from the [task scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/) and [strong dependencies](/cms_trial/space/SPM/1918536086/Dependencies/).

### Locked scheduling mode

You cannot bulk change start and end dates if you select at least one task in the locked scheduling mode (the task has its start and end dates locked).

### Auto bottom-up scheduling mode

You cannot bulk change the start and end dates of tasks that are set to the auto bottom-up mode (the task schedule is determined by its children).