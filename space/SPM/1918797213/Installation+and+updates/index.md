# Installation and updates

## Before you start

- Important: before installing the app, visit  [Atlassian Marketplace](https://marketplace.atlassian.com/plugins/eu.softwareplant.bigpicture/versions) and check which Jira versions are compatible with BigPicture.
- To check for updates, make sure you have an Internet connection and check the Manage apps section of the Jira administration.
- We recommend backing up your Jira and checking the release notes for any known bugs and planned changes, such as migration to a new module.
- If you encounter any problems, use your backup, follow the [reporting procedure](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297667417), and provide us with Jira logs.
- We do not recommend a rollback to an earlier version. Use the backup and install the exact version that was installed when the backup was created.

After the BigPicture app is upgraded or enabled, the app runs a complete scope synchronization process of all existing active (not closed) Programs. As a result, there is an increased probability that all active Programs will be synchronized once a user wants to open a given Program and start working with it.

## Installing BigPicture in Jira

We recommend installing the app using Atlassian's Universal Plugin Manager, which will always install the latest version and - what's more important - the one compatible with your Jira instance.

You must be logged in as a Jira admin to install the app - go to Jira Administration → Manage apps → Find new apps; and search for "BigPicture.”

![contentId-1918797213](/cms_trial/assets/7ba18560-a33a-4263-996a-6918a20078b6.png)

Are you curious about BigPicture Enterprise? Click [here](https://appfire.atlassian.net/wiki/spaces/DOCUMENTATION/pages/275648486) to learn more about it!

## Manual installation

If your instance is not connected to the Internet, or you want to test a specific version, visit [this website](https://marketplace.atlassian.com/plugins/eu.softwareplant.bigpicture/cloud/versionhistory) to see all available versions. Be careful to choose the correct version for your Jira instance! When sure, click on the desired version to expand its row. Hit "Download" on the right-hand side.

The only thing left is to upload the file to Jira. This can be done in Jira Administration → Manage apps → Manage apps. Select "Upload app" on the right-hand side.

![contentId-1918797213](/cms_trial/assets/35c51b3d-fd75-44f3-8b8f-89bba137904a.png)![contentId-1918797213](/cms_trial/assets/95ec2258-a87a-4ca6-89a2-74b910a959aa.png)![contentId-1918797213](/cms_trial/assets/3b8716ea-8f5b-4638-bd80-27ff86067a8d.png)

Important: Note that some problems may occur with upgrading your tasks after an update between two app versions, e.g., 8.0.2 → 8.3.0. To ensure all of your functions are updated correctly, upload the intermediate versions and refresh the **Home page**.

## Example

1. Create a backup of your database.
2. Uninstall BigPicture from your Jira instance.
3. Download BigPicture version 8.1.12 from the [Marketplace](https://marketplace.atlassian.com/apps/1213016/biggantt-gantt-chart-for-jira?tab=overview&hosting=server), install it and proceed with any required steps to activate the app (such as upgrading the app database schema after opening it - go to the **Home** directory). If BigPicture works correctly in this version, please proceed to the next step. If there are any errors, please let us know about them and provide a new [Jira Support zip file](https://appfire.atlassian.net/wiki/spaces/DLP/pages/296981153).
4. Check if the app works properly in version 8.1.12 - if yes, please perform the upgrade to the newest version from *Jira Administration > Manage apps*. If there are any errors, please provide a new Jira Support zip file.

![contentId-1918797213](/cms_trial/assets/2b92f973-9eea-45b5-aef2-21db2e0cc435.png)

## BigPicture updates

From the 8.39.0 version, BigPicture is compatible with **Jira 10**. For more information, see the [Plugin compatibility](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=DLP&title=Plugin%20Compatibility.) page.

## Jira Cloud

BigPicture is always automatically updated to the latest version on Jira Cloud.

## Jira Data Center

Only Jira admins can update BigPicture. The update process varies depending on the version of BigPicture you have installed.

If you use BigPicture with [BigTemplate](https://marketplace.atlassian.com/apps/1215229/bigtemplate-export-to-pdf-word-excel?tab=overview&hosting=datacenter) or [BigPicture Enterprise](https://marketplace.atlassian.com/apps/1215158/bigpicture-enterprise?tab=overview&hosting=datacenter), you must update each application separately.

With version 8.0.19, release versions have been matched - the BigTemplate version matches the BigPicture and BigGantt versions. For example, if you are using BigPicture 8.0.19, the compatible version of BigTemplate is 8.0.19.

To find out more about compatibility, see the [Plugin Compatibility](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=DLP&title=Plugin%20Compatibility.) page.

### Before you begin

BigPicture **doesn’t support** rollbacks. When updating BigPicture, we **highly recommend** creating the following:

1. Database backup.
2. BigPicture backup (see the [Backup, restore and migration](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297047453) page for more information).   
   Jira and BigPicture store their data **separately**. Creating a BigPicture dump **IS NOT** a Jira backup.

Once you have backups ready, you need to check what BigPicture version you have installed:  
**Method 1:**

1. Go to **BigPicture** > **Get help icon** > **About App**.

   ![image-20241011-104720.png](/cms_trial/assets/6689da6b-b61d-4fa0-93bf-51a98e7e7851.png)
2. The version is displayed.

   ![image-20241011-104950.png](/cms_trial/assets/5ac77ce2-cea9-4182-95f4-d1dc9fd17cab.png)

**Method 2:**

1. Go to **Jira Administration** > **Manage apps**.
2. Select **Manage apps** on the left.
3. Locate BigPicture.

   ![image-20241017-072716.png](/cms_trial/assets/336ab9a2-327a-415f-b2fb-6d7153ec4817.png)
4. Expand the drop-down menu to see which BigPicture version is installed.

   ![image-20241011-104254.png](/cms_trial/assets/2e99e9cd-ac4d-4753-b13e-a52ec92b640c.png)

Depending on your version, follow the appropriate path described below.

### BigPicture versions before 8.1.12

#### Jira version 9 or higher

Java 17 **IS NOT** supported. You need to use Java 8 or 11.

If you are using the BigPicture version before 8.1.12 and Jira version 9 or higher, you need to install a modified version of BigPicture that isn’t available on the Atlassian Marketplace.

1. To get this version, contact our [Support](https://appfire.atlassian.net/servicedesk/customer/portal/11) team, who will assist you with the process.
2. Once you have that version, go to **Jira Administration** > **Manage apps**.
3. Select **Manage apps** on the left.
4. Click the **Upload app** button.   
   If you can’t see the **Upload app** button, you must enable it manually. For instructions, refer to the [How to re-enable plugin upload in Jira Data Center](https://confluence.atlassian.com/jirakb/how-to-re-enable-plugin-upload-in-jira-data-center-1364557898.html) article.

   Image — asset pipeline pending  
   image-20241017-085011.png
5. Choose a file and click **Upload**.

   Image — asset pipeline pending  
   image-20241017-084852.png
6. After the update is complete, go to BigPicture.
7. Perform a [database schema upgrade](https://appfire.atlassian.net/wiki/spaces/DLP/pages/300122393).
8. In case of any problems, contact our [Support](https://appfire.atlassian.net/servicedesk/customer/portal/11).
9. After a successful BigPicture update to version 8.1.12, you can now follow the steps in the **BigPicture version 8.1.12 or higher** section below.

#### Jira version before 9

If you are using BigPicture before 8.1.12 and Jira before 9, download BigPicture version 8.1.12 from the Atlassian Marketplace.

We recommend migrating BigPicture before migrating Jira to Jira 9 or 10.

1. Go to the [BigPicture version history](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm/version-history?versionHistoryHosting=dataCenter) on the Atlassian Marketplace.
2. Find BigPicture version 8.1.12.
3. Expand the drop-down and click **Download**.

   ![image-20241009-075016.png](/cms_trial/assets/e0340e73-f5cc-4828-b82e-2b2303060307.png)
4. When the file is downloaded, you need to upload it to Jira.
5. Go to **Jira Administration** > **Manage apps**.
6. Select **Manage apps** on the left.
7. Click the **Upload app** button.   
   If you can’t see the **Upload app** button, you must enable it manually. For instructions, refer to the [How to re-enable plugin upload in Jira Data Center](https://confluence.atlassian.com/jirakb/how-to-re-enable-plugin-upload-in-jira-data-center-1364557898.html) article.

   ![image-20241017-085011.png](/cms_trial/assets/de3b54dd-56ae-4c21-8d9b-36f14cbc172b.png)
8. Choose a file and click **Upload**.

   ![image-20241017-084852.png](/cms_trial/assets/9b50b8b9-0696-4a10-adc9-4f18c2bb5c77.png)
9. After the update is complete, go to BigPicture.
10. Perform a [database schema upgrade](https://appfire.atlassian.net/wiki/spaces/DLP/pages/300122393).
11. In case of any problems, contact our [Support](https://appfire.atlassian.net/servicedesk/customer/portal/11).
12. After a successful BigPicture update to version 8.1.12, you can now follow the steps in the **BigPicture version 8.1.12 or higher** section below.

### BigPicture version 8.1.12 or higher

If you are using the BigPicture version 8.1.12 or higher, you can:

- If compatible with Jira, update BigPicture to the latest version or
- Update BigPicture to the highest version compatible with your current Jira version (see the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm/version-history?versionHistoryHosting=dataCenter) to check compatibility)

#### Update to the latest version

To update BigPicture version 8.1.12 or higher to the latest version:

1. Go to **Jira Administration** > **Manage apps**.
2. Select **Manage apps** on the left.
3. Locate BigPicture.

   ![image-20241017-072716.png](/cms_trial/assets/336ab9a2-327a-415f-b2fb-6d7153ec4817.png)
4. Click the **Update** button next to BigPicture.
5. This will download and apply the latest version of the app. When finished, a success message appears.
6. After the update is complete, go to BigPicture.
7. Perform a [database schema upgrade](https://appfire.atlassian.net/wiki/spaces/DLP/pages/300122393).
8. In case of any problems, contact our [Support](https://appfire.atlassian.net/servicedesk/customer/portal/11).

#### Update to the highest version compatible with your current Jira version

To update BigPicture version 8.1.12 or higher to the highest version compatible with your current Jira version, you need to download that version from the [Version history](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm/version-history?versionHistoryHosting=dataCenter) page on the Atlassian Marketplace.

1. Go to the [BigPicture version history](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm/version-history?versionHistoryHosting=dataCenter) on the Atlassian Marketplace.
2. Find a version you want to update to.
3. Make sure the BigPicture version is compatible with your current Jira version.
4. Expand the drop-down and click **Download** next to that version.

   ![image-20241008-124404.png](/cms_trial/assets/350e9bb3-5ed7-485b-bac4-e2a642f3a742.png)
5. When the file is downloaded, you need to upload it to Jira.
6. Go to **Jira Administration** > **Manage apps**.
7. Select **Manage apps** on the left.
8. Click the **Upload app** button.   
   If you can’t see the **Upload app** button, you must enable it manually. For instructions, refer to the [How to re-enable plugin upload in Jira Data Center](https://confluence.atlassian.com/jirakb/how-to-re-enable-plugin-upload-in-jira-data-center-1364557898.html) article.

   ![image-20241017-085011.png](/cms_trial/assets/de3b54dd-56ae-4c21-8d9b-36f14cbc172b.png)
9. Choose a file and click **Upload**.

   ![image-20241017-084852.png](/cms_trial/assets/9b50b8b9-0696-4a10-adc9-4f18c2bb5c77.png)
10. After the update is complete, go to BigPicture.
11. Perform a [database schema upgrade](https://appfire.atlassian.net/wiki/spaces/DLP/pages/300122393).
12. In case of any problems, contact our [Support](https://appfire.atlassian.net/servicedesk/customer/portal/11).