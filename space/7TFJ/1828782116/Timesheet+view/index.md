# Timesheet view

7pace Timetracker has a *Timesheet* view for tracking and editing time. To access this view, click **Apps** > **Timetracker** > **Timesheet**. The Timesheet view lets you enter time for a week and has several keyboard shortcuts that make time entry quicker.

**Note**: Timesheet view is limited to the logged-in user. It cannot be used to view or report on worklogs entered by other users. To report on worklogs from multiple users, see the [Times Explorer view](/cms_trial/space/7TFJ/1920729127/Times+Explorer+view/).

## Watch the video

Video transcript:

7pace Timetracker has a timesheet view for entering and editing time. To access this view, click Apps > Timetracker. Then, in the left-hand pane, select Timesheet. Here, your time displays for a single week with a row for each issue or time entry you've entered. To add time, simply select a cell to open the time entry dialog. Hit Enter to save your changes. To add time for a new issue, click the + Add time button in the upper right corner. To edit an entry, click it in the timesheet grid. The Worklogs menu displays where you can edit the Duration, Comment, and other custom fields, or you can add a new worklog to the issue for that same day. To delete a worklog, click the entry in the timesheet grid to open the dialog and click Delete. Please note that no confirmation dialog will be shown when deleting worklogs this way. To add time that isn't associated with a ticket, for example, a one-on-one meeting with your manager, click + Add time to create a new entry, but leave the issue field blank. The comment field will be used for the row title. In summary, 7pace Timetracker's Timesheet view can be used to quickly track, edit, and delete time on a weekly basis.

## Timesheet view

### Access

7pace Timetracker has a *Timesheet* View for entering and tracking time. To access this view, click **Apps** > **Timetracker**. Then, in the left-hand pane, select **Timesheet**.

![user-MenuTimesheets.png](/cms_trial/assets/157e8512-6cc7-4112-92cf-30c061d7b7ad.png)

### Displayed information

Until you enter time for a week, the Timesheet view will be blank and display a button in the upper right corner, **Add Time**. Click the button to log work; after a single log has been added, the Timesheet view will display a grid for all work logged in that week. Each row on the grid represents an issue to which you have logged work, with the time for that issue displayed under each day.

![user-TimesheetView.png](/cms_trial/assets/beaf9eeb-10a1-4ff6-90d2-bffc6be9822b.png)

If you enable the [BigPicture integration](/cms_trial/space/7TFJ/2106556524/BigPicture+integration/), capacity appears in the header:

![timesheet-capacity.png](/cms_trial/assets/d2584683-ff48-4b5d-8c19-fdb6b3a73e1d.png)

## Timesheet tools

Timesheet view includes several tools for sorting, filtering, and reporting on worklogs. These tools are all located at the upper right of the screen and include:

- **Total time** - the total time for all worklogs for the week is displayed above the data grid.
- **Time period** - The date range for the visible timesheet.
- **Current Week** - Click to jump to the timesheet for the current week.
- **Show items** - Display items from previous time periods in the current timesheet view. See **Show items** below for more information.   
  [note icon] **Note**: This does not add the time logged in previous worklogs to the current timesheet display and does not change the totals for work items, days, or the current time period.
- **Add Time** - Click to add a new worklog.

Additionally, you can also check time summed up from many cells by highlighting them by dragging a cursor through the cells:

![time-sheet-highlightinh.png](/cms_trial/assets/8d36a00d-21c3-45ba-8ec9-6c9d1207efc8.png)

## Show items

The **Show items** menu allows you to list worklogs from previous timesheets to the current view; this is a convenient way to add additional worklogs to work items without needing to search for them individually. The Show items menu has three options:

- **Items hierarchy** - switch this toggle on to see nesting of the work items.
- **Assigned to me** - Display work items assigned to the current user even if they have not had worklogs added within the selected period of time.
- **Recently tracked on** - Display only work items that have had worklogs added within the period of time selected under **Timeframe**.

  - **From previous week** - Display work items with time logged in the week previous.
  - **From previous two weeks** - Display work items with time logged in the two weeks previous.
  - **From previous month** - Display work items with time logged in the four weeks previous.

**Note**: Activating options from the **Show items** menu only adds those work items to the list of items on the left side of the Timesheet view. It does not add the time logged in previous weeks to the total column, or to daily or weekly totals.

**Warning**: Turning on **Show items** will only display seven (7) additional work items. This is due to an Atlassian limitation.

## Keyboard shortcuts

There are several keyboard shortcuts that enable you to enter time quickly on the Timesheet view.

### Timesheet grid

- **Tab/Shift+Tab** to move between cells on the Timesheet grid.
- **Arrow keys** to move between cells on the Timesheet grid.
- **Enter** to open the Worklog menu for the selected cell.
- **Del** to remove all entries for the selected cell.

### Worklogs menu

- **Tab/Shift+Tab** to move between fields in the menu.
- **Arrow keys** to increase or decrease the **Duration** field.
- **Space** to activate the **Billable** toggle or the **Add worklog** button.
- **Esc** to close the menu and accept all saved changes.

### Add time in Timesheet view - New issue

![monthly-view-add-time.png](/cms_trial/assets/60721f6f-7d24-42fe-a487-e2f1e61287ed.png)

Adding time to an existing issue is as straightforward as selecting the cell for the worklog you want to create. To create a worklog for a new issue:

1. click **Add Time** in the upper right corner of the window. The *Add Time* window opens.
2. In the left panel you can check smart suggestions for Jira issues to use, based on you previous time logs.
3. Use the **Search** field to select a new issue. Alternately, you can leave this field blank if the worklog should not be created for a specific issue. The **Comment** field is used as the worklog title (the row title in the Timesheet view).
4. Edit the **Date** as needed.
5. To create a worklog for a specific time period, check the **Timeframe** toggle and enter the **From** and **To** times. If you do not need to record a specific time of day, enter a **Duration**.
6. Use the Duration buttons to add blocks of time as needed.
7. Add a **Comment** and any other fields as required by your teams' process.
8. Click **Save**.

### Update time in Timesheet view

Use the following steps to edit or delete worklogs:

1. Select a cell in the Timesheet grid. Click the cell or highlight the cell using the arrow keys and press **Enter**. The **Worklogs** dialog opens.
2. Edit the worklog as needed, or click **Add worklog** to create a new entry for that issue on that day.
3. To delete a worklog, click the **Delete** button ( ▢ ).

   ![user-TimesheetsWorklogDialog.png](/cms_trial/assets/7a10dae4-71f1-4308-9944-a414c5841d81.png)

Changes to existing entries will be saved as you move from field to field.

**Note**: Deleting a worklog using the above method does not include a check for you to confirm deletion, and this cannot be undone!