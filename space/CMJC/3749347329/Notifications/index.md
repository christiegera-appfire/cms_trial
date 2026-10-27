# Notifications

Some CMJ Cloud operations can take time to complete. Notifications let you continue working without having to keep checking CMJ Cloud to see whether an operation has finished.

You can receive Slack notifications when CMJ Cloud finishes creating a snapshot or while processing a snapshot deployment. Each notification tells you whether the operation **succeeded, failed,** or was **canceled**.

Notifications are currently available for:

- Snapshot creation
- Snapshot deployment
- Analysis
- Transformations

Before you can use notifications with snapshots or deployments, you need to configure at least one Slack notification.

![Example Slack notification showing the outcome of a CMJ Cloud operation.](/cms_trial/assets/8be5ae42-263f-4f23-8b1d-3b75f1af6cf5.png)

## Set up a Slack notification

Notifications are managed from **Settings** *>* **Notifications**.

The *Notifications* tab lists notifications you have already configured. From here, you can create new notifications or delete ones you no longer need.

![Notifications tab showing configured Slack notifications and available actions.](/cms_trial/assets/90dabf0d-15ee-4c07-a346-d29aa0291e35.png)

To create a notification:

1. Go to **Settings** *>* **Notifications**.
2. Select **New notification**.
3. Enter a **Name** for the notification.
4. In **URL**, enter the Slack webhook URL you want CMJ Cloud to use.
5. Select **Test connection**.

   If CMJ Cloud can connect successfully, a **Connection successful** message appears, and a test notification is sent to Slack.
6. Select **Create**.

![Notification configuration form with name, webhook URL, and connection test controls.](/cms_trial/assets/78b6c749-6283-4b99-80be-98e509def6a9.png)

You can now select the notification when creating snapshots or deployments.

### Delete a notification

You can remove notifications in the *Notifications* tab by selecting the trash ([delete2 icon]) icon in the *Actions* column for the notification you no longer need.

## Get notified when a snapshot is created

You can select a notification each time you create a snapshot.

When taking a snapshot, use the **Notification** field to select one of your configured notifications.

![Snapshot scope screen showing the notification settings.](/cms_trial/assets/0cdadef1-4084-4081-b95c-379e85501dad.png)

The selected notification is used for the current snapshot creation and automatically becomes the default notification for the snapshot scope. This means it will also be used for future snapshot versions created from the same scope, [unless you change it](#Change-the-default-notification-for-a-snapshot-scope). When the snapshot creation finishes, CMJ Cloud sends a Slack notification indicating whether it succeeded, failed, or was canceled.

If the notification you need hasn't been configured yet, select **Add** next to the Notification field. Enter a name and Slack webhook URL, test the connection, and create the notification without leaving the snapshot workflow.

![Form for adding a Slack notification during snapshot creation.](/cms_trial/assets/22f754e2-3f2a-41b8-9f41-dbd0ec41eb2b.png)

### Change the default notification for a snapshot scope

To change the default notification for a snapshot scope, open the *Snapshot Scope* summary screen by using the **Notification** (🔔) button between the **Schedule** (🗓️ ) and **Close** (X) buttons.

Select the notification you want to use and click **Save**.

![Snapshot Scope summary screen showing the Notification button used to configure a default notification.](/cms_trial/assets/41d3a868-0991-4d96-81ea-5b9e8c1ae941.png)

The selected notification becomes the default for future snapshot versions created from that scope.

## Get notified about a snapshot deployment

You can receive notifications throughout a snapshot deployment.

When creating a deployment, select a configured notification from the **Notification** field on the first *New deployment* screen.

![New deployment screen showing the Notification field for selecting a Slack notification.](/cms_trial/assets/2b0eeedb-3420-4fce-8d49-0710b25a0e96.png)

If you need to create another notification, select **Add** next to the Notification field and configure it without leaving the deployment workflow.

![Form for adding a Slack notification during deployment creation.](/cms_trial/assets/8b7e109c-44dc-4a2d-a152-867c807539d5.png)

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