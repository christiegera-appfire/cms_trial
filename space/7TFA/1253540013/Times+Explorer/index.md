# Times Explorer

View team worklogs, pick columns, group data, save your personal layout and then export to Excel on 7pace Timetracker's Times Explorer page.

### Introduction

Even with a small team, you can quickly log hundreds or even thousands of worklogs each month. 7pace Timetracker's Times Explorer page allows you to organize all your worklogs in a way that makes the most sense for you.

When an administrator adds a user to the Team user role, they can access a special version of Times Explorer that displays the logged-in user's personal data only. In addition, to see the Person filter, the user must have at least the Product role assigned. This filter is not available for Team role users. To check on your users' permissions, you can go to the Settings page of **Timetracker** > [**User Management**](/cms_trial/space/7TFA/1253539946/Misc%3A+User+%26+Subscription+Management/).

Roles higher than team will see the \*worklogs for the entire team.

*\*A worklog is created any time you start tracking time and then stop tracking time = one worklog.*

On this page, you can:

- Add time (manually as a single time entry)
- Assign budgets (singularly or in bulk with selected rows)
- Add, edit and save as many of your own "Layouts" as you wish

|  |
| --- |

- Click on editable blue text/links on the page for additional functionality
- Mark worklogs as Billable or Non-Billable
- Delete selected rows (singularly or in bulk with selected rows)
- Cherry-pick which columns display on the page from the Timetracker database AND your Azure DevOps project
- Ability to see when every worklog was created: when added, optional "Created Date" column displays on Times Explorer, Budgets Export and API.
- Export (worklog details to Excel)
- Import (external time tracked outside of Timetracker from Excel)
- Group worklogs (based on different fields like months, work item ID or users)
- Sort and filter columns (see exactly what you want to see on the page, how you want to see it)
- Resize and move columns (get a better look at the data that is important to you)
- Remove filters (resets all grid filtering/sorting/grouping)
- Assign activity type categories to your worklogs (when enabled by your admin)

Please note that Azure DevOps Activity and 7pace Timetracker Activity Types are separate entities.

### Times Explorer Page: First Glance

When making changes to worklogs in the grid below, if you receive a message informing you that changes could not be made or that only certain rows updated, this is because you either don't have permissions to the associated work item to which the worklog belongs, it is locked, or it no longer exists.

![Times_Explorer_Page.png](/cms_trial/assets/4aa2c3a0-fbc1-43e2-bec1-75990f9d07a0.png)

| **ID** | **Description** |
| --- | --- |
| 1 | New Layout  Clicking on this button allows you to create a new customizable layout that will be available to you each time you navigate to the Times Explorer page: New_Layout_Name.png Once you name your layout, you can customize it to show exactly what data and columns you want to see on the Times Explorer page. You can save your column order, column width, filters, groupings, sorting, etc. You can also click on an existing layout, make changes to it, and then click New Layout, and your changes will be saved as a whole new layout. |
| 2 | List of Times Explorer Layouts  When you first navigate to the Times Explorer page, you will see a list of pre-configured Layouts hat display for every user (the screenshot, above, shows pre-configured layouts for an administrator user). You can edit, rename, and/or delete these pre-existing Layouts as you choose. If you have already configured your Times Explorer page prior to the new Layouts feature being introduced, you will see an additional layout added to the list displayed in the above screenshot; My Layout will show the Times Explorer page as you last customized it before the Layouts feature was added.  Pre-configured layouts are created and display per user and depending on the role that user has when they first visit the Times Explorer page. If a regular user accesses the page but then gets increased permissions (like an administrator, for example) later, the admin-specific pre-configured layouts are not added.  To reset the default layouts on the page, simply delete all existing layouts and reload the page and the default layouts will appear.  The Layout section is collapsible. By clicking the < icon above the New Layout link, the list of layouts can be collapsed to give you more real estate on the Times Explorer page. Layout.png By clicking the > icon, the list of your Layout displays again. |
| 3 | Add Time  Clicking on this opens the Add Time dialog box so you can manually add time for completed work. |
| 4 | The date range or timeframe of worklog details currently displaying on the Times Explorer page. The grid pre-loads the defined number of rows into the browser's memory for the quickest response time.  By default, the page displays the worklog details for the timeframe that you set in **Configuration** > **Timetracker System Settings**. This timeframe is the total number of months prior to the current date. For more information, see this section of **Settings** > [**Rules**](/cms_trial/space/7TFA/1253540033/General+Settings/). |
| 5 | Change Dates  By clicking this link, you can temporarily change the timeframe of displayed worklog details on the Times Explorer page. To learn how an admin can permanently change this, click [here](/cms_trial/space/7TFA/1253540033/General+Settings/).  Timetracker calculates the timeframe in the following way:   - **Start date**   `{Today} - {Time frame set in <%PRODUCTSERVERNAME%>} = month = 1st day of that month`  `Example, {8/29/2017} - {3} = 5/1/2017`   - **End date**   The date of the last recorded time in the Timetracker database.  If today's date is `8/31/2017` but the Timetracker database contains the last recorded date as `8/29/2017`, then the Times Explorer page displays `8/29/2017` as the end date.  If you change the To or From date range on the calendar picker, you must specifically click on a date within the calendar because changing the month or year automatically de-selects any date from the calendar. Once you select a specific date within the calendar and click ok, your selected date range will display in the results. |
| 6 | Project dropdown list  You can cherry-pick/check which projects you want to display on the Times Explorer page or use the following quick filters:  All Projectsfilter selects only DevOps projects and displays work items with work item IDs associated with them.  Select All filter will display all work items from all projects, including non-DevOps items.  When you navigate away from the page, Timetracker remembers your selection when you return. |
| 7 | Iteration dropdown list  You can cherry-pick/check which iterations you want to display on the Times Explorer page. When younavigate away from the page, Timetracker remembers your selection when you return. The Iteration column filter lists only the iterations where time was tracked on work items within those iterations. |
| 8 | Columns  When you click this button, the Select Columns to Display box appears, allowing you to pick not only columns from the Timetracker database, but also custom columns from your Azure DevOps project.  Some columns (Budgets, Billable and Billable hours) are visible only to user users with Product (and higher) role.  Click **Save** to maintain any changes to the list of columns and the specific details of tracked time you want to display on the Times Explorer page as part of your specific Layout.  The columns on Times Explorer page's worklog details table are movable by simply dragging them to display in the order that you prefer.  They are also resizable by simply hovering your mouse to the right of each column header until a double-ended arrow icon displays and then dragging that to the right until the column is the width you prefer. You can also double-click the right column border to auto-resize the column to the maximum size of the content in that column. Auto_Resize.png Each column allows you to simply click in the field below the column header and enter or select the value you want to filter by and display in the table details.  You can also sort worklogs according to certain fields or columns by clicking the field name in the table header to sort the time details. Click the field name once to sort the time details in ascending order. Click the same field name again to sort the time details in descending order. The column header displays the appropriate icon to indicates the sorting order.   - Up arrow indicates the column is sorted in ascending order. - Down arrowindicates the column is sorted in descending order.   You can also sort by multiple columns. Press Shift + click to sort additional columns after the first one. Press Control + click in a table heading to remove the sorting of a column once multiple columns have been sorted. |
| 9 | Export  You can export worklogs to an Excel file. Before exporting, you can filter the worklogs on the page to suit your needs and then export only those worklogs displaying on the page after matching the filter criteria.  For more information, see [Exporting Worklogs](/cms_trial/space/7TFA/1253540013/Times+Explorer/). |
| 10 | Import  You can import worklog details that you have tracked outside of 7pace Timetracker, on the Times Explorer page.  For more information, see [Importing Worklogs](/cms_trial/space/7TFA/1253540013/Times+Explorer/). |
| 11 | Reset Filters  Clicking this button causes the page to once again display all worklogs, unfiltered. |
| 12 | Rows Filtered  At the top-right of the Times Explorer grid, the total number of worklogs listed and the total number of hours tracked for the listed worklogs display. If you have filtered the columns on the page to only display certain worklogs, this field displays the total number of filtered worklogs and the number of hours for those filtered worklogs.  For example, if the total number of worklogs before you apply filters is 1500 and the total number of hours for these worklogs is 1,150 hours, then this field displays 1500 (1,150 h). If you then filter the columns to view fewer worklogs, and the new total number of filtered worklogs is 750 and the total number of hours associated with those filtered worklogs becomes 350 hours, then this field displays 750 (350 h).  For more information, see [Changing the Timeframe of Displayed Worklogs](/cms_trial/space/7TFA/1253540033/General+Settings/). |

### Times Explorer page: A second look

![Times_Explorer_Page_Second_Look.png](/cms_trial/assets/fb7f61d9-5e43-4e48-9687-8ee77a25ee10.png)

| ID | Description |
| --- | --- |
| 1 | With each worklog (row) that you select, this field updates - the first number displays the total number of worklogs you have checked/selected and the number in parenthesis displays the total time tracked in hours for those selected worklogs. For example, if you select three rows of worklog details and there is a total of 2.6 hours associated with those selected worklogs, this field will display as 3 (2.6h). If you have no rows selected, it displays as 0 (0 h), as depicted in the screenshot above. |
| 2 | The Select All/Deselect All checkbox. |
| 3 | The checkboxes by each row on the page allow you to cherry-pick the worklogs you want to view (with each worklogs you check or uncheck, the rows-selected and hours associated to those rows update in the 0 (0 h) field at the beginning of the header row - see #1, above). You can also click anywhere on a row on the page and that row is automatically selected and the corresponding checkbox is checked.  When a row is checked, #4, #5, #6, and #7, below, display as options. |
| 4 | Assign Budget  This selection only displays when a row or rows are selected/checked. This opens a dialog box that allows you to assign a budget to the checked worklogs.  By default, each work item inherits the budget assigned to the corresponding iteration. However, you can assign different budgets to a specific work item.  The Budget column displays assigned budgets in the following ways:   - Budget Name: This indicates the name of the budget assigned. - NA: This indicates that there is no budget set for the worklogs. - (Processing ..): This indicates that the budget for the worklog has not yet been computed. It appears when adding worklogs of the recently added work item. - Budget name displayed in blue, preceded by an exclamation mark (!): This indicates that the budget assigned to the work item is different than the budget assigned to the iteration of that work item. The work item is not inheriting the budget from the iteration.   The Budgets filter list displays the following filter criteria:   - (No Budget Set): This criteria displays the work items that are not assigned to any budget. - (Custom Budget per Time): This criteria displays the work items that do not inherit the budget assigned to the iteration. These are the work items to which you have assigned a different budget. - (Inherited): This criterion displays all work items that inherit the budget assigned to the corresponding iteration. - (!<budget\_name>): This criterion displays all work items to which you assigned a budget different than the iteration budget. All such custom budget names are listed only if you have assigned them to a work item. For example, !DistributeMe budget is listed only if you have assigned the DistrubuteMe budget to a work item.   For more information, see [Budgets Page Overview](/cms_trial/space/7TFA/1253540085/Budgets/) and other articles related to Budgets. |
| 5 | Billable  This selection only displays when a row or rows are selected/checked. You can cherry-pick/select specific worklog details on the page, click on the Billable button, and then choose Mark as Billable. These specific worklogs can then be billed to your customer. Alternatively, you can also click this Billable button again and choose Mark as Unbillable.  Once selected and marked as Billable, the billable hours data is then available when you create reports via the Times Explorer export, Budgets export, and the Reporting API export process. |
| 6 | Change Activity Type  This selection only displays when a row or rows are selected/checked and when your administrator has enabled the Activity Types feature in Configuration. When both of these preconditions exist, the Times Explorer page displays a Change Activity Type button that allows you to select multiple worklogs and assign activity types to them in bulk. Additionally, Activity Type also displays as a selection when you click on the Columns button. Adding this column allows you to assign activity types to your v one-by-one, or filter and group by activity types like you do with other columns on this page.  For more information, see our [Activity Types](/cms_trial/space/7TFA/1253540033/General+Settings/)article. |
| 7 | Delete  This selection only displays when a row or rows are selected/checked. You can select multiple rows and delete worklogs in bulk with the Delete button. |
| 8 | You can click anywhere in the Times Explorer grid, on a row, and the row will automatically be checked/highlighted. |
| 9 | Editable blue links display where further action can be taken by the user. Click on a blue highlighted link and you will be prompted to take additional action if desired. |

### Make changes to Layouts

When you make edits or changes to any of your Layouts (for example, moving a column to a different location, filtering certain rows to view specific time details, or picking certain columns to display on the page), those changes are immediately saved in the Timetracker database. If you open the Times Explorer page on a different PC or browser, you will still see the page in exactly the same state as you left it. If you make any changes to an existing layout, the "Save" button will display by the name of the layout:

![Make_Changes_to_Layout.png](/cms_trial/assets/970d6c84-f4ca-4734-9367-966cedbf2b9e.png)

You can then choose to **Save** by simply clicking the button, or you can click the down arrow icon to **Rename**, **Delete**, or **Undo Changes**.

![Rename_Delete_Undo_Changes_Options.png](/cms_trial/assets/2179a1f9-2e09-481d-b3db-ea2a03042dfa.png)

If you make changes to a layout and then navigate away from it without saving, you will receive the following prompt:

![Unsaved_Changes.png](/cms_trial/assets/47ac475f-a3df-4c84-85ef-c01ac5bd36b0.png)

### Work Item form integration

On the 7pace Timetracker tab of the work item form, under Work Item, a calendar icon displays next to Hours tracked on that work item.

![Work_Item_Form_Integration.png](/cms_trial/assets/5c19597a-779f-4087-ad68-6124be9b38cd.png)

Click the calendar to open details on the Times Explorer page:

![Calendar_Details.png](/cms_trial/assets/0ed1e110-9577-49bf-85b9-ac72c055c3f9.png)

### Grouping

Grouping is a powerful feature within the Times Explorer page that allows you to filter and group fields within existing workload data in a more concise but in-depth way. Each column header within the Times Explorer table contains different fields in its dropdown list (for example, the "Month" column header contains the calendar months in the dropdown during which time was tracked). By clicking on the grouping symbol, in the top-right corner of each column header, you can add the column - and subsequently, the fields - you want to group, in the details panel below. The column you group first is the top-level group, and every subsequent grouped column then displays one level below that. You can then get a filtered snapshot of the number of rows and the totals within each group that you create.

1. In the Times Explorer table, hover your mouse pointer over the top-right corner of the column header you want to be the top-level group.

![Grouping.png](/cms_trial/assets/4ce0edc2-c746-4dc1-a0c7-bd2cc3e6d649.png)

2. Click the **Add group** icon. The page filters and displays the time details of just that column, grouped accordingly (in this example, below, the "Person" column grouping displays the various Timetracker users and the worklogs associated with them.

![Add_Group.png](/cms_trial/assets/44f41d9f-18db-4407-bf9e-69e403969817.png)

You can group time details only for the fields that display the "Add group" icon by the column header. You can group time details for multiple fields by clicking the respective column headers. Once you group the time details of a specific column, the field names in the column header display the grouping icon without having to hover over it.

3. (Optional) Click the group header icon arrow to expand the group and view the worklogs in that group.

4. (Optional) Click the group header icon arrow that points down to collapse group and hide the worklogs in that group.

5. (Optional) Click the **Remove Filters** button or simply click the grouping icon again to remove the grouping and display all worklog details in the table.

### Add a new worklog

1. On the Times Explorer page, click the **Add Time** button.

![Add_New_Worklog.png](/cms_trial/assets/f26d1a48-0b0d-4bb5-bac0-e76af864d358.png)

The system displays the Add Time dialog box.

The Add Time interface is based on the mode that you set in **Settings** > **General** >**Rules**. For more information, see [Settings: General: Rules](/cms_trial/space/7TFA/1253540033/General+Settings/)

If a 7pace Timetracker administrator has enabled Prevent Time Entry Against Closed Items in **Settings** > **Rules**, if you try to add time to a workitem that is in closed status, the system will prevent you from saving.

The top username field defaults to the logged-in user. As an administrator, this field will display to you as a droplist list that contains team members who have access to 7pace Timetracker. Users with lesser permissions, such as Team will only see their own name here.

2. Enter the appropriate values in other fields.

3. Click the **Save** button.

### Edit a worklog

1. In the worklog details table, click or hover over the pencil icon for the worklog or row you want to edit.

![Edit_Worklog.png](/cms_trial/assets/6a69471a-81af-4431-a1b4-b50cf186f12f.png)

The pencil icon is enabled only for the worklogs that the logged in user has tracked/added/imported unless you have a user role that has been configured to edit/delete the worklogs of others. If the pencil icon is disabled/grayed out next to a worklog, that means that the workitem to which it belongs is closed and a 7pace Timetracker administrator has enabled Prevent Time Entry Against Closed Items in **Settings** > **Rules**.

![Edit_Worklog_Closed_Item.png](/cms_trial/assets/86219b72-ec8d-4dce-a650-affcacc5cf96.png)

If you try to bulk-edit worklogs by selecting multiple checkboxes/worklogs at the same time and some of the workitems of those worklogs were closed, the system will inform you that only "x number of worklogs out of <insert total> were updated".

The system displays the "Edit Time" dialog box.

2. Change the values you wish to change in the required fields.

3. Click the **Save** button.

If a user is tracking time and edits (removes) the worklog currently being tracked by the Windows Client or the Timetracker Web Client, the system will automatically stop tracking.

### Delete a worklog

You can only delete the time details that you have tracked on the system. However, an administrator can enable the option in the Settings page to allow another user role to edit or delete worklogs as well. For more information, see [Settings: General: Rules](/cms_trial/space/7TFA/1253540033/General+Settings/)

You can delete time in two ways on the Times Explorer page.

1. To delete multiple worklogs simultaneously, in the worklog details table, select the worklogs that you want to delete by clicking on the checkboxes by the specific rules.

![Delete_Worklog.png](/cms_trial/assets/7a1a468f-ee12-4f90-82f4-f1313c7c2b32.png)

The Delete button is enabled on the toolbar.

2. You can either click the **Delete** button or you can also click the bin icon for the worklogs you want to delete.

The bin icon is enabled only for open worklogs that the logged in user has tracked unless you belong to the user group that has been configured to edit/delete time. If the bin icon is disabled/grayed out next to a worklog, that means that the workitem to which it belongs is closed and a 7pace Timetracker administrator has enabled Prevent Time Entry Against Closed Items in **Settings** > **Rules**. If you try to bulk-delete worklogs by selecting multiple checkboxes/worklogs at the same time and some of the workitems of those worklogs were closed, the system will inform you that some of the worklogs can't be deleted and once you continue, you'll receive a message that only "x number of worklogs out of <insert total> were deleted".

If a user is tracking time and edits (removes) the worklog currently being tracked by the Windows Client or the Timetracker Web Client, the system will automatically stop tracking.

### Change displayed time worklogs temporarily

By clicking the Change Dates link on the Times Explorer page, team members can temporarily change the date range of displayed worklog details. If that team member visits another page within Timetracker, however, and returns to the Times Explorer page, that temporary setting will return to the configured setting. This configured date range can be changed more permanently by an administrator within Timetracker's settings. We will show you how to do both, below.

1. On the 7pace Timetracker menu bar, click **Times Explorer**.

2. Click the **Change Dates** link.

![Change_Dates.png](/cms_trial/assets/3c48ad02-42a5-4314-91a4-9a53701834e3.png)

Side-by-side calendars display:

![Calendar_Side_to_Side_Display.png](/cms_trial/assets/3ed2467b-15d4-4118-b2f5-f5f674a26b81.png)

3. On the left-side calendar, select the From date.

4. On the right-side calendar, select the To date.

5. Click the **OK** button.

The date range of displayed worklogs is updated temporarily on the Times Explorer page.

### Change displayed time worklogs permanently

The administrator role is required to perform this function.

1. On the **7pace Timetracker** menu bar, click **Settings**> **Rules**.

![Change_Displayed_Time_Worklog.png](/cms_trial/assets/c6e37451-a8eb-473a-9db5-980cc6c808bd.png)

2. Under Times Explorer Preloaded Timeframe, type in the preferred number of months you want to be preloaded on the Times Explorer page prior to the current month.

The page refreshes automatically and the changes are saved. Times Explorer will now always show this date range on the page when you and your team members navigate to that page.

### Single-Assign a budget

On the Times Explorer page, on the row/worklog to which you want to assign a budget, under the Budgetcolumn, click by NA or the name of the already-assigned budget if you want to change it.

![Single_Assign_Budget.png](/cms_trial/assets/521cf34f-5389-4902-8558-3c132dfea520.png)

When the list of budget names populates/displays, click on the budget you want to assign to the work log.

![Single_Assign_Budget_Names_List.png](/cms_trial/assets/10e5713e-ed5f-4a90-b38c-073fb134f9dc.png)

The selected budget is verified and assigned to the specific worklog.

### Bulk-Assign budgets

To assign a budget to multiple worklogs, select multiple rows or worklogs. When you do this, additional menu items display on the toolbar next to the Add Time button, including the Assign Budget button:

![Multiple_Assign_Budget.png](/cms_trial/assets/10b55e30-8ebe-4de6-988a-20c7faf6bd88.png)

When you click the Assign Budget button, the Assign Budget dialog box displays a list of configured budgets.

![Multiple_Assign_Budget_Configure_List.png](/cms_trial/assets/b4301cae-7762-4209-ab4e-6f554dc4e17f.png)

In the Title column, click the budget name that you want to assign and click Assign to selected. The bulk budget assignment confirmation dialog box will display, asking you if you'd like to continue. If a 7pace Timetracker administrator has enabled Prevent Time Entry Against Closed Items in **Settings** > **Rules**, you’ll receive a message from the system that not all worklogs can't be updated.

When you click the Assign button, the Budget column now displays the chosen budget for the selected worklogs (that are not in a closed state).

### Remove a budget

To remove a budget from a worklog, select the worklog/row or highlight it with your mouse. In the Budget column, but still within the same row, click the budget name so that the list of budgets is displayed.

![Remove_Budget.png](/cms_trial/assets/92cb3e9e-25a9-4493-b3b0-599391c04914.png)

In the budgets list, click the [Inherited budget] budget. The previously-assigned budget for the selected time worklog is removed.

If the budget of the parent work item or the iteration is removed, the worklog, which inherits that budget, will display NA in the Budget column.

### Import worklogs

To import worklogs that you've tracked outside of 7pace Timetracker, you simply copy data from the source application (like Excel) and paste it into the Import Times popup window of the Times Explorer page. You then associate each worklog detail to the specific field in the Timetracker database. Once verified, the imported worklogs are stored in our database. Import can be performed via the UI, but it can also be performed by using the workLogs endpoint from our [REST CRUD API](/cms_trial/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3/) and also our [NPM package](/cms_trial/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3/).

If the system finds any errors, the import process will stop and the errors will display for you to correct before attempting to import again.

1. On the 7pace Timetracker menu bar, click **Times Explorer**.

2. On the Times Explorer page, click **Import**.

![Import_Worklog.png](/cms_trial/assets/8bc36af8-6abb-4af4-ab66-03171e66d7cb.png)

The Import Times page displays:

![Import_Times_Page.png](/cms_trial/assets/1b045729-88f4-4cee-bc4d-5fcfac180269.png)

3. Paste the time details that you copied from the source application (Excel).

![Import_Times_Page_Next.png](/cms_trial/assets/ace8a389-3809-4f49-a0a5-4a00a46ba25a.png)

4. Click the **Next** button.

Timetracker analyzes the data that you pasted and displays it in a tabular format so you can properly associate each time detail in the column headers to the appropriate Timetracker field.

![Import_Times_Table_Format.png](/cms_trial/assets/4ec07352-4f7f-48ae-9002-ce30e0ca71ad.png)

5. (Optional) In the far-left column, check the boxes for the time details you want to import. By default, all are selected.

6. Select the Date Format and the Time Format of your preference for the import.

![Select_Date_Time_Format.png](/cms_trial/assets/846b485b-4b46-475b-ac38-9fa66bc673fd.png)

If you'd like to customize or change the format for your import, please find additional information at this link - [Custom Date and Format Strings](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings) - and/or simply use the most popular formats (we used standard .NET Framework DateTime object format settings):

**Basic Format Specifiers:**

mm: minutes

MM: month

dd: day of month

h: hour in format 1-12 without leading zero

hh: hour in format 1-12 with leading zero

H: hour in 24h format without leading zero

HH: hour in 24h format with leading zero

mm: minutes with leading zero

tt: am/pm designator

yyyy: year

**Templates for Date/Time Formats**

| **Date Format** | **Time Format** |
| --- | --- |
| MM/dd/yyyy | h:mm tt |
| dd.MM.yyyy | HH:mm |
| yyyy-MM-dd | HH:mm |

7. Copy-paste the Date Format and Time Format of your choice into the corresponding fields.

8. In the Column Name headers, click the dropdown arrows on each and select the appropriate header names for the time details below.

9. Click the **Import Now** button.

While importing, if there are any issues with the data, those issues will be highlighted and an error message displays.

![Import_Now_Error.png](/cms_trial/assets/bac6f3e2-0e90-4281-9347-5962237b165c.png)

10. (Optional) Check Rows With Errors Only to see just the rows that are causing issues in your import.

11. (Optional) After correcting your errors, if any, click the **Import Now** button again.

Once the time details are successfully imported, you can view these details on the Times Explorer page.

### Export worklogs

You can export worklogs to an Excel file that will have the following naming convention format: `timetracker_<export_date>-<export_time>.xlsx.`

Before exporting, filter the worklogs on the page to suit your needs and then export only those worklogs displaying on the page after matching the filter criteria.

1. On the 7pace Timetracker menu bar, click **Times Explorer**.

2. (Optional) Filter the worklogs as per your requirements.

3. On the toolbar, click the **Export to Excel** button.

The browser downloads the Excel file containing the worklogs shown on the Times Explorer page.