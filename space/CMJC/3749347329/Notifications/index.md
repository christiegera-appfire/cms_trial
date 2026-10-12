# Notifications

Some CMJ Cloud operations can take time to complete. Notifications let you continue working without having to keep checking CMJ Cloud to see whether an operation has finished.

You can receive Slack notifications when CMJ Cloud finishes creating a snapshot or while processing a snapshot deployment. Each notification tells you whether the operation **succeeded, failed,** or was **canceled**.

Notifications are currently available for:

- Snapshot creation
- Snapshot deployment
- Analysis
- Transformations

Before you can use notifications with snapshots or deployments, you need to configure at least one Slack notification.

![Slack-notifications.png](/cms_trial/assets/b404b545-95ae-4dcb-ad9c-838c42554255.png)

## Set up a Slack notification

Notifications are managed from *Settings > Notifications*.

The Notifications tab lists notifications you have already configured. From here, you can create new notifications or delete ones you no longer need.

![Notifications-tab.png](/cms_trial/assets/6c7dc9bf-2760-45fa-8f6e-ddb5dc9c1dff.png)

To create a notification:

1. Go to *Settings > Notifications*.
2. Select **New notification**.
3. Enter a **Name** for the notification.
4. In **URL**, enter the Slack webhook URL you want CMJ Cloud to use.
5. Select **Test connection**.

   If CMJ Cloud can connect successfully, a **Connection successful** message appears, and a test notification is sent to Slack.
6. Select **Create**.

![Add-notification.png](/cms_trial/assets/9f537145-23b0-4287-a0e3-1e607a743787.png)

You can now select the notification when creating snapshots or deployments.

### Delete a notification

You can remove notifications in the *Notifications* tab by selecting the trash ([delete2 icon]) icon in the *Actions* column for the notification you no longer need.

## Get notified when a snapshot is created

You can select a notification each time you create a snapshot.

When taking a snapshot, use the **Notification** field to select one of your configured notifications.

![Notification-field-SC.png](/cms_trial/assets/4dbc2d5c-1138-4267-b36a-f0de8f778b97.png)

The selected notification applies only to that snapshot creation and not to any future snapshot versions within this same scope. You can set up the [scope’s notifications](#Set-a-default-notification-for-a-snapshot-scope) later. When the snapshot creation finishes, CMJ Cloud sends a Slack notification indicating whether it succeeded, failed, or was canceled.

If the notification you need hasn't been configured yet, select **Add** next to the Notification field. Enter a name and Slack webhook URL, test the connection, and create the notification without leaving the snapshot workflow.

![Add-notification-SC.png](/cms_trial/assets/5f8f8161-a315-4287-a721-873631031ae9.png)

### Set a default notification for a snapshot scope

If you want notifications for every new snapshot version created from the same scope, you can set a default notification for the snapshot scope.

From the *Snapshot Scope* summary screen, select the **Notification** (🔔) button between the **Schedule** (🗓️ ) and **Close** (X) buttons.

Select the notification you want to use and select **Save**.

![Snapshot-scope.png](/cms_trial/assets/1bc3afb5-9083-44e1-8b1e-ecf1ccd4ddbe.png)

The selected notification becomes the default whenever you create another snapshot version from that scope.

You can still select a different notification from the **Notification** field when creating a new snapshot version. That selection applies only to that snapshot creation and doesn't change the default notification for the scope.

If no notification is set for the scope, you can still select one when creating a new snapshot version.

## Get notified about a snapshot deployment

You can receive notifications throughout a snapshot deployment.

When creating a deployment, select a configured notification from the **Notification** field on the first *New deployment* screen.

![Notification-field-SD.png](/cms_trial/assets/17d7841b-cccd-42fa-b2a0-8388213c79d0.png)

If you need to create another notification, select **Add** next to the Notification field and configure it without leaving the deployment workflow.

![Add-notification-SD.png](/cms_trial/assets/ee6fa1cf-775b-48f2-977c-e80c4d7a58ae.png)

Unlike snapshot creation, the notification selected here applies to the entire deployment process. You receive notifications as CMJ Cloud completes:

1. Analysis
2. Transformations
3. Snapshot deployment

Each operation sends its own notification and reports whether it **succeeded, failed,** or was **canceled**.

## What information is included in a notification?

Slack notifications identify the CMJ Cloud operation and its outcome.

Depending on the operation and outcome, the notification can include information such as:

- the operation performed;
- the operation ID;
- the Jira site;
- the completion time; and
- error information when an operation fails.