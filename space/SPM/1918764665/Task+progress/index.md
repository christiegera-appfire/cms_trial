# Task progress

## Calculate task progress

You can calculate the task progress using different fields and formulas. The progress can be displayed as a column, on the taskbar, and on the task details dialog once you click the taskbar.

For example: The SHPBOWM project is mapped to use the Time Tracking fields to calculate the progress (Remaining estimate and Spent time). The Select the property to build on (SHPBOWM-2) completed in 33% according to the following formula Time spent (1w)/Time spent + Remaining estimate (3w) \* 100 %:

![Task progress shown in Gantt chart](/cms_trial/assets/30df7e3d-7304-490f-859f-58ade6ca219e.png)

## Configuration

You can configure the [progress field](/cms_trial/space/SPM/1918669957/Progress+field/) in the App Configuration, which requires Jira Administrator permissions. You can use one of the following options:

- Time Tracking Progress (Spent)
- Time Tracking Progress (Original)
- Custom number field — values ranging from 0-100

## Displaying progress on the taskbar

To show the progress directly on the task, click **View** > **Progress**.

![Task progress bar displayed in the Gantt chart](/cms_trial/assets/49a96d31-ee5d-4504-b952-213c2c86cdda.png)

Once enabled, the progress is displayed on both the child and parent taskbars:

![Progress bar displayed on parent and child tasks in Gantt chart](/cms_trial/assets/ff98b202-ece8-4036-9b5f-1161b02f38ee.png)

## Updating task progress

You can update the progress of your task by editing the relevant fields (depending on the configuration).

Updating the progress using the slider on the taskbar feature is not available anymore in the new Gantt.