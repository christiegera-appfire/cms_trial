# Migrating using Jira Cloud Migration Assistant (JCMA)

The JMWE app has an automated migration path and can be migrated from **Jira Server/Data Center** (JMWE version 7.2.0 and later) using **Jira Cloud Migration Assistant (JCMA)**. Be aware that JMWE’s Cloud migration may not migrate all of your extensions identically, so you should test the JMWE migration in a trial/test Cloud instance.

**BEFORE YOU BEGIN**

- Please be sure to review all [Jira documentation](https://support.atlassian.com/migration/docs/jira-cloud-migration-assistant/) for the migration process.
- Note that migration of third-party apps using JCMA is still in Beta; while every effort has been made to migrate all JMWE configurations **the process is not 100% comprehensive**. Some manual updates will be required!
- The migration process is **not aware of context** - when migrating a single project, you will encounter many warnings!

![A screenshot of the Migration Assistant page.](/cms_trial/assets/75fde98f-32cf-406f-ab06-87136deed58c.png)

**Note:** If you have already migrated to the Cloud and need information regarding how to fix errors, see the [Post Migration page](/cms_trial/space/JMWEC/465473765/Post+migration/).

## Start the Migration

Before preparing your Data Center/Server instance for, verify that **Jira Cloud Migration Assistant** is installed!

The migration process starts on your Jira Data Center/Server instance, where you must prepare your data for migration.

To begin the migration, follow these steps:

1. Log into your Jira instance as an Administrator.
2. From the **Administration** menu ( ⚙️ ) click **System**.
3. In the left-hand panel, scroll down to *IMPORT AND EXPORT*and click **Migrate to cloud**. The Migration Assistant home page will open (Figure 1, right).
4. The following sections will detail any special considerations for JMWE in each of the major steps of the migration process.

## Assess your apps

![Jira Misc Workflow Extension showing the Needed in cloud status.](/cms_trial/assets/2c95ae92-7fcc-45a8-9477-7ad0b087be62.png)

During the [**Assess your apps**](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/#1.-Assess-your-apps) [step](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/#1.-Assess-your-apps), make sure that you have marked Jira Misc Workflow Extensions status as **Needed in cloud** (Figure 2, right). If a green check does not appear, you will need to upgrade to version 7.2.0 or later of JMWE [Server](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe?tab=versions&hosting=server) or [Data Center](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe?tab=versions&hosting=datacenter) to migrate using JCMA.

You can check the compatibility of your extensions using the **View differences** link, or you can see the feature comparison between Data Center/Server and Cloud [here](/cms_trial/space/JMWEC/465473954/Feature+Comparison+-+JMWE+Data+Center+vs.+JMWE+Cloud/).

When you have determined the migration status of all of your installed apps, click **Done**.

## Prepare your apps

During the[**Prepare your apps**](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/#2.-Prepare-your-apps) [step](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/#2.-Prepare-your-apps), the migration process will verify that **JMWE for Jira Cloud** is installed on the destination Jira Cloud instance. You must be an Administrator on **both** the source Data Center/Server instance and the destination Cloud instance. Selecting your destination cloud instance will require that you input the base URL of your Data Center/Server instance, found under **System** → **System info**.

![JMWE for Jira Cloud migration assistant app preparation interface](/cms_trial/assets/f0684b48-c517-4868-a238-2aaa646ac14b.png)

Once you have verified that all required apps are installed on your destination Cloud instance, you can continue to prepare your migration by completing the **Assess and prepare your users** step and the **Review all email domains** step. When you are fully prepared to complete the migration, move to the next step.

## Create a migration

After completing all of the pre-migration steps, you create a migration and then execute that migration. JCMA will walk you through the steps necessary to complete the migration. You will need to name your migration, choose a migration stage (Production vs Testing), and verify the destination Cloud instance. During the setup of your migration, you will be prompted to choose what to migrate - be sure to select **Choose what to migrate** so that JMWE can be added to the migration.

During the pre-migration checks, the **Apps** section will likely display a warning. click **View app vendor checks** to open a list of potential issues. These issues can include:

- **Groovy scripts** - Jira Cloud does not support Groovy; instead, it utilizes **Jira expressions** or **Nunjucks** for scripting purposes.
- **Known incompatibilities** - Known issues such as extensions that do not exist in Jira Cloud, or other incompatible configurations.

You can download CSV reports for each of the issues; **it is highly recommended that you download and review these reports**. They will provide guidance on any extensions, actions, or configurations that may not migrate completely.

When the JMWE migration is finished, you will see the status as Complete in the Apps section.

![JMWE for Jira Cloud migration status display showing completion progress](/cms_trial/assets/eb199fe1-86d3-4315-b326-8f394bfa7b2d.png)

A message will display telling you whether the migration was successful, along with information about the total number of workflow extensions, how many were fully migrated, how many could not be migrated, and how many need attention.

## Check the completed migration

When the JMWE app migration is shown as complete in JCMA on your Jira Data Center/Server instance, open your Jira Cloud instance. Navigate to the JMWE app pages. If there are any migration issues requiring your attention, you are notified on the JMWE Overview page.

Click the **Take action** link in the notification box to proceed directly to the *Post Migration* page. Alternatively, you can select **Post Migration** at the bottom of the left navigation. This page and page link only displays if you have migrated JMWE data from Jira Server or Data Center to Jira Cloud.

The *Post Migration* page will list any extensions that encountered warnings or errors during migration, and you can open the extension directly by clicking the **Edit** button to the right of the extension in the list. The *Post Migration* page is organized into four tabs:

- **JMWE extensions** - Extensions grouped by their Workflow; use the pulldown menu at the top of the list to view any extensions that have errors or warnings.
- **Shared actions**
- **Scheduled actions**
- **Event-based actions**

Additionally, you can filter the list using the **Group by** and **Show Prolem(s)** toggles to the right of the list. You can group by Transition or by Extension type, and you can display either a Summary or Details of the issue.

![JMWE for Jira Cloud migration overview interface with detailed progress information](/cms_trial/assets/0d4660c7-bc19-4206-8ef7-4e455e8ee66f.png)