# Migrate from Dataplane Reports to Dashboard Hub Pro Cloud

## Overview

Dataplane Reports is not available for Jira Cloud, but you can migrate your Dataplane Reports to Cloud using [Dashboard Hub Pro](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-for-jira-reports-charts?tab=overview&hosting=cloud).

Due to Dashboard Hub Pro’s high compatibility with Dataplane, we’re adding Dataplane’s best features to Dashboard Hub Pro to give you a Dataplane Reports-compatible Cloud solution. To that end, we’ve enabled a seamless path to automatically migrate your Dataplane Reports data to Dashboard Hub for Jira Cloud using JCMA.

## Automatic migration from Dataplane Reports to the Dashboard Hub Pro Cloud using JCMA

## Preparing your migration

If you plan to migrate Dataplane to Jira Cloud, you must plan and choose the strategy that best fits your environment/business requirements.

### Migration prerequisites

1. Assess your app, data, and users.

|  |
| --- |
| From your Dataplane Reports Data Center instance, use the Migration Assistant to complete all the pre-migration assessment steps. The pre-migration assessment steps are:   - Assess app - Prepare your app - Assess and prepare users |

1. Install or access the Migration Assistant.

|  |  |
| --- | --- |
| **How to install JCMA**   1. In the Dataplane Reports Server or Data Center Administration page, select Manage apps. 2. Select Find new apps. 3. Search for **Jira Cloud Migration Assistant.** 4. Select Install.   To learn more, see [Update or install the Jira Cloud Migration Assistant | Atlassian Support](https://support.atlassian.com/migration/docs/update-or-install-the-jira-cloud-migration-assistant/#Install-the-Jira-Cloud-Migration-Assistant)  The migration assistant (JCMA) allows you to migrate your app and data to your Cloud instance and your Cloud instance is, of course, your destination where you migrate apps, data, and users. | **How to access JCMA**   1. Select **Settings** ⚙️ in the top right corner of the screen. 2. Select **System**. 3. Select **Import and Export** from the left navigation menu. 4. Select **Migrate to Cloud**. |

1. Create or have a Cloud site/instance.
2. Locate your base URL (source) - required when you connect to your Cloud instance.

**How to locate your base URL (source)**

1. In your Data Center instance, go to **System**.
2. Select **General Configuration**.The *Settings* page shows the Base URL.

**Required permissions for viewing report data:**

- Appropriate Jira project permissions
- Developer role assignment in relevant projects
- Active membership in the jira-users group

Direct Jira issue access doesn't automatically grant access through Dashboard Hub reports. You may need to configure project role memberships.

### Starting your migration

The Migration Assistant automates the migration of the Dataplane Reports Data Center instance to the Cloud. To learn more about planning and executing your migration, refer to the [Cloud migration guide](https://www.atlassian.com/migration/plan/cloud-guide#migration-tools) from Atlassian.

The migration consists of two main phases: Assessing your app, data, and users, and the actual migration (Create migration).

The JCMA migration workflow table shows the steps that you do in your instance and the ones you have to do in your Cloud instance.

### The JCMA migration workflow

1. ON JIRA DC Install and verify that the JCMA app is installed and updated to the latest version.
2. ON JIRA CLOUD Identify or create your target Jira Cloud instance.
3. ON JIRA CLOUD Install the [Dashboard Hub for the Jira Cloud](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-for-jira-custom-charts-share-reports) app.
4. ON JIRA DC Go to the JCMA *Migration Assistant home* page by navigating to **Jira Administration** > **System** > **Migrate to cloud.**
5. ON JIRA DC On the JCMA *Migration Assistant home* page, prepare for migrating Jira data by selecting the Dataplane Reports app for migration, assessing and preparing your users, and reviewing your users and email domains.

   1. Review all email domains and select **Trusted domain** for those that are legitimate.

      ![Dashboard Hub trusted domain setup for Dataplane migration](/cms_trial/assets/e504aba1-3158-43da-a36b-8d57dcb20a46.png)
   2. In the app assessment, select Dataplane Reports for Jira as **Needed in cloud**.

      ![Dashboard Hub Cloud migration page showing required app settings](/cms_trial/assets/f22a46cf-25e2-4189-ba5c-017e5f152de8.png)
   3. Accept the agreement for the app migration.
   4. ![Dashboard Hub app migration agreement step](/cms_trial/assets/6156f4fc-3735-4174-95fb-8356e968ade6.png)![Dashboard Hub Cloud migration page showing required app settings](/cms_trial/assets/f22a46cf-25e2-4189-ba5c-017e5f152de8.png)

      Check your users' assessment.

      ![Dashboard Hub migration user assessment step](/cms_trial/assets/06a75c80-a99e-46ca-8e9c-c2339efe64da.png)
6. ON JIRA DC Create a new JCMA Migration plan using the **Choose what to migrate** option for migrating your Jira users and groups.

   1. In the *Connect to your cloud site* step, name your migration and select the migration stage and your destination cloud site.

      ![Dashboard Hub migration target cloud site selection step](/cms_trial/assets/e0527e8d-f471-4861-a53b-f5fb4523e18e.png)
   2. Click **Choose cloud site**.
   3. Click **Select all data** or **Choose what to migrate** to access all options and review possible pitfalls.  
      For this guide, we select the *Choose what to migrate* option*.*

If you select *Choose what to migrate*, select as much data as possible. The more Jira data you migrate, the better the Dataplane Reports app migration will perform.

![Dashboard Hub migration content selection step](/cms_trial/assets/399aa7c3-e83e-4467-b8ba-d90fc1989870.png)

d. Select the **Users and group** to migrate first.

If you skip this step or run it out of order, users will end up with two pending migrations. If you have previously migrated them, selecting these options will migrate only the difference between your previous migration and the current state.

![Dashboard Hub migration users and groups selection step](/cms_trial/assets/2d700b97-cdf2-4ac0-99d3-adc5550cbc46.png)

1. ON JIRA DC Create a second JCMA Migration plan using **Choose what to migrate** for migrating projects, boards, and filters, and run this Migration plan to migrate the bulk of Jira data to Cloud.
2. Click **Choose what to migrate** again.
3. Select the projects that you are interested in.

   Make sure that all the projects are selected at the bottom of the view.

   ![Dashboard Hub migration project selection step](/cms_trial/assets/68e8c5eb-81b2-4308-83e7-a2c6d1d981ae.png)
4. Migrate Advanced Roadmaps plans.

   ![Dashboard Hub migration step for Advanced Roadmaps data](/cms_trial/assets/4c083fe3-a2d2-4d79-84ce-8474fbc32a44.png)
5. Migrate Jira native dashboards, filters, and related items. If you aren’t sure which native Jira dashboards to include, select **All dashboards**. This helps ensure your migration runs smoothly.

   ![Dashboard Hub migration dashboard selection step](/cms_trial/assets/84edf708-dcd5-4cb3-9032-d73a43be14da.png)
6. Migrate users and groups. Even if you have previously migrated them, selecting these options will migrate only the diff between your previous migration and the current state.
7. Select the option **All**. Expect to see the number of apps that you marked as *Needed in cloud*.

   ![Dashboard Hub migration All option selected](/cms_trial/assets/8f40eea0-b896-4939-9721-cf97c7e0748f.png)

   The original migration options screen will now show blue checkmarks before each option.

   ![Dashboard Hub migration options step](/cms_trial/assets/3f9b1642-0f13-4075-8f73-4da4f7a409c6.png)
8. ON JIRA DC Run the pre-migration checks.

Groups can be marked with a warning (usually not a problem), but projects marked as an error must be resolved. Delete those projects from the cloud site and remove them completely, including from the trash, before proceeding.

![Dashboard Hub premigration checks step](/cms_trial/assets/52c09ca7-430b-4ec7-ab16-aa16b0cb5734.png)

1. ON JIRA DC and JIRA CLOUD Correct any issues with the initial Jira data migration that were flagged by the Dataplane Reports' pre-migration checks.

   1. Click the **Refresh** button at the top of the projects section.

      ![Dashboard Hub Dataplane migration Refresh section](/cms_trial/assets/249ba67e-e6e6-4a2f-aab9-d92d3a24a640.png)
   2. Click **Review migration**.
2. ON JIRA DC Click **Run** to start the migration process. Clicking **View warnings** will return you to the previous screen.

   ![Dashboard Hub run migration step](/cms_trial/assets/0015547b-c231-4227-b610-e714333dba16.png)
3. ON JIRA CLOUD Navigate to **Jira** > **Apps** > **Dashboard Hub** > **App Settings** > **Post migration reports**. For the migration just performed, click **View Details** to review the post-migration report.

   ![Dashboard Hub Dataplane migration Details section](/cms_trial/assets/3220b29a-df58-4f74-8f7d-ce8c30978891.png)

   The report also shows the total number of reports that were available for migration in the Data Center instance.

   ![Dashboard Hub Dataplane migration report configuration](/cms_trial/assets/76a0e28f-0ada-47a2-bf74-33cb7ee3c44f.png)
4. ON JIRA CLOUD Navigate to **Apps** > **Dashboard Hub** to review the new Dashboard Hub dashboards and gadgets created from your Dataplane reports.
5. ON JIRA DC and JIRA CLOUD Correct any issues with the initial Dataplane Reports data migration.
6. ON JIRA DC Re-run the Dataplane Reports Migration plan as many times as needed until you are satisfied with the migration.

## Create the migration

To start migrating your data, log in to the Dataplane server instance you want to migrate your users and projects from, this is also called base URL. This is the source from which you move your data.

### Connect to the Cloud

When you connect to the Cloud, provide the following information:

- Migration name
- Migration stage, for example, test or production
- Destination - your cloud site
- Base URL from where you want to migrate, that is, your Dataplane Reports server instance.

![Dashboard Hub Dataplane migration report selector](/cms_trial/assets/b123aed0-f539-4ef2-bb41-fb63f1c44626.png)

### Migration options

A cloud migration strategy is the high-level plan an organization adopts to move an existing server DC installation and co-located applications and their associated data into the cloud.

![Dashboard Hub migration progress or completion screen](/cms_trial/assets/fdbef9e3-7cf9-4c4f-9567-7cba48dc2e4e.png)

Specific to the migration of Dataplane Reports to Cloud, you can choose from two migration options:

- **Migrate all your data at once**

When you choose to migrate all at once, you need to start with an empty Cloud site.  
You can also exclude or include the attachments by selecting the Exclude all attachments option.

- **You choose your migration strategy in Dataplane**

This option allows you to migrate selected data, projects, and users into an existing Cloud site.   
You can repeat this option as many times as you require until everything is migrated to the Cloud site.

Re-run the app migration within 12 days of when you first started running the original migration.  
The app re-run feature is unavailable after the 12-day time limit.  
After 12 days, the option is disabled.

For more information, see  
<https://support.atlassian.com/migration/docs/use-the-confluence-cloud-migration-assistant-to-migrate/#Re-run-an-app-migration>

### Re-run migration

If you need to re-run part or all of the migration:

- Don’tdelete Cloud-based native dashboards prior to migration.
- Dashboard relationships between DC and Cloud systems remain linked.
- Removing Cloud dashboards triggers migration failures.

**Solution:** To migrate native dashboards successfully, modify the dashboard names in your Dataplane Server/DC environment before initiating another migration.

## Run pre-migration checks

After you choose your migration strategy, the Pre-migration page displays all the checks that are run.

The Pre-migration checks are standard Atlassian controls to verify the status and readiness of your:

- System
- User and Groups
- Projects
- Cross-projects
- Data preparation
- Apps

In addition to the standard Atlassian checks, two additional app vendor checks are implemented for Dataplane.

### The App Vendor Checks

The app vendor checks are designed to reduce the possibility of app migration failure.   
Dataplane Reports performs the following app vendor checks:

- **Invalid reference report**  
  This pre-migration check will detect any inconsistencies in your Dataplane Reports configurations. That might already be a problem in Dataplane Reports on your Jira Server/Data Center instance. Dataplane Reports might not be able to run those reports correctly.  
  For best results after your cloud migration, we recommend fixing these problems in Dataplane Reports on your Jira Data Center instance.  
  You could move on with your cloud migration without fixing anything. But the detected inconsistencies will be the same problem in Dashboard Hub Pro Cloud.

![Dashboard Hub Dataplane migration invalid references warning](/cms_trial/assets/31c8a86f-fcd8-4d9d-ad4d-676e81b9d1b1.png)

If there are errors or warnings, you can re-run all checks or select only the ones that show errors, using the Refresh icon next to each set of checks.

- **Permission and datasource verification**  
  This validation confirms that user accounts, groups, and roles in your Dataplane Reports configuration will migrate correctly. Address these alerts before migrating:

  - User accounts not found in the Cloud environment
  - Differences in group memberships
  - Incomplete project role configurations

## Review your migration

Once the pre-migration checks are complete, you can review the items included in the migration, their status, logs, and reports.

![Dashboard Hub Dataplane migration report details](/cms_trial/assets/51d7cb29-6983-4195-9409-0ea6cc0fa9dd.png)![Dashboard Hub Dataplane migration report output preview](/cms_trial/assets/bf3fb2cf-b64b-4e3f-8b67-c664a3749ef9.png)

## Running the migration

You can run your migration now or save it and come back later.

Once you save your migration, you won’t be able to add or remove projects.

When you are ready, click **Run** to start migrating to your Cloud instance.

## Post-migration reports and messages

When the migration is complete, a URL link is created.

Click the link to view the post-migration report. In the post-migration report, messages are displayed showing items that were skipped in the migration and why.

The types of messages that are provided are:

- Skipped messages

Skipped messages are displayed when one or more reports/records cannot be imported.  
For example, if a type of report in Dataplane Report is yet to be implemented on the Cloud or the owner of a report (user account) does not exist in the Cloud.

For each skipped record, we write 1 skippedMessage.

- Warning message

Warning messages alert that there is a problem in a report. For example, if the configuration contains a reference to a custom field that does not exist on Cloud.

The reports with warning messages count towards importedCounts.

- Error message

Error messages let you know of major problems encountered during the migration.

**Access and permission notifications**

Review these items carefully:

- Users with report visibility but insufficient data access permissions
- Missing project role assignments needed for viewing data
- Restrictions on datasource access

**Verification tasks after migration:**

When your migration finishes:

1. Check the post-migration report for access-related notifications
2. Confirm report viewers have the necessary project role memberships
3. Test report functionality using non-administrator accounts that require access
4. If users see empty reports despite having project access, verify their Developer role assignment

Take immediate action on these items to guarantee proper user access across your organization.