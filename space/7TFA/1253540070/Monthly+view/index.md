# Monthly view

Learn how to add, edit and delete time, as well as submit and revoke your timesheet on 7pace Timetracker's Monthly page.

## **7pace Timetracker for Azure DevOps**

***30-Minute live demo***

## Monthly page: your personal calendar

The Monthly page's calendar interface allows team members to enter time, track, and maintain their work efforts. When you click on the Monthly page, the calendar view defaults to the current month and year. As a developer, you can easily navigate to different months and years, view daily, weekly, and monthly totals of time entered, as well as view the time entry details of a particular day.

### Calendar view

![Calendar_View.png](/cms_trial/assets/61990acb-e308-4a38-954b-70e78070fae1.png)

| **ID** | **Description** |
| --- | --- |
| 1 | Month and year navigator.  Click the [Unmapped macro: inline-external-image — no content to fall back on] and ▢ icons to navigate to previous months and years. |
| 2 | Clicking on the Current Month link will bring you back to the current month if you have scrolled backwards or forward in time. |
| 3 | Your total time tracked for the month displays here. |
| 4 | Click the + icon to add a new time entry on a particular day.  When you hover your mouse over a day block in the calendar, the + icon displays. Clicking the + icon allows you to add a new time entry for that day. When you click this icon, the system displays the Add Time dialog box.  For more information about adding and editing a worklog, see [Adding a Worklog.](/cms_trial/space/7TFA/1253540070/Monthly+view/) |
| 5 | The icons used that in the Week Total column reflect various states within the time approval process. Hovering over these icons will display a tool tip with additional information on the meaning of each icon.  For more information about these icons, see [Approval Icons](/cms_trial/space/7TFA/1253539865/Approvals/). |
| 6 | The Week Total column displays the total hours you have worked each week. It also displays the week number in the current calendar year of each week, for example, w26. |
| 7 | The Weeks Total displays at the bottom of the Week Total column and reflects all days of the work week for which time was entered in the current month, *in addition to* any days that overlapped from the month before or the month after (for example, if Monday, August 29, Tuesday, August 30, and Wednesday, August 31 fall within August, but Thursday, September 1 and Friday, September 2 fall within September, the Weeks Total for September will reflect the totals for all these days of the week, regardless of the month in which they fell. |
| 8 | The Month Total displays only totals of hours worked within the displayed calendar month (no overlapping days of the week from previous or subsequent months are included). |

### Time Details view

You can click on any day within the calendar to display additional details of time added and tracked on that day.

Here you can:

- Click Add Time to add a new worklog
- Edit worklogs (pencil icon)
- Delete worklogs (trashcan icon)
- View which worklogs were marked as billable.
- Open the work item form of the worklog by clicking on the work item ID
- See which worklogs are locked for editing because the work items to which they belong are closed

![Time_Details_Overview.png](/cms_trial/assets/64caf0a0-51fb-43cf-9093-b84e4296ec77.png)

## Add a new worklog

You can add time on the Monthly calendar page in two ways:

- Clicking the + icon on a particular day/block on the calendar.
- Clicking on the day/block on the calendar to view the time details panel, then clicking the Add Time link.

If you try to add time on a closed item and Prevent Time Entry Against Closed Items is enabled under **Settings** > **Rules**, you will receive an error message and won’t be allowed to add time.

1. On the time entry calendar, hover your mouse over the day/block on which you want to add a new time entry.

![Add_New_Worklog.png](/cms_trial/assets/ec705629-0d5b-46da-911c-9e25cf344d9e.png)

The system displays the plus + icon on the selected day.

2. You can also click directly on the day/block on the calendar on which you want to add a new worklog.

![Add_Time.png](/cms_trial/assets/041f7537-ca25-44c6-9e01-eb05564b1ff7.png)

1. The time details panel populates below the day on which you click, displaying details of the time logged/tracked on that day, if any.

4. Click the plus + icon on the calendar day/block or click the Add Time link in the time details panel.

![Add_Appropraite_Values.png](/cms_trial/assets/6228e350-6b2f-4efb-8a27-19c7e9cfa1ad.png)

The Add Time dialog box displays.

5. Add the appropriate values in the fields.

6. Click the **Save** button to save the time entry for that day.

## Edit a worklog

1. In the calendar, click directly on the day on which you want to edit a worklog.

The time details panel populates below the day in which you click, displaying details of the time logged/tracked on that day.

![Edit_Worklog_Step_1.png](/cms_trial/assets/78d4c52a-2f1c-41ba-bf4f-cda3c53f74d9.png)

If a 7pace Timetracker administrator has enabled Prevent Time Entry Against Closed Items in **Settings** > **Rules**, when you hover over the work log, you’ll see a lock icon next to the work log that belongs to the closed item.

![Edit_Worklog_Step_2.png](/cms_trial/assets/ced3e3db-20cd-495e-8d50-9b0c38ac37e4.png)

2. With your mouse, hover over the editable worklog you want to edit.

The (

[Unmapped macro: inline-external-image — no content to fall back on]

) icon displays.

3. Click the

[Unmapped macro: inline-external-image — no content to fall back on]

.

![Edit_Worklog_Save.png](/cms_trial/assets/4e3cd5c6-b597-436f-98ec-e82b005d38a5.png)

The system displays the Edit Time dialog box.

4. Edit the fields you wish to update.

5. Click **Save**.

## Delete a worklog

1. In the calendar, click directly on the day on which you want to delete a worklog.

The time details panel populates below the day in which you click, displaying details of the time logged/tracked on that day.

![Delete_Worklog_Step_1.png](/cms_trial/assets/9570f276-c53d-4795-8917-11d131ee48f2.png)

If a 7pace Timetracker administrator has enabled Prevent Time Entry Against Closed Items in **Settings** > **Rules**, you’ll see the a lock icon next to the worklog that belongs to the closed item:, so you won't be able to delete the worklog:

2. With your mouse, hover over the worklog you want to delete.

![Delete_Worklog_Step_2.png](/cms_trial/assets/937cfcac-4970-4c96-938d-68beffa14f83.png)

The  (

[Unmapped macro: inline-external-image — no content to fall back on]

) icon displays, along with the edit icon.

3. Click the

[Unmapped macro: inline-external-image — no content to fall back on]

.

The system displays a confirmation dialog box.

4. Click **OK**.

The dialog box closes, and the time entry is deleted.

If a user is tracking time and edits (removes) the worklog currently being tracked by the Windows or Mac App or the Web App, the system will automatically stop tracking.

## Submit your timesheet

One of the ways you can submit your timesheet to your project manager for approval at the end of the work week is via the 7pace Timetracker "Monthly" calendar page. Before doing so, ensure that you have correctly tracked your time for each day of the work week.  Best practices also include checking the Week Total column for the total number of tracked hours in the week before you submit that week for approval.

1. On the 7pace Timetracker menu bar, select **Monthly**.

2. In the Week Total column, click the Week is in progress icon (

[Unmapped macro: inline-external-image — no content to fall back on]

).

![Submit_Timesheet_Step_1.png](/cms_trial/assets/6cfa640e-f1c9-446a-a6eb-4b43d68c45b6.png)

The Submit for Approval option displays.

3. Click **Submit for Approval**.

![Submit_Timesheet_Step_2.png](/cms_trial/assets/8aed10bf-96d8-428e-a3a6-19cb99448489.png)

The Time Approval popup box displays.

4. In the Send for approval to dropdown, select the manager to whom you want your timesheet approved.

5. On the approval confirmation dialog box, click **Send for Approval**.

The icon in the week total column changes to Submitted for approval (

[Unmapped macro: inline-external-image — no content to fall back on]

).

## Revoke your timesheet

1. If you need to revoke your timesheet after submitting it to your project manager for approval, in the Week Total column of the week that includes the timesheet you want to revoke, click the Submitted for approval (

[Unmapped macro: inline-external-image — no content to fall back on]

) icon.

![Revoke_Your_Timesheet_Step_1.png](/cms_trial/assets/a7087289-04fa-43e8-9bd4-46719b532de8.png)

The Revoke submission popup displays.

![Revoke_Your_Timesheet_Step_2.png](/cms_trial/assets/e545cbd8-2756-47cb-82be-b60e322ad5a8.png)

2. On the Revoke Submission Confirmation dialog box, click **Revoke submission**.

![Revoke_Your_Timesheet_Step_3.png](/cms_trial/assets/fec4a9ae-2006-49f1-98fc-f42a3aab78ac.png)

The Revoke submission confirmation dialog box displays.

3. Click **Revoke submission**.

![Revoke_Your_Timesheet_Step_4.png](/cms_trial/assets/f07a01aa-82f3-49dc-bb92-f946175f7669.png)

The page refreshes, and the week is reopened.

Once you revoke the submitted time sheet, that time sheet is removed from the Approval Pending list on your manager's Approval page, and the submitted icon on your Monthly page changes to Week is reopened(

[Unmapped macro: inline-external-image — no content to fall back on]

).

## Related Articles

- ["Approval" Page and Process Overview](/cms_trial/space/7TFA/1253539865/Approvals/)