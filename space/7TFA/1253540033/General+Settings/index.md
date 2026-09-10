# General Settings

Customize time formats, global filters, set up pace, remaining time, completed work, time tracking activity checks, add approval managers and activity types.

## Introduction - Time and formats

Under **Settings** > **General** > **Time and Format Settings**, you can configure options such as the time format, first day of the week, first week of the year, and personal date and time formats throughout 7pace Timetracker.

This is what a 7pace Timetrackeradministrator can see when they expand the *Time and Format Settings* section:

![7pace-azure-general-settings.png](/cms_trial/assets/e78d4910-cf09-456e-98b3-34a97f13a9aa.png)

A user can only see the the **Locale (Personal Settings)** section.

### Change the format for time entry

#### Time Format

Administrator Setting

Here, you can select the time format in which you want your time entry to display throughout 7pace Timetracker at anytime. 7pace Timetracker internally calculates the time and appropriately represents it in the selected format.

For the time representation in decimal format, the time interval of six minutes is calculated as one point.

- **"0.0" (rounded)**: This displays the time in a default one-decimal point format. For example, 2 hours and 35 minutes are represented as 2.6.
- **"0.00" (rounded)**: This displays the time in two decimal points. For example, 2 hours and 35 minutesare represented as 2.58.
- **"00:00:00" HH:MM:SS (precise)**: Displays the time precisely in an hours, minutes, and seconds format. For example, 2 hours 35 minutes and 5 seconds is represented as 2:35:05.
- **"00:00" HH:MM (rounded up)**: This format displays the time in hours and minutes. For example, 2 hours, 35 minutes, and 5 seconds are represented as 2:36. In this format, the seconds are rounded up into minutes.

### Change the first day of the week

#### First Day of the Week

Administrator Setting

With the **Approval** feature enabled by default, the first day of the week is also set to Monday. If you are using the **Approval** feature in 7pace Timetracker, you cannot change the current first day of the week since the approval process has data based on weeks. Changing the first day of the week, in this case, resets **Approval**, which means that all data, such as weeks that are approved, pending, etc., fall back into an **In Progress** state. If you do not use the **Approval** feature, you can change the first day of the week, and it will have little effect on your workflow.

For more information, see [Settings: Approval Process Settings](/cms_trial/space/7TFA/1253540033/General+Settings/).

### Change the first week of the year

#### First Week of the Year

Administrator Setting

You can set how you start or view the first calendar week of the year. This is visible on Timetracker pages like *Monthly* or *Times Explorer*.

You can select from the following options:

- **Week containing first day of the year**: The week regarded as the first week of the year is that which contains at least one day of the new year.
- **First full 7-day week in January**: The week regarded as the first week of the year is that which contains 7 full days in the new year.
- **First 4-day week in January**: The week regarded to be the first week of the year is that which contains at least 4 days of the new year.

### Change the date format

#### Locale (Personal Settings)

Non-administrator personal setting

If you do not want to choose **Azure DevOps locale settings** uncheck this selection and choose your own date format from the **Date Format** dropdown under **Locale (Personal Settings)**. This date format now displays throughout 7pace Timetracker.

Time and Formats settings apply to Timetracker fields and interfaces only. Any DevOps specific fields are not formatted by 7pace.

### Change time format

Non-administrator personal setting

If you do not want to choose **Azure DevOps locale settings**, uncheck this selection and choose your own date format from the **Time Format** dropdown under **Locale (Personal Settings)**. This time format now displays throughout 7pace Timetracker.

The Time and Formats settings apply to 7pace Timetracker fields and interfaces only. 7pace does not format DevOps-specific fields.

## Rules

Only a 7pace Timetracker administrator can see the *Rules* section of **Settings**.

Under **Settings** > **General** > **Rules,** if you want to disallow tracking, you can prevent/forbid time entry beyond a certain day by disabling/blocking those days. In the future, you can set tracking details, make adding a work item or comment mandatory when your team members add time, select the mode available on your *Add Time* dialog box when adding time, choose how many months of data load on the *Times Explorer* page, set what role can edit time entries other than the actual user, and you can make any worklogs billable by default.

### Prevent time tracking in the future

#### Tracking Control Settings

**Prevent Time Tracking Beyond Present Day** lets you enable or disable time tracking for days in the future.

![rules-prevent-time-tracking.png](/cms_trial/assets/f3dd4ef5-c58d-4e1c-b76c-b6149a92393f.png)

Here, you can manually type in the day(s) in the future that you want to allow users of 7pace Timetracker to be able to track time. If you set the interval to zero days, users cannot track time beyond the present day. The default interval of one day indicates that you can track time today and tomorrow only.

#### Prevent time tracking on closed Items

A 7pace Timetracker administrator can **Prevent Time Entry Against Closed Items** by enabling the checkbox, highlighted below:

![rules-prevent-time-entry.png](/cms_trial/assets/577fdef7-3d4a-4e03-b025-4747871e5b3c.png)

This checkbox is not enabled by default. A 7pace Timetracker administrator must manually enable it if they wish to restrict time entry for their team on closed items. This prevents users from tracking time, adding, editing, or deleting time on work items closed on the *Monthly*, *Timesheet*, and *Times Explorer* pages, the Azure DevOps work item form, the integrated web app found at the top of each 7pace Timetracker page, and the 7pace desktop app for Mac and Windows. You can set a grace period or amount of time (in hours) after an item is closed so that your team can no longer add, edit, or delete worklogs on that item.

### Make a work item, comment or activity type mandatory

The ability to track time without associating that time with specific work items is set to **ON** by default to allow users to track time on non-work-related or impromptu items. Please select **Always require a work item** if you want all tracked time to be associated with a specific work item ID.

#### Tracking Details

**Always require a work item**

With this option enabled, users can only start tracking or can only add/edit time if a work item is provided for the worklog.

**Always ask for tracking details**

Here, you can require users to enter a comment and/or activity type before tracking commences.

If you set the activity type as required here, this forces users to manually select an activity type every time they add time or start tracking time. Enabling this resets any default **Activity Type** to **[Not Set]** under **Settings** > **Activity Types**.

The logic is that a user must not just use the default or their favorite activity type if activity types are required for time entry and logging. With *Activity Type Required* enabled, it forces users to think about the activity type they want associated with each specific time entry and to make a deliberate choice instead of just using whatever the default is, which could lead to incorrect categorization of activity types when tracking or adding time.

### Set up global filters on the Add time dialog

#### Global filters

As a 7pace Timetracker administrator, you can set default filters for your organization, implementing company-wide tracking rules.

![rules-global-filter.png](/cms_trial/assets/7835ab0f-9278-495a-ae5e-d60a051c3944.png)

You can set up filters according to **Project**, **Status**, and (work item) **Type** that renders specific outcomes in the search results within the *Add Time* dialog.

Global filters do not prevent your users from adding time on items matching the filter; the items just do not appear in the search in the *Add time* dialogue pop-up. Users can still temporarily adjust/remove these filters from the *Add time* dialog search when needed. When the page reloads, global filter settings are renewed. Change the mode on the *Add time* dialog.

Because of existing prerequisites, Global filters are disabled by default in **Timetracker on-premise**. In order to enable the Global filters feature for Timetracker on-premise, please follow the steps below:

1. Ensure that [Advanced Search](https://learn.microsoft.com/en-us/azure/devops/project/search/install-configure-search?view=azure-devops-2022) is installed on your Azure DevOps server
2. Open the `onPrem.appsettings.Dynamic.json` file and set the **Advanced Search Options** to enabled, as such:   
   `"AdvancedSearchOptions": {"IsEnabled": true}`
3. Restart the 7pace Timetracker application pool in your server IIS settings

#### Management of worklog settings

The following describes each mode and how the *Add Time* dialog displays, depending on how you configure it.

To configure the *Add Time*dialog box to display in the mode of your choice, you can choose from **Timeframe** mode, **Duration** mode, or a **combination** of the two.

**Timeframe Mode**

When you select/configure **Timeframe Mode**, the *Add Time* dialog opens. It allows you to enter time with **From**, **To**, and **Duration fields**.

Note that on the *Times Explorer* page, the name field can be a dropdown containing other team members' names, depending on your user role and configured settings.

![add-timeframe-mode.png](/cms_trial/assets/3d6b324a-5b43-41ae-8d7f-f9b2a4468343.png)

**Duration Mode**

When you select/configure **Duration Mode**, the *Add Time* dialog opens with just the Duration field to specify the length of time you work.

In this mode, the **From** and **To** fields are not available. This mode is useful when the length of time worked is more important than the timeframe in which you work.

![duration-mode.png](/cms_trial/assets/ad98754e-c8d2-4f84-a856-4229400fe61c.png)

**Allow Both Modes**

When you select/configure **Allow Both Modes**, the *Add Time* dialog opens, displaying a **Timeframe** toggle switch. Enabling the toggle switch option displays both **From** and **To** fields on the **Add Time** popup dialog (see screenshots below), in addition to the **Duration** field. Disabling the toggle switch only displays the **Duration** field.

![add-time-both-modes.png](/cms_trial/assets/bd7782c9-4f66-4133-a14f-d87614c3edeb.png)

### Select number of months that load on Times Explorer page

#### Times Explorer Pre-loaded Timeframe

On the *Times Explorer* page, data is pre-loaded into the memory of the browser. Here, you can select how many months, by default, is to be preloaded into memory, from 1 - 12 months.

### Select role that can edit/delete others' time

#### Editing Time

**Allow time to be edited by role other than user**

This option allows you to give permissions to a specific role, and therefore, user(s), to edit other users' worklogs. Select thecheckbox and from the dropdown list, select the role to which you want to give permissions for this.

Any worklogs edited by anyone other than the team member who originally tracked the time will show as **Edited by** on the *Times Explorer* page (when this specific column is selected from the *Columns* link to display on the grid). Additionally, when you hover over a new icon placed on a time track on the *Monthly* page’s details panel, you can see the name of the user who edited the track (specifically what has been changed is not displayed).

### Set time tracks to billable by default

**Billable Settings**

With the **Billable as Default** checkbox enabled, every new worklog or track of time will be logged as billable (billable time = period length).

## Work item automation

Only a 7pace Timetracker administrator can see the **Work Item Automation** menu option of **Settings**.

When you click the **Work Item Automation** menu option of the **Settings** section, you can control the integration of 7pace Timetracker with the time management capabilities of the DevOps server/services.

In addition to enabling the settings below, in order to make automatic completed/remaining work adjustment work, please ensure the following:

- DevOps services (cloud): Authorize 7pace Timetracker in DevOps services
- DevOps server (on-prem): Set up a valid service account

This is what you can see when an administrator opens the **Work Item Automation** menu option:

![work-item-automation.png](/cms_trial/assets/96a3c64a-bd0b-4d7b-b12c-dd61adb36153.png)

### Pace calculation

**Select the field used for "estimated effort"**

![work-automation-field.png](/cms_trial/assets/39a33305-3349-4000-a80b-3ec911341f88.png)

The value in this field is used to calculate pace. Use the **Select the "estimated effort"** field in the drop-down list to view the effort and pace calculations on the [Iterations](https://appfire.atlassian.net/wiki/x/bYO3Sg) page and in 7pace Timetracker reports.

The Pace in 7pace Timetracker for Azure DevOps measures the correlation between time spent and estimated effort. It is calculated by dividing the hours spent on the task by the effort.

![Pace_Formula.png](/cms_trial/assets/57b9b55b-5b80-40f5-ba7c-519668a90c53.png)

Pace refers to the capacity of work that a team or individual completes. It is a measure of productivity that helps teams understand the complexity of work they can accomplish within a given timeframe. By tracking pace, teams or individuals can predict future performance, make informed planning decisions, and adjust their workload to ensure consistent delivery. This metric is crucial in Agile environments, where it helps to balance workload, avoid burnout, and maintain a sustainable work rhythm.

**Example scenario**

- **Sprint Duration:** 2 weeks
- **Total Time Spent:** 80 hours
- **Total Story Points Completed**: 20 Story Points  
  In this case:

![Pace_Formula_Example.png](/cms_trial/assets/b37111a6-93ed-4736-a8b0-4346efd0333d.png)

This means that, on average, your team takes four hours to complete one story point.

**Usage of pace**

- **Sprint Planning:** Use Pace to estimate how many story points your team can realistically complete in a sprint.
- **Performance Tracking:** Monitor Pace over time to identify trends and make data-driven decisions for improving team productivity.

For additional questions on Work Item Automation, please check the Frequently Asked Questions article: [How to utilize Completed and Remaining work, Original Estimate, Effort, and Pace.](https://appfire.atlassian.net/wiki/x/dIC3Sg)

### Estimated remaining time

**Enable automatic reduction of remaining time for a work item field**

![estimated-remaining-time.png](/cms_trial/assets/f6d41cd2-aded-4471-b20e-67af981f4de7.png)

If **Enable automatic reduction of remaining time for a work item field** is selected, the time tracked in 7pace Timetracker automatically reduces the chosen value in the **Remaining Time** field on your work item form. You can choose from a drop-down list that includes all fields as specified in the Work Item Template (WIT) that can be used with this feature. The field on the work item form remains fully writable by users, so it can be manually adjusted at any time.

For example, if the planned remaining time for a work item is five hours and a developer works for two hours on it, the **Remaining Time** field on your work item form is automatically reduced to three based on the time the developer spent on it.

Note that when the **Remaining time** field reaches zero (0), it will not reduce any further.

### Completed work

**Enable filling in total tracked time for a work item field**

![complete-work.png](/cms_trial/assets/27d3d20a-8b9b-4dd8-a2f0-1502a6815367.png)

If **Enable filling in total tracked time for a work item field is selected**, the time tracked in 7pace Timetracker automatically updates in the **Completed Work** field on the work item form. This field is also fully writable by users, and the value in this field will always be overwritten by 7pace Timetracker with the sum of workloads from the database. You can choose from a drop-down list, which lists all fields as specified in the Work Item Template that can be used with this feature. If you track time on a work item, then the **Completed Work** field is automatically updated with the total time that is tracked or added for that work item by all team members.

For example, if a team member has five hours remaining on a work item, as we mentioned already, and then tracks two hours of time for that work item, the **Completed Work** field is automatically updated to two.

7pace Timetracker uses the **Completed Work** field from the DevOps server/services to display the completed hours for a work item.

![Completed_Work_Hours.png](/cms_trial/assets/37d2aa71-e9a4-420b-aedb-0d761ee5428e.png)

**Overwriting Completed Work:** Before you configure **Completed Work** in 7pace Timetracker's **Settings**, if the corresponding DevOps server/services field already contains a value, then 7pace Timetracker will overwrite that value and keep updating the field based on your tracking and manual time adjustment. There is no option to prevent overwriting the original value in this field.

**Work Item Automation and Custom Fields**: You can create a new, custom field for a specific project in DevOps server/services, similar to the **Completed Work** field. You can then select this new field in 7pace Timetracker under **Settings** > **Work Item Automation** > **Completed Work** dropdown.

### Apply & Copy to Other Projects

**Completed Work** and **Remaining Work** can be configured on a project basis. To apply these settings to multiple projects all at once, click the **Apply to Other Projects** button.

![apply-to-other-projects.png](/cms_trial/assets/dc3b1e19-34cf-4bdb-add0-5a8bdfc08208.png)

This opens the *Apply and Copy to Other Projects* dialog window. Here, you can select which projects you want to exhibit the same work item settings as the current one:

## Time Tracking

Under **Settings** > **Time Tracking**, you can configure options for 7pace Timetracker for Windows or Mac app and web app. **Time Tracker System Settings** are administrator-only settings that are system-wide and are grayed out if a user does not have permission to access them. **Time Tracking Personal Settings** are for regular users of Timetracker.

This is what a 7pace Timetracker administrator can see when they expand the *Time Tracking* section:

![Time_Track_System_Settings.png](/cms_trial/assets/4e694e97-1ac6-4a24-9f30-b3f1d9cee5ae.png)

This screenshot is from 7pace Timetracker (cloud); 7pace Timetracker (on-prem) looks the same, with the exception of **Enable email notifications** (see below for further information).

A user of 7pace Timetracker can see this screen:

![Time_Track_Personal_Settings.png](/cms_trial/assets/cf0b2da4-c0dd-4212-b944-1afcf1824652.png)

### How to set tracking limits

**Time Tracking System Settings** > **Max single track length**

Only a 7pace Timetracker administrator can set the **Max single track length**; this section will be grayed out for users.

![system-settings-time-tracking.png](/cms_trial/assets/ca296f01-14f6-428f-bb03-017319c3f8da.png)

Here, you can set a number, in hours, at which your apps will stop tracking once this number has been exceeded. For example, if you set the maximum track length to `1` hour and you are tracking time on a work item, tracking automatically stops once the one-hour mark has been exceeded.

### How to enable automated activity checks when time tracking

**Time Tracking Personal Settings** > **Enable activity check on time tracking**

![enable-activity-check.png](/cms_trial/assets/2faa3873-120b-4999-87d7-f22e59348beb.png)

With this option enabled, the system checks with you during time tracking to see if you are still tracking.

### How to set how often activity check reminders display

You can set the amount of time, in minutes, that passes before the 7pace Timetracker system checks if you are still working on a current work item.

![standard-interval.png](/cms_trial/assets/645b46f5-5347-4546-b38a-5d8a0daa0b46.png)

**Standard Interval**: Enter the number of minutes that you want to pass before the Timetracker apps display a user prompt to check if you are still tracking time on the current item.

### How to set the length of time in seconds that the activity check reminder displays

You can also set the amount of time, in seconds, to display the resulting time-tracking prompt from whatever app(s) you are using.

![waiting-time.png](/cms_trial/assets/2cacbadf-8be0-4eb1-aab7-c1a910dc8cb4.png)

**Waiting Time**: Enter the number of seconds you want to keep the Timetracker apps' user prompt message displayed, waiting for action from you. If you do not confirm that you are still tracking time within the defined time (by either continuing or stopping time tracking), tracking will stop due to a N*o response from user during activity check* status.

## Approval Settings

Only a 7pace Timetracker administrator can be able to see the **Approval** section of **Settings**.

### Enable approval and set approval start date

1. Navigate to the *Settings* page of 7pace Timetracker, then under the *General* section, select **Approval**.

![approval-start-date.png](/cms_trial/assets/6c46786f-3c31-4258-8769-b1a2c5f48fc5.png)

2. Click the **Approval Start Date** field and select the date on the popup calendar from which you want to start using the approval functionality.

The page refreshes and changes are saved automatically. The approval feature is now enabled.

Once you save the start date, you cannot change the first day of the week unless you want to [reset all approval data](/cms_trial/space/7TFA/1253540033/General+Settings/). Similarly, all the weeks prior to the approval start date are automatically locked to all users for editing.

### Lock weeks automatically after approval

Select the **Lock Weeks Automatically** check box to automatically lock the week for further editing after the timesheet for that week is approved or closed by a manager.

![Lock_Weeks_Automatic.png](/cms_trial/assets/c3ba880c-b1cf-4578-aed9-c5aea2d7be05.png)

The page refreshes and the changes save automatically and all the weeks prior to your selected date will be locked for editing for all 7pace Timetracker users.

With this selection checked, when a manager approves or closes a timesheet for one of his/her users, that week is automatically locked so that user can no longer make any additional changes.

If this option is not selected, the *Lock* confirmation dialog box appears after a manager approves or closes a timesheet. The manager can then click "Lock" to lock the week or "Cancel" to leave it unlocked.

### How to submit a timesheet in advance

To allow your team to submit timesheets beyond the present week, enable the **Submit timesheet in advance** button.

![Submit_Timesheet_Advance.png](/cms_trial/assets/42336321-5ecd-44f0-83d2-63a11106817f.png)

Now, your team members will be able to submit their timesheets for weeks in the future on the Monthly and Timesheet pages.

### How to add an Approval Manager

A 7pace Timetracker administrator can create Approval Managers and Global Approval Managers who can view and approve the timesheets of their team members. Approval and Global Approval Managers can have any user role within 7pace Timetracker (they do not need administrator permissions) to approve time. Once set as an Approval or Global Approval Manager, these team members can then access the *Approval* page of 7pace Timetracker, and view and approve timesheets accordingly.

Approval Managerscan see and approve only those timesheets specifically submitted to them.

Global Approval Managers can see and/or approve all timesheets that have been submitted by members of the team (regardless of to whom they were submitted).

The *Unsubmitted* section of the *Approval* page is available/visible to any approval manager (both regular and global).

1. Navigate to the *Settings* page of 7pace Timetracker, then expand *General Settings*, and finally, **Approval**.

![add-manager.png](/cms_trial/assets/d9102a99-fa24-4642-bdc9-fcf1b21adbba.png)

2. Click the **Add Manager** button.

![add-manager-2.png](/cms_trial/assets/8077961b-502c-4313-be8d-0bf02959467a.png)

A list of team members is displayed.

This list shows only users that already exist in 7pace Timetracker (user needs to open 7paceTimetracker at least once to appear in the users' list).

3. Click the name of a team member.

![chosen-name.png](/cms_trial/assets/20b8c1dc-d672-4aa1-94b6-09437e623f49.png)

The team member's name displays in the **Add Manager** field.

4. Click the blue **Add** button.

Your team member is added to the list of 7pace Timetracker managers who team members can select when sending time for approval. This Approval Manager will only see the timesheets submitted to him/her specifically when the *Approval* page is accessed. When a team member submits his/her time at the end of each week, he/she can now see this person's name in the list of potential Approval Manager names.

5. Click the **Is Global** checkbox next to an Approval Manager's name.

This Global Approval Manager now has the ability to see all the submitted timesheets, regardless of to whom they were submitted, when they access the *Approval* page of 7pace Timetracker.

### Change the first day of the week for time entry

1. Navigate to the *Settings* page of 7pace Timetracker, then expand *General* *Settings*, and finally, **Approval**.

![reset-all-approved.png](/cms_trial/assets/f41bc893-2d78-45ca-b022-84e9f4424107.png)

2. Click the **Reset All Approval Data** button to reset/clear approval data that is in either a submitted or approved state, which allows you to change the first day of the week for future time entry.

This will delete all existing approval data from the database. If you confirm this action, all approval settings are then reset to their default values. However, worklogs are never deleted. It will reset the approval state only, so the manager just needs to approve the timesheets again.

3. Select the **Reset** button.

4. Click **Apply** to save changes.

You can then change the first day of the week for time entry (which defaults to Monday).

## Reminders and Notifications Settings

### Reminders and notifications

Navigate to **Settings** > **General** > **Reminders and Notifications**. Under the *Reminders* tab, you can configure time entry settings that will send you an email reminder if you have logged less than a set number of hours per day or per week. You can send your reminder at a specific time (local time) the following day/week.

You can also configure settings to email you at a specific time to remind you to log time.

Finally, you can enable email reminders that will remind you to submit your timesheet (at the end or the beginning of the week).

Under **Settings** > **General** > **Reminders & Notifications** on the *Notifications* tab, a 7pace Timetracker administrator can enable email notifications for time tracking and approval under **Notifications - System Settings**. This section will be grayed out/disabled for users of 7pace Timetracker.

![reminders-notifications.png](/cms_trial/assets/67dbb73d-2601-45fc-b50f-f046b50b7b4c.png)

### Enable email notifications

 Under **Settings** > **General** > **Notifications** > **Notifications - System Settings**, click the **Enable email notifications** checkbox. With this enabled, the user will receive an email notification when tracking is stopped by the system due to no response from the user during those prompts.

Please note that in 7pace Timetracker (on-prem), this setting is not displayed here but in the configuration tool.

Also, note that **Email to send notification** can be changed here: `https://dev.azure.com/your-Devops-organization-name/_usersSettings/about`

### Enable email notifications on time tracking

Under **Settings** > **General** > **Notifications** > **Notifications - Personal Settings** (Time Tracking Notifications), click the **Enable email notifications on time tracking** checkbox. With this option enabled, an email will be sent to the user when tracking is stopped by the system due to no response from the user.

### Enable email notifications on timesheet approval

Under **Settings** > **General** > **Notifications** > **Notifications - Personal Settings** (Approval Notifications), click the **Enable email notifications on timesheet approval** checkbox. With this option enabled, the user will be notified when their timesheet has been approved by their approval manager.

### Enable email notifications on timesheet submittal

Under **Settings** > **General** > **Notifications** > **Notifications - Personal Settings** (Approval Notifications), click the **Enable email notifications on timesheet submittal** checkbox. With this option enabled, Approval Managers will be notified via email when the team members assigned to them submit their timesheets.

### How to enable activity types

Under **Settings** > **General** > **Activity Types**, you can enable or disable Activity Types settings throughout 7pace Timetracker. Enable or disable the ability of all users to change the activity types for all other users in *Times Explorer*, add, edit, or, delete "Activity Types", and set the default activity type to be used throughout 7pace Timetracker. Activity types allow you to categorize every worklog by an activity type (such as "Development", "Testing", "Design", "Documentation", etc.).

This is what you can see when you expand the **Activity Types** section before **Enable “Activity Type" feature** is enabled:

![activity-types.png](/cms_trial/assets/0b7953df-412b-440c-9dda-553d4e3ae7cf.png)

When you click the **Enable “Activity Type” feature** button, any previously added activity types are populated, along with the **All users can change “Activity Type” for everyone in the Times Explorer** checkbox, the ability to add, edit, delete activity types, as well as set the default activity type.

![Activity_Types_Enable.png](/cms_trial/assets/2b1a0fd2-d6a7-4014-add3-fc1c47cc8a76.png)

### How to set the system default activity type

The **System Default** is only used if a regular user has not set their favorite activity type in their own Activity Types settings. As an administrator, you can set your personal **My Favorite** activity type to be your personal default selection throughout 7pace Timetracker, and team members can do the same on their own Activity Types settings (see below).

Team members without administrator access on their *Settings* page for activity types will see the **Default** column as disabled/grayed out.

As an administrator, clicking the **System Default** checkbox makes that activity type the default choice throughout 7pace Timetracker for your users, until/unless they choose a favorite activity type in their own Activity Types settings. Clicking the default selection saves your choice automatically.

If you have an activity type set as required under **Settings** > **Rules** > **Tracking Details** > **Require an activity type**, this setting forces users to manually select an activity type every time they add time or start tracking time. Enabling this resets any default **Activity Type** to **[Not Set]**.

The logic is that a user must not just use their favorite activity type if activity types are required for time entry and logging. With *activity type required* enabled, it forces users to think about the activity type they want associated with each specific time entry and to make a deliberate choice as opposed to just using whatever the default is.

### How to allow users to change the activity type for your entire team

By default, you can edit all worklogs added by you, but you cannot edit time that was added by other users, unless under **Settings** > **Rules**, you select a user role that can edit time for others. With **All users can change “Activity Type” for everyone in Times Explorer** enabled, the system allows all users to change the activity type for worklogs they normally cannot (only on the *Times Explorer* page!).

![Change_Activity_Type_Allow_Users.png](/cms_trial/assets/93c6f0b6-4847-420f-9f2c-b7d67b571f81.png)

### How to add a new activity type

Clicking the **Add Activity Type** button displays the *Adding/Changing Activity Type* dialog box.

Here, you can enter an activity type name in the corresponding field:

![add-activity.png](/cms_trial/assets/471c7829-5c38-44ce-ae19-af934a39e900.png)

Clicking in the **Color** field allows you to add a color to your new activity type from the resulting spectrum:

![choose-color.png](/cms_trial/assets/ff9d7558-043e-4838-9c89-847d26c175d5.png)

Click **Save**.

### How to edit or delete an activity type

Hovering over an activity type row with your mouse displays the **Edit** or **Delete** icon options:

![edit-delete.png](/cms_trial/assets/90d1fffd-c7b6-48a5-92ec-6d00b8880dd7.png)

Clicking the Edit icon (pencil) displays the *Adding/Changing Activity Type* dialog box, with the existing fields already populated:

![edit-activity-2.png](/cms_trial/assets/c2aa747a-35f8-40a4-b0b5-47be7686a68f.png)

You can edit the existing activity type by changing its name and/or color. Clicking in the **Color** field allows you to edit the current color to a different one in the spectrum. Or, you can make this the default activity type by clicking the **System Default** checkbox.

Click **Save** to maintain your changes or **Cancel** to disregard.

In the **Edit** column, when you click the **Trash can** icon, the following dialog box is displayed:

![delete-activity.png](/cms_trial/assets/c536a08c-206d-4a1b-9b1a-f3189f6cd98b.png)

If there are worklogs assigned to this activity type, you can choose to assign a new activity type to them before deletion or select **[Not Set]**. You can then continue to delete the activity type or select the **Cancel** button to stop the deletion process.

### Activity types within 7pace Timetracker's UI

With **Activity Type** enabled in *Settings*, the **Activity Type** dropdown selection list displays on the *Add Time* dialog box when you add time on the *Monthly*, *Timesheet*, and *Times Explorer* pages, and in the work item *7pace Timetracker* tab's Add Time feature.

![list-of-activities.png](/cms_trial/assets/6fbc2067-ea6e-4538-b17a-ef6c6bb95ebf.png)

Activity type is also displayed as a selection on the *Timesheet* page's *Add Time* list editor dialog box:

![Activity_Type_Add_Time_Window.png](/cms_trial/assets/32bcd7cf-991e-4bdb-aa84-362777e47f08.png)

With this feature enabled, the *Monthly* page displays the corresponding activity type colors on each calendar day/square, and an **Activity Type** column is added in the time details panel when you click a day/square:

![Activity_Type_Color_Display.png](/cms_trial/assets/6cd81ed0-45c6-4323-beac-70d2671aa905.png)

On the *Times Explorer* page, you can select single or multiple worklogs and assign an activity type to them by clicking the **Change Activity Type** button. The **Activity Type** column will display the various activity types added to each worklog if the user chooses to select this option:

You can also click a worklog within the **Activity Type** column and change the activity type there as well.

![Change_Activity_Type.png](/cms_trial/assets/a5e45576-3660-472b-ba03-29c568287254.png)

With **Activity Types** enabled, the work item form's *7pace Timetracker* tab now reflects the activity types categorized for each work item:

![Activity_Type_Enable_Activities.png](/cms_trial/assets/029ca1ca-4cda-4312-b9af-5c9357ca2157.png)

The 7pace Timetracker web app also features an **Activity Type** dropdown:

![Activity_Type_Dropdown.png](/cms_trial/assets/dd8a3d26-348e-4697-828c-f05e9e3c6e17.png)

The 7pace Timetracker Windows and Mac app has an **Activity Types** dropdown as well.

![Activity_Type_Windows_&_Mac_App.png](/cms_trial/assets/de45a907-3f06-43a6-9c97-6c82f52506f8.png)