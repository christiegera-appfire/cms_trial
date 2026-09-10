# 7pace Timetracker for Azure DevOps Web App

Understand Web App activity check messages, track with non-DevOp items, track time from a work item, and what you'll see if tracking stops and why.

### 7pace Timetracker for Azure DevOps web app overview

The 7pace Timetracker for web app is built right into every single page of the web interface of Timetracker. It is available from within the web access of DevOps server/services and allows you to start tracking right from any work item, without any additional action required.

The web app works in conjunction with or separately from the 7pace Timetracker for Windows app. If you choose to download, install, and pair the Windows app, both work together as a team. If you close out of your web browser while tracking time with the web app, and you have the Windows app installed and paired, it will take over the job and continue tracking your time. Similarly, if you have both the web app and the Windows app running, clicking **Start Tracking** on one also starts tracking on the other (as well as on the *Details* tab's **Start Tracking** button functionality on the work item form). If you are only using the web app and do not have the Windows app, if you close out of 7pace Timetracker and then open it again on another browser or computer, tracking will still resume where you left off.

If you open any page in the 7pace Timetracker main web server extension, the web app displays at the top of each page (this screenshot shows the *Monthly* page):

![Monthly_Page.png](/cms_trial/assets/64c0dbdf-d041-4d81-8dfc-dd20acd6dcc4.png)

If you have previously tracked an item, the last item tracked is displayed. The prediction feature remembers the last ten items on which you last worked. Once you click anywhere on the gray tracker bar, the fields expand and display the following:

![Field_Expand.png](/cms_trial/assets/4a81c43a-0d59-4f21-a793-69b15745d21c.png)

| **No.** | **Description** |
| --- | --- |
| 1 | **Work Item**  The **Work Item** field allows you to enter a work item ID from the DevOps server/services or the task name. An administrator can set this to **Always require a work item** under **Settings** > **Rules**.  The ability to track time without associating it with specific work items is set to **ON** by default, which conveniently allows users to track time on non-work-related or impromptu items. You can change this on the *Settings* page of **7pace Timetracker** > **Rules** > **Tracking Details**.  When you click in this field, Timetracker displays the list of DevOps work items that you have been assigned, have tracked in the past, or the work items that are in progress.  If the ID is a valid work item, the tracker displays the following information in the highlighted section:   - The specified work item ID with a hyperlink that, when clicked on, opens the work item details in the DevOps server/services web access - The title of the work item - The project of the work item - The parent work item ID, if there is one, also with a hyperlink to DevOps web access   If it is not recognized in DevOps Server/Services, the list will be empty. DevOps_Server_Empty_List.png For a non-DevOps server/services work item, your administrator must ensure that under **Settings** > **Rules** > **Tracking Details**, the **Always require a work item** box is unchecked. Then, simply leave the **Work Item** field blank (the **Project** and **Parent** fields likewise, also blank). Click the **X** icon at the end of the **Work Item** field (see following screenshot) and write the title or description in the **Comment** field. You can then click **Start Tracking** on that non-DevOps server/services item. Rules_Tracking_Details.png |
| 2 | **Comment**  Additional information can be added to the **Comment** field. This field is optional, depending on if your administrator has set it as such under **Settings** > **Rules**. If you want to track a non-DevOps server/services work item, ensure that your administrator unchecks the **Always require a work item** box, then type in the item description in this field, leave the **Work Item** field blank, and then. click **Start Tracking**.  As soon as you select another work item, the **Comment** field is reset to empty. |
| 3 | **Activity Type**  (Optional) An **Activity Type** can be selected from the configured dropdown list.  As soon as you select another work item, the **Activity Type** dropdown is reset to the default activity type set in Configuration. |
| 4 | **Billable Hours**  Mark the worklog or track of time as billable or non-billable. |
| 5 | **Total**  Shows the total time you spent on this work item, including days other than today. |
| 6 | **Current Track Time**  Shows the current total time spent on the work item since you last clicked the **Start Tracking** button. |
| 7 | **Start Time**  Shows the start time of the current work item since you last clicked the **Start Tracking** button. |
| 8 | **Close**  Clicking this button minimizes the main tracker fields so that only the following is displayed on each 7pace Timetracker page: Close.png |
| 9 | **Start Tracking**/**Stop Tracking**  Clicking this button starts tracking the selected work item.  Once you click **Start Tracking** and tracking commences, the button changes to **Stop Tracking**. |
| 10 | **Start Tracking**/Time Tracked on Work Item Since **Start Tracking**  This button displays even when the expanded tracker fields are closed/minimized and serves as a reminder of how much time has been logged on the current work item since you clicked **Start Tracking**. When you click **Stop Tracking** once the fields are expanded, this button is then shown as **Start Tracking**. |
| 11 | **Today**  This field shows how much time you have tracked on the work item in the current day. |
| 12 | This field displays the **Activity Type** you have selected for the current time track. |
| 13 | These fields remain/display on every page of Timetracker when you click **Close** and minimize the expanded tracker fields. You can click anywhere within this gray section to expand or minimize the tracker fields. |
| 14 | **Tracking**  This field displays the work item on which you are currently tracking time. |

### 7pace Timetracker for Azure DevOps web app activity check settings

Under the *Settings* page of Timetracker, the [Time Tracking](https://appfire.atlassian.net/wiki/x/wYC3Sg#Time-Tracking) section allows an administrator to configure settings within the web app to prompt users, after a defined period of time, to respond as to whether or not they are still working.

#### Are you still working?

![Webapp_Activity_Check_Settings.png](/cms_trial/assets/c42b868a-8368-4e4b-af5d-704a33f4734d.png)

If you receive this prompt and select **Continue**, time tracking resumes without pause until you reach the configured threshold again. Additionally, once displayed, the message features a countdown, and after that countdown expires, the web app stops tracking and displays the *Tracking stopped - no response from the user during the activity check* message.

#### Tracking stopped - no response

![Tracking_Stopped.png](/cms_trial/assets/6c2cbbb7-33cb-4752-81a8-a576a7a19c17.png)

The countdown can also be set under the **Settings** > **Time Tracking** settings.

### Tracking time on a DevOps item with the 7pace Timetracker for the Azure DevOps web app - Web interface

1. Open any page in 7paceTimetracker.

The web app displays at the top of every page (this screenshot shows the *Monthly* page):

![Start_Tracking.png](/cms_trial/assets/5b8797bf-3429-4ff2-a16a-a66dc0d4100f.png)

If you have not logged any time with the web app in the current day yet, the **TODAY** field displays 00:00 (the **TODAY** field updates as you track time with the web app and reflects time tracked on all work items within the current calendar day). A *Your tracker is not currently running* message is displayed if you are not tracking time. If you have previously tracked an item, the last item you tracked is displayed on the minimized web app bar, and you can simply click the white **Start Tracking** button to resume tracking on it.

2. Click anywhere on the gray area of the tracker bar.

![Stop_Tracking.png](/cms_trial/assets/1fd5bf84-7153-42c5-8484-d570566550a1.png)

The web app fields expand and display.

3. Click in the **Work Item** field.

If you have previously worked on a work item(s), the prediction feature of the web app automatically populates the items you were previously working on or assigned in the **Work Item** field (it displays a maximum of ten items). The last item you tracked time on will be the default selection that displays first in the list.

The ability to track time without associating that time with specific work items is set to **ON** by default, as it conveniently allows users to track time on non-work-related or impromptu items. You can change this on the *Settings* page of **7pace Timetracker** > **Rules** > **Tracking Details**.

4. Select a previously-entered item in the **Work Item** field from the list or begin typing in a new item utilizing the Smart search feature.

Once selected, the **Project** and **Parent** fields are also populated (the **parent** field will be blank if it is the top-level item). The **Work Item** and **Parent** fields include item ID links that, when clicked, open the corresponding work item forms. When you click the **Work Item** ID, the item form opens. The **Start Tracking** button on the *Details* tab of that project also reflects that time tracking has commenced (see more information on tracking time within the work item form further down in this article).

![Work_Start_Tracking.png](/cms_trial/assets/23fa08d2-9ba7-4b44-8e41-ccc06b106c66.png)

5. Enter additional information in the **Comment** text field (this is optional, depending on what your administrator configured under **Settings** > **Rules**.

6. (Optional) Select an **Activity Type** from the dropdown list.

7. Click the **Start Tracking** button.

Time tracking commences.

Note that when you start tracking via the web app and also have the Windows app paired with your account, it begins tracking too. As mentioned above, if you open the work item form, it too will show tracking has commenced on the *Details* tab. All time tracking in Timetracker is synced.

7. Click the **Close** button.

The tracker fields are minimized, allowing you to continue your work. Once minimized, the current work item number and description displayed in the **Tracking** field, the **Activity Type** you selected (if any), the total length of time you have worked on this item in the current calendar day (**TODAY** field), and the current length of time you have tracked on the item since selecting **Start Tracking** (to the right of the **TODAY** field).

![Today_Field.png](/cms_trial/assets/f02ac76d-6017-4b84-971e-236b86789515.png)

### Tracking time on a non-DevOps server/services item with the 7pace Timetracker for Azure DevOps web app - Web interface

You can also track time on the Web App on non-DevOps Server/Services items, such as client/customer calls or meetings.

Ensure that your administrator has unchecked the **Always require a work item** box under **Settings** > **Rules** > **Tracking Details**. By default, the ability to track time without associating it with specific work items is set to **ON**, which conveniently allows users to track time on non-work-related or impromptu items.

1. In the **Work Item** field, if a DevOps server/services item is displayed, simply click the **x** icon at the end of the field.

![Work_Item.png](/cms_trial/assets/49a32ea8-9853-45e9-894b-6feb8d119822.png)

This clears out the **Work Item** field and displays it as blank:

![Work_Item_Blank.png](/cms_trial/assets/ce8dc9e6-7a9d-4f51-9ecc-19006fce72dd.png)

2. (Required) Enter additional information in the **Comment** text field. When the **Work Item** field is blank, the **Comment** field becomes required to start tracking time.

3. (Optional) Select an **Activity Type** from the dropdown list.

4. Click the **Start Tracking** button.

Time tracking commences.

### Tracking time with the 7pace Timetracker for Azure DevOps web app - Work item form

You can find the **Start Tracking** button on the work item [Details page](https://appfire.atlassian.net/wiki/x/wYC3Sg#Time-Tracking) when you open any item to view or edit.

To see how to start tracking from the work item form, click [here](https://appfire.atlassian.net/wiki/x/FIC3Sg#Work-Items%3A-Start-Tracking-and-Add-Time).

Tracking from here also initiates tracking to commence on the web app.

### Automatic tracking stopped messages

The following reasons can cause tracking to pause or stop on the Timetracker web app:

#### Tracking stopped - track length exceeded

Under Settings > [Time Tracking](https://appfire.atlassian.net/wiki/x/wYC3Sg#Time-Tracking), an administrator can set a number, in hours, at which the web app stops tracking once this number of hours is exceeded. When you cross that threshold, time tracking stops, and the following message is displayed:

![Track_Length_Exceed.png](/cms_trial/assets/9efa4061-4f3a-4d91-b1c0-82081f212998.png)

#### Tracking stopped - entry edited or deleted by you

 If you edits or deletes the current time track (on the *Times Explorer* page, for example), tracking will stop on that work item, and the following message will be displayed:

![Entry_Edit_Delete.png](/cms_trial/assets/fbf8f0f4-516b-4883-b564-972231e120d1.png)

#### Connection to server lost

If the web app loses connection due to some kind of network issue, the following message is displayed. Note that time tracking does not stop in this case and continues in the background until connectivity has been re-established.

![Connection_Server_Lost.png](/cms_trial/assets/63046cf7-6044-454d-9c0d-dbf58e7cb697.png)