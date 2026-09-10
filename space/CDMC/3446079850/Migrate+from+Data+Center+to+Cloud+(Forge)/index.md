# Migrate from Data Center to Cloud (Forge)

Migrate Comala Document Management (CDM) from Confluence Data Center to Confluence Cloud using the Atlassian Confluence Cloud Migration Assistant (CCMA).

---

## About this guide

As part of Atlassian's platform modernization, Comala Document Management for Cloud has been rebuilt on the Atlassian Forge platform. Starting July 1, 2026, all new Data Center to Cloud migrations use this updated architecture.

This rebuild brings several improvements to the migration experience:

- **No page-restriction removal required**: restricted pages are handled automatically during migration.
- **Faster migrations**: backend optimizations deliver significant performance improvements for bulk data transfers.
- **Migration Dashboard**: monitor batch progress in real time and retry only failed batches without restarting the entire migration.
- **Resilient retries**: successfully migrated data is retained if a batch fails.
- **Automatic metadata migration**: document metadata and page parameters are included in the migration without a manual export step.

Before you begin, ensure your Data Center instance is running a supported version of Comala Document Management for Data Center. The minimum version depends on your Confluence Data Center version. See [Version requirements](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/3406004237/Migrate+from+Data+Center+to+Cloud+Forge#Version-requirements) below.

If you started your migration testing before July 2026 and are following a previously agreed migration plan with Appfire Support, refer to this [migration guide](/cms_trial/space/CDMC/2192967667/Migrate+to+Confluence+Cloud/).

---

## Version requirements

|  |  |  |
| --- | --- | --- |
| **Confluence DC version** | **Minimum CDM DC version** | **CDM Cloud version** |
| 8.5.10 – 9.5.4 | **v9.0.1+** | **v41+** (Forge) |
| 10.x | **v10.0.0+** | **v41+** (Forge) |

Install the latest version of Confluence Cloud Migration Assistant (CCMA).

Use the minimum CDM Data Center version that matches your Confluence Data Center version. Migration tests performed with earlier versions are not valid with the current Cloud version.

---

## What gets migrated

| **Component** | **Included in migration** | **Details** |
| --- | --- | --- |
| Global workflows | ✅ | Translated to cloud-compatible equivalents |
| Space workflows | ✅ | Label conditions and invert labels preserved |
| Current workflow state | ✅ | State, expiration date, approvers, approval statuses |
| Workflow parameter values (space-level) | ✅ | Migrated with the workflow |
| Document metadata and page parameters | ✅ | Migrated automatically via CCMA |
| User and group references | ✅ | Mapped to Cloud user IDs automatically |
| Page workflows | ❌ | Must be consolidated as space workflows before migration (see Step 2) |

---

## Step 1: Prepare your environment

### Install required versions

Update your Data Center instance to:

- [Comala Document Management for Data Center](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=datacenter&tab=overview) - see the [Version requirements](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/3406004237/Migrate+from+Data+Center+to+Cloud+Forge#Version-requirements) above for the minimum version that matches your Confluence Data Center version.
- [Confluence Cloud Migration Assistant (CCMA)](https://marketplace.atlassian.com/apps/1219672/confluence-cloud-migration-assistant?hosting=datacenter&tab=overview) - latest version

### Set up your Confluence Cloud site

1. Create or confirm your Confluence Cloud site.
2. Install the **Forge version** of Comala Document Management for Cloud from the Atlassian Marketplace.
3. Install any other cloud apps you need.
4. Ensure you have **administrator permission** on both the Data Center instance and the Cloud site.

### Review your workflows

Assess your current CDM usage before migrating. In your Data Center instance:

Go to **Confluence Global Administration** > **Comala Document Management** > **Migration CDM Usage** to generate the following reports.

- **Space Workflows Report**: lists global and space workflows across your instance.
- **Page Workflows Report**: lists page workflows that need consolidation before migration.

![Migration CDM Usage page showing the available migration reports, including Space Workflows and Page Workflows.](/cms_trial/assets/34206bc3-6ea4-4511-960b-c5938be412a5.png)

Some workflow features work differently in the cloud. Use the [Workflow Translator for Cloud](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649924970) tool in your Data Center app to preview how each workflow translates to cloud-compatible JSON. This helps you identify any elements that will be adapted or removed during migration.

For details on which elements are translated and which aren't, see [Workflow elements translated from Data Center](/cms_trial/space/CDMC/2232485018/Workflow+elements+translated+from+data+center/).

For a comparison of Data Center and Cloud features, see [Product comparison](/cms_trial/space/CDMC/2192677102/Product+comparison/).

---

## Step 2: Consolidate page workflows

Page workflows are **not migrated** to the cloud. If your spaces use page workflows that you need to preserve, consolidate them into labeled space workflows before migration.

If you're not sure if you have page workflows, generate and check the **Page Workflows Report** from Step 1.

To generate the page workflows report:

1. Go to **Space tools** at the bottom-left corner of the page and select **Document management.**

   ![Space tools menu showing the Document management option.](/cms_trial/assets/3a401070-525b-4372-83ce-74f771ae66ea.png)
2. Navigate to the *Document Management* tabandchoose **Page Workflows** from thedropdown menu.

   ![Document Management tab showing the Page Workflows option selected.](/cms_trial/assets/7240b526-b355-4018-ab81-3864506f4557.png)
3. For each page workflow, select **Consolidate** from the **Actions** menu.

   ![Document Management Dashboard showing the Consolidate action in the Actions menu.](/cms_trial/assets/ac0adc4d-c44e-42f9-b4a0-d48262ceab5a.png)
4. Enter a label string; this becomes the content label filter.

   ![Consolidate workflow dialog showing the label field with a label string.](/cms_trial/assets/649ab531-efa1-4eec-9aa3-1b8e07d219f5.png)

The page workflow is removed from individual pages and added as a space workflow with the label condition.

### Bulk method (scripted)

For instances with many page workflows, use a script to consolidate in bulk.

Refer to [Consolidating page workflows for migration to the cloud](/cms_trial/space/CDMC/3446112260/Consolidating+Page+Workflows+for+Migration+to+the+Cloud/) for detailed steps for bulk page workflow consolidation.

---

## Step 3: Run the migration

We recommend migrating in small groups of spaces rather than all at once.

### Assess your apps

You can decide which apps need to be migrated to the cloud.

To assess your apps:

1. Go to **Confluence Global Administration** > **Migration Assistant** in your Data Center instance.

   ![Confluence Global Administration showing the Migration Assistant page.](/cms_trial/assets/20249852-c789-48d3-b4c5-c7e02434e98e.png)
2. Click **View app assessment** under *Assess your apps.*

   ![Migration Assistant showing the View app assessment option.](/cms_trial/assets/e1149f60-b239-4cdf-86b5-ba91b7840e44.png)
3. Set Comala Document Management as **Needed in Cloud** using the Decision menu.

   ![App assessment page showing Comala Document Management marked as Needed in Cloud.](/cms_trial/assets/6de7d4b2-31d7-43f3-976c-7cfd2474b05a.png)

1. Review other apps for cloud availability.
2. Click **Done.**

### Prepare your apps

**Connect** to your destination Cloud site and **install** apps marked as Needed in Cloud before you start the migration.

To prepare your apps,

1. Click **Begin preparing** under *Prepare your apps* in the Migration assistant page.

   ![Migration Assistant showing the Begin preparing option.](/cms_trial/assets/cfee3911-ee78-4dee-a4e9-3c23fb41ce7d.png)
2. Connect to your Cloud site and click **Continue**.
3. **Install** apps marked as Needed in Cloud.
4. **Agree to app migration** to allow the CCMA to transfer app data. Click **Done**.

   ![App preparation page showing the Agree to app migration step before continuing.](/cms_trial/assets/c1e2c91e-f189-40c3-a6e7-3737dd30ab6e.png)

### Review users and email domains

1. Click **Review all email domains** in the *Migration Assistant Home.*

   ![Migration Assistant showing the Review all email domains option.](/cms_trial/assets/43e6af1f-f1b2-4ef6-8d5e-23c0b567e127.png)
2. Confirm all email addresses are valid and unique.
3. Set email domains as trusted or blocked. Review and click **Done**.

   ![Email domain review page showing trusted and blocked domain settings.](/cms_trial/assets/39bc133b-9acc-4c5f-972a-55fc28e7569a.png)

### Create and configure a migration plan

1. Select **Migrate your data** on the *Migration Assistant* homescreen.
2. Click **Continue with Migration Assistant.**

   ![Migration Assistant showing the Continue with Migration Assistant button.](/cms_trial/assets/78dfa187-e25d-4202-97c9-807c44655b43.png)

1. Click **Connect to Cloud.**

   ![How it works page showing the migration steps and the Connect to Cloud button.](/cms_trial/assets/9060bab9-2985-4201-9f78-578be5542fdb.png)

1. In the *Connect to your Cloud site* page:

- Name your migration.
- **Choose stage**: Testing or Production.
- **Connect** to the destination Cloud site (sign in as Site Administrator).
- **Select spaces** to include in your migration.
- **Choose what to migrate**: spaces, pages, attachments, users, groups, and vendor apps.

![Connect to your Cloud site page showing migration name, stage, destination site, and space selection.](/cms_trial/assets/72e39bfd-87b0-4705-992a-d62f46fd3d20.png)

1. Review and click **Check for errors**.

![Migration summary page showing the Check for errors option before validation.](/cms_trial/assets/52d9f88a-12ff-452f-9085-a04fdcdc04f4.png)

### Run pre-migration checks

The migration assistant automatically runs a **Check for errors** for each of your systems, app versions, apps, spaces, users, and user group data

This includes specific **App vendor checks**.

**App vendor checks** are run for the apps marked as **Needed in Cloud**. Warnings can be viewed and, if necessary, resolved before proceeding with the migration. **Pre-Migration Workflow Assessment**: identifies workflows that aren't fully cloud-compatible and lists global and page workflows for each space.

Workflows with incompatible elements are still migrated: the incompatible elements are adapted or removed. You can review them in the Cloud after migration.

To run pre-migration checks,

1. Click **Continue** in the *App vendor checks* page.

![App vendor checks page showing the Continue button.](/cms_trial/assets/0873e266-ab54-4a73-8b6b-0276b05818dc.png)

1. In the pre-migration checks page, click **Review migration** if there are no blocking errors.

![Pre-migration checks results showing Review migration when no blocking errors are found.](/cms_trial/assets/0633ba19-59e7-4f75-a146-6e8005a8e768.png)

1. With no blocking errors, choose **Run now** to start or **Save** the plan to run later.

![Migration review page showing the Run now and Save options.](/cms_trial/assets/d0ef06e6-54b8-4c8a-b65a-8ff9f1f29da8.png)

Data is migrated in this order:

1. Global Workflows
2. Space Workflows and Page State
3. Document Activity and Metadata

### Monitor progress

#### Migration Dashboard

The migration includes an administrative dashboard for monitoring.

You can do the following:

- View real-time batch progress.
- See the status of each batch (Succeeded / Failed).
- **Retry only failed batches**: successfully migrated data is retained.

![Migration Dashboard showing batch progress and migration status for each batch.](/cms_trial/assets/6ad9ce8b-050f-4225-901d-e32661b17073.png)

There is no need to restart the entire migration or clear cloud data if a batch fails.

#### Migration Logs

Go to **Confluence Global Administration** > **Comala Document Management** > **Migration Logs**

In the Migration logs dashboard, you can:

- Monitor active migrations in real time.
- Review completed migrations with status badges (SUCCESS / FAILED).
- Search by migration name, transfer name, or status.

![Migration Logs page showing active and completed migrations with searchable status information.](/cms_trial/assets/d3c6e0e1-ed78-48dc-8276-8aaccf88b70e.png)

---

## Step 4: After migration

After a successful migration, post-migration tasks include:

- Review of migrated space workflows identified in the CCMA precheck as not fully cloud-compatible. If required, these need to be edited to ensure the workflow elements are cloud-compatible and the workflow functionality meets your needs.
- If multiple workflows are active in a space, review the order in which the workflows are applied to ensure the correct workflow is applied to each document.

You can also edit pages to add the [Document metadata macro](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CDMC&title=Document%20Metadata) to retrieve and display migrated metadata.

### Review enabled workflows

Reapply workflows in each space using the app space settings.

![Space Workflows tab showing where to enable or manage workflows after migration.](/cms_trial/assets/dcfe6865-1dfa-4ace-a6ec-f4fdc5464ff7.png)

Refer to [Apply workflows at the space level](/cms_trial/space/CDMC/2193033075/At+space+level/) for more details

### Edit workflows for cloud compatibility

Some workflows might have been identified as not fully cloud-compatible during the **Migration Assistant** vendor app checks or when using the Workflow Translator for Cloud tool. Review and edit these workflows to ensure the functionality meets your needs in Confluence Cloud:

- Open each flagged workflow in the **visual editor** or **code editor**
- Review workflow triggers. The Cloud supports a different set of trigger events and actions. You might need to update [workflow trigger events](/cms_trial/space/CDMC/2193950329/Trigger+events/) or [workflow trigger actions](/cms_trial/space/CDMC/2193950329/Trigger+events/).
- Check for triggers with empty actions (unsupported actions were omitted during translation)

See: [Workflow elements translated from Data Center](/cms_trial/space/CDMC/2232485018/Workflow+elements+translated+from+data+center/)

### Adjust workflow states

If any documents have mismatched workflow states:

- **Per page**: use the Workflow State Dialog on each document.
- **In bulk**: Use the space settings to initialize states for all documents with an active workflow.

  ![Space workflow settings showing the option to initialize workflow states.](/cms_trial/assets/7e13cc65-2332-4b4c-90bf-2c51f5b634bc.png)

### Verify metadata

Metadata is migrated automatically. To display it on a page, add the **Document Metadata Get** macro and specify the metadata name.

![Page showing the Document Metadata Get macro used to display migrated metadata.](/cms_trial/assets/5aeab170-6e4e-42ea-b132-f66c4c8fbc13.png)

The following types are preserved:

- Metadata from the Comala Metadata app
- Metadata set using the set-metadata trigger action
- Page-level workflow parameters

See: [Migrating Metadata Macros](/cms_trial/space/CDMC/2514452500/Migrating+Metadata+Macros/)

### Check document activity

The Document Activity report on each migrated page shows the full workflow activity migrated from Data Center, including the current workflow state and related activity.

### New capabilities available after migration

The current Cloud version introduces capabilities that were not available in the previous version:

- **Workflow Version Control**: [Global Workflows](/cms_trial/space/CDMC/2276786309/Global+workflows/) now keep a full version history. Administrators can view and revert to previous versions.
- **Advanced Approvals**: redesigned approval builder with participation requirements (all, minimum participants) and decision types (unanimity, majority, minimum approvals/rejections).
- **Manual state override**: administrators can force a document into any workflow state, bypassing standard transitions. Overrides are logged in Document Activity.
- **Document Report CSV export**: export the space-wide Document Report with full metadata.
- **Document Activity CSV export**: export activity logs. State expiration events are now recorded.
- **Sequential trigger execution**: trigger actions now run in strict order, making dependent action pairs reliable (for example, labels run before restrictions).
- **Localization**: English (en-US) and Spanish (es-ES) are supported. Additional languages are planned.

The Cloud version built on Forge includes several behavioral changes compared to Data Center, including where workflow actions appear and how page workflows are applied. Review these before your team starts using the migrated content.

---

## Need help?

- Check the **Migration Dashboard** for batch-level status and retry options.
- Review the **Migration Logs** for detailed diagnostics.
- [Contact Appfire Support](https://appfire.atlassian.net/servicedesk/customer/portal/11) - include migration logs or a support package with your request.
- For complex instances (large data sets, multiple products), see the [Atlassian Migration Guide](https://www.atlassian.com/migration/plan/cloud-guide).

**Do not uninstall the app** as a troubleshooting step. Uninstalling removes app data. If a reinstall is required, please contact Atlassian Support to recover data within their retention period.