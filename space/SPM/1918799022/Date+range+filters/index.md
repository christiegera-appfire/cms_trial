# Date range filters

## Date range filters (old navigation)

Click to expand the guide

You can use the date range filters to show Jira issues, basic tasks, or boxes scheduled in a specified period of time.

You can find the date range filters in the following modules:

- **Overview**  
  When you filter by the date range using the Overview module, the Box start and end dates will be used (tasks' dates are not relevant).
- **Gantt**
- **Risks**

When you filter by the date range using the Gantt or the Risks modules, the tasks' Start and End Dates presented on the timeline will be used.

The date range filter affects only the module in which you have applied it.

![image-20250306-132233.png](/cms_trial/assets/7f9ffee1-1693-4800-9cd9-315bd6818b0f.png)

## Filter by dates in the Overview module

Use the calendar picker to set the preferred date range to check all the Boxes assigned. Use the Clear button to clear the chosen date range. The **Today** button opens the current month in the calendar.

![filter-dates.png](/cms_trial/assets/39c0b034-a463-4d6a-8517-726305751cce.png)

For example, the image below shows the Overview module date range filter. The date range in that module uses the Box start and end dates which are not synchronized with Jira or connected tools:

![The chosen date range is marked](/cms_trial/assets/804df78a-755d-4e64-8b81-4ec9d8f00c22.png)

## Filter by dates in the Gantt and Risks modules

- Filtering is available on the tasks that are visible on the timeline.
- The position on the timeline determines the field mapping configured. The start/end dates are not related to Jira fields.
- If any part of the Box/Task duration fits between start/end date filters, a task is found (partial overlap is sufficient).
- Using only the start date means everything from that date onwards meets the criteria (once again, the partial overlap is sufficient).
- Using only the end date means everything preceding that date meets the criteria (once again, the partial overlap is sufficient).

When you apply a filter, all tasks scheduled beyond the defined period will be filtered out.

Your filter remains active even when you switch to a different module or return to the Box. Remember to clear the filter to see all tasks/Boxes once again.

## Date range filters (new navigation)

Click to expand the guide

You can use the date range filters to show Jira work items, BigPicture tasks, or boxes scheduled in a specified period of time.

You can find the date range filters in the following modules:

- **Overview**  
  When you filter by the date range using the Overview module, the box start and end dates will be used (tasks' dates are not relevant).
- **Gantt**
- **Risks**

When you filter by the date range using the Gantt or the Risks modules, the start and end dates of tasks presented on the timeline will be used.

The date range filter affects only the module in which you have applied it.

![Screenshot of the date range filter in the Gantt module.](/cms_trial/assets/cc30c8c2-2541-4a10-8767-ae0a4fc46a9a.png)

## Filter by dates in the Overview module

Use the calendar picker to set the preferred date range to check all the boxes assigned. Use the **Clear** button to clear the chosen date range. The **Today** button opens the current month in the calendar.

![Screenshot of the date range filter in the Overview module. ](/cms_trial/assets/e30a0c03-bbad-4c0c-aff4-dcf8b2ea9311.png)

## Filter by dates in the Gantt and Risks modules

- Filtering is available for tasks visible on the timeline.
- The position on the timeline determines the configured field mapping. The start/end dates are not related to Jira fields.
- If any part of the box/task duration fits between start/end date filters, a task is found (partial overlap is sufficient).
- Using only the start date means everything from that date onwards meets the criteria (once again, the partial overlap is sufficient).
- Using only the end date means everything preceding that date meets the criteria (once again, the partial overlap is sufficient).

When you apply a filter, all tasks scheduled beyond the defined period will be filtered out.

Your filter remains active even when you switch to a different module or return to the box. Remember to clear the filter to see all tasks/boxes once again.