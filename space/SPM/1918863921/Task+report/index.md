# Task report

Task reports provide basic statistics, such as counting tasks in specific categories or summing the values of numeric fields on tasks.

You **cannot** see a report if it includes tasks you do not have access to.

There are three types of task report visualization:

- Pie chart
- Column chart
- Tree view (with collapsed lines)

To change the current view, click one of the view buttons at the top right corner of the chart area.

![Software Less project charts](/cms_trial/assets/11d1fb5d-ae8d-4001-ad0c-352ed227a5e9.png)

---

### **Report configuration**

| **Element** | **Description** |
| --- | --- |
| **Name** | The report name is displayed in the header of each report. |
| **Chart type** | The visualization is presented by default after refreshing the page:   - Column chart - Pie chart - Tree view |
| **Formula** | - **Task count** – the number of tasks in chosen categories, e.g., the number of tasks with the "To do" status - **Field sum** – the sum of the selected 'Number' field values in a given category, e.g., the sum of all Story Points for tasks with the "To do" status - **Time-type field**- the sum of the "Time-type" field values, e.g. sum of the fields such as "Original estimate", "Remaining Estimate", "Time spent"   Depending on the count strategy, some fields may be unavailable for a given formula  (for example, task count would make no sense for a story points field; field sum would make no sense for a status field, etc.). |
| **Group by** | Data presented can be grouped into different fields (up to four levels). It is possible to use fields from a task source (such as Jira and Trello) and/or built-in fields.  From the 8.19 version of BigPicture, you can group by **"Number"** type fields (e.g., "Duration Calendar Days", "Task Progress", "Time Tracking Progress"). edit-report.png |
| **Date filter** | Only data that fits within the selected time frame is part of the report.  Examples:   - If you set the filter to Created date between March 1 and March 31, you'll get the sum of Story Points only from tasks created in March. - If you set the filter to Resolved date between April 1 and April 30, you can generate a "Task count" report showing how many Bugs were closed in April.   Without the date filter, you will get the count or sum from all tasks. |
| **Narrow down** | Use JQL to filter data for customized reports.  Examples:   - Create a report focusing on Story Point burndown in open sprints with the following settings: report-configuration-narrow.png - Create a report focusing on time logged by users in the current month: report-narrow-down.png - Create a report focusing on open, high-priority bugs in team Alpha grouped by status: report-configuration-narrow-2.png |

### Creating a multi-level report

The **Group by**option allows you to break down data without the need to create multi-level reports.

In the example below:

- First, data is grouped by Assignee,
- Next, each chunk is further broken down by Status,

  ![edit-report-2.png](/cms_trial/assets/f61577c8-0a33-43bf-bb28-0da9761010e2.png)![status-per-assignee-2.png](/cms_trial/assets/ce01cc66-76fd-4c76-8c3a-043d0432ddb1.png)

When you click on a data chunk, you go to the level below.

### **Navigating between 'Group by' levels (with breadcrumbs)**

The chart shows data from the 'Group by' level that you are on. You can click on a chart (on a particular data slice) to go to a lower level.

Breadcrumbs can be used to navigate back to a higher level of grouping.

![status-per-assignee-assignee.png](/cms_trial/assets/8badc85e-7284-4ec7-9810-2534318b9d41.png)