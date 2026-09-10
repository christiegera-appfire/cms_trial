# Iterations

Use the Iterations page to evaluate how your sprint is progressing, what items are being worked on and by whom, your effort, tracked time for parent and child items, and pace.

## Introduction

The Iterations page provides you with a quick snapshot of how your sprint is progressing. Here, you can view the tracked time details of work items according to the specific iterations to which they belong. Featuring a sprint-oriented view of the time spent by your team, the Iterations page is similar to the look and feel of the Backlog page of Azure DevOps, but with more robust information. The Iterations page allows you to assign budgets to whole releases or single work items and provides you with a unique window into the following:

- How is the sprint running?
- What work items are currently being worked on and by whom?
- Which work items were moved to a different iteration?
- What is progressing well in the sprint and what requires our attention?
- How accurate were our team's estimations?
- What is the team's pace on particular work items or the sprint as a whole?

## Iterations page at-a-glance

![Iterations_Page_Overview.png](/cms_trial/assets/dd368366-d69a-418a-9aa3-736328ce2196.png)

| **ID** | **Description** |
| --- | --- |
| 1 | The list of all iterations from your DevOps project settings. |
| 2 | The name of the iteration you currently have selected. |
| 3 | The timeframe or date range of the current iteration.  The date range appears only if you have configured it for the iteration. Otherwise, "No Iteration Dates" displays. |
| 4 | Options to view the tracked time details of work items within an iteration:   - **Expand One Level (+ )**: Expand the work items list by one level at a time. The top level work items are expanded first and after that, the child work items. - **Collapse One Level (-)**: Collapse the work items list by one level at a time. The child work items are collapsed first and after that, the top level items are collapsed. - **View by Iteration Date Range Only**: Displays the total tracked time of the work items according to the iteration timeframe. If you set this field to ON, the total tracked time for work items is shown only by the iteration period. If you set this field to OFF, total time for all work items is shown. If you did not configure a date range for the iteration, this field is disabled and set to NA. - **View Moved Items**: Displays the work items that were a part of the selected iteration at the beginning of the iteration, but were later moved to different one. If a date range was not configured for the iteration, this field is disabled and set to NA.   The start of the iteration is computed as: `Iteration Start Date + 1 day 00:00AM == midnight next day` |
| 5 | Total time tracked for all work items from the selected iteration.  Additionally, the total tracked time for work items in a completed state and work items in an incomplete state is also displayed. |
| 6 | The Total Story Points (total effort) of all work items from the selected iteration.  Additionally, you can view the total effort/story points for the work items in completed and incomplete state.  This field displays the total only if you configure the Pace Calculation option on the **Settings** > [**Work Item Automation**](/cms_trial/space/7TFA/1253540033/General+Settings/) [page](https://support.7pace.com/hc/en-us/articles/360025251172-Settings-General#Work%20Item%20Automation). If this isn't configured, the Total Effort field displays the status as Inactive. |
| 7 | The budget inherited from the parent item or specifically assigned to the iteration.  If there is no budget assigned to the iteration, this field displays **None**. For more information about assigning budget to an iteration, click [here](/cms_trial/space/7TFA/1253540717/Iterations/). |

## Iterations page columns

The following table details the columns found on the Iterations page.

| **Column** | **Description** |
| --- | --- |
| ID | The unique ID of the work item within DevOps Server/Services. |
| Title | The title of the task within DevOps Server/Services. |
| Iteration Path | The path of the iteration.  This column also displays the new iteration path for work items that are moved from the selected iteration. |
| Assigned To | The name of the person to whom the work item is assigned. |
| State | The current state of the work item. |
| Effort | The number of user story/complexity points (effort) estimated for the work item. |
| Tracked | The total time tracked for the corresponding work item.  There are two states - tracked within last 2 hours and 48 hours. Hover your mouse over your entry to see the state of the work item:  Tracked within the last two (2) hours: Last_Track_Within_Two_Hours.png Tracked within 48 hours: Last_Track_Within_48_Hours.png |
| Tracked Summary | The total tracked time for the parent work item and all its child work items. |
| Pace | The pace at which the task is performed. This number is calculated by dividing the number of tracked hours by estimated effort. |
| Budget | Displays the current budget assigned to the work item.  Budgets are usually assigned to iterations or even whole releases. However, if you don't want to bill a customer for certain work items in a sprint/iteration, you can simply exclude them from one budget (e.g. "Company X Billable") and move them to a different budget instead (e.g. "Company X Non-Billable") by clicking on the "Budget" column dropdown arrow next to each work item row. |

## Assign a budget to an iteration

Budgets are usually assigned to iterations or even whole releases. After you assign a budget to an iteration, you can go to the "Budgets" page, click on that budget, and verify that the iteration was added by looking in the Includedsection of the page. You can also view the list of included work items from that iteration.  For more information about the "Budgets" page, see [Budgets Page Overview](/cms_trial/space/7TFA/1253540085/Budgets/).

1. On the 7pace Timetracker menu bar, click **Iterations**.

2. In the left pane, click the iteration name for which you want to assign a budget.

3. At the top-right corner of the web page, click the **Budget**dropdown.

![Assign_Budget_to_Iteration_Step_1.png](/cms_trial/assets/1f6b5946-37da-43c3-a1dd-9f3648ec8259.png)

The list of budgets created on the Budgets page is displayed.

4. From the dropdown list, select the budget that you want to assign to the selected iteration.

![Assign_Budget_to_Iteration_Step_2.png](/cms_trial/assets/1289892a-5b86-47f1-8141-2c89a713f613.png)

The entire iteration is assigned to that budget.

## Assign a budget to a work item

If you only want to bill a customer for certain work items in an iteration, you can simply exclude those unbillable work items from one budget by assigning them to a different one. You can do this on the "Iterations" page by clicking on the "Budget" column dropdown arrow next to each work item row (see more details, below). These work items will display in the **Excluded** section of that budget on the "Budgets" page. For more information on changing work item on budgets, see [how to include work items in a budget](/cms_trial/space/7TFA/1253540085/Budgets/) and how to [exclude work items from a budget](/cms_trial/space/7TFA/1253540085/Budgets/).

Please note that budgets are inherited. A budget that is assigned to a parent object will be used by all child objects as long as no other budget is assigned.  When you assign a different budget to child items, they are considered exceptions to the inherited budget settings.

For example, if you assigned a budget to the whole release (Budget "A"), but you assign a different budget (Budget "B") to a product backlog item (PBI), somewhere deep inside this release (e.g. in release\iteration\parent PBI\child PBI), all time that has been recorded on that PBI or to its child items will then be counted in Budget B.

The budget inheritance from a parent work item to child work items overrides the budget inheritance from an iteration to its work items.

1. In the left pane of the Iterations page, click the iteration name.

![Assign_Budget_to_Work_Item_Step_1.png](/cms_trial/assets/c82b1799-d110-4da2-a533-8231138a6d78.png)

2. Highlight the row of the specific work item you want to assign to a different budget than that of the entire iteration. When you hover over the row with your mouse, the row will be highlighted in blue.

3. In the Budget column of the highlighted row, click the row corresponding to the work item.

![Assign_Budget_to_Work_Item_Step_2.png](/cms_trial/assets/8321ded4-d094-4fdb-be88-39e00e5786d6.png)

4. From the drop-down list, select the budget that you want to assign to the work item.

The work item is automatically assigned to the new budget. If you now go to the "Budget" page of Timetracker, you will see that work item in the "Excluded" section of the budget from which you removed it.

Related Articles

- ["Budgets" Page Overview](/cms_trial/space/7TFA/1253540085/Budgets/)