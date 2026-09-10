# Manual script migration

Power Scripts will be unavailable during scheduled maintenance on August 8-9, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

This page explains the steps for manually migrating your SIL scripts from Jira Server/Data Center (Jira DC) to Jira Cloud.

While migrating scripts and settings from Jira Server/Data Center to Jira Cloud can be done manually, there are automation tools that can help with large script volumes. In such cases, we can provide assistance with the script migration process. See [how to get help](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15481538).

## Prerеquisites

Your Power Scripts and SIL Engine version must be 5.8.0.0 or higher.

## Procedure

1. Export all scripts from your Jira Server or DC instance.

   1. Open the SIL Manager and right-click the **silprograms** folder.
   2. From the dropdown menu that opens, select **Download**.

      ![This screenshot shows the Download menu that opens after right-clicking on the silprograms folder in the SIL Manager.](/cms_trial/assets/13a45902-6d25-4a08-86c2-0d5cb8c860c0.png)
2. Install Power Script for Jira Cloud on your target cloud instance.
3. From the application server running Jira, create a zip file of the **silprograms** directory found in the Jira Home folder.
4. In your Jira Cloud instance:

   1. Navigate to the **Apps** > **Power Scripts** > **Self Help** page.
   2. Select the **Backup/Restore** tab.
   3. Upload the zip file.

![This screenshot shows the Self Help page open on the Backup-Restore tab where the Upload button is located.](/cms_trial/assets/e9240197-efbf-4c3d-9d96-4141cac563bf.png)

Your SIL scripts are now migrated to the new Jira Cloud instance.