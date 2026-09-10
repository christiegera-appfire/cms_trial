# Task dates based on estimates

## Task dates based on estimates (old navigation)

Click to expand the guide

BigPicture provides the possibility to automatically calculate task dates based on estimates or the time spent on tasks.

Key benefits of task dates based on estimates include:

- BigPicture updates the start or end date automatically based on modifications made to an estimate (similar to editing the “Duration Working Days” field). A user can decide which date should be modified (“Start Date” or “End Date”). Estimates can be defined in hours.
- Task estimates (“Original Estimate”) are updated on an ongoing basis when task dates change (e.g., when a task is longer than initially planned, the project estimate is updated accordingly).
- Task dates can be modified directly in Jira (the “Original Estimate” field in BigPicture needs to be synchronized with the “Original Estimate” field in Jira).
- You can configure a project where a person who works on a task updates the time remaining to complete a task (the “Time Spent + Remaining Estimate” mechanism). As a result, task dates are adjusted to this information.
- Inline editing the “Start Date” field results in moving a task. The scheduling mechanism moves a task and **does NOT** change the duration of a task.

## Activate automation

### Box level

For more information, see the [Field mapping](/cms_trial/space/SPM/1918700586/Field+mapping/) page.

**Method 1:**

[Unmapped block: nestedExpand]

If there are tasks from a few Jira projects in one box and the projects have separate custom configurations set, tasks in one box may behave differently according to the rules configured for the project they are in).

**Method 2:**

[Unmapped block: nestedExpand]

### App configuration level

The field mapping can also be configured from the global configuration level on the **App configuration > General > Fields** page.

If you set the default field mapping rules for the whole BigPicture, all tasks will follow the same rule unless a custom configuration is created for a project.

![contentId-1918539473](/cms_trial/assets/fd74e12f-a8ed-46fb-a215-9f06cc6ecc36.png)

### Field mapping scenarios

The table below presents the most popular field mapping scenarios.

| **Field mapping** | **Description** |
| --- | --- |
| Start Date = Start Date  End Date = End Date | Dates in BigPicture **are synchronized** with dates in Jira (the default mode). |
| Start Date = Not synchronized  End Date = Not synchronized | Dates in BigPicture **are not synchronized** with dates in Jira. |
| Start Date = Original Estimate  One-way sync = Start Date  End Date = End Date | Changes made to the “Original Estimate” field update the “Start Date” field. |
| Start Date = Start Date  End Date = Original Estimate  One-way sync = End Date | Changes made to the “Original Estimate” field update the “End Date” field. |
| Start Date = Start Date  End Date = Time Spent + Remaining Estimate  One-way sync = End Date | Changes made to the “Remaining Estimate” field can update the “End Date” field.  Time logged on a task can update the “End Date” field. |

You can also synchronize the “Start Date” and “End Date” fields with different fields, e.g., “Due Date”.

## Rules for editing “Start Date”, “End Date”, and “Duration Working Days”

When task dates are calculated based on estimates, the “Start Date” field is modified. When you set a new “Start Date”, a task is moved. The task duration (“Original Estimate”) remains the same.

- Changing the “Start Date” (11/Apr → 10/Apr) moves a task, and the “Original Estimate” **remains unchanged**:

![contentId-1918539473](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![contentId-1918539473](/cms_trial/assets/e5269046-8cc8-475a-b219-725684bba0c6.png)

- Changing the “End Date” (13/Apr → 12/Apr) **resizes** a task, and the “Original Estimate” is changed (-1 MD):

![contentId-1918539473](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![contentId-1918539473](/cms_trial/assets/4c4969d8-f3ac-4562-8336-2bdbec37004d.png)

- Changing the “Duration Working Days” field (3d → 1d) **results in changing the “End Date”** (-2 days) and the “Original Estimate” (-2 MD):

![contentId-1918539473](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![contentId-1918539473](/cms_trial/assets/e081f355-7065-4e17-bee6-757e7ec02b31.png)

## Rules for editing “Original Estimate”

When the “Start Date” or “End Date” is synchronized with the “Original Estimate” field, task dates are updated accordingly to changes made to the “Original Estimate” field.

- **The “Start Date” is synchronized with the “Original Estimate”:**

Changing the “Original Estimate” (3d → 4d) results in changing the “**Start Date”**.

![contentId-1918539473](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![contentId-1918539473](/cms_trial/assets/e3d6e828-3766-4979-bc03-31476babd483.png)

- **The “End Date” is synchronized with the “Original Estimate”:**

Changing the “Original Estimate” (3d → 4d) results in changing the **“End Date”**.

![contentId-1918539473](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![contentId-1918539473](/cms_trial/assets/4cf9ce02-9eba-486a-a768-c064e1b2a2dc.png)

When the “Original Estimate” field is set, the “Remaining Estimate” field is overwritten, as long as there is no time logged on a task.

The mechanism **does NOT** work the other way around. Editing the “Remaining Estimate” field **never overwrites** the “Original Estimate” field.

## Rules for editing “Time Spent + Remaining Estimate”

Synchronizing the “End Date” with the **“Time Spent + Remaining Estimate”** field activates the mechanism that adjusts task dates to the time logged on a task.

The “End Date” is calculated based on information provided by a person who does a task, e.i., the time logged on a task and data entered in the “Remaining Estimate” field.

Find out more in the example below.

- You set the **“Remaining Estimate”** to 3 MD.  
  You can also complete the “Original Estimate” field (the “Original Estimate” will overwrite the “Remaining Estimate” field as long as there is no time logged on a task yet).

![contentId-1918539473](/cms_trial/assets/76b01887-a58a-4361-a025-26b324a794a0.png)

- You start working and spend 1 MD on a task. The “Remaining Estimate” changes from 3 MD to 2 MD. The “Original Estimate” and task dates remain unchanged.

![contentId-1918539473](/cms_trial/assets/2d002feb-7ea9-4357-854e-71661037702c.png)

- You spend another 3 MD on a task (the time allocated to a task is exceeded by 1 MD). The “Remaining Estimate” value changes from 2 MD to 0. The “End Date” of a task changes (is 1 MD more). The “Original Estimate” remains unchanged so that you can check the initial estimate of a task.

![contentId-1918539473](/cms_trial/assets/a6febf76-9ae1-4e0a-88d7-e22f2aefada5.png)

- If you need to spend 1 MD more to complete a task, you can modify the “Remaining Estimate” field (e.g., in Jira) by entering 1 MD. Then, the “End Date” is automatically updated.

![contentId-1918539473](/cms_trial/assets/960eef21-64bd-45d2-a29c-7cf0d2f742a1.png)

## Milestones

The value of the “Original Estimate” and “Remaining Estimate” fields for a milestone is always 0.

## Tasks without dates

It is **not required** for tasks to have start and end dates defined.

### Rules for deleting and assigning dates

If the mechanism for calculating task dates based on estimated is enabled:

- Deleting one of the dates for a task results in removing the other date (otherwise, Bigpicture would recalculate the deleted date based on the entered estimate).
- Providing one of the dates for a task that has an estimate but does not have dates results in calculating the other date for a task.

### Rules for deleting “Original Estimate” and “Remaining Estimate”

- Removing the value from the “Original Estimate” field will also clear the value from the “Remaining Estimate” field as long as there is no time logged on a task. If there is time logged on a task, the “Remaining Estimate” field is not cleared.
- If the “Start Date” is synchronized with the “Original Estimate” field, clearing the “Original Estimate” field causes the deletion of the “Start Date” (otherwise, BigPicture would recalculate the deleted estimate based on task dates).
- If the “End Date” is synchronized with the “Original Estimate” field, clearing the “Original Estimate” field causes the deletion of the “End Date” (otherwise, BigPicture would recalculate the deleted estimate based on task dates).
- If the “End Date” is synchronized with the “Time Spent + Remaining Estimate” field, clearing the “Remaining Estimate” field causes the deletion of the “End Date” (otherwise, BigPicture would recalculate the deleted estimate based on task dates). If there is time logged on a task, the “End Date” field is calculated based on the time logged on a task.

## Task dates based on estimates (new navigation)

Click to expand the guide

BigPicture provides the possibility to automatically calculate task dates based on estimates or the time spent on tasks.

Key benefits of task dates based on estimates include:

- BigPicture automatically updates the start or end date when you modify an estimate (similar to editing the **Duration Working Days** field). A user can decide which date to modify (**Start Date** or **End Date**). Estimates can be defined in hours.
- Task estimates (**Original Estimate**) update automatically when task dates change (for example, when a task takes longer than planned, the project estimate updates accordingly).
- You can modify task dates directly in Jira (the **Original Estimate** field in BigPicture needs to be synchronized with the **Original Estimate** field in Jira).
- You can configure a project so that a person working on a task updates the time remaining to complete it (the **Time Spent** **+** **Remaining Estimate** mechanism). As a result, task dates are adjusted to reflect it.
- Inline editing the **Start Date** field moves a task. The scheduling mechanism moves a task and does not change the task duration.

## Configure field mapping (sync) for start/end dates

For more information, see the [Field mapping](/cms_trial/space/SPM/1918700586/Field+mapping/) page.

### Box-level field-mapping

If tasks in your box belong to more than one Jira project and the projects have separate custom configurations, tasks in that box may behave differently depending to the rules configured for the project they belong to.

1. Open your box in the Gantt or Scope module.
2. Click the **plus** button in the column view.
3. On the modal, click **Field mapping**.

![Accessing box-level Field mapping.](/cms_trial/assets/72c08e5d-2ed8-43ca-8396-2ef8876d3ae2.png)

Alternatively:

1. Click **App settings** (wrench icon in the top-right corner).
2. From the dropdown, select **Field mapping**.

A **Field sync configuration** modal displays.

![Field sync configuration modal inside a box.](/cms_trial/assets/4171583c-997e-4660-928e-227b03caaee0.png)

On this modal, you can:

- Restore default settings.
- Reset settings to default.
- Customize settings.

### App-level field mapping

You can also configure field mapping at the global configuration level.

1. Click **App settings**.
2. On the dropdown, mouse over **App configuration** and select **General**.

Default field-mapping rules apply to all tasks in BigPicture boxes unless a custom project configuration overrides them.

![Field mapping page in App settings.](/cms_trial/assets/5fbd81ce-68fd-44af-9f72-6fdbd53e41ca.png)

### Field mapping scenarios

The table below presents the most popular field mapping scenarios.

| **Field mapping** | **Description** |
| --- | --- |
| Start Date = Start Date  End Date = End Date | Dates in BigPicture are synchronized with date in Jira (the default mode). |
| Start Date = Not synchronized  End Date = Not synchronized | Dates in BigPicture are not synchronized with dates in Jira. |
| Start Date = Original Estimate  One-way sync = Start Date  End Date = End Date | Changes made to the Original Estimate field update the Start Date field. |
| Start Date = Start Date  End Date = Original Estimate  One-way sync = End Date | Changes made to the Original Estimate field update the End Date field. |
| Start Date = Start Date  End Date = Time Spent + Remaining Estimate  One-way sync = End Date | Changes made to the Remaining Estimate field can update the End Date field.  Time logged on a task can update the “End Date” field. |

You can also synchronize the Start Date and End Date fields with different fields, for example, Due Date.

## Rules for editing Start Date, End Date, and Duration Working Days

When task dates are calculated from estimates, the Start Date field is updated. When you set a new Start Date, a task is moved. The task duration (Original Estimate) remains the same.

- Changing the Start Date (11/Apr → 10/Apr) moves a task, and the Original Estimate remains unchanged:

![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/e5269046-8cc8-475a-b219-725684bba0c6.png)

- Changing the End Date (13/Apr → 12/Apr) resizes a task, and the Original Estimate is changed (-1 MD):

![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/4c4969d8-f3ac-4562-8336-2bdbec37004d.png)

- Changing the Duration Working Days field (3d → 1d) changes the End Date (-2 days) and the Original Estimate (-2 MD):

![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/e081f355-7065-4e17-bee6-757e7ec02b31.png)

## Rules for editing Original Estimate

When the Start Date or End Date is synchronized with the Original Estimate field, task dates update based to changes made to the Original Estimate field.

- The Start Date is synchronized with the Original Estimate: Changing the Original Estimate (3d → 4d) changes the Start Date.

![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/e3d6e828-3766-4979-bc03-31476babd483.png)

- The End Date is synchronized with the Original Estimate: Changing the Original Estimate (3d → 4d) changes the End Date.

![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/b687a8b1-cb5f-485c-a223-45e289596bde.png)![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/4cf9ce02-9eba-486a-a768-c064e1b2a2dc.png)

When the Original Estimate field is set, the Remaining Estimate field is overwritten, provided no time has been logged on the task.

The mechanism does not work the other way around. Editing the Remaining Estimate field never overwrites the Original Estimate field.

## Rules for editing Time Spent + Remaining Estimate

Synchronizing the End Date with the Time Spent + Remaining Estimate field activates the mechanism that adjusts task dates to the time logged on a task.

The End Date is calculated based on information provided by the person performing the task, that is, the time logged for the task and the data entered in the Remaining Estimate field.

Example:

- You set the Remaining Estimate to 3 MD. You can also fill the Original Estimate field (the Original Estimate will overwrite the Remaining Estimate field as long as no time has been logged on the task yet).

![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/76b01887-a58a-4361-a025-26b324a794a0.png)

- You start working and spend 1 MD on a task. The Remaining Estimate changes from 3 MD to 2 MD. The Original Estimate and task dates remain unchanged.

![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/2d002feb-7ea9-4357-854e-71661037702c.png)

- You spend another 3 MD on a task (the time allocated to a task is exceeded by 1 MD). The Remaining Estimate value changes from 2 MD to 0. The task's End Date changes (by 1 MD). The Original Estimate remains unchanged, so you can check the task's initial estimate.

![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/a6febf76-9ae1-4e0a-88d7-e22f2aefada5.png)

- If you need to spend 1 MD more to complete a task, you can modify the Remaining Estimate field (for example, in Jira) by entering 1 MD. Then the End Date updates automatically.

![Partial screenshot of the task list and Gantt timeline.](/cms_trial/assets/960eef21-64bd-45d2-a29c-7cf0d2f742a1.png)

## Milestones

The Original Estimate and Remaining Estimate fields for a milestone are always 0.

## Tasks without dates

It is not required for tasks to have start and end dates defined.

### Rules for deleting and assigning dates

If the mechanism for calculating task dates based on the estimate is enabled:

- Deleting one date for a task removes the other date (otherwise, Bigpicture would recalculate the deleted date based on the entered estimate).
- Adding one date to a task with an estimate but no start or end dates results in the other date being calculated for that task.

### Rules for deleting Original Estimate and Remaining Estimate

- Removing the value from the Original Estimate field will also clear it from the Remaining Estimate field, provided no time has been logged on the task. If there is time logged on a task, the Remaining Estimate field is not cleared.
- If the Start Date is synchronized with the Original Estimate field, clearing the Original Estimate field deletes the Start Date (otherwise, BigPicture would recalculate the removed estimate based on task dates).
- If the End Date is synchronized with the Original Estimate field, clearing the Original Estimate field deletes the End Date (otherwise, BigPicture would recalculate the removed estimate based on task dates).
- If the End Date is synchronized with the Time Spent + Remaining Estimate field, clearing the Remaining Estimate field deletes the End Date (otherwise, BigPicture would recalculate the removed estimate based on task dates). If time is logged on a task, the End Date field is calculated based on that time.