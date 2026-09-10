# Migrating using Jira Cloud Migration Assistant (JCMA)

The JMWE app has an automated migration path and can be migrated from **Jira Server/Data Center** (JMCF version 2.5.1 and later) using **Jira Cloud Migration Assistant (JCMA)**. Be aware that JMCF’s Cloud migration using JCMA is currently in beta, so you may wish to test the JMCF migration in a trial/test Cloud instance.

**BEFORE YOU BEGIN**

- Please be sure to review all [Jira documentation](https://support.atlassian.com/migration/docs/jira-cloud-migration-assistant/) for the migration process.
- Note that third-party app migration using JCMA is still in Beta; while every effort has been made to migrate all JMCF configurations, **the process is not 100% comprehensive**. Some manual updates will be required!
- The migration process is **not aware of context** - when migrating a single project, you will encounter many warnings!

**Note:** If you have already migrated to the Cloud and need information regarding how to fix errors, see the [Post Migration page](/cms_trial/space/JMCFC/1465843750/Post+migration/).

## Start the Migration

Before preparing your Data Center/Server instance for migration, verify that **Jira Cloud Migration Assistant** is installed!

The migration process starts on your Jira Data Center instance, where you must prepare your data for migration.

To begin the migration, follow these steps:

1. Log into your Jira instance as an Administrator.
2. From the **Administration** menu ( ⚙️ ) click **System**.
3. In the left-hand panel, scroll down to *IMPORT AND EXPORT*and click **Migrate to cloud**. The Migration Assistant home page will open (Figure 1, right).
4. The following sections will detail any special considerations for JMCF in each of the major steps of the migration process.

## Assess your apps

![Jira Misc Custom Fields (JMCF) Cloud JCMA app assessment results](/cms_trial/assets/1df56687-af8d-469f-84c5-c8f39f02f85b.png)

During the [**Assess your apps**](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/#1.-Assess-your-apps) [step](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/#1.-Assess-your-apps), make sure that you have marked Jira Misc Custom Fields status as **Needed in cloud** (Figure 2, right). If a green check does not appear, you will need to upgrade to version 2.5.1 or later of JMCF [Data Center](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe?tab=versions&hosting=datacenter) to migrate using JCMA.

You can check the compatibility of your custom fields with the feature comparison between Data Center and Cloud [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmcfc&title=Feature%20Comparison%20-%20JMWE%20Data%20Center%2FServer%20vs.%20JMWE%20Cloud&linkCreation=true&fromPageId=1466499089).

When you have determined the migration status of all of your installed apps, click **Done**.

## Prepare your apps

During the[**Prepare your apps**](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/#2.-Prepare-your-apps) [step](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/#2.-Prepare-your-apps), the migration process will verify that **JMCF for Jira Cloud** is installed on the destination Jira Cloud instance. You must be an Administrator on **both** the source Data Center instance and the destination Cloud instance. Selecting your destination Cloud instance will require that you input the base URL of your Data Center instance, found under **System** → **System info**.

![Jira Misc Custom Fields (JMCF) Cloud JCMA app preparation interface](/cms_trial/assets/641a114b-e51c-4a07-b72b-bd564cf529c1.png)

Once you have verified that all required apps are installed on your destination Cloud instance, you can continue to prepare your migration by completing the **Assess and prepare your users** step and the **Review all email domains** step. When you are fully prepared to complete the migration, move to the next step.

## Create a migration

After completing all of the pre-migration steps, you create a migration and then execute that migration. JCMA will walk you through the steps necessary to complete the migration. You will need to name your migration, choose a migration stage (Production vs Testing), and verify the destination Cloud instance. During the setup of your migration, you will be prompted to choose what to migrate - be sure to select **Choose what to migrate** so that JMCF can be added to the migration.

During the pre-migration checks, the **Apps** section will likely display a warning. click **View app vendor checks** to open a list of potential issues. These issues can include:

- **Groovy scripts** - Jira Cloud does not support Groovy; instead, it utilizes **JavaScript** for scripting purposes.
- **Known incompatibilities** - Known issues such as custom fields that do not exist in Jira Cloud, or other incompatible configurations.
- **Fields included in this migration** - An attachment is included with a list of all fields that will be migrated to Jira Cloud based on the projects selected.

You can download CSV reports for each of the issues; **it is highly recommended that you download and review these reports**. They will provide guidance on any extensions, actions, or configurations that may not migrate completely.

When the JMCF migration is finished, you will see the status as Complete in the Apps section.

![Jira Misc Custom Fields (JMCF) Cloud migration status indicator](/cms_trial/assets/aa82dd88-a2ab-4f13-b1e4-c895f8eea929.png)

A message will display telling you whether the migration was successful, along with information about the total number of custom fields, how many were fully migrated, how many could not be migrated, and how many need attention.

You are viewing the documentation for **Jira Cloud**.

![Jira Misc Custom Fields (JMCF) Cloud migration assistant home page](/cms_trial/assets/a64b18d1-69e9-4800-9f1e-a1f0cc29cca6.png)

## Check the completed migration

When the JMCF app migration is shown as complete in JCMA on your Jira Data Center instance, open your Jira Cloud instance. Navigate to the JMCF app pages. If there are any migration issues requiring your attention, you are notified in a banner at the top of the page (Figure 4, right).

Click the **Take action** link in the notification box to proceed directly to the **Post Migration** page. Alternatively, you can select **Post Migration** at the bottom of the left navigation. This page and page link only displays if you have migrated JMCF data from Jira Data Center to Jira Cloud.

The Post Migration page will list custom fields that were migrated, and any that encountered warnings or errors during migration can be opened directly by clicking the **Edit** button to the right of the list. Additionally, you can filter the list using the **Migration name** and **From/To** fields at the top of the list. You can display only X based on the specific migration, or for any migrations that occurred between the selected dates.

![Jira Misc Custom Fields (JMCF) Migration notification in the My custom fields page.](/cms_trial/assets/39cbe2ae-fb45-43fc-b1c0-1493813a94c4.png)