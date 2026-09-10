# Mute notifications

You can mute SLA notifications either by selecting issues or SLAs using Time to SLA Issue Actions.

## How to mute notifications in the work item view

1. Go to the related work item and click the actions button at the top of the *Details* section.
2. Click **Time to SLA** **Issue Actions**.

   ![Time to SLA Mute notifications page with notification settings](/cms_trial/assets/b8632632-f367-46e1-bea0-2f4c77606400.png)
3. From the *Actions* dropdown menu, pick **Mute SLA**. The *Mute SLA Notifications* screen appears.

   ![Time to SLA Mute notifications dialog with mute options](/cms_trial/assets/8daf1791-5ee7-4b1e-9e2a-21196fb6ca7d.png)
4. In the *Mute Duration* section, select how long you want to mute notifications. You can mute notifications until they are manually unmuted with an action or choose an end date to unmute them automatically.

   - Click **Until Unmuted** if you want to unmute the work item with an action later.
   - Click **Custom** to pick an end date. When this date is reached, the work item will be unmuted automatically.
5. You can mute notifications by specifying work items. To do that, you have three options:

   - Muting all notifications by selecting all work items.
   - Muting notifications by selecting the work item keys. You can also add a work item key using the **Add item** button. Only recently viewed work items are listed here. To populate the combo box, you can use the `issuekey in issueHistory() order by lastViewed DESC` statement, which will filter issues.

     ![Time to SLA Mute notifications option in SLA panel](/cms_trial/assets/2d5af70b-7fd8-4936-aa89-b315e0feec09.png)
   - Muting notifications for work items filtered by the JQL statement you entered.

     ![Time to SLA Mute notifications confirmation message](/cms_trial/assets/edc9ef03-f4e0-4a14-ab9c-87b039a5114d.png)
6. You can mute notifications by specifying SLAs. To do that, you have two options:

   - Muting all notifications by selecting **All**.
   - Muting notifications by selecting specific SLAs.

     ![Time to SLA Mute notifications settings with user options](/cms_trial/assets/a9b7ea58-4f4a-4beb-9c64-f6e1a683d8ec.png)
7. Click the **Done** button, and your configurations will be saved.

## Manage muted SLA notifications

To review and manage your muted SLA notifications, click **Jira** **Settings** > **General Settings** > **Apps** > **TTS Mute SLA**.

![Time to SLA Mute notifications page with multiple notification rules](/cms_trial/assets/9f7e844e-2f23-4fa0-b502-571a5f854d4e.png)

Here, you can see all of your muted SLA notifications, edit them, and unmute them. You can also mute notifications using the same process described above.

![Time to SLA Mute notifications rule configuration details](/cms_trial/assets/4f630e9d-98e2-4a30-bee3-44124c252f82.png)