# Timesheet

Filter by current project, iteration, or your items. On 7pace Timetracker's keyboard-optimized Timesheet page, use blue cells to add and submit time.

## Overview

The Timesheet page provides an alternate method of viewing, managing, and entering your work time details on a weekly basis. Time you've tracked displays with the work items associated with that time listed in rows, and the days of the week presented in columns. The design of the page allows you to view the work items you've tracked or entered time on during a given week, the level of effort assigned to PBIs, features, and epics, the total time you've tracked for all work items, as well as the total hours logged on a work item on a given day or for the current week. Like an Excel spreadsheet, each cell in the Timesheet table can contain single or multiple worklogs.

### Timesheet Filters Bar

![Timesheet_Filters_Bar.png](/cms_trial/assets/4474a17f-a53c-4e3c-8a2b-8e1a2a0f09c8.png)

In an effort to optimize performance on the Timesheet page, some changes have been made to the original page filters to reduce page load time, starting with Timetracker 5.1. If the DevOps organization is large, it creates requests that take a long time for DevOps Services to get information on all projects and all Iterations within those projects and then all work items within those iterations. In order to see the View by This Week's Iterations option, please ensure that the Current Project filter is checked/enabled. This will show all iteration work items, but only for the current project. You can also filter by My Items Only.

- All filters disabled - With no filters checked, the page will display only work items that you have already tracked time on during the selected week. Results will display on the page quickly, as only those work items on which you have tracked time will show.
- Current project selected - With Current Project enabled, the results will show only items from the currently selected project (work items with time tracks from different projects will be filtered out). Therefore, page results may display even faster.
- View by This Week's Iterations is ON - With this option enabled, the system will search for and add all active iterations and all work items of those iterations to the Timesheet results, in addition to building and processing its relations tree. This filter may slow page load time if you have a large project and a lot of active iterations/work items.

This filter is available only if the Current Project filter is checked.

- My Items Only is selected - With this filter enabled, the system will filter out the previous request and will display work items that are assigned directly to you. This significantly reduces the number of work items and decreases the load time of the page.

This filter is available only if the **Current Project** filter is checked.

- Show items from ... is enabled - With this option enabled, the page shows work items from previous weeks even if there are no tracks assigned to these items in the displayed week. This makes the process of filling your timesheet easier if you work on the same items for multiple weeks. Once enabled, you can choose to show items from 1 week, 2 weeks or 4 weeks prior to the current week.

### Blue Highlighted Cells

- You might notice that some cells within your timesheet are highlighted with a bold blue background. This means that during this period, the corresponding work item had an In progress state and was assigned to you, the current user. This makes it easy to add your time at the end of any given week (see number 17, below).
- Rows highlighted with a light blue background indicates that there are items without worklogs during this week; they are displayed because the Show items from previous weeks option is enabled.

### Add Time

You can add, edit, and delete (and even submit) time in a variety of ways on this page, which are outlined in more detail, below. Any changes or additions made on the Timesheet page are fully integrated with the rest of Timetracker and DevOps Server/DevOps Services.

### Keyboard Optimization

The Timesheet page is also keyboard-optimized. Just by using the Tab, Enter, and arrow keys on your keyboard, you can navigate everywhere within the timesheet, and add or edit your time. For additional and more detailed information on Keyboard Shortcuts and on the Timesheet page in general, please scroll below.

## Timesheet View

![Timesheet_View.png](/cms_trial/assets/8ad20938-7ade-4591-a9ab-d26efc2afde0.png)

| **Number** | **Description** |
| --- | --- |
| 1 | Add Time  Clicking on this opens the Add Time dialog box, which can be configured in different modes: Timeframe, Duration or Mixed mode.  An administrator can configure different modes on your behalf under **Settings** > **Rules**. |
| 2 | Date range of the current week   - Click the ▢ icon to display the previous week. - Click the ▢ icon to display the next week.   If you are viewing a week that is not the current one, the Current Week link is enabled. |
| 3 | +/-  You can expand or collapse the items that display on the page by one level for a more concise or more detailed view. |
| 4 | Current Project  Filters the page results to the current project only. Enabling this allows you to also view and/or select the selections View by This Week's Iterations (choose On or Off) and when you turn View by This Week's Iterations to On, you also have the option to enable the filter My Items Only. |
| 5 | View by This Week's Iterations  Turning this On filters the page by the current week's iterations. This will show all iteration work items for the current project. This action also displays the My Items Only checkbox.  If View by This Week's Iterations is off, then only your items with worklogs remain. |
| 6 | My Items Only  With this On, the page is filtered by current project, By Iterations view and by items assigned to the user. You can then easily view and add your time to the items that have been assigned to you. With this selection turned Off, the page populates with the items assigned to the whole team. |
| 7 | Image — asset pipeline pending Image  The effort value assigned to PBIs, features, and epics. |
| 8 | Image — asset pipeline pending Image  The total time that you have tracked for the work item up until the present time. |
| 9 | The [Unmapped macro: inline-external-image — no content to fall back on]  When you click this icon, the Add Time dialog box opens with the worklog details. Here, you can add, edit or delete worklogs and it fully integrates with the rest of Dev Ops Server/Services and 7pace Timetracker.  If you make any changes, click the **Save** button to have those changes reflected on the timesheet.  For single worklogs per work item ID per day, you can directly edit or delete a worklog in the table cell, similar to an Excel spreadsheet. Simply double-click within the cell and start typing the new time from your keyboard. To delete the worklog, go to that cell and press the **Delete** key from the keyboard. |
| 10 | The time that you tracked or added for the work item on that day. |
| 11 | The ▢ icon indicates that you have multiple worklogs for that work item ID on that day.  When you click this icon, the Add Time dialog box opens and displays the list of worklogs for that work item. The Add Time dialog box is unique to the Timesheet page. In this dialog box, you can view multiple worklogs, make worklogs as billable or non-billable, and add, edit or delete worklogs. Any changes made are reflected throughout the rest of DevOps Server/Services and 7pace Timetracker. Add_Time_1.png If you make changes, click the **Save** button and these changes will be reflected on the page.  When there are multiple worklogs, you cannot edit or delete the worklogs directly in the cell by double-clicking the cell. Instead, the Add Time dialog box will open and you can make the necessary changes to the entries there. |
| 12 | Bold blue cells  Blue cells within the Timesheet table highlight Tasks, Bugs, User Stories and PBIs that are assigned to the current, logged-in user. It highlights only days when these items were In Progress (or a similar state, depending on your specific template).  If your data and sprint backlog is in good shape, the user only has to fill in the blue cells at the end of the week.  Please note that if a particular task is assigned to you until just Wednesday during a given week, for example, and then for the remainder of the week, that task is assigned to a different team member, your timesheet will only be highlighted in blue for that task until Wednesday. |
| 13 | Week is in progress/Submit for Approval  The status of the current week's timesheet (Week is submitted for approval displays if you have already sent your timesheet to your manager).  Submit for Approval  The button to submit your timesheet for approval displays when you hover over Week is in progress. A pop-up window will then display to allow you to choose your approval manager. Once your timesheet is submitted, this button will then display as Week is submitted for approval. Hovering over this will allow you to Revoke submission any time before your manager approves your timesheet.  Once your manager approves your submitted timesheet, the Timesheet table becomes read-only for that week. If you open the Add Time dialog box, all worklogs will display in read-only mode. |
| 14 | Image — asset pipeline pending Image  The total time that you spent on each work item during that week. |
| 15 | Total  The total time that you spent for each work item on each day in the week. |
| 16 | Show items from previous week / previous 2 weeks / previous 4 weeks  This option displays work items from previous weeks, even if there are no tracks assigned to these items in the displayed week. This makes filling the timesheet easier for users who work on the same items for more than one week. Items from previous weeks are highlighted by a light blue color within the Timesheet grid. |
| 17 | Light blue rows  Some work item rows are highlighted in light blue to indicate that the Show items from option is enabled. This means that these work items don't have worklogs assigned during the current week, but do have worklogs on the previous 1, 2, or 4 weeks, depending on the setting. |
| 18 | Show parents / Hide parents  This dropdown control allows you to choose one of two modes:   - Show parents - for every work item that is shown on the page, the entire hierarchy, up to the top parent item, is also displayed - Hide parents - parents/hierarchies are hidden |

## Keyboard Shortcuts

The following table lists the keyboard shortcuts that you can use on the Timesheet page to quickly perform various operations.

| **Shortcut Keys** | **Description** |
| --- | --- |
| Ctrl + Del | Removes the worklog from the Add Time dialog box. |
| Ctrl + S | Saves the worklog entries in the Add Time dialog box. |
| Tab key  Left, Right, Up, Down arrows | Easily navigates within in the Timesheet table and Add Time dialog box. |
| Enter | In the Timesheet table:   - If the cell is empty or contains only one worklog, the table cell turns to a text editor when you click Enter within it . You can then add or edit time details. - If the cell contains multiple worklogs, clicking Enter in the cell opens the Add Time dialog box. You can then add, edit, or delete your time. |
| Del | - Deletes the single worklog entry from the table cell. - Opens the Add Time dialog box for multiple worklogs. - In the Add Time dialog box, deletes the worklogs details. |
| Esc | - Cancels the operation. - Closes the Add Time dialog box without saving any changes. |

## Add Time

The Timesheet page allows you to add your time on a weekly basis. You can:

- Click the Add Time link at the top left of the Timesheet page and use the Add Time dialog box to enter your time details.
- Double-click within a table cell and add time directly within that cell.
- Click the▢or▢icons within the table cells and use the Add Time dialog box to enter your time details.

If Prevent Time Entry Against Closed Items is enabled under **Settings** > **Rules**, you will see This workitem is closed when you hover over a corresponding cell:

![Add_Time.png](/cms_trial/assets/40ead6cf-9e70-4be5-937b-e6502fa86aee.png)

### Add time with the Add Time link

1. On the **Timesheet**page, click the **Add Time** link.

2. Fill in the fields that display that your admin has configured in Settings.

3. Click the **Save** button.

![Add_Time_With_Time_Link.gif](/cms_trial/assets/a78c1734-e26c-42ec-a44c-eedc7b92486a.gif)

### Add time directly within the Timesheet Table

1. Double-click in an empty or single-time entry table cell where you want to add or edit time.

The cell becomes an editable textbox.

- Enter your time in `HH:MM` format.
- Use the arrow keys to select hours and minutes.

2. Press **Tab** or **Enter** on your keyboard to save the time entry.

### Add time with the Add Time list editor

You'll notice that the Timesheet table features icons (▢ or ▢ ) in its table cells. The ▢ icon indicates either no time entry or just a single time entry in that cell. The ▢ icon indicates there are multiple time entries in that cell.

1. Within a cell, click ▢ or ▢ .

The Add Time list editor, which can only be opened from within the Timesheet table, displays. The Add Time dialog box shows multiple time entries (you can add up to five time entries here).

The ID and name of the work item for which you are adding time displays, as well as the weekday and date on which you are adding time.

2. Click in an empty row to add a new worklog.

A new empty row automatically displays under the current one (up to 5 entries).

The Total time of all the entries also displays.

(Click the x icon at the end of a row to delete the row/entry.)

3. Add the following into each corresponding cell within the new row:

- Length: The duration of your work.
- Start: The start time of your work.
- Activity Type: Displays when enabled in Setting. You can categorize your time entries by the activity types created by your administrator.
- Comment: Any extra information relevant to your time entry.

4. Click **Save**.

![Add_Time_Within_Timesheet_Table.gif](/cms_trial/assets/c20f0e6e-431b-4d5f-b82f-9dea924c7f34.gif)

## Edit and delete time

If a cell in the Timesheet table contains a single worklog (

[Unmapped macro: inline-external-image — no content to fall back on]

), you can click directly in that cell and delete the worklog using just the delete key on your keyboard. Clicking within a single worklog or blank cell also turns it into a text editor, so you ad▢ )d or edit time directly in the cell, also using your keyboard. If a cell contains multiple worklogs (▢ ), the Add Time text editor box opens when you click Delete on your keyboard, allowing you to delete worklogs one-by-one.

You can also delete single or multiple worklogs by clicking on the

[Unmapped macro: inline-external-image — no content to fall back on]

or ▢ icons within a cell, which opens the Add Time text editor box. This allows you to delete worklogs with the Remove Row (▢ ) icon.

If a user is tracking time and edits (removes) the worklog currently being tracked by the Windows Client or Timetracker Web Client, the system will automatically stop tracking.

Also, if Prevent Time Entry Against Closed Items is enabled under **Settings** > **Rules**, you will see This workitem is closed when you hover over a corresponding cell.

1. In the Timesheet table, navigate to a table cell with a single worklog (

[Unmapped macro: inline-external-image — no content to fall back on]

) and click within the cell.

2. From your keyboard, press the **Delete** key.

The time entry is deleted immediately.

3. Press **Enter**.

The deletion is complete.

4. Now, navigate to a table cell with multiple worklogs (

[Unmapped macro: inline-external-image — no content to fall back on]

) and press the **Delete** key.

The Add Time text editor box displays.

5. Click the **Remove row** (

[Unmapped macro: inline-external-image — no content to fall back on]

) icon on the worklog you want to delete.

The time entry/row is removed.

6. Click the **Save** button.

The deletion is saved.

7. You can also delete time on the Timesheet page by clicking on either a single-time entry (

[Unmapped macro: inline-external-image — no content to fall back on]

) icon or a multiple-icon entry (▢ ) icon.

This causes the Add Time dialog box to display.

8. Click the **Remove row** (

[Unmapped macro: inline-external-image — no content to fall back on]

) icon on the worklog you want to delete.

The time entry/row is removed.

9. Click the **Save** button.

The deletion is saved.

![Edit_&_Delete_Time.gif](/cms_trial/assets/d3cc1d0a-6f10-4918-a275-2147bbc66982.gif)

## Submit and revoke time

### Submit time

1. Click the icon beside Week is in progress.

2. Click **Submit for approval**.

3. Select your approval manager from the Send for approval to dropdown and then click the blue Send for approval button.

The timesheet is submitted for approval. The week's status and button change accordingly.

### Revoke time

4. (Optional) Hover over the Submitted for approval icon if you want to make changes to your submitted timesheet, before it is approved by your manager.

5. Click the blue **Revoke submission** button.

The status of the week changes to Week is reopened. The timesheet is revoked and you can now make changes to it.

![Submit_&_Revoke_Time.gif](/cms_trial/assets/921c5123-ed26-44c5-bad0-13412d98e02b.gif)