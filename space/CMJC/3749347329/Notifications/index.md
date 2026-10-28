# Notifications

Some CMJ Cloud operations can take time to complete. Notifications let you continue working without having to keep checking CMJ Cloud to see whether an operation has finished.

You can receive Slack notifications when CMJ Cloud finishes creating a snapshot or while processing a snapshot deployment. Each notification tells you whether the operation **succeeded, failed,** or was **canceled**.

Notifications are currently available for:

- Snapshot creation
- Snapshot deployment
- Analysis
- Transformations

Before you can use notifications with snapshots or deployments, you need to configure at least one Slack notification.

## Set up a Slack notification

Notifications are managed from **Settings** *>* **Notifications**.

The *Notifications* tab lists notifications you have already configured. From here, you can create new notifications or delete ones you no longer need.

![Notifications tab showing configured Slack notifications and available actions.](/cms_trial/assets/90561929-0602-448f-8178-9d54ab58d0b0.png)

To create a notification:

1. Go to **Settings** *>* **Notifications**.
2. Select **New notification**.
3. Enter a **Name** for the notification.
4. In **URL**, enter the Slack webhook URL you want CMJ Cloud to use.
5. Select **Test connection**.

   If CMJ Cloud can connect successfully, a **Connection successful** message appears, and a test notification is sent to Slack.
6. Select **Create**.

![Notification configuration form with name, webhook URL, and connection test controls.](/cms_trial/assets/15f966b5-50a3-4d01-bca2-5ec980ce4c56.png)

You can now select the notification when creating snapshots or deployments.

### Delete a notification

You can remove notifications in the *Notifications* tab by selecting the trash ([delete2 icon]) icon in the *Actions* column for the notification you no longer need.

## Get notified when a snapshot is created

You can select a notification each time you create a snapshot.

When taking a snapshot, use the **Notification** field to select one of your configured notifications.

![Snapshot scope screen showing the notification settings.](/cms_trial/assets/3a3485d6-d55e-4415-a986-adc02ee2b22c.png)

The selected notification is used for the current snapshot creation and automatically becomes the default notification for the snapshot scope. This means it will also be used for future snapshot versions created from the same scope, [unless you change it](#Change-the-default-notification-for-a-snapshot-scope). When the snapshot creation finishes, CMJ Cloud sends a Slack notification indicating whether it succeeded, failed, or was canceled.

If the notification you need hasn't been configured yet, select **Add** next to the Notification field. Enter a name and Slack webhook URL, test the connection, and create the notification without leaving the snapshot workflow.

![Form for adding a Slack notification during snapshot creation.](/cms_trial/assets/06471ff2-4df4-40c1-9f76-01a0e9e47589.png)

### Change the default notification for a snapshot scope

To change the default notification for a snapshot scope, open the *Snapshot Scope* summary screen by using the **Notification** (🔔) button between the **Schedule** (🗓️ ) and **Close** (X) buttons.

Select the notification you want to use and click **Save**.

![Snapshot Scope summary screen showing the Notification button used to configure a default notification.](/cms_trial/assets/359818e2-9d28-48ca-b7e6-0b0c3f11eae7.png)

The selected notification becomes the default for future snapshot versions created from that scope.

## Get notified about a snapshot deployment

You can receive notifications throughout a snapshot deployment.

When creating a deployment, select a configured notification from the **Notification** field on the first *New deployment* screen.

![New deployment screen showing the Notification field for selecting a Slack notification.](/cms_trial/assets/ed93752e-47ea-4aa4-8c04-ac7dd2cfe81b.png)

If you need to create another notification, select **Add** next to the Notification field and configure it without leaving the deployment workflow.

![Form for adding a Slack notification during deployment creation.](/cms_trial/assets/8b9b0025-5e1b-4111-a57a-798c2f020508.png)

The selected notification applies to the entire deployment process. You receive notifications as CMJ Cloud completes:

1. Analysis
2. Transformations
3. Snapshot deployment

Each operation sends its own notification and reports whether it **succeeded, failed,** or was **canceled**.

## What information is included in a notification?

Slack notifications identify the CMJ Cloud operation and its outcome.

Depending on the operation and outcome, the notification can include information such as:

- The operation performed
- The operation ID
- The Jira site
- The completion time
- Error information when an operation fails