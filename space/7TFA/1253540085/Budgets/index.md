# Budgets

Create unlimited budgets, assign them to iterations, work items, or individual workloads, and export the tracked time data to Excel.

## Introduction

### Budgets Add Value

From an economic perspective, the reporting or billing of efforts spent in development does not always follow sprints, releases, or product backlog items. Your team members create a large number of worklogs every minute of every day, and it can be challenging to manage these worklogs. Additionally, you may want to bill only specific hours to a client or report those internally.

The *Budgets* page allows you to simply and easily create unlimited budgets, so you can then assign the tracked time you want to those budgets. You can include or exclude items from a budget or assign a budget to an object, such as:

- Releases
- Iterations/sprints
- Items like PBIs, bugs, impediments
- Work Items
- Single Worklogs

When you assign a budget to any of the above objects, the child objects also inherit that budget. If you assign a different budget to one of the child objects, the parent inheritance is then broken, and the new assignment of this item is inherited by its children. Therefore, if you assign a budget to a release, all work that is tracked to items in that release will be counted in that budget, automatically and instantly. If you want to set an exception for a child item, for example, a product backlog item in a sprint, just assign a different budget to that child item (like "Do Not Bill").

You can also assign a specific work item to a budget directly from the work item form in the *7pace Timetracker* tab (for more information, click [here](/cms_trial/space/7TFA/1253539860/Work+item+form/)).

### The Budgets page components

![Budgets_Page_Components.png](/cms_trial/assets/c450c8a4-1b8f-4e40-aa10-abfb16d92211.png)

| **No.** | **Description** |
| --- | --- |
| 1 | Click here to create a new budget. |
| 2 | The list of created budgets.The [Unmapped macro: inline-external-image — no content to fall back on] icon indicates that the budget is open and can be assigned to iterations and items. The ▢ icon indicates that the budget is closed and is no longer actively assignable. |
| 3 | Click this button to populate and display budgets in the list that once existed but are now closed. |
| 4 | Click **Export** to export tracked time details for selected projects. |
| 5 | The name of the budget with a **Comment** added underneath as additional information. |
| 6 | The toolbar with options to edit, delete, and close a selected budget. |
| 7 | The list of objects *included* in the selected budget. Objects can be iterations, work items, or worklogs.  You can assign individual time tracks to any budget from the *Times Explorer* page only, and these tracks are listed in this section of the *Budget* page. To do this, select the checkbox(es) of one or more time tracks on *Times Explorer*, and then, click the **Assign Budgets** button. A popup dialog box is displayed, allowing you to assign the specific tracks of time to the budget of your choice. You can then see these tracks of time displayed under **Time Tracks** on the *Budgets* page. The *Included* section displays the worklogs to which the budget is assigned. |
| 8 | The **Add** button allows you to add objects in the **Included** list of a budget. |
| 9 | The list of objects excluded from the selected budget. Objects can be iterations, work items, worklogs, etc.  You can assign individual worklogs to any budget from the *Times Explorer* page only and these worklogs are listed in this section of the *Budget* page. To do this, select the checkbox(es) of one or more time worklogs on *Times Explorer*, and then, click the **Assign Budgets** button. A popup dialog box is displayed, allowing you to assign the specific worklogs to the budget of your choice. You can then see these worklogs displayed under **Time Tracks** on the *Budgets* page. The *Excluded* section displays the worklogs of the work items that are included in the budget but that worklog has a different budget assigned. |
| 10 | The date and time when the selected budget was created. |
| 11 | The total hours planned for the selected budget. |
| 12 | The total hours tracked for work items included in the selected budget. |
| 13 | The **Exclude** button allows you to add objects to the **Excluded** list of a budget, thus removing them from the budget and adding them to another. |

### Adding a new budget

1. On the 7pace Timetracker menu bar, click **Budgets**.

2. In the left panel, click the **New Budget** button.

![Add_New_Budget.png](/cms_trial/assets/63c2c7d7-46c5-423c-9aa3-33df78b7e59c.png)

The *Budget* dialog box is displayed.

![Add_New_Budget_Window.png](/cms_trial/assets/d94160b9-1517-4d8c-819f-ceaf915d1999.png)

3. In the **Budget Name** field, enter the name of the budget.

4. In the **Planned Hours** field, enter the number of hours planned for the budget.

5. (Optional) In the **Comment** field, enter any additional information you want to add to the budget.

6. Click the **Save** button.

### Including iterations or work items in a budget

Once a budget has been created, you can directly add objects like iterations or work items to the budget in the **Included** section of the page. The items in the **Included** list indicate that for all these items, any tracked time is logged to and included in that budget. The **Tracked** field at the top of the page then displays the total time tracked for all included items in that budget, be it an entire iteration, just specific work items, or even a single worklog.

1. In the far left pane, click the budget name to which you want to include specific iterations or work items.

![Include_Iterations_in_Budget.png](/cms_trial/assets/d75204ca-6000-4711-8f7a-d4016ba8e4de.png)

The budget details are displayed in the right pane.

2. In the middle-right *Included* section of the page, click the **Add** button for **Iterations** or **Work Items** that you want to *include* in the budget.

![Add_Iterations_in_Budget.png](/cms_trial/assets/c615dc0f-5943-4284-aa21-64b701775ee1.png)

#### INCLUDE ITERATION IN BUDGET dialog

![Include_Iterations_in_Budget_Window.png](/cms_trial/assets/3f2fd7f0-4184-4bfb-a1be-7e2dc8ab0bb7.png)

In the *INCLUDE ITERATION IN BUDGET* dialog box, click the **Select Project** drop-down list and select a project.

Click the **Select Iteration** drop-down list and select the iteration/sprint that you want to add.

#### INCLUDE WORK ITEM IN BUDGET dialog

![Include_Work_Item_in_Budget.png](/cms_trial/assets/e13cb41e-4e0c-4e88-9208-f1bac73a2838.png)

In the *INCLUDE WORK ITEM IN BUDGET* dialog box, enter the work item ID or title in the **Search for Work Items** text field/search box.

In the resulting list, select the work item that you want to add.

Click **Ok**.

### Excluding iterations or work items from a budget

You can also specifically set iterations and work items to be *excluded* from certain budgets.

The items in the **Excluded** list indicate that for all these items, the tracked time is not calculated in that budget. The **Tracked** field at the top of the page does not include the tracked time for any of the excluded items in that budget. Usually, you can use the excluded items list to remove certain items from the budget. For example, you can include a parent iteration or a PBI in the budget but want to exclude certain iterations or child work items from the budget.

You must add an iteration to a budget in the **Included** section *first*, before then excluding certain iterations or child items from the budget.

1. In the left pane of the *Budgets* page, click the budget to which you want to exclude specific iterations or work items.

2. In the far-right **Excluded** section of the page, click the **Exclude** button for iterations or work items that you want to exclude from this budget.

![Exclude_Iterations_from_Budget.png](/cms_trial/assets/d8feebc6-d5a1-4404-846a-1760f831f57a.png)

#### EXCLUDE ITERATION FROM BUDGET dialog

![Exclude_Iterations_from_Budget_Window.png](/cms_trial/assets/40653d7a-2227-4fec-bae2-7a99992f22fb.png)

In the *EXCLUDE ITERATION FROM BUDGET* dialog box, click the **Select Project** drop-down list and select a project.

Click the **Select Iteration** drop-down list and select the iteration that you want to exclude from the budget.

Click the **Select Another Budget** drop-down list and select another budget to which the iteration is to be assigned.

#### EXCLUDE WORK ITEM FROM BUDGET dialog

![Exclude_Iterations.png](/cms_trial/assets/ace0d7d1-dc85-4f64-8a3e-f6492e05234a.png)

1. In the *EXCLUDE WORK ITEM FROM BUDGET* dialog box, enter the work item ID or title in the **Search for Work Items** dropdown.

2. In the resulting list, select the work item that you want to exclude from the budget.

3. Click the **Select Another Budget** drop-down list and select the budget to which you want to exclude the selected work item, and click Ok.

From the *Iterations* page, you can also assign iterations or work items to a budget. See [this article](https://appfire.atlassian.net/wiki/x/bYO3Sg) for more information.

### Adding individual worklogs to a budget

You can assign budgets to one or many worklogs to override the inherited budget. You can only do this on the *Times Explorer* page.

1. On the *Times Explorer* page, check/select every worklog that you want to assign to a specific budget or to a budget that is different from the inherited budget.

![Add_Individual_Worklog_to_Budget.png](/cms_trial/assets/05bd6521-605f-48f0-8b56-edb32d31697b.png)

Note that additional menu options display/are enabled, including **Assign Budget**, **Billable**, **Change Activity Type**, and **Delete**.

2. Click the **Assign Budget** button.

3. On the resulting pop-up dialog, select the budget to which you want to assign these worklogs, and then click the **Assign to Selected** button.

![Add_Individual_Worklog_to_Budget_Assign_Selected.png](/cms_trial/assets/352a61d5-0f73-47c4-a57d-0b6a92b7b053.png)

Now, when you go to the *Budgets* page, these worklogs are displayed under the *Included* - **Time Tracks** section.

![Budget_Page_Time_Tracks.png](/cms_trial/assets/eed2ba63-3346-4e2e-ac94-b6b31fb86e16.png)

Similarly, you can also exclude worklogs that have been automatically assigned via an iteration or work item, by moving those specific worklogs on the *Times Explorer* page to a different budget. These worklogs are displayed in the *Excluded* - **Time Tracks** section of the *Budget* page.

### Adding a budget from the work item form

![Add_Budget_from_Work_Item_Form.gif](/cms_trial/assets/4ce3b76b-8ed3-4b63-97cc-436f84935ba4.gif)

1. Open the work item form and click the *7pace Timetracker* tab.

![7pace_Timetracker_Tab.png](/cms_trial/assets/96e513f1-e061-446c-a176-6b849eec7974.png)

In the upper-right corner, you can see **Budget** information. In this example, this work item task has inherited the budget from its parent user story.

![7pace_Timetracker_Tab_Budget.png](/cms_trial/assets/2bd6509d-504c-453d-838f-5baecfc2e12d.png)

2. Click the **Budget** dropdown.

![7pace_Timetracker_Tab_Budget_Dropdown.png](/cms_trial/assets/30c956e0-47de-4af2-a4ea-1177c045532b.png)

All budgets that have been created from the *Budgets* page are displayed as options.

3. Click a different budget.

![7pace_Timetracker_Tab_Budget_Dropdown_2.png](/cms_trial/assets/7bbfb362-d80c-4c80-a46a-a58f134b7961.png)

Page refreshes, confirmation message displays, and newly-assigned budget displays.

4. Navigate to Timetracker’s *Budgets* page and click the budget name to which you just assigned the work item.

![Budget_Page_Name.png](/cms_trial/assets/bcc7f70b-d06b-4e5a-99ad-66669379552e.png)

The work item now displays within the budget's *Included* section.

### Editing a budget

1. From the list of budgets on the left panel of the *Budgets* page, select the budget that you want to edit.

2. On the toolbar on the right panel of the page, click the **Edit** button.

![Edit_Budget.png](/cms_trial/assets/21fe837c-8ef0-4f4c-ab4e-1b48c3e87aad.png)

The budget *CREATE/EDIT* dialog box is displayed.

![Edit_Budget_Window.png](/cms_trial/assets/0b4e68ef-498e-4cd5-91ac-061cb1d72cd0.png)

5. Change the values in the required fields.

6. Click the **Save** button.

### Opening and closing a budget

On the *Budgets* page, beside each budget in the list, the

[Unmapped macro: inline-external-image — no content to fall back on]

icon indicates that the corresponding budget is open. The ▢ icon indicates that the budget is closed.

1. If you do not see any closed budgets, click the **Show closed** icon (▢) on the toolbar.

After clicking the **Show Closed** icon, closed budgets are displayed in the existing list of open budgets.

2. On the toolbar:

- Click the **Open** button to open a closed budget.

![Open_Budget.png](/cms_trial/assets/a1e5bb83-d146-432a-b660-8b6aa60f4806.png)

- Click the **Close** button to close an open budget.

![Close_Budget.png](/cms_trial/assets/38cc0a41-551e-4456-b637-37dbafb22b99.png)

The icon and the color of the budget name changes according to the action that you perform.

### Deleting a budget

You cannot delete a budget that contains tracked worklogs. If this is the case, the **Delete** button is grayed out.

1. From the list of budgets on the left panel of the *Budgets* page, select the budget you want to delete.

2. Click the **Delete** button.

![Delete_Budget.png](/cms_trial/assets/c7753851-d047-482d-ad25-8b49e5e24128.png)

A confirmation dialog box is displayed:

![Delete_Budget_Confirm.png](/cms_trial/assets/73536f57-4e40-4373-a379-46f576072658.png)

3. Select the **Delete** button again.

The page refreshes and the budget is deleted.

### Exporting worklog details from the Budgets page

You can export worklog details from the *Budgets* page. By default, 7pace Timetracker exports these time details in the form of an Excel file.

1. On the 7pace Timetracker menu bar, click **Budgets**.

2. In the left pane, click

[Unmapped macro: inline-external-image — no content to fall back on]

.

![Export_Time_Report.png](/cms_trial/assets/fea32477-8d03-4e16-a316-dca3abb91cf1.png)

The *EXPORT TIME REPORT* dialog box displays.

3. Click in the **From** field and select the start date from when you want to export the worklogs.

4. Click the **To** field and select the end date up to which you want to export the worklogs.

5. (Optional) Select one of the following options to export your worklog details:

- [Add the sum of effort/story points to topmost parent items](#Add%20some%20of%20effort/story%20points%20to%20top-most%20parent)
- [Group identical data for the same work item ID by dates](#Group%20totals%20of%20all%20tracked%20time%20with%20same%20work%20item%20ID%20together%20per%20calendar%20day)
- [Include Billable and Billable Hours columns in the Export](#Include%20Billable%20and%20Billable%20Hours%20Columns%20in%20Export)

6. In the **Projects** list, check the projects for which you want to export the worklogs.

In the projects list, you can only view the projects to which you have access/permissions.

7. Click the **Get Report** button.

The report is downloaded as an Excel file with extension `.xlsx`.

### Add sum of effort/story points to top-most parent items

When you select this option, 7pace Timetracker first adds the effort/story points of all child work items to the effort/story points of the respective parent work item and then exports the work items. With this calculation, the exported Excel file displays the effort/story point details as the total of the effort/story points of the parent work item and all corresponding child work items.

Timetracker also adds a new column—**Top Work Item Story Point**—to the exported Excel file. This column displays the total number of effort/story points of all child work items and their parent work item.

If you do not choose this option, Timetracker separately exports the worklog details of the parent and and child work items.

Selecting this option might take additional time to populate results, as 7pace Timetracker needs to calculate the efforts/story points of all child work items and their parent items.

**Exported Excel file without selecting this option**

The exported Excel file only contains the **Parent Work Item Story Point** column and not the**Top Work Item Story Point** column. The **Parent Work Item Story Point** column displays the efforts/story points of all work items.

![Export_Excel_Without_Option.png](/cms_trial/assets/e8bd9d22-eb8c-4655-af89-7b841f8c9052.png)

**Exported Excel file with this option**

The exported Excel file contains the additional **Top Work Item Story Point** column. This column displays the total of the efforts/story points of the parent work item and all corresponding child work items.

![Export_Excel_With_Option.png](/cms_trial/assets/1199134e-b53f-4732-8795-2e29b6536dbd.png)

### Group totals of all worklogs with the same work item ID together per calendar day

If, on a particular date, you work on the same work item at different times during the day, 7pace Timetracker separately records each time you work on that work item and for how long.

When you select this option, 7pace Timetracker exports your worklogs by grouping the time of the work item that you tracked on a particular date, but at different times on that date, *together*. The exported file displays the work item only once, with the date and time details grouped into the **Record Date** column. In the Excel file, the **Tracked** column displays thetotal time tracked for the same work item at different times.

When you export your worklogs without selecting this option, the Excel file separately displays the date and time details of the same work item, tracked at different times during that date, in separate rows.

**Exported file without selecting this option**

The exported Excel file contains separate entries for the same work item. The **Start**, **End**, and **Tracked** columns display the work log details separately for each work item.

![Exported_File_without_Option.png](/cms_trial/assets/729c1d3b-6dd8-4869-9bfc-8c6b4a7befce.png)

**Exported file with this option**

When you select this option, the exported Excel file contains the **Record Date** column instead of the **Start** and **End** columns.

![Exported_File_with_Option.png](/cms_trial/assets/0cf79135-b7c7-41fc-b3a8-edefbc007049.png)

### Include Billable and Billable Hours Columns in Export

Checking this option before you export worklog data populates your resulting Excel file with the **Is Billable** (**TRUE** or **FALSE**) and **Billable Period Length** columns included. On the *Times Explorer* page, you can select certain worklogs and mark them as **Billable**. Then, when exporting on the *Budgets* page and choosing this option, those marked as **Billable** are now shown as **TRUE** in the corresponding column with the time included.

![Include_Billable_Hours.png](/cms_trial/assets/d1857c19-d469-4fd4-95f0-ad9db14b50ae.png)

## Related articles

- [Times Explorer Page Overview](https://appfire.atlassian.net/wiki/x/rYC3Sg)
- [Iterations Page Overview](https://appfire.atlassian.net/wiki/x/bYO3Sg)