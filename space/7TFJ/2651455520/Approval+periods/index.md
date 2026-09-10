# Approval periods

Approval periods are a useful tool for reporting on individual and team effort and for ensuring more complete data on time spent working. This is done by creating a schedule for submitting worklogs, with reminders sent to team members who have not completed their entries. Additionally, as an administrator, you can also configure time periods to include approvals, where Managers can sign off on worklogs submitted by their team, or follow up with individual members on their submissions. Combined together, these features - schedules, reminders, and approvals - help keep your team accountable for thorough and complete worklogs. With better data at hand, reporting and planning future efforts become more effective!

## How approval periods work

How you interact with approvals depends on your role within your organization and, more importantly, your [role in 7pace Timetracker](/cms_trial/space/7TFJ/1875247419/Manage+roles+and+permissions/).

- **User** - If you are a standard Jira user, such as a developer (a user in the role **Individual** or **Team** in 7pace), you will not interact directly with approvals or approval periods. Simply enter worklogs for work items!
- **People Manager** - If you manage other people and have been assigned the **Manager** role in 7pace, you are responsible for approving your team members' submitted worklogs.

When a user’s worklogs are approved by a Manager, all worklogs for that approval period are locked from future changes! This includes updating existing worklogs or adding new worklogs within the approval period.

- **Administrator** - If you are a 7pace **Administrator**, you can [lock approval periods](/cms_trial/space/7TFJ/2183954434/Lock+time+periods/) in addition to approving user worklogs. Locking an approval period prevents any changes to the submitted worklogs and to approvals.

Locking a time period does not automatically approve worklogs within that period. If a user’s worklogs are not approved they will remain unapproved.

![admin-ApprovalPeriods.png](/cms_trial/assets/23d65575-9e1e-407f-b927-2033e26c532a.png)

## Create an approval schedule

To use approvals in 7pace Timetracker, first create an Approval schedule.

1. In the left-hand panel of any view, expand **Apps** and click **7pace Timetracker**, then click **Settings**.

   Or
2. Within any Space, if you have added the **7pace Timetracker** tab, click the tab to open the 7pace app, then click **Settings**.
3. Select **Approval Periods**.
4. Click **Create schedule**.
5. Define the approval schedule:

   1. Set the **Cadence** and the **Start date**.
   2. Additionally, you can set Approval periods to split after a specific day regardless of the approval schedule cadence, using the **Split approval periods** option.
   3. If you turn on **Split approval periods**, select the day of the month that approval periods will split under **Split day**.
6. Click **Save schedule**.
7. After saving the approval schedule, flag it as active using the toggle.

After an approval schedule has been created, you can reset and delete all locked time periods using the option **Reset all approval periods**.

**Warning**: Resetting approval periods cannot be undone!

Image — asset pipeline pending  
7pace Timetracker for Jira Create approval schedule dialog

## Turn on Time approval

Creating and activating an approval schedule is separate from activating approvals. You need to activate Time approval so that Managers can review and approve submitted worklogs. Use the **Time approval** toggle to turn approvals on and off (Figures 1 and 2, above).

## Required permissions

Only users with the 7pace Timetracker **Admin**, **Global Approval Manager** or **Manager** role can view and approve time. To verify a user’s role, use the following steps:

1. Click **Settings** > **Role Management**.
2. Expand the **Admin**, **Global Approval Manager** or **Manager** role and verify the user is a part of this group.

Review [Managing roles and permissions](/cms_trial/space/7TFJ/1875247419/Manage+roles+and+permissions/) for more information about managing permissions in 7pace Timetracker for Jira.

![manage-roles.png](/cms_trial/assets/e4206235-ba8e-40cc-86a8-bb20674da349.png)