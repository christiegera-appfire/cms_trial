# TTS work item actions

The Time to SLA work item actions feature lets you perform work-item-specific actions without changing SLA configurations for all work items, such as reset, recalculate, or troubleshoot SLAs, and manage SLA notifications.

Refer to the tutorial below to get an overview:

## How to access Time to SLA work item actions

1. Open the work item you want to manage in Jira Cloud.
2. Click the actions icon at the top of the **Details** section.
3. Select **Time to SLA issue actions** from the dropdown menu. A dialog appears.

   ![Time to SLA work item actions page with SLA action list](/cms_trial/assets/3f21c042-e2f9-4292-aedd-f2ee94237a33.png)
4. Click the **Actions** dropdown menu to view your options.

   ![Time to SLA work item actions dialog for start SLA action](/cms_trial/assets/646001cd-f9ca-439f-810b-88611723d206.png)

### Available actions

All of these actions, except for *Mute SLA*, are **work item-specific**. Using them won’t affect any other work items or their SLAs.

#### **Reset SLA**

Reset SLAs for the selected work item. The resets you define in this section won’t interfere with the ones you’ve defined in SLA configurations.

1. Select **Reset SLA** from the *Actions* dropdown menu.
2. Choose the SLA(s) to reset.

   ![image-20260827-150054.png](/cms_trial/assets/43615319-701f-4af6-99c8-5732d43d765d.png)
3. Select a reset date, or leave it blank to reset immediately.
4. Define how the reset action should behave for completed SLAs.
5. Enter a reason for the reset. Depending on your app settings, this field may be required.
6. Click **Proceed**.

#### **Undo Reset SLA**

Revert a previously executed reset action for SLAs.

1. Select **Undo Reset SLA** from the *Actions* dropdown menu.
2. Choose the SLA(s) to undo the reset.

   ![image-20260827-150320.png](/cms_trial/assets/a9b97c31-69d5-47be-9b4b-03ac84dde039.png)
3. Click **Undo**.

#### **Where is my SLA?**

Diagnose why the SLA panel is not visible on a work item.

1. Select **Where is my SLA?** from the *Actions* dropdown menu.
2. Choose the SLA(s) you want to investigate.

   ![Time to SLA work item actions configuration with action rules](/cms_trial/assets/185e391c-ff0f-4c0e-9c1c-db545c7081ea.png)
3. Optionally, select a user to perform the action (leave blank to use your own account).
4. Click **Search**. The results appear.
5. Review the results to identify and resolve configuration issues.

#### **Recalculate SLA**

Recalculate SLA data for the selected issue.

1. Select **Recalculate SLA** from the *Actions* dropdown menu.
2. Choose specific SLA(s) to recalculate, or apply the action to all SLAs.

   ![Time to SLA work item actions dialog for SLA action details](/cms_trial/assets/ec4dfeab-a5ca-46df-bf08-65f8bd86fcfb.png)
3. Click **Proceed**.

The page will refresh automatically after recalculation.

#### **Mute SLA**

Mute SLA notifications for the selected work item. To learn how, refer to [this documentation](/cms_trial/space/TTSC/169978040/Mute+notifications/).