# Times Explorer view

The Times Explorer view allows you to monitor and report on worklogs. To access this view, click **Apps** > **Timetracker** > **Times Explorer**. Here, worklogs are displayed in a table view.

## Watch a video

Review the following video to learn about the features in 7pace Timetracker’s *Times Explorer* view.

Video transcript:

7pace Timetracker includes a tool called the Times Explorer for monitoring and reporting on worklogs. To access this view, click Apps > 7pace Timetracker. Then, in the left-hand pane, select Times Explorer. The Times Explorer view consists of a table listing all of the worklogs for the current view. Views are saved configurations of filters. Views can be used to create reports that you run for any slice of your organization's worklog data, by month or quarter, by project, or even by individual users. To switch between views, use the pull-down menu in the upper right corner of the screen. To create a new view, set the table filters as needed, and then open the Views pulldown, and select Save as new view. There are several tools available to filter your worklog data. These include: Search, which lets you search most fields. Time filter, which lets you filter on common time periods. The Date filter. Column filters, which include tools for nested queries using AND/OR logic, and group filters. Group by settings, which lets you group worklogs by most columns. The Export tool, which saves the workload data as an Excel spreadsheet. Finally, column settings let you control which columns are displayed in your view. Lastly, you can add new worklogs using the Add Time button in the upper right corner. In summary, 7pace Timetracker's Times Explorer view can be used to monitor and report on worklogs, team effort, and project progress. Thanks for watching.

## Times Explorer view

7pace Timetracker has a *Times Explorer* view for reporting and entering time. To access this view, click **Apps** > **7pace Timetracker**. Then, in the left-hand pane, select **Times Explorer**.

![7pace Timetracker showing the Times Explorer option.](/cms_trial/assets/0fa4bcd8-ef03-4529-8243-6bde6a65559e.png)

### Timetracker commands

The *Times Explorer* view includes several commands for monitoring and reporting on worklogs.

![The Times Explorer view showing the search field and the Time, Date, and Columns filters.](/cms_trial/assets/32c597e4-16d5-41f5-a047-6832ebadd4c1.png)

The commands, from left to right, are:

- **Search** - Search using most fields, including Key, Issue Title, Project, Comment, and many others.
- **Time filter** - Filter the displayed worklogs by the selected block of time.

The **Time filter** and **Date filter** work together. Selecting an option from the Time filter will update the values of the Date filter. Selecting a specific date or date range will automatically set the Time filter to **Custom**.

- **Date filter** - Filter the displayed worklogs by a date range. Click to select the starting and ending dates.
- **Column filter** - Filter the displayed worklogs by any **visible** column. See **Filter and Group** below for more information.

**Note**: The column filter can be used to filter the displayed issues by any filter currently visible in the Times Explorer; nearly any issue field can be added to the displayed columns. If you need to filter issues by a different data point, just add that column using the **Customize columns** option!

- **Group by** - Group the displayed worklogs by the selected column or columns.
- **Add time** - Click the **Add time** button to create a new worklog.
- **Export all** - Export all visible worklogs to an XLSX file.
- **Customize columns** - Select which columns are displayed in the Times Explorer table.
- **View selection** - Select which view to display or create a new Private view based on your current configuration. See **Times Explorer Views** below for more information.

## Filter

![user-TimesExplorerFilter.png](/cms_trial/assets/697850da-072d-4be7-9498-d6198242eafe.png)

In the Times Explorer, you can create filters to limit the worklogs that are displayed in the Times Explorer table. This includes:

- A single filter on one column (for example, `A = value 1`)
- Multiple filters combined using AND/OR logic (for example, `A = value 1 OR B = value 2`)
- Filter groups for nesting one or more filters that use their own AND/OR logic  
  (for example, `A = value 1 AND (B = value 2 OR B = value 3)`)

Filters and filter groups can be combined to create complex reports on your team or organization's worklogs. To create a new filter or filter group:

1. Click the **Filter** button ( ▢ ).
2. Select a **Column**, a **Condition**, and set a **Value** for the filter.
3. Click **Add filter** to create additional filters. Select **And** or **Or** to set the logic for additional filters.
4. Click **Add filter group** to create a nested set of filters. Within the filter group, you can add additional conditions using the **Add filter** button for that group.
5. Click the **X** beside any filter or filter group to remove it.

Filter groups will always be evaluated as a unit before individual filters are applied. This lets you create more complex queries when viewing worklogs. For example, if you wanted to see only Epics and Stories for a specific project:

1. For the initial filter, set **Column** to **Project** and select your project under **Value**.
2. Click **Add filter group**.
3. Within that filter group, set **Column** to **Issue Type** and set **Value** to **Epic**.
4. Click **Add filter** within the same group and set **Column** to **Issue Type** and set **Value** to **Story**.

Combine Filters with **Views** to create customized reports you can run whenever necessary!

![user-TimesExplorerGroupBy.png](/cms_trial/assets/fe0812a3-e3cf-4df2-8011-320af3d8dd3e.png)

In addition to filtering worklogs, you can also group worklogs by any visible column in the Times Explorer table. When grouping, the field or fields you select become clickable tiles in the Times Explorer table that work like folders. Worklogs will be grouped in the order of fields selected in the **Group by** menu; use the handles beside the field (pictured right) to reorder the fields. Click **Add new group** to create a new group, and click the **X** beside a group to remove it.

## Group worklogs by columns

You can group the table rows by columns by selecting Group in the table header or by clicking the Group icon in a column header:

![times-explorer-worklog-grouping.png](/cms_trial/assets/420b4e93-c22a-4bd1-9914-dd14a67c4682.png)

Grouping roll the rows into groups based on column. In this example

![times-explorer.png](/cms_trial/assets/70b51991-1a7e-4d1e-a67a-9ca07a8e9c62.png)

## Customize columns

The **Customize columns** menu lets you add or remove columns from your current Times Explorer view and set by which columns the list of worklogs is grouped. The menu consists of three main sections:

- **7pace columns** - The standard fields used in 7pace Timetracker.
- **Jira Columns** - All issue fields in your Jira instance.
- **7pace Custom fields** - Any [custom fields](/cms_trial/space/7TFJ/1355415553/Working+with+Custom+Fields/) your Jira administrator has added to 7pace Timetracker.
- **BigPicture columns** - if the BigPicture integration is turned on, you can choose some of the fields.

Click the section name to expand or collapse that set of fields. Check the box next to a field to show or hide that field in the Times Explorer window. Toggle the **Group** button to group all displayed worklogs by that field. See **Filter and Group** above for more information on grouping.

### Approval Status, Approver

If the [Approvals setting](/cms_trial/space/7TFJ/2651455520/Approval+periods/) in turned on, two additional columns are available to choose: Approval Status and Approver.

### Reorder, resize, and sort columns

You can reorganize the Times Explorer table to display your selected columns in any order and sort your worklogs by any column. Additionally, you can resize any column.

- Click and hold and drag any column to move it.
- Click and drag the divider between column headings to resize that column.
- Click any column to sort by that column.
- Hover over any column and click the **Group** button to toggle grouping by that column.

**Note**: Displayed columns are saved for each private view you create. The columns for the Default view, however, can not be changed.

## Times Explorer Views

Within the Times Explorer, you can save a configuration of columns, filters, and groups as a new View. The views you create are private and only accessible by you. They allow you to create on-demand reports for teams, projects, or even individual users.

The following settings are saved as a View:

- Time filter/Date filter settings
- Column filters
- Group by settings
- Customize columns displayed

To create a new View, or edit or delete an existing View:

1. Within the Times Explorer, configure the filters as needed.
2. In the upper right corner of the screen, open the **View selector**.

   1. To create a new view, click **Save as new view**.
   2. To edit the name of a View, hover over the View to be edited and click the **Edit** ▢ button.
   3. To delete a View, hover over the View and click the **Delete** ▢ button.

7pace Timetracker has a Timesheet view for entering and editing time.