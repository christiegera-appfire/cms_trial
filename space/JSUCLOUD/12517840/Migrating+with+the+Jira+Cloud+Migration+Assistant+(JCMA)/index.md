# Migrating with the Jira Cloud Migration Assistant (JCMA)

This information is accurate as of **August 2025.**

**JSU Automation Suite for Jira Workflows (JSU)** is compatible with Atlassian’s Jira Cloud Migration Assistant (JCMA) for app migrations. This means that you can automatically migrate most of your JSU workflow automations from your Data Center instance to your Cloud instance.

It is highly recommended that you test your migration on a **staging** Cloud instance so you can become familiar with the results before proceeding with a migration of your Data Center app data to your production Cloud instance.

You should also review our [feature parity page](/cms_trial/space/JSUCLOUD/12519139/JSU+Data+Center+vs+Cloud+feature+comparison/), particularly the references to Screen Security Configuration on Jira Cloud and the behavior of the Perform As User feature in JSU Cloud.

## Important

Before migrating JSU configuration to Jira Cloud, make sure you are using supported and up-to-date versions of Jira, JSU, and the Jira Cloud Migration Assistant (JCMA).

- Review [Atlassian's End of Support policy](https://confluence.atlassian.com/support/atlassian-end-of-support-policy-201851003.html) and verify that your Jira version is still supported.
- Upgrade to the [latest supported version of JSU](https://support.appfire.com/space/JSU/12682813/Release+notes) before migrating.
- Upgrade to the [latest version of JCMA](https://marketplace.atlassian.com/apps/1222010/jira-cloud-migration-assistant/version-history) before migrating.
- Migration-related improvements and fixes are regularly delivered in both JSU and JCMA releases.

Older Jira versions may rely on Connect-based modules that are no longer aligned with current migration capabilities. Atlassian has transitioned to Forge-based modules, and JSU migration support has evolved accordingly.

---

## How to navigate to the Jira Cloud Migration Assistant add-on

It is recommended to always use the **latest available version** of the Jira Cloud Migratio ‘Assistant (JCMA)’ section of the Jira administration settings.

1. Select **Administration > System.**
2. Under *IMPORT AND EXPORT* in the left sidebar, select **Migrate to cloud**. The *Migration Assistant home* page is displayed.

![The Migration Assistant home page displayed in Jira.](/cms_trial/assets/4986d678-c017-4fcc-a11a-f8448ac0a57d.png)

Before you can commence a migration, you need to complete the steps outlined in the JCMA tool to **assess and prepare your apps**. This guide will give a brief overview of how to do this with JSU. It is highly recommended to become familiar with Atlassian’s <https://support.atlassian.com/migration/docs/jira-cloud-migration-assistant/> while preparing your instance and other apps for a Cloud migration.

---

## How to include JSU in your app assessment

1. **Assess your apps**: Select which apps you want to include in your migration. All apps must have a decision status selected before you can proceed to the next step.

   1. Select **View app assessment**.
   2. Find JSU in the list of apps and select **Needed in Cloud** from the Status dropdown.
   3. When you’re happy to proceed, select **Done***.*

      ![Asses your apps page in Jira with JSU set to Needed in Cloud.](/cms_trial/assets/098ae5b1-28c8-4689-8d20-f08505384a76.png)
2. **Prepare your apps**: Next, follow the prompts to link your Jira Cloud instance to the JCMA tool.

   1. Select **Begin preparing** on the *Prepare your apps* panel on the *Migration Assistant home* page.
   2. Select the required destination Cloud site, then select **Choose cloud site** to link your chosen cloud instance.
   3. Select **Continue** to navigate through the remaining preparatory steps, then click **Done**.

      ![The Choose your destination cloud site prompt for JCMA.](/cms_trial/assets/1f2c21e0-21bc-458b-93ee-c0689c4f327b.png)
3. **Migrate your data**

   1. When you are ready, go to the Migrate your data panel on the *Migrations Assistant home* pageand select **Create a migration** to begin your migration activity. If you have already performed a migration, you can select **Create a migration** on the *Migrations dashboard* page.
   2. Select **Connect to cloud**.

      ![Overview of the migration steps for JCMA as described on this page.](/cms_trial/assets/aa58cb6b-1239-463b-998e-ad0cd16f5e72.png)
   3. Select the **Choose what to migrate** option.
   4. Edit the options as required. For the *Apps* option, select **All** to ensure JSU is included in your migration activity.

      ![Confirm migration options and run pre-migration checks](/cms_trial/assets/299884a2-2d62-4072-b937-5d7394dee574.png)
   5. Select **Run pre-migration checks**.
   6. The migration assistant displays the results of all the pre-migration checks. Expand the relevant check to review any possible issues.

      ![Pre-migration check results](/cms_trial/assets/b9e6d4f3-6303-4317-819b-20ba5ffcdc34.png)
   7. Under *Apps*, select **View app vendor checks**.   
      JSU has implemented two app vendor checks to help your JSU data migrations run smoothly.   
      JSU’s vendor check is compatible with JCMA versions earlier than 1.9.5, or with version 1.9.14 and later. See <https://support.atlassian.com/migration/docs/app-vendor-checks/> to learn more about app vendor checks.

      ![Select 'View app vendor checks'](/cms_trial/assets/a98a8729-af88-484b-9ac9-7df6a740ab2b.png)
   8. Follow the steps to resolve any issues before proceeding, or download a report to help with post-migration cleanup as described in the next sections.

      ![Review JSU Automation Suite app vendor checks](/cms_trial/assets/f3e813bd-248c-4152-8289-63de57b18f4c.png)
   9. Select **Continue** to move to the Review stage of your migration, then when you are ready, select **Run**to commence your Cloud migration which includes your JSU app data.

---

## Reviewing the status of your migration

After starting the migration, you can review its progress by returning to the Migrations dashboard. Your Jira data will be migrated first, followed by your app data.

![Sample migration progress status.](/cms_trial/assets/2638b72f-64b5-4808-9d54-e8803dc2170e.png)

Click **View details** to see more information about the migration activity.

![Sample migration progress status.](/cms_trial/assets/dc444be3-a28d-4416-bdfb-a1e6acb36904.png)

The app-migration stage is the last step of the migration activity. Once this stage is complete, you can expand to view more information, including a link to the *JSU Cloud Post-Migration Report*.

![Sample migration completion status showing link to post migration report.](/cms_trial/assets/f13abc2f-2f6f-4724-8cb0-cbff2a8671e6.png)

The post-migration report will show a summary of *INCOMPLETE* if any warnings or errors were found during the migration. JSU relies on the JCMA tool to move across any workflows, resolutions, transitions, etc., to configure your workflow rules correctly on your cloud site.

---

## Post-migration report and cleanup

Click the link in the expanded section to open a new tab with your post-migration report for this specific migration. To view any of your post-migration reports on your cloud instance, go to **Admin** **Settings** > **Apps** > **JSU Automation Suite for Jira Workflows** > **Reporting**.

![The JSU migration reports page.](/cms_trial/assets/e6479a31-fd83-4769-9fd2-a51fcabebd60.png)

The examples on this page were created using our original beta Migration report.

![The expanded view of the migration report for the sample migration described on this page.](/cms_trial/assets/1206fe4c-601a-484f-9dbd-9fba401845f2.png)

From January 2023, our Migration report contains additional details and features to help you to identify and resolve any problems with your workflows post-migration. You can see an example of the new report is in our release documentation.

The report now includes:

- The rule name, workflow, and transition with links to take you directly to the appropriate pages in your Jira instance.
- Sortable columns to help you organize the work items in a way that suits you best
- A Resolved checkbox to help you keep track of problems as they are fixed

Looking at the post-migration report, we can see there are two warnings reported: one *Missing resolution* and one *Missing transition*.

These are because JSU couldn’t find a specific resolution and transition required to configure some features correctly on the cloud instance. This specific scenario is likely to be caused by one of three scenarios:

- The JCMA tool didn’t migrate that specific resolution and transition for unknown reasons
- The JCMA tool didn’t migrate that specific resolution and transition because they already exist on the Cloud site but with different IDs
- The JCMA tool migrated that specific resolution and transition but in doing so gave them new IDs which don’t match the Server configuration

At this stage, we can say that JSU has successfully performed an app-migration to the Cloud.

All that remains is the specific clean-up of workflow rules relating to any warnings identified

---

Let’s compare the workflow rules on both platforms: how they were originally on our Server instance and how they look after being migrated to the Cloud instance.

**Data Center**

![The post function summary from the server instance described on this page.](/cms_trial/assets/32c11945-cee1-4b1a-bb96-903fd7b518b0.png)

Our Data Center workflow contains three JSU post functions, one each for Linked Transition, Clear Field Value, and Update Any Issue Field.

**Cloud**

![The post function summary from the cloud instance described on this page.](/cms_trial/assets/244260eb-9c43-4e4a-a9b8-76d7e710e344.png)

All three have been successfully migrated to the Cloud, but the Linked Transition has a visible error.

Our Cloud post function is missing a value for the *Transition* field, while the Server field contains the “Done” transition.

The *Missing transition* warning from the post-migration report, showed that a transition with ID “31” couldn’t be found. This is likely the missing field, so let’s fix it.

First, look at the specific configuration of this post function on the Server instance compared to the Cloud instance.

**Server**

![The Linked Transition configuration from the source Server instance.](/cms_trial/assets/87715303-4b09-4280-9e4d-f4737d470319.png)

**Cloud**

![The Linked Transition configuration from the destination Cloud instance.](/cms_trial/assets/c1f2d989-dac5-410e-8a4a-cb0ee50051d1.png)

On your cloud instance, edit the misconfigured post function and ensure the correct values are added to the *Transition* values (in our case, the same workflow with transition “Done” and ID “31”), and then click **Update** to save your changes.

![The post function summary from the cloud instance showing the resolved error described on this page.](/cms_trial/assets/4b88b3d6-72c3-42be-a895-7ac71596ef43.png)

After updating the post function, the error no longer appears. After you’ve resolved all issues on your workflow, remember to **publish it**.

![The publish workflow confirmation popup in Jira.](/cms_trial/assets/45c0eea2-a54f-429f-8f89-1217a71725c6.png)

You’ve now successfully migrated to Cloud with all of your JSU workflow rules included!

---

**Feedback wanted!**

How did your migration go? Was this guide helpful? Still have questions?

Please feel free to contact us through our [support channel](https://appf.re/support), and we’ll be happy to assist.