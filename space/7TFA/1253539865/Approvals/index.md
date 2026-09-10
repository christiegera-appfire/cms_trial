# Approvals

On this page, learn how to view and approve timesheets that are pending approval, close, reopen, revoke, lock weeks for editing, and learn what our approval icons mean.

## Introduction

7pace Timetracker’s Approval page and workflow is designed to be simple and easy to navigate for managers and team members.

When you install Timetracker for the first time, the Approval feature is enabled by default, with the start date set to <today> - <1 day> - <1 year>. Therefore, if you install Timetracker on August 3, 2019, the start date for approval is automatically set to August 2, 2018.  All weeks prior to this date are automatically locked for editing.

The three main pages of Timetracker involved in the approval process are the Monthly and Timesheet pages for team members and the Approvalpage for managers.

## Approval Manager Overview

As a manager,  you can view, approve, and archive timesheets that your team members have submitted to you on a weekly basis on the Approval page. You can view or close the unsubmitted timesheets of team members who may have forgotten to submit their time or for weeks where no time was logged/submitted. Weeks in which all timesheets are approved or closed can be made read-only by locking them for further editing. You can also re-open closed or approved timesheets for your team members if changes need to be made. We will provide an overview of these approval features throughout this article.

The Approval page is accessible only to configured Approval Managers or Global Approval Managers. Approval and Global Approval Managers must be added by administrators to approve time. Before a manager can be granted permissions to approve time, an administrator must first assign roles to every user of 7pace Timetracker under **Settings** > **User Management**. Then, the administrator can navigate to **Settings** > **General** and expand **Approval** to select which users are permitted to access the Approval page and perform all tasks related to approval. Admins can select anyone, with any user role, to become an Approval or Global Approval Manager. A Global Approval Manager can see and approve all timesheets submitted by the team. Approval Managers can just see those timesheets that were specifically submitted to him/her.

*For more information, see*[*How to Add an Approval Manager*](/cms_trial/space/7TFA/1253540033/General+Settings/)*.*

Upon clicking the Approval page, managers will see that the page is categorized into the following sections: Pending Approval, Unsubmitted, and Archived. Expanding each section will allow you to view the weekly timesheets of each of your team members that fall into each category.

![Approval_Manager_Overview.png](/cms_trial/assets/e30b4aba-4404-4d10-b654-08bdcaf3e6aa.png)

### Pending Approval

Under Pending Approval, as a manager, you can view the timesheets your team members have submitted that require your approval. If you are a Global Approval Manager or an administrator, you will also see the timesheets that have been submitted for approval to other managers. Here, you can approve selected user’s timesheets, approve multiple users’ timesheets, or view the details of a selected user’s timesheet.

#### Timesheet Approved

Once approved, the timesheet(s) automatically moves to the Archived section (see below), marked as Approved in the timesheet details, as well as indicating who approved it. Weekly timesheets you approve show up on your team members’ Monthly calendar with the Week is approved icon in the Week Total column and on their Timesheet page as Week is approved.

When you approve a timesheet, you may get a dialog prompt asking you if you want to lock the week for further editing. This prompt will only display if there are no pending or unsubmitted timesheets for that week and if you haven't [configured the automatic locking feature](/cms_trial/space/7TFA/1253540033/General+Settings/). Pending timesheets must be approved and unsubmitted timesheets must be closed before you can lock a week for editing. You can also go into **Settings** > **General** > **Approval** > **Approval Process Settings** and click the **Lock Weeks Automatically** checkbox to bypass the manual process (again, the rules for pending and unsubmitted timesheets still apply). If you decide to lock the week after the dialog prompt to do so, your team member will see the Week is locked icon in the Week Total column of the Monthly page as well as on their Timesheet page for that week.

#### Alternate Flow - Timesheet not approved

As a manager, if you want changes made to a team member's timesheet, Timetracker’s workflow requires that you contact that team member personally to discuss and request those changes. Pre-approval, a team member can also proactively choose to revoke their submitted timesheet. In both cases, your team member can either go to the Timesheet page or the Monthly page, hover over the submitted for approval icon revoke the submission, confirm the revoke message, make the changes required, and submit again. When revoked, the timesheet will disappear from your "Pending Approval" section until updates are made and it is submitted again by your team member; it will then display under your Pending Approval section again.

You can also reopen an already-approved or closed timesheet from the Archived section of the Approval page (see the Archived section below).

For more information on the Pending Approval process, please see [Approving a Submitted Timesheet](/cms_trial/space/7TFA/1253539865/Approvals/).

#### Approval Process Flowchart

![Approval_Process_Flowchart.png](/cms_trial/assets/96397ab2-edb0-40c1-97b2-47cd59679c3f.png)

### Unsubmitted

Under the Unsubmitted section of the Approval page, as a manager, you can view the timesheets of your team members who have not requested approval. The Unsubmitted section is available to any approval manager (both regular and global). Timetracker automatically sends timesheets that aren't submitted by your team members to this section at the end of each week. You can view unsubmitted timesheets for a specific calendar year, close selected user’s timesheets, close multiple users’ timesheets, or view the details of a selected user’s unsubmitted timesheet.

Once closed, the timesheet automatically moves to the Archived section (see below), marked as Closed and by whom in the timesheet details panel. The team member will then see the Week is closed message and icon on the Timesheet page for that week and on the Monthly calendar in the Week Total column.

For more information on the “Unsubmitted” process, please see [Closing an Unsubmitted Timesheet](/cms_trial/space/7TFA/1253539865/Approvals/).

### Archived

In the Archived section, as a manager, you can view approved timesheets that have moved from Pending Approval and closed timesheets that have moved from Unsubmitted; these two categories make up the Archived section. You can view archived timesheets for a specific calendar year, re-open selected user’s timesheets, re-open multiple users’ timesheets, view the details of a selected user’s timesheet (including if it is marked as Approved or Closed and by whom), or lock weeks for editing.

### Reopen a Timesheet

If a timesheet has already been approved or closed and changes need to be made to it, you will need to reopen the timesheet for your team member from the Archived section of your Approval page.

If you reopen an approved timesheet from the current week, the timesheet will move from Archived and show up on your team members’ Timesheet page as Week is reopened and the Submit for Approval button re-enabled for that week. On the Monthly calendar, the Week is reopened icon will display in the Week Total column. Once a team member resubmits the timesheet again, it will then display in your Pending Approval section.

If you reopen a timesheet for any week prior to the current week and the timesheet was originally in an unsubmitted status, then that timesheet initially moves from Archived to the Unsubmitted section. If the timesheet was from a prior week and was originally approved, the timesheet will move from Archived and show up on your team members’ Timesheet page as Week is reopened and the Submit for Approval button re-enabled for that week. On the Monthly calendar, the Week is reopened icon will display in the Week Total column. When your team member resubmits this timesheet, then it returns to the Pending Approval section for the manager's approval.

### Lock Weeks for Editing

By default, all weeks prior to a team member’s start date are automatically locked.

As mentioned, you can lock weeks in the Archived section so that your team members can no longer make edits to their timesheets during those weeks, provided there are no pending or unsubmitted timesheets during the week(s) in question. You can lock each week manually or configure Timetracker to automatically lock a week after the timesheets for that week are approved or closed. You can do this by navigating to **Settings** > **General** > **Approval** > **Approval Process Settings** and checking **Lock Weeks Automatically**. In the Archived section, unlocked weeks will have a key icon next to them. Hovering over this icon will turn it gray and display the tooltip Click to lock week. If the week can't be locked, the following message will display: This week cannot be locked. Please ensure that there are no pending or unsubmitted timesheets and try again. If it can be locked, clicking the unlocked week icon will refresh the page and the locked icon will display. Hovering over this icon will display the unlock icon and clicking on it will unlock the week.

You must first unlock a week before you can reopen a timesheet in that week.

For more information on the “Archived” process, please see [Reopen a Timesheet](/cms_trial/space/7TFA/1253539865/Approvals/).

## Approval for team members

With a simple click of a button on the Monthly or Timesheet page, team members can send their weekly timesheets to the manager of their choice, whether they logged time for one day or every day of that week. Designed with the collaboration and facilitation of an Agile environment in mind, the Approval process encourages direct communication between team members and management without the time-consuming back and forth of the reject or decline email notifications found in many time-tracking approval workflows. If changes need to be made to a timesheet after submittal, either the manager reaches out directly to their team member to request changes, or the team member proactively revokes their timesheet of their own accord before it is approved. Once revoked, changes can be made to the timesheet and it can be resubmitted. Similarly, if a timesheet has already been approved or closed, a manager can reopen that timesheet on behalf of their team member, if changes need to be made.

Approval status updates made by a team member on the Monthly or Timesheet pages of 7pace Timetracker are reflected on the Approval page and vice versa, and the full integration of the system allows both managers and team members to be continually in-the-loop.

Team members will see the following statuses on their Monthly and Timesheet pages, depending on which stage of approval their timesheet is currently in:

### In progress

The team member has not yet submitted their weekly timesheet. On the Monthly page, the team member will see the Week is in progress icon in the Week Total column and on the Timesheet page for the current week and any weeks that have not been closed or locked for editing. Weeks beyond the current week are automatically locked for entry.

### Submitted

The team member has submitted their timesheet for approval. On the Monthly page, the team member will see the Week is submitted for approval icon in the Week Total column and on the Timesheet page for that week. Once submitted, the manager will see their team member's timesheet in the Pending Approval section of the Approval page.

### Approved

The team member's timesheet has been approved by their manager. On the Monthly page, the Week is approved icon displays in the Week Total column of the submitted and approved week. Similarly, on the Timesheet page, Week is approved displays for the submitted and approved week. For the manager, once approved, their team member's timesheet automatically moves to the Archived section of the Approval page, with the Approved tag, along with by whom it was approved. The manager can choose to lock that week for further editing, given there are no pending or unsubmitted timesheets in that week, or reopen the timesheet at a later time if need be.

### Revoke/Reopen

A team member can revoke their submitted timesheet before it is approved by their manager if they need to make changes to it. Likewise, if their manager has viewed it and determines that changes need to be made to it, they can personally request that the team member revoke it. On the Monthly page, the team member simply clicks the Week is submitted for approval icon in the Week Total column and confirms the Do you want to revoke your submission? dialog box message. The icon then changes to Week is reopened. On the Timesheet page, the team member can see Week is submitted for approval on that week and has the option to revoke their timesheet. Once confirmed, the page will then refresh to display Week is reopened along with the Submit for Approval button. Once revoked, the timesheet disappears from the manager's Pending Approval section on the Approval page. A team member will also see this message and icon if their timesheet was already approved or closed and their manager reopened it from the Archived section of Approval.

### Closed/Locked

If a manager closes an Unsubmitted timesheet, the team member will then see the Disabled due to approval status when they hover over that week and the ▢ icon on their Timesheet page for that week and on the Monthly calendar in the Week Total column.

Once in the Archived section of Approval (either because the submitted timesheet was approved or the unsubmitted timesheet was closed), a manager can choose to lock the week for editing or configure it to lock automatically in such a case. Once locked, team members will then see the "Week is closed" message and icon (▢ ) on their Timesheet page for that week or on the Monthly calendar in the Week Total column. If a team member wants to edit a closed or approved timesheet, they need to ask their manager to reopen it. If the week is locked, the manager must unlock the week first, before the timesheet can be reopened.

## Approval Icons

Below is a list of the icons that are used in the approval process. You will find these icons on the following pages of 7pace Timetracker:

- Monthly Page
- Timesheet Page
- Approval Page
- Archived Section of the Approval page

### Monthly and Timesheet Page

On the "Monthly" and "Timesheet" pages, the icons featured below indicate the approval status of your timesheet for current and past weeks. On the "Monthly" page, you can view the approval process icons in the **Week Total** column of the calendar format. On the "Timesheet" page, these icons display to the top-right of the timesheet, in a weekly timesheet format.

| Icon | Description |
| --- | --- |
| ▢ - Week In Progress | This icon indicates that the timesheet is currently in progress and it is not submitted for approval.  This is the default icon that appears for the week. |
| ▢ - Submitted | This icon indicates that the timesheet for the current week has been submitted for approval.  The manager can view submitted timesheets in the Pending Approval section. |
| ▢ - Approved | This icon indicates that the timesheet for the week has been approved by the manager.  Once the manager approves the timesheet, the week will either automatically lock for editing (if configured as such in Approval Process Settings) if there are no other pending or unsubmitted timesheets, or the manager can choose whether or not to lock the week for editing. Once approved, the timesheet moves from Pending Approval to the Archived section of the Approval page. If an approved timesheet needs to be edited, a manager has to reopen it from the Archived section. If the week is locked for editing, the manager has to unlock the week before the timesheet can be reopened. |
| ▢ - Revoke/ Reopen | This icon indicates that the team member has revoked their timesheet or the manager has reopened their team member's timesheet from the Archived section of the Approval page.  The Revoke option allows the user to revoke their submitted timesheet if they need to make corrections to it before re-submitting to their manager for approval. The reopen option allows a manager to reopen an archived timesheet for re-submission. |
| ▢ - Closed | This icon means the week has been closed for further editing by team members. To reopen a timesheet, the week must first be unlocked from the Archived section, and then the timesheet must be reopened. |

**Approval Page**

| Icon | Description |
| --- | --- |
| ▢ - Activity Types | Hovering over this icon displays the worklog(s) and the activity types they are categorized by. For more information, see [Activity Types](/cms_trial/space/7TFA/1253540033/General+Settings/). |
| ▢ - Work Item/Comments | Hovering over this icon displays the work items and any comments. |

### Archived Section of Approval

The following table lists and describes the icons used in the Archived section of the Approval page. Managers can view these icons adjacent to the week's name in the Week column.

| Icon | Description |
| --- | --- |
| Image — asset pipeline pending mceclip7.png  (Unlocked/Might be locked) | This blue key icon indicates that the corresponding week is currently unlocked, but can potentially be locked for editing.  The gray key icon appears when you hover your mouse over the blue key. If you click on this icon and the week doesn't contain any unsubmitted or pending timesheets, the week will automatically lock and change to the locked icon (see below). If there are unsubmitted or pending timesheets for the week, you will receive a warning message that the week cannot be locked. |
| ▢ - Locked | This icon indicates that the corresponding week is locked for editing.  The opened lock icon in red appears when you hover your mouse over the locked icon. |

## How to approve a timesheet

Only a user who has been added by a 7pace Timetracker administrator to the role of Approval Manager or Global Approval Manager (see [How to Add an Approval Manager](/cms_trial/space/7TFA/1253540033/General+Settings/)) can approve timesheets submitted by team members. 7pace Timetracker admins can automatically view and/or approve submitted timesheets as well. Admins and Approval Managers can view submitted timesheets in the Pending Approval section of the Approval page.

1. Expand the **Pending Approval** section on the Approval page.

2. In the left-hand column, expand the year and click the week in which you want to view timesheets that have been submitted for approval.

![Pending_Approval_Step_1.png](/cms_trial/assets/39468334-0365-45a9-ab76-5ca1ca10686c.png)

In the week depicted above, this is what you will see if you are a 7pace Timetracker administrator or a user who has been assigned as a [Global Approval Manager](/cms_trial/space/7TFA/1253540033/General+Settings/). You will see timesheets awaiting the approval of others, in addition to timesheets awaiting your approval. Timesheets who have not been submitted but not assigned to a specific approval manager will be displayed here as well.

3. In the second column, select the team member whose timesheet you want to approve.

![Pending_Approval_Step_2.png](/cms_trial/assets/478f9a80-efa9-4b9a-b169-4de733b39d36.png)

When you select the team member, their timesheet details display on the far right, third column of the page.

4. Click the < by the red arrow, above.

![Pending_Approval_Step_3.png](/cms_trial/assets/88b808fb-b82e-44c8-8a42-62165c081add.png)

This creates more real estate on the page.

Here, you can check the tracked time details for different work items and also the total time logged by your team members for each day or the entire week. The icons indicate that there is an activity type associated with the time tracked. Hovering over the mceclip4.png icon displays the work log(s) and the activity types they are categorized by.

The approval workflow requires that you personally discuss any changes that need to be made to a timesheet with your team members and ask them to revoke and submit their timesheet again if needed.

5. After verifying the submitted timesheet details, click **Approve Timesheet**.

### Approving the timesheets of multiple users:

1. In the second column, click each team member and verify the submitted timesheet details of each.
2. Click the checkbox for each team member whose timesheet you want to approve.

   To select all team members, click the checkbox by the **Approve Selected** label.
3. Click **Approve Selected**.

### Approving timesheets for all weeks:

1. In the first column, click each week and then verify the timesheet details of each team member is correct.
2. Click **Approve All Weeks**.

On the Approve Selected timesheet confirmation dialog box, click **Approve**.

On the Lock Week dialog box (which will display if you haven't configured automatic locking), click **Lock** to lock the week during which the approved timesheet was submitted for further editing (or Cancel to leave the week unlocked). On the Monthly page, the team member whose timesheet was approved can see the Week is approved icon in the Week Total column, and this message and status also display on the Timesheets page for that week. If the manager also locks the week, the user will see a Disabled due to approval status message on the Timesheet and Monthly pages when they hover within that week.

## How to close an unsubmitted timesheet

Unsubmitted timesheets are those timesheets that team members did not submit to their manager for approval. 7pace Timetracker checks each week starting from the [Approval Start Date](/cms_trial/space/7TFA/1253540033/General+Settings/) configured in [Settings](/cms_trial/space/7TFA/1253540033/General+Settings/) and automatically moves weeks in which unsubmitted timesheets exist to the Unsubmitted section of the Approval page at the end of each week.

In the Unsubmitted section, a manager can close unsubmitted timesheets, which moves them to the Archived section. Closed timesheets can still be reopened from the archive, if changes need to be made, provided they are not locked (more details on that, below).

1. In the left pane, expand the Unsubmitted section on the Approval page.

2. In the first, far-left column, expand the year in which the timesheet you are looking for exists.

3. Select the week in which you want to close the timesheet.

![Close_Unsubmitted_Timesheet_Step_1.png](/cms_trial/assets/be37c752-3adb-4612-ad3b-804aff4d5b47.png)

4. In the second column, select the team member whose timesheet you want to close.

When you select a team member, their timesheet details display in the far-right, third column:

![Close_Unsubmitted_Timesheet_Step_2.png](/cms_trial/assets/5a2520ac-95d9-41d0-a4b7-849f8774e3cb.png)

5. If you want to close the timesheet for multiple team members, in the second column, click the checkbox for each team member whose timesheet you want to close. To select all team members, click the top checkbox by the Close Selected label.

6. Click **Close Selected** or **Close Timesheet**.

![Close_Unsubmitted_Timesheet_Step_3.png](/cms_trial/assets/6db0de09-5c86-4494-b20b-b9faba590454.png)

7. If you want to close all unsubmitted timesheets within a specific year, in the first column, select the year and click **Close All Weeks**.

![Close_Unsubmitted_Timesheet_Step_4.png](/cms_trial/assets/58450cd5-b7e1-4d1c-98d0-a70cfd616f68.png)

8. On the confirmation dialog box, click **Close all**.

9. In the Lock Additional Weeks dialog box (which will display if you haven't [configured automatic locking in Settings](/cms_trial/space/7TFA/1253540033/General+Settings/)), click **Lock** if you want to lock all weeks that don't have pending or unsubmitted timesheets remaining (or Cancel to leave the weeks unlocked).

![Close_Unsubmitted_Timesheet_Step_5.png](/cms_trial/assets/0fbc4e93-e71e-4651-acba-87dfabd36f4c.png)

The closed timesheet moves to the Archived section with the Closed flag and by whom it was closed. On the Monthly and Timesheet pages, the team member whose timesheet was closed will see The week is closed as well as Disabled due to approval status for that week.

## How to reopen a timesheet

1. In the left pane, expand the Archived section on the Approval page.

2. In the first column, expand the appropriate year and then select the week that corresponds to the timesheet you want to re-open from the list of displayed weeks.

![Reopen_Timesheet_Step_1.png](/cms_trial/assets/c01432d7-90b3-47a4-ab05-f4e926277ef6.png)

If you are looking at the current week, you will see team members whose timesheets have been approved.

If you look at past weeks, you could see a combination of team members' timesheets that have been approved or closed.

3. Click a team member's name.

![Reopen_Timesheet_Step_2.png](/cms_trial/assets/5a2122f5-4a70-4185-ba7f-9f385bc17701.png)

The details panel displays for the specific timesheet, including whether the timesheet was Approved or Closed and by whom.

4. Select one or multiple team members' timesheets and click Re-open Timesheet or Re-open Selected (this will be grayed out unless you click one or multiple checkboxes).

![Reopen_Timesheet_Step_3.png](/cms_trial/assets/2a123f24-cbf2-4ee2-8120-0a4f15cb6255.png)

If you are trying to open a timesheet from a week that has been locked for editing, you will see the Locked icon (▢ ) next to the week. The Reopen Selected and Reopen Timesheet buttons will be disabled. You will first have to unlock the week to reopen the timesheet.

![Reopen_Timesheet_Step_4.png](/cms_trial/assets/e05f8fd4-2375-4e28-95fc-2a90767d9aaf.png)

Once you click either Reopen Selected or Reopen Timesheet, the following confirmation dialog box displays:

![Reopen_Timesheet_Step_5.png](/cms_trial/assets/6f06e314-c54d-4ab1-a44a-533d761ac192.png)

5. Click "Reopen".

If the timesheet you reopened was from the current week, the timesheet disappears from the Archived section and shows up on the team member’s Timesheet page as Timesheet is Reopened, with the Submit for Approval button re-enabled for that week. On the Monthly calendar, the Week is reopened icon will display in the Week Total column.

If you reopen a timesheet from any prior weekand the timesheet was originally in anunsubmitted status, then that timesheet initially moves from Archived back to the Unsubmitted section. When a user resubmits this timesheet, then it is removed from the Unsubmitted section and added to the Pending Approval section for the manager's approval.

If you reopen a timesheet from any prior week and it was originally in an approved status, the timesheet will move from Archived and will immediately show up on your team members’ Timesheet page as Week is reopened with the"Submit for Approval button re-enabled for that week. On the Monthly calendar, the Week is reopened icon will display in the Week Total column. When your team member resubmits this timesheet, then it returns to the Pending Approval section for the manager's approval.

### How to lock and unlock a week

By default, all weeks prior to a team member’s start date are automatically locked.

You can lock weeks in the Archived section of the Approval page so that your team members can no longer make edits to their timesheets during those weeks (provided there are no pending or unsubmitted timesheets during the weeks in question).

If you wish to [reopen a timesheet that has been closed](/cms_trial/space/7TFA/1253540033/General+Settings/), so a team member can make edits to it, you must unlock the week first, before the timesheet can be reopened.

**Note:** You can configure Timetracker to [automatically lock a week](/cms_trial/space/7TFA/1253540033/General+Settings/) after the timesheets for that week are approved or closed.

1. In the left pane, expand the **Archived** section on the Approval page.

2. In the first column, expand the appropriate year.

![Lock_&_Unlock_Week_Step_1.png](/cms_trial/assets/082f9155-9faa-4705-a90a-407d70352883.png)

Unlocked weeks will have a key icon next to them.

3. Hover over this icon.

![Lock_&_Unlock_Week_Step_2.png](/cms_trial/assets/8696454f-a333-45c3-a34b-162a27ee2dca.png)

The icon turns gray and displays the tooltip Click to lock week.

4. Click the icon.

![Lock_&_Unlock_Week_Step_3.png](/cms_trial/assets/4388fcd5-e5e9-4df9-8599-d446f2d50e92.png)

If the week can't be locked, the following message will display: This week cannot be locked. Please ensure that there are no pending or unsubmitted timesheets and try again.

If it can be locked, the page will refresh and the locked icon will display.

![Lock_&_Unlock_Week_Step_4.png](/cms_trial/assets/dea350e6-dcbf-4b52-b9c8-6c8bdfedb99e.png)

Once locked, team members will then Week is disabled due to approval status on their Timesheet page for that week or on the Monthly calendar within that week. No further edits can be made.

5. Hover over the lock icon.

![Lock_&_Unlock_Week_Step_5.png](/cms_trial/assets/37c9a73f-7ce7-4323-b68a-46fb2254957e.png)

The unlock icon displays.

6. Click the unlock icon.

![Lock_&_Unlock_Week_Step_6.png](/cms_trial/assets/e01d60a5-7411-4c31-97f1-98529dc13db9.png)

The week is unlocked.

The key icon displays next to the week. Timesheets from this week can now be reopened and edited by team members if necessary.