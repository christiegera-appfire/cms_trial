# Migrate from Data Center to Cloud (Connect)

This migration guide applies only to exception customers who are migrating from Data Center to the Connect version of Comala Document Management for Cloud after June 30, 2026. These are customers who registered their migration with Appfire Support prior to that date. This guide will be retired on October 1, 2026.

For all other migrations, refer to the [Migrate from Data Center to Cloud (Forge)](/cms_trial/space/CDMC/3446079850/Migrate+from+Data+Center+to+Cloud+(Forge)/) guide.

## Overview

To migrate from a hosted instance, use the [Atlassian Confluence Cloud Migration Assistant (CCMA)](https://marketplace.atlassian.com/apps/1219672/confluence-cloud-migration-assistant?hosting=datacenter&tab=overview) to transfer spaces, users, and groups. It includes a migration pathway for Comala Document Management workflow-related data and your hosted app space workflows.

However, there are differences in the features and functionality between the hosted and cloud versions of Comala Document Management. You can check the differences on the [Product comparison](/cms_trial/space/CDMC/2192677102/Product+comparison/) page.

The **supported migration pathway** for Comala Document Management migrates:

- **Current workflow state** **and related data**, including the expiration date, approvers, and their statuses.
- **Global workflows,** including details of the spaces where the global workflows are linked
- **Space workflows**, taking into account labeled workflows, and maintain the hosted instance workflow order in the Cloud when the space includes global scope and space scope workflows
- **Workflow parameter values** are defined at the space level.
- **Document metadata and page parameter values**
- **Full workflow events and activity history** (as an auditable record, but not accessible by the Comala workflow in the cloud).

After the migration, the workflow state is automatically applied when the workflow is activated in each space. User and user group references (within any macro) are automatically replaced with the corresponding cloud IDs, preserving workflow functionality.

## Prerequisites

Before you review the Confluence Cloud platform features and the apps needed in the cloud, ensure the following:

### Install the latest app versions

You must update your Confluence Data Center instance to the latest versions of the [Comala Document Management for Data Center](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=datacenter&tab=overview) app and the [Atlassian Confluence Cloud Migration Assistant (CCMA)](https://marketplace.atlassian.com/apps/1219672/confluence-cloud-migration-assistant?hosting=datacenter&tab=overview).

## Version requirements

Check the table below for the versions required for a Connect migration, based on your Confluence Data Center version.

| **Confluence DC version** | **Minimum CDM DC version** | **CDM Cloud version** |
| --- | --- | --- |
| 8.5.10 – 9.5.4 | v7.14.4 - 7.14.9 | v41 or lower |
| 10.x | v8.0.1 - v8.0.4 | v41 or lower |

For a DC to Connect migration, the CDM Cloud app must be on **v41 or lower**. Upgrading toa higher version installs the Forge version, which makes the Connect migration no longer possible. On the Data Center side, upgrading to the latest compatible version is strongly recommended.

### Review app functionality in the Cloud

You can review the [product comparison](/cms_trial/space/CDMC/2192677102/Product+comparison/) for our cloud and data center apps. We also recommend installing and exploring our app in Confluence Cloud.

When migrating to Confluence Cloud, existing space workflows are migrated, but some features can differ in functionality.

Before migration, in your data center app, you can use the [Workflow Translator for Cloud](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649924970) tool to convert each hosted app workflow to a cloud-compatible workflow template and add it to Confluence Cloud to review workflow functionality.

See: [Moving your workflows to the cloud](/cms_trial/space/CDMC/2192902721/Moving+your+workflows+to+the+cloud/)

In some cases, when you have multiple workflows, consider performing a test migration and exploring the workflows in your migrated space in Confluence Cloud.

Page workflows are not migrated, but you can [consolidate a page workflow as a labeled space workflow](/cms_trial/space/CDMC/2192902721/Moving+your+workflows+to+the+cloud/) in each space to include in the migration.

## Pre-migration assessment

You can review your current Comala Document Management usage in your hosted instance to check your workflow activity.

Go to **Confluence Global Administration** > **Comala Document Management** > **Migration CDM Usage** to generate the following pre-migration reports as downloadable CSV files:

- **Space Workflows Report**
- **Page Workflows Report**

![image-20260709-113640.png](/cms_trial/assets/305c52c7-92c9-4a12-a8c7-68b60d34f978.png)

Global and space workflows are migrated to the cloud. Page workflows are not migrated; however, before migration, they can be consolidated into a labeled space workflow.

*Import these CSV files into Excel, Google Sheets, or other compatible applications to easily filter and analyze the data.*

## Pre-migration steps

Before starting a migration, ensure that you have installed and are using the latest version of the Comala Document Management app in both your hosted data center instance and your cloud site.

You should then complete the following to prepare your instance:

### Set up your Confluence Cloud site

You must create a Confluence Cloud site and install Comala Document Management for Cloud, as well as and other necessary cloud-based apps. You must have administrator permission for the site when creating and running a migration.

### Convert page workflows to space workflows

Page workflows are not migrated to the cloud. If required, you can consolidate these as space workflows in two ways:

- **Manually** **in each space** - More info [here](/cms_trial/space/CDMC/2192902721/Moving+your+workflows+to+the+cloud/)
- **Scripted** - [Bulk consolidation using a script](/cms_trial/space/CDMC/2193130141/Support+and+troubleshooting+for+migration/)

In both cases, each page workflow is consolidated as a label space workflow.

## Production migration

We recommend migrating a production instance in several smaller groups of spaces rather than all at once. This makes it easier to review results and fix any issues.

During migration:

- Global workflows are translated automatically
- Space workflows are translated automatically.
- If a space workflow contains links to global workflows, the space includes

  - The **name** of the linked global workflow
  - A **flag** indicating that this space workflow has `scope:global`
- Hardcoded users are mapped to their Cloud user IDs.
- The current workflow state of each page is preserved.

Remember, the latest versions of both our Data Center and Cloud apps should be installed before migrating.

### Migration process steps

- [Step 1 - Assess and prepare your migration in the Confluence Cloud Migration Assistant](/cms_trial/space/CDMC/2193195711/Step+1+-+Assess+and+prepare+your+migration+in+the+Confluence+Cloud+Migration+Assistant/)
- [Step 2 - Migrate your data using the Confluence Cloud Migration Assistant](/cms_trial/space/CDMC/2193130034/Step+2+-+Migrate+your+data+using+the+Confluence+Cloud+Migration+Assistant/)
- [Step 3 - Post-migration](/cms_trial/space/CDMC/2193097068/Step+3+-+Post-migration/)

### Atlassian EAP **Cloud-first migration**

Atlassian is rolling out an [EAP for creating migrations](https://community.atlassian.com/t5/Atlassian-Migration-Program/Join-our-EAP-to-execute-your-Data-Center-to-Cloud-migration-from/ba-p/2917047) from the Data Center to the Cloud for your cloud organization. You must opt into this Atlassian EAP. It lets you create migrations from your cloud organization and is currently designed for organizations with fewer than 10,000 users.

- [Atlassian Migration Program | Join the EAP](https://community.atlassian.com/forums/Atlassian-Migration-Program/Join-our-EAP-to-execute-your-Data-Center-to-Cloud-migration-from/ba-p/2917047)

### Migration of complex instances

Some factors can [increase the complexity of your migration](https://www.atlassian.com/migration/plan/cloud-guide#understand-migration-complexity), and you may need assistance with planning. For example, if the migration involves

- Large amounts of data or users
- Several products and apps

The [Atlassian Migration Guide](https://www.atlassian.com/migration/plan/cloud-guide#atlassian-team) includes a range of resources and guides.

If you have any questions or require assistance, [contact Appfire support](http://appf.re/support).

## Resources

- [Product comparison](/cms_trial/space/CDMC/2192677102/Product+comparison/)
- [What is migrated?](/cms_trial/space/CDMC/2192870471/What+is+migrated%3F/)
- [Support and troubleshooting for migration](/cms_trial/space/CDMC/2193130141/Support+and+troubleshooting+for+migration/)