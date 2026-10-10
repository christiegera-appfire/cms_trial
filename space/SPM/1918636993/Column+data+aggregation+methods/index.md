# Column data aggregation methods

## Column data aggregation methods (old navigation)

Click to expand the guide

## Data aggregation in the column view

You can aggregate data on several different columns that display numeric data. Depending on the data field the column represents, not all methods are available. Aggregation methods roll up data from children and display the result on the parent.

You can aggregate all task types, including basic tasks and milestones.

**Aggregation can be adjusted directly in the module views**

- Those changes are temporary and reversible (until you save them and update the view).
- Temporary changes made to your current view affect only you (other users don’t see them).
- Available options differ depending on the field.

![ggregation methods as seen in the Gantt module.](/cms_trial/assets/03399cc4-82d3-4a11-bfd4-8480f6709444.png)

### None

The **None** aggregation method means that no aggregation is applied to the data in that specific column. This setting essentially disables any type of summarization or consolidation of the data, and it leaves the raw, individual data values visible without any kind of calculation or combination.

When to use aggregation **None**:

- When you don't need to aggregate data but rather need to track individual values.
- When you want to maintain visibility into all individual elements.

In the example below, the **Duration Working Days** column displays the duration of the “Location search” task as is, based on its start and end dates.

![Data aggregation on the column is set to None.](/cms_trial/assets/8ee456e0-043e-450a-a466-41cfeac56bf7.png)

### Minimum

The **Minimum** aggregation methodshows the smallest value in a parent column when multiple items or tasks are under consideration. This aggregation type helps to highlight the lowest or least significant value across a group of tasks, issues, or other data points.

When to use aggregation **Minimum**:

- When you want to find the smallest value in a set of data, such as the shortest time, the least amount of work, or the earliest deadline.
- It is useful for highlighting tasks that may require the least effort or that need to be completed first (in terms of due date or duration).

In the example below, the **Duration Working Days** column displays the duration of the “Location search” task as 0 days based on the milestone “Location found” (milestones have no duration). If we were to remove the milestone from the structure, the value would switch to 21 (the days it will take to complete the task “Survey and footprint the house”).

![Data aggregation on the column is set to Minimum.](/cms_trial/assets/dcdd1108-fe20-402f-8786-27d45fe69f8b.png)

### Maximum

The **Maximum** aggregation method shows the largest value in a column when there are multiple items, tasks, or issues in that column. This aggregation type helps you identify the highest or most significant value across a group of data points.

When to use aggregation **Maximum**:

- When you have tasks with different time or effort estimates, applying **Maximum** aggregation will show the task with the highest estimated time or effort.
- If you're tracking task progress, the **Maximum** aggregation can display the highest progress percentage, helping you see the most completed task.
- In cases where you are tracking deadlines, applying the **Maximum** aggregation will display the latest due date, indicating the task that has the farthest deadline.

In the example below, the **Duration Working Days** column displays the duration of the “Location search” task as 33 based on the task “Select a desirable place for the model house.”

![Data aggregation on the column is set to Maximum.](/cms_trial/assets/4e837c59-ac0d-4c18-8a2d-149ee34c9407.png)

### Sum

The **Sum** aggregation method addsup all the values in a column. This aggregation type lets you quickly calculate the total of a set of values for multiple tasks and their parent.

When to use aggregation **Sum**:

- When you want to calculate the total of any numeric values in a column, such as total effort, time spent, cost, duration, completion, or story points.
- It is particularly useful for reporting on cumulative metrics across multiple tasks or issues.

In the example below, the **Duration Working Days** column displays the duration of the “Location search” task as 169 based on the duration of the parent and all the tasks under that parent.

![Data aggregation on the column is set to Sum.](/cms_trial/assets/6aa21ff1-c1bb-4252-b6f7-e312caff00c9.png)

### Sum, without parent

The **Sum, without parent** aggregation method is a variation of the **Sum** aggregation. It adds the values of the child tasks or issues but excludes the parent task from the calculation.

When to use aggregation **Sum, without parent**:

- When you are focused on the total of child tasks (for example, total effort, cost, or time) but do not want to include the parent's aggregated values.
- This aggregation method is helpful for granular insights into the lower-level work, without distorting the overall numbers with higher-level aggregations.

In the example below, the **Duration Working Days** column displays the duration of the “Location search” task as 85 based on the duration of all the tasks under that parent.

![Data aggregation on the column is set to Sum without parent.](/cms_trial/assets/0378a063-454b-4b79-ba8f-5bf15bdea7a6.png)

### Average

The **Average** aggregation method calculates the average (mean) value of a specific column across multiple tasks or issues. Instead of showing the sum of the values, it provides the average value for a set of tasks and their parent.

When to use aggregation **Average**:

- When you want to understand the average completion level, effort, or cost for tasks without focusing on extreme values.
- When you need a more balanced view of metrics by smoothing out any large or small values that might skew the results.

In the example below, the **Duration Working Days** column displays the duration of the “Location search” task as 33.8 based on the duration of all the tasks and their parent.

![Data aggregation on the column is set to Average.](/cms_trial/assets/bb65cee2-6c16-4c05-837c-9a5abd48c67e.png)

### Average, without parent

The **Average, without parent** aggregation method is a variation of the **Average** aggregation. It calculates the average value of child tasks or issues while excluding any parent tasks from the calculation.

This type of aggregation lets you focus on the average of the child tasks without considering the parent task's value, ensuring that only the individual task data is included.

When to use aggregation **Average, without parent**:

- When you want to calculate the average value of child tasks only and exclude the parent task's aggregated value from affecting the result.

In the example below, the **Duration Working Days** column displays the duration of the “Location search” task as 21.25 based on the duration of all the tasks under that parent.

![Data aggregation on the column is set to Average without parent.](/cms_trial/assets/61b4899c-9ff7-44de-a074-5872676fdc81.png)

### Status categories in %

The **Status categories %** aggregation method is a specific aggregation type used to represent the distribution of tasks and their parent based on their status categories as percentages.

This type of aggregation shows how tasks are distributed across different status categories, such as **To Do**, **In Progress**, **Completed**, or any custom status categories defined in your project.

The result is presented as a percentage of tasks and the parent that falls into each status category, displayed in a **Lozenge** format. The data is shown even if you do not have the **Status** column added to your current view.

When to use aggregation **Status categories %**:

- This aggregation is ideal when you want to quickly see how tasks and a parent are progressing across different status categories.
- When you want to identify where tasks are stalled (for example, if a large percentage of items are still in the "To Do" category) and take action to move them forward.
- When you want to see how much work is completed, how much is in progress, and how much is still pending.

In the example below, the **Duration Working Days** column displays each status category and the percentage of tasks (including the parent) that fall into each category. Note that the data is aggregated by the status only; the duration of the task is irrelevant.

![Data aggregation on the column is set to Status categories percent..](/cms_trial/assets/8fa13963-c7a7-4b14-be15-ed4b4db58b84.png)

### Children status categories

The **Children status categories** aggregation method is a specific aggregation type used to represent the distribution of tasks based on:

- status categories of the child tasks
- value under the specific column.

This aggregation type lets you see the distribution of child task statuses (for example, **To Do**, **In Progress**, **Completed**) without being influenced by the parent task status and value.

The result is presented as a sum of values of tasks that fall into each status category, displayed in a **Lozenge** format. The data is shown even if you do not have the **Status** column added to your current view.

When to use aggregation **Children** **status categories**:

- When you want to see the number of days, cost, story points, etc., that have remained in each category.

In the example below, the **Duration Working Days** column displays the total number of working days from all tasks and groups them into their status-based categories.

![Data aggregation on the column is set to Children status categories.](/cms_trial/assets/0145f95f-a8b2-42e4-aa08-007ee8666853.png)

### Children status categories in %

The **Children status categories %** aggregation method is a specific aggregation type used to represent the distribution of tasks excluding their parent based on their status categories as percentages.

This type of aggregation shows how tasks are distributed across different status categories, such as **To Do**, **In Progress**, **Completed**, or any custom status categories defined in your project.

The result is presented as a percentage of tasks that fall into each status category, displayed in a **Lozenge** format. The data is shown even if you do not have the **Status** column added to your current view.

When to use aggregation **Children** **status categories**:

- When you need a percentage-based overview of how child tasks are spread across different statuses.
- When managing a large project with multiple tasks and subtasks, this aggregation gives a quick view of the number of child tasks in each status, which helps to track progress.
- This aggregation type helps you identify if a high percentage of child tasks are stuck in a particular status, like "To Do" or "In Progress", which may indicate delays or bottlenecks.

In the example below, the **Duration Working Days** column displays each status category and the percentage of tasks (excluding the parent) that fall into each category. Note that the data is aggregated by status only; the duration of the task is irrelevant.

![Data aggregation on the column is set to Children status categories percent.](/cms_trial/assets/f27a8509-e901-49a2-a545-380ea2e6da54.png)

## Column data aggregation methods (new navigation)

Click to expand the guide

## Data aggregation in the column view

You can aggregate data on several different columns that display numeric data. Depending on the data field the column represents, not all methods are available. Aggregation methods roll up data from children and display the result on the parent.

You can aggregate all task types, including BigPicture tasks and milestones.

**Aggregation can be adjusted directly in the module views**

- Those changes are temporary and reversible (until you save them and update the view).
- Temporary changes made to your current view affect only you (other users don’t see them).
- Available options differ depending on the field.

![ggregation methods as seen in the Gantt module.](/cms_trial/assets/03399cc4-82d3-4a11-bfd4-8480f6709444.png)

### None

The **None** aggregation method means that no aggregation is applied to the data in that specific column. This setting essentially disables any type of summarization or consolidation of the data, and it leaves the raw, individual data values visible without any kind of calculation or combination.

When to use aggregation **None**:

- When you don't need to aggregate data but rather need to track individual values.
- When you want to maintain visibility into all individual elements.

In the example below, the **Duration Working Days** column displays the duration of the “Unstructured Features and Tasks” as is, based on its start and end dates.

![Screenshot of aggregating the Duration Working Days field by None in the Gantt module.](/cms_trial/assets/6d2444f9-23fd-4b93-89bd-ae8750442d80.png)

### Minimum

The **Minimum** aggregation methodshows the smallest value in a parent column when multiple items or tasks are under consideration. This aggregation type helps to highlight the lowest or least significant value across a group of tasks, work items, or other data points.

When to use aggregation **Minimum**:

- When you want to find the smallest value in a set of data, such as the shortest time, the least amount of work, or the earliest deadline.
- It is useful for highlighting tasks that may require the least effort or that need to be completed first (in terms of due date or duration).

![Screenshot of aggregating the Duration Working Days field by Minimum in the Gantt module.](/cms_trial/assets/fab998f4-5355-46f0-beb6-6fdfe732139e.png)

### Maximum

The **Maximum** aggregation method shows the largest value in a column when there are multiple items, tasks, or work items in that column. This aggregation type helps you identify the highest or most significant value across a group of data points.

When to use aggregation **Maximum**:

- When you have tasks with different time or effort estimates, applying **Maximum** aggregation will show the task with the highest estimated time or effort.
- If you're tracking task progress, the **Maximum** aggregation can display the highest progress percentage, helping you see the most completed task.
- In cases where you are tracking deadlines, applying the **Maximum** aggregation will display the latest due date, indicating the task that has the farthest deadline.

![Screenshot of aggregating the Duration Working Days field by Maximum in the Gantt module.](/cms_trial/assets/b0663b35-f5da-46f1-affe-f90170c42d03.png)

### Sum

The **Sum** aggregation method addsup all the values in a column. This aggregation type lets you quickly calculate the total of a set of values for multiple tasks and their parent.

When to use aggregation **Sum**:

- When you want to calculate the total of any numeric values in a column, such as total effort, time spent, cost, duration, completion, or story points.
- It is particularly useful for reporting on cumulative metrics across multiple tasks or work items.

![Screenshot of aggregating the Duration Working Days field by Sum in the Gantt module.](/cms_trial/assets/96a1fc2f-0158-4222-bb11-242ae36de55c.png)

### Sum, without parent

The **Sum, without a parent** aggregation method, is a variation of the **Sum** aggregation. It adds the values of the child tasks or work items, but excludes the parent task from the calculation.

When to use aggregation **Sum, without parent**:

- When you are focused on the total of child tasks (for example, total effort, cost, or time) but do not want to include the parent's aggregated values.
- This aggregation method is helpful for granular insights into the lower-level work, without distorting the overall numbers with higher-level aggregations.

![Screenshot of aggregating the Duration Working Days field by Sum, without parent in the Gantt module.](/cms_trial/assets/7729cc83-be94-41c8-a1f3-ce8eee872c34.png)

### Average

The **Average** aggregation method calculates the average (mean) value of a specific column across multiple tasks or work items. Instead of showing the sum of the values, it provides the average value for a set of tasks and their parent.

When to use aggregation **Average**:

- When you want to understand the average completion level, effort, or cost for tasks without focusing on extreme values.
- When you need a more balanced view of metrics, you can smooth out any large or small values that might skew the results.

![Screenshot of aggregating the Duration Working Days field by Average in the Gantt module.](/cms_trial/assets/bb56a0c6-14b5-4b84-9930-8017ae676f32.png)

### Average, without parent

The **Average, without parent** aggregation method, is a variation of the **Average** aggregation. It calculates the average value of child tasks or work items while excluding any parent tasks from the calculation.

This type of aggregation lets you focus on the average of the child tasks without considering the parent task's value, ensuring that only the individual task data is included.

When to use aggregation **Average, without parent**:

- When you want to calculate the average value of child tasks only and exclude the parent task's aggregated value from affecting the result.

![Screenshot of aggregating the Duration Working Days field by Average, without parent in the Gantt module.](/cms_trial/assets/690e191c-7bda-4ecf-a468-5a53ffb8f347.png)

### Status categories in %

The **Status categories %** aggregation method is a specific aggregation type used to represent the distribution of tasks and their parent based on their status categories as percentages.

This type of aggregation shows how tasks are distributed across different status categories, such as **To Do**, **In Progress**, **Completed**, or any custom status categories defined in your project.

The result is presented as a percentage of tasks and the parent that falls into each status category, displayed in a **Lozenge** format. The data is shown even if you do not have the **Status** column added to your current view.

When to use aggregation **Status categories %**:

- This aggregation is ideal when you want to quickly see how tasks and a parent are progressing across different status categories.
- When you want to identify where tasks are stalled (for example, if a large percentage of items are still in the "To Do" category) and take action to move them forward.
- When you want to see how much work is completed, how much is in progress, and how much is still pending.

![Screenshot of aggregating the Duration Working Days field by Status categories in percent in the Gantt module.](/cms_trial/assets/6bb0bdbe-1e36-4ab0-a052-8a1d5b00e1f6.png)

### Children status categories

The **Children status categories** aggregation method is a specific aggregation type used to represent the distribution of tasks based on:

- status categories of the child tasks
- value under the specific column.

This aggregation type lets you see the distribution of child task statuses (for example, **To Do**, **In Progress**, **Completed**) without being influenced by the parent task status and value.

The result is presented as a sum of values of tasks that fall into each status category, displayed in a **Lozenge** format. The data is shown even if you do not have the **Status** column added to your current view.

When to use aggregation **Children** **status categories**:

- When you want to see the number of days, cost, story points, etc., that have remained in each category.

![Screenshot of aggregating the Duration Working Days field by Children status categories in the Gantt module.](/cms_trial/assets/2114748f-1348-4156-ad49-b51ecd731cb2.png)

### Children status categories in %

The **Children status categories %** aggregation method is a specific aggregation type used to represent the distribution of tasks excluding their parent based on their status categories as percentages.

This type of aggregation shows how tasks are distributed across different status categories, such as **To Do**, **In Progress**, **Completed**, or any custom status categories defined in your project.

The result is presented as a percentage of tasks that fall into each status category, displayed in a **Lozenge** format. The data is shown even if you do not have the **Status** column added to your current view.

When to use aggregation **Children** **status categories**:

- When you need a percentage-based overview of how child tasks are spread across different statuses.
- When managing a large project with multiple tasks and subtasks, this aggregation gives a quick view of the number of child tasks in each status, which helps to track progress.
- This aggregation type helps you identify if a high percentage of child tasks are stuck in a particular status, like "To Do" or "In Progress", which may indicate delays or bottlenecks.

![Screenshot of aggregating the Duration Working Days field by Children status categories in percentin the Gantt module.](/cms_trial/assets/7e3ad70b-8f8d-43dc-9d5f-4c60d75cb9fe.png)