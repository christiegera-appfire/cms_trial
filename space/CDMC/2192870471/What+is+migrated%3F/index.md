# What is migrated?

## Overview

When migrating to Comala Document Management for Cloud using the Atlassian CCMA, the following are included in the migration:

- Global workflow and space workflows
- Current workflow state and workflow-related data within this state

For audit purposes, the migration data for each page includes a record of the document workflow events and activity history as a custom content property in CSV file format (from Comala Document Management Data Center v7.10.1).

You can also include page metadata and page workflows in the migration data if you undertake the following tasks before migration:

- [Consolidate your page workflows](/cms_trial/space/CDMC/2192902721/Moving+your+workflows+to+the+cloud/) as a label space workflow

In the hosted Confluence app, a global administrator can run [pre-migration reports](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649957481) on workflow usage to help prepare for a migration to Confluence Cloud.

## Workflow migration

In a migration, global workflows and space workflows are translated into their cloud-valid equivalents. The migrated workflow includes

- all the users and user groups (in any macro that uses them), replaced with the right cloud IDs, are created in the cloud spaces (taking into account if they were enabled or disabled on the server side)
- **Label** conditions, including **Invert labels**
- workflow parameter values defined at the space level

All the linked global scope workflows in a space are migrated and automatically set as enabled space workflows in the migrated space. When the migrated space includes both global scope and space workflows, space scope workflow names are appended with a "~" prefix in the cloud. This means that the workflow order in the app space settings is maintained from the hosted instance (v7.12.1+).

![contentId-2192870471](/cms_trial/assets/0f4d64e1-dd96-4c6a-a4f1-b15c69e895bb.png)

**Page workflows** in each space are not included in the migration. However, a space administrator can [consolidate page workflows](/cms_trial/space/CDMC/2192902721/Moving+your+workflows+to+the+cloud/) in each space as a space workflow before migration using the Page Workflows dashboard in the data center app.

The Atlassian CCMA includes an app vendor precheck for the workflows in the spaces to be migrated. This assessment checks

- Which global and space workflows are fully cloud-compatible
- Whether the space workflows include global-scope workflows
- Whether page workflows are present in the selected spaces

See: [Moving your workflows to the cloud](/cms_trial/space/CDMC/2192902721/Moving+your+workflows+to+the+cloud/)

## Migration of the current workflow state

The migration includes the data for the current workflow state on a page.

The migrated workflow state data includes the following elements (if present):

![contentId-2192870471](/cms_trial/assets/7139e3eb-5309-4131-a6e3-1f32643cb93b.png)

- state due date
- assignees of any approvals in the state
- status of each assignee in each approval

  - approved
  - rejected
  - pending
- byline link to the last approved version (the **View approved** byline)

The workflow **document activity report** on the migrated page in Confluence Cloud includes all the workflow activity that occurred in the current workflow state.

Data for the current workflow state is migrated only for pages with an active workflow.

Once you use Comala Document Management in the Cloud, the page's workflow state is set using the migrated data. Subsequently, workflow events and activities are recorded as part of the page-level document activity.

## Migrating metadata

Metadata is now automatically migrated through the Confluence Cloud Migration Assistant (CCMA), eliminating the need for manual export. The following metadata is included in the migration and available on the page or blog post in the cloud:

- Metadata set with the "set-metadata" trigger action
- Metadata set with the [Comala Metadata app](https://marketplace.atlassian.com/apps/5295/comala-metadata?hosting=datacenter&tab=overview) page macros
- [Workflow Parameters](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649760641) at page level

The transfer order for Data Center migration follows the sequence as shown below:

1. **Global Workflows**
2. **Space Workflows and Page State** – starts after Global Workflows migration is complete
3. **Document Activity and Metadata** – starts after Space Workflows and Page State migration is complete.

The metadata is added as a JSON content property on each page and blog post, and it can be retrieved in the Confluence Cloud site using the Comala Document Management Cloud [**Document metadata**](/cms_trial/space/CDMC/2192838382/Document+Metadata+Get/) [macro](/cms_trial/space/CDMC/2192838382/Document+Metadata+Get/).

In the hosted Confluence app, a global administrator can run an [audit and validation report](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649957481) to generate a CSV file containing all key-value pairs of page parameters and metadata.

## Workflow historical activity migration

In the cloud app, the **Document Activity report** on a migrated page includes the last workflow state and the related workflow state information. The document activity also includes a **View Historical Activity** option (from Comala Document Management Data Center 7.10.1) that lets you view the **migrated full workflow history data**. This means any historical activity information that was moved from the server during migration, such as who edited or approved a page, is now easily accessible directly from the report with a single click.

![contentId-2192870471](/cms_trial/assets/f4778a46-6c46-42ca-b957-4aacb9e4f8b1.png)

Migrated workflow history does not merge with the existing Cloud document activity.