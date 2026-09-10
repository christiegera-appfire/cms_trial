# Work Item Automation Questions - How to utilize Completed and Remaining work, Original Estimate, Effort and Pace

Completed and Remaining Work fields tutorial video:

## Question - How do I track all time in the past under Completed Work?

We just activated the feature "Work Item Automation - Completed Work". However, all times tracked in the past are not shown under Completed Work. How can we enable this?

### Answer - Trigger work item fields in a specific work item

Updating the work item fields Completed/Remaining Work is triggered when time is added/edited to a specific work item. Unfortunately, historical tracks/work items will not be updated/filled in automatically before the feature was enabled under Settings -> Work Item Automation.

## Question - Where is the new DevOps field I added?

Why is the new field I added to DevOps not displaying in the Timetracker dropdown list for "Completed Work" under  "Settings" -> "Work Item Automation"?

### Answer - Double-check the creation criteria

Timetracker has no limitation on the number of items that can display in the "Completed Work" dropdown list in "Settings" -> "Work Item Automation" -> "Completed Work". If the field meets the creation criteria, listed below, it will show up in the dropdown list.

The criteria for adding a new field that will successfully display in the "Completed Work" dropdown list is:

1. Type==Double
2. It is not in { "StackRank", "Story Points", "Size", "BacklogPriority", "Effort" } field's list
3. Is returned by API call https:// [DevOps Server|DevOps Services\_url] / [collection\_name] /\_apis/wit/fields?api-version=1.0

## Question - Why doesn’t completed work match remaining work?

Why is the "Completed Work" field value or sum not the same as the "Remaining Work" field value or sum (for example, "Remaining Work" was 8 hours and becomes 0, but "Completed Work" displays as 0h to 7.6h)?

### Answer - Calculation details

"Completed Work" is calculated every time you add or remove time and/or each time you "Stop Tracking" on the WinClient. It then adds up all tracks for a particular DevOps ID from the database. Then, this summed value is rounded to one (1) decimal and is written to the "Completed Work" field. Therefore, it represents the exact value of hours spent on a task from the database.

The "Remaining work" field is calculated in different way. Every time you add or remove time on the WinClient and/or "Stop Tracking", this method takes the current "Remaining work" field value and increases/decreases it with a new track length rounded (up). Therefore, this field represents the approximate progress on this task (due to rounding on each iteration of a field update).

## Question - How can I add “total time spent” as a column in the backlog?

Is it possible to add "total time spent" to the stories backlog as a column, on the story level and on individual tasks and bugs? What about on the Kanban board?

### Answer - Use the “completed work” feature

Yes, this is possible. 7pace Timetracker can automatically fills a field from DevOps Server or Services with the time spent on this particular item. This is possible with the "Completed Work" feature.

First, you need to have a field in DevOps, either an existing field such as "Completed Work" or you can update the work item template with your own custom field.

Then go to the "Settings" page of Timetracker -> "Work Item Automation" -> "Completed Work" -> click the "Enable filling in total tracked time for a work item field" checkbox -> select the field that you want to use in the dropdown, and then click "Apply".

Timetracker will then fill in this field automatically and you can use it everywhere in DevOps Server or Services.

## Question - The effort field is empty in my Budget export to Excel

We have data filled in a work item for the effort field but when we export the Budget to Excel the effort field is empty. Why is this happening?

### Answer - Review Work Item Automation settings

The Budgets export does not look at the Effort field itself, but instead at whatever is selected in Work Item Automation settings for Pace Calculation:

![Work_Item_Automation.png](/cms_trial/assets/319c15bd-362e-4a25-b86d-8c2390ef2de1.png)

If you select the Effort field for Pace Calculation, it will be reflected in the export.

## Question - How is the Completed Work field updated?

When an existing work item already has a value specified directly in Azure DevOps in the Completed Work field, and a subsequent work log entry is created using Timetracker, the Completed Work field value is updated to only reflect the Timetracker work log total, overwriting the previous Completed Work value.

### Answer - How is the Completed Work field overwritten

The value entered manually into the Completed Work field will be overwritten with the data entered into Timetracker, since once Work Item Automation is enabled, and the Completed Work field selected, this field is used for filling the time tracked within Timetracker. So anything that is not entered into Timetracker will not be included.

## Question - How do I evaluate the actual time spent on a task?

Is there a way to evaluate an engineer by comparing his evaluation of a task with the real-time he spent on it? The challenge is to compare original estimations of efforts with the eventual tracked time.

### Answer - Use the effort and pace fields

There are several ways to achieve this - here are some starting points.

It's good practice to use the **effort field** for estimations in parent items (such as stories, PBI's or bugs). The effort can be a unit like *story points*, *complexity points*, or - even *hours*. So, the engineer first estimates the whole story, then breaks it down into tasks, and tracks time on the tasks. If you proceed like this, you can use the Timetracker **pace** field that indicates the ratio between initially-estimated effort and the eventual tracked time. As estimation skills are usually some kind of holy grail, this is very educational for the team to understand previous estimations after work has been finished. (Start here for additional information: [Iterations Page Overview](/cms_trial/space/7TFA/1253540717/Iterations/))

You will find the pace information in a lot of places in the Timetracker UI, e.g. in the "7pace Timetracker" tab (formerly the "Time" tab) from within the work item form, for every work item type, even high-level items such as epics.

In addition, the task itself will also be estimated during the process, this time (depending on your work item template in DevOps Server/Services) in the **remaining hours** field, in the unit *hours,* but in a different context. The number will usually get updated multiple times until this work is completed, as the engineer is supposed to report how much time from the current perspective is still remaining every day. For that reason, this field is not that suitable for comparing an initial estimation with the final tracked time, as it is intended to be used as the snapshot of *now*, how many hours remain in the sprint, e.g. to compute the burndown.

However, if you need to compare the *remaining hours* with the tracked time, there are some tricks as well. First of all, DevOps Server/Services saves all ever-filled fields in estimations of remaining hours in the work item history. This data is available via the REST interface directly from DevOps Server/Services; you can get this for any given date. If you only need some samples, you can also open the work item itself with a browser and scroll down the history to see the initial estimation. You should keep in mind that there might be a huge number of entries for that field available, and it might be hard to automatically grab the correct value for meaningful analytics. (A good start for further information might be [here](https://docs.microsoft.com/en-us/rest/api/azure/devops/wit/?view=azure-devops-rest-6.0#get-a-work-items-full-history))

Another option is to add an additional field in the work item template of your project in DevOps Server/Services that represents the binding initial estimation on the task perspective. This field should be not changed during the development process and can serve as a good helper to remember how the situation was estimated at the very beginning.

If you want to track and control spending on a larger scale, it makes sense to use the budget feature. (For more info, please see [Budgets Page Overview](/cms_trial/space/7TFA/1253540085/Budgets/))