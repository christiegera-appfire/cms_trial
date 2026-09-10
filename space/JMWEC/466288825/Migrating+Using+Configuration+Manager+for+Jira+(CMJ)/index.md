# Migrating Using Configuration Manager for Jira (CMJ)

The JMWE app has an automated migration path and can be migrated from **Jira Server/Data Center** (JMWE version 7.2.0 and later) using [**Configuration Manager for Jira (CMJ)**](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira?tab=overview&hosting=cloud) along with the free tool [**Configuration Manager Cloud Migration Tool**](https://marketplace.atlassian.com/apps/1224900/configuration-manager-cloud-migration-tool?tab=overview&hosting=server). Be aware that JMWE’s Cloud migration using CMJ is currently in beta, so you may wish to test the JMWE migration in a trial/test Cloud instance.

**BEFORE YOU BEGIN**

- You **must have either the Standard, Enterprise, or Premium** *Cloud plan*. Trial or paid licenses of these three types are supported. Migrations to **Jira Cloud on the Free plan are not supported**.
- Please be sure to review all [Configuration Manager for Jira (CMJ) documentation](https://appfire.atlassian.net/wiki/spaces/CMJ) and [Configuration Manager Cloud Migration Tool documentation](https://appfire.atlassian.net/wiki/spaces/CMT) for details on the migration process.
- Note that migration of JMWE using CMJ is still in Beta; while every effort has been made to migrate all JMWE configurations **the process is not 100% comprehensive**. Some manual updates will be required!
- The migration process is **not aware of context** - when migrating a single project, you will encounter many warnings!

**Note:** If you have already migrated to the Cloud and need information regarding how to fix errors, see the [Post Migration page](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458196147).

![JMWE for Jira Cloud Configuration Manager migration home interface](/cms_trial/assets/a19dbe62-c31b-427e-a9c3-d3fcb0441bce.png)

## Start the Migration

Before preparing your Data Center/Server instance for migration, verify that **Configuration Manager for Jira (CMJ)** and **Configuration Manager Cloud Migration Tool** are both installed!

For full details on how to migration to Jira Cloud using **Configuration Manager Cloud Migration Tool**, see [Migrations](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CMT&title=Migrations).

The migration process starts on your Jira Data Center/Server instance, where you must prepare your data for migration.

To being the migration, follow these steps:

1. Log into your Jira Data Center/Server instance as an Administrator.
2. From the **Administration** menu ( ⚙️ ) click **Configuration Manager**.
3. In the left-hand panel click **Move to Jira Cloud**. The migration page will open (Figure 1, right).
4. Follow the migration instructions available here to create a Cloud connection, build a migration, and complete the migration.
5. The following sections will detail any special considerations for JMWE in each of the major steps of the migration process.

## Create a cloud connection

There are no special considerations for **JMWE** when creating a cloud connection.

## Create a migration

JMWE Extensions, including **Shared Extensions**, **Scheduled Actions**, and **Event-based Actions**, will be added to your migration automatically when you add a project in which the extension is used in that project’s Workflow. You do not need to add JMWE extensions manually.

## Check the completed migration

![JMWE for Jira Cloud postmigration results dashboard with configuration data](/cms_trial/assets/948793d9-c20e-421b-b6dd-3f504cec0db0.png)

When the JMWE app migration is shown as complete in JCMA on your Jira Data Center/Server instance, open your Jira Cloud instance. Navigate to the JMWE app pages. If there are any migration issues requiring your attention, you are notified on the JMWE Overview page.

Click the **Take action** link in the notification box to proceed directly to the **Post Migration** page. Alternatively, you can select **Post Migration** at the bottom of the left navigation. This page and page link only displays if you have migrated JMWE data from Jira Server or Data Center to Jira Cloud.

The Post Migration page will list any extensions that encountered warnings or errors during migration, and you can open the extension directly by clicking the **Edit** button to the right of the extension in the list. The Post Migration page is organized into four tabs:

- **JMWE extensions** - Extensions grouped by their Workflow; use the pulldown menu at the top of the list to view any extensions that have errors or warnings.

**Note**: Currently, only workflow extensions can be migrated using **CMJ**. Shared actions, Scheduled actions, and Event-based actions will **not be migrated**.

Additionally, you can filter the list using the **Group by** and **Show Prolem(s)** toggles to the right of the list. You can group by Transition or by Extension type, and you can display either a Summary or Details of the issue.