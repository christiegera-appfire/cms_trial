# Add Time Dialog

7pace Timetracker's *Add Time* dialog features smart search and keyboard support and can be configured in three modes: Timeframe, Duration, or a combination of both.

The *Add Time* dialog box displays when you click **Add Time** or when you edit time on the Monthly, Timesheet, or Times Explorer pages. You can also add time directly from the work item form.

The *Add Time* dialog features a modern design consistent with Azure DevOps (ADO) user interface. It includes keyboard support and the ability to:

- Quickly select specific work log durations (0.5h, 1h, 2h, 4h)
- Mark tracked time as billable.

![Add Time dialog showing the work item search, date, time entry fields, and activity options.](/cms_trial/assets/324f927c-a755-4a84-98ac-2d0dab62839d.png)

The user name displayed at the top of the *Add Time* dialog defaults to the user who is signed in on the Monthly and Timesheet pages. On the Times Explorer page, depending on the role configured in **Settings** to add/edit time, a user may be able to click in this field and select another user to add or edit a time entry.

To display search results, begin typing a work item name or number. If you hold the pointer over a work item in the **Search work items** results, the work item hierarchy and project name display inside a tooltip.

![Search work items results in the Add Time dialog showing matching work items with a tooltip showing the hierarchy and project name.](/cms_trial/assets/c5895169-959c-4975-9a85-c469956d05ef.png)

If a 7pace Timetracker administrator enables **Prevent Time Entry Against Closed Items** in **Settings** > **Rules**, a `This work item is closed` message displays if you try to add time to a closed work item.

Beginning with 7pace Timetracker version 5.42.0, additional search filters allow you to filter items based on attributes.

Beginning with 7pace Timetracker version 5.44.0, administrators can [set global/default filters for the whole organization](/cms_trial/space/7TFA/1253540033/General+Settings/).

Additional filter options can be displayed by entering a forward slash in the work item search field.

![Filter menu in the Add Time dialog showing the available search filter options.](/cms_trial/assets/dcf12416-e2ea-4eec-b906-612f30978262.png)

Once you select a filter, choose a value.

![Filter by Status selected in the Add Time dialog with Active and Approved options shown.](/cms_trial/assets/08d606b5-630c-466c-bfd3-d5b70dfed626.png)![Filter by Status selected in the Add Time dialog with Project, Status, and Type options shown.](/cms_trial/assets/dcf12416-e2ea-4eec-b906-612f30978262.png)

The applied counter filter increments based on the number of filters applied.

![Filter counter indicating the number of active search filters in the Add Time dialog.](/cms_trial/assets/51c51230-d17c-45e9-964f-7bd9ca71a905.png)

Click the counter to see a list of applied filters, and click the **X** to remove a filter.

![List of active search filters with options to remove individual filters.](/cms_trial/assets/d140c550-7b47-4cf8-bfc7-b18a406fa0db.png)

Filters are applied when searching by keywords, and filters are ignored when searching by ID number.

After selecting an open work item, the calendar opens and defaults to today’s date. Depending on how your system is configured, you may or may not be able to select a time beyond the present date.

![Add Time dialog showing the date selection field for a work item.](/cms_trial/assets/5d3a6be9-7d6c-4100-ace9-229d276f6ce7.png)

Also, depending on how your system is configured, you may or may not be able to switch between **Timeframe** and **Duration** mode.

With **Timeframe** enabled, the *Add Time* dialog displays as shown in the following image.

When you change the **From**, **To**, or **Duration** fields, the corresponding fields also update and reflect the text input in the first field.

![Add Time dialog in Timeframe mode with From, To, and Duration fields.](/cms_trial/assets/412c8068-e0bb-4604-bc46-4ed0d4ee42b3.png)

With **Duration** mode enabled, the *Add Time* dialog appears similar to the following image:

![Add Time dialog showing the duration field.](/cms_trial/assets/f288876e-9a4d-4ec9-b867-3bf74479ce84.png)

With **Allow Both Modes** enabled, a toggle button displays, allowing you to toggle back and forth between the duration and timeframe methods.

![Add Time dialog with the toggle for switching between Timeframe and Duration modes.](/cms_trial/assets/6ee821d6-f4ad-4dd4-a251-6ece4717d2cb.png)

After completing the timeframe section, select a corresponding **Activity Type** and add a multi-line comment. Depending on your system settings in **Settings**>**Rules**, the **Work Item**, **Activity Type**, and **Comment** fields may or may not be required.

![Add Time dialog showing the required Work Item, Activity Type, and Comment fields.](/cms_trial/assets/08d2958f-ad55-41b7-882f-af218aab7844.png)![Add time dialog showing Comments field left blank.](/cms_trial/assets/6ee821d6-f4ad-4dd4-a251-6ece4717d2cb.png)

If a required field is blank, a notification displays next to each field that must be completed.

![Validation messages displayed for required fields that have not been completed.](/cms_trial/assets/b4608091-d449-4301-8997-d6b8fc0e59a9.png)

After completing all required fields, click **Save**.