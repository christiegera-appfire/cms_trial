# Mute notifications

You can mute SLA notifications either by selecting issues or SLAs using Time to SLA Issue Actions.

## How to mute notifications in the work item view

1. Go to the related work item and click the actions button at the top of the *Details* section.
2. Click **Time to SLA** **Issue Actions**.

   Image — asset pipeline pending  
   Time to SLA Mute notifications page with notification settings
3. From the *Actions* dropdown menu, pick **Mute SLA**. The *Mute SLA Notifications* screen appears.

   Image — asset pipeline pending  
   Time to SLA Mute notifications dialog with mute options
4. In the *Mute Duration* section, select how long you want to mute notifications. You can mute notifications until they are manually unmuted with an action or choose an end date to unmute them automatically.

   - Click **Until Unmuted** if you want to unmute the work item with an action later.
   - Click **Custom** to pick an end date. When this date is reached, the work item will be unmuted automatically.
5. You can mute notifications by specifying work items. To do that, you have three options:

   - Muting all notifications by selecting all work items.
   - Muting notifications by selecting the work item keys. You can also add a work item key using the **Add item** button. Only recently viewed work items are listed here. To populate the combo box, you can use the `issuekey in issueHistory() order by lastViewed DESC` statement, which will filter issues.

     Image — asset pipeline pending  
     Time to SLA Mute notifications option in SLA panel
   - Muting notifications for work items filtered by the JQL statement you entered.

     Image — asset pipeline pending  
     Time to SLA Mute notifications confirmation message
6. You can mute notifications by specifying SLAs. To do that, you have two options:

   - Muting all notifications by selecting **All**.
   - Muting notifications by selecting specific SLAs.

     Image — asset pipeline pending  
     Time to SLA Mute notifications settings with user options
7. Click the **Done** button, and your configurations will be saved.

## Manage muted SLA notifications

To review and manage your muted SLA notifications, click **Jira** **Settings** > **General Settings** > **Apps** > **TTS Mute SLA**.

Image — asset pipeline pending  
Time to SLA Mute notifications page with multiple notification rules

Here, you can see all of your muted SLA notifications, edit them, and unmute them. You can also mute notifications using the same process described above.

Image — asset pipeline pending  
Time to SLA Mute notifications rule configuration details