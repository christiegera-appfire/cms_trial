# Settings (Cloud)

This page is about **Planning Poker for Jira Cloud**. Using **DC**? [**Click here**](/cms_trial/space/PP/1144061984/Planning+Poker+for+Jira+Data+Center/).

This page outlines the configuration options for Planning Poker for Jira Cloud.

### How to access global settings

1. Navigate to **Apps** > **Manage your apps**.
2. Find Planning Poker in the apps list, and click **Configure**.

   ![Screenshot 2024-07-29 at 14.26.46.png](/cms_trial/assets/c9091977-606c-46c4-9dd5-25512f344646.png)

- **Limit access to specific user groups –** Use this setting to restrict access to the app for specific user groups in Jira. Users outside those groups will see a "Sorry, you don't have permissions for Planning Poker" message upon trying to access it. Keep in mind that default Jira admin groups always have access.
- **Enable estimation from issue details –** Activate the Planning Poker tab and perform estimations within the issue view for all Jira users. You'll need to select an estimation field and a card deck. Project admins can still disable or enable this feature at the project level.

### How to access project settings

1. Navigate to a project.
2. From the side menu, click **Project settings** > **Planning Poker**.

   ![image-20240729-112946.png](/cms_trial/assets/e6c5c457-7842-4445-a284-b7c981319c7a.png)

- **Show Planning Poker in board menu –** Determines whether the Planning Poker tab appears in the issue view. Uncheck to hide it.
- **Enable estimation from issue details –** Overrides the global setting. Enable this option to allow estimation directly from the issue view for this specific project.
- **Inherit global settings for estimating from issue details –** Use the global settings for the estimation field and card deck instead of configuring them at the project level.

Changes to global settings will automatically apply to all projects that inherit them.