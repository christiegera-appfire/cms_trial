# Installation guide

## Supported Jira Cloud plans

You **must** have either the*Standard*, *Enterprise*, or *Premium* cloud plan on both Jira Cloud sites. Trial and paid licenses of these three types are supported. Migrations and configuration deployments to Jira Cloud on the*Free* plan are **not supported**.

[Learn more about the Jira Cloud plans](https://support.atlassian.com/jira-cloud-administration/docs/explore-jira-cloud-plans/)

## Install Configuration Manager for Jira (CMJ) Cloud

You can use **Configuration Manager for Jira (CMJ) Cloud** to deploy configurations between Jira Cloud sites. For this, you need to install the app on both the source and destination Jira Cloud sites.For more information, read the[use case](/cms_trial/space/CMJC/258053021/Deploy+configuration+changes+from+Jira+Cloud+to+Cloud/) document.

**License tokens needed**

To use CMJ Cloud, you need two license tokens:

- one for the source Jira Cloud site, and
- one for the destination site.

Appfire will provide you with these tokens upon purchase.

**To install the CMJ Cloud app on a Jira Cloud site:**

1. Log into your Jira Cloud site as an administrator with the **Jira System Administrators**and **Site admin** or **Organization admin** permissions.
2. From Jira's top navigation bar, choose **Settings > Apps**.
3. In the **Find new apps** page, search by the **Configuration Manager for Jira Cloud** name.

   ![contentId-194183182](/cms_trial/assets/e5edb924-e1d7-48da-b51b-23486ba7e3f9.PNG)
4. Try the app with a **Free trial** for 30 days orenter a license token in the **Access token** field in the app space.

   ![contentId-194183182](/cms_trial/assets/25b3e70d-7ac8-4309-9009-f21f6ed9fc49.PNG)

After installing CMJ Cloud, you can visit its Get Started page under **Apps > Configuration Manager**. The page contains information about the cloud-to-cloud configuration deployment and the server-to-cloud migration use cases.

## Upgrade Configuration Manager for Jira (CMJ) Cloud

**Automatic and manual updates**

If the released CMJ Cloud changes do not require manual approval, they are deployed to your instances automatically.

However, if the app changes need manual approval, each instance will show that an update is available to the latest version of CMJ Cloud. Then, you will have to approve and update the app manually.

**To update Configuration Manager for Jira Cloud:**

1. Log into your Jira Cloud site as an administrator with the **Jira System Administrators**and **Site admin** or **Organization admin** permissions.
2. From Jira's top navigation bar, choose **Settings**.
3. Select **Apps**and then open the **Manage apps** page.
4. Locate **Configuration Manager for Jira Cloud** in the list of apps**.**
5. Click the **Update** button next to its name.

## Migratе from Jira Server/DC to Jira Cloud

You can also use Configuration Manager for Jira (CMJ) Cloud to migrate projects and issues from a Jira Server/DC instance to a Jira Cloud site.

**Which apps must you install to migrate from Jira Server/DC to Cloud?**

To migrate projects and issues from Jira Server/Data Center to Jira Cloud, you'll need to install two apps and create a connection between them. Here are the steps:

1. Install the [Cloud Migration Tool](https://marketplace.atlassian.com/apps/1224900/configuration-manager-cloud-migration-tool?tab=overview&hosting=datacenter) on your Jira Server or Data Center instance.
2. Install [Configuration Manager for Jira (CMJ) Cloud](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) on your Jira Cloud site.
3. Create a [connection](https://appfire.atlassian.net/wiki/spaces/CMT/pages/197856330) between the two apps.
4. Follow the migration process in the Cloud Migration Tool's UI, as described in our [guides](https://appfire.atlassian.net/wiki/spaces/CMT/pages/197856030).

For more information, please refer to the [Migrate Projects and Issues to Jira Cloud](https://appfire.atlassian.net/wiki/spaces/CMT/pages/197922405) document.

Visit [Cloud Migration Tool's documentation](https://appfire.atlassian.net/wiki/spaces/CMT) to learn more about migrating projects and issues from Jira Server or Data Center to Jira Cloud.