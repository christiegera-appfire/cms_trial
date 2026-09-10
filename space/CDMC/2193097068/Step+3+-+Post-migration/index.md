# Step 3 - Post-migration

## Overview

You can migrate your Comala Document Management app data from a hosted instance using the [Atlassian Confluence Cloud Migration Assistant (CCMA)](https://marketplace.atlassian.com/apps/1219672/confluence-cloud-migration-assistant?hosting=datacenter&tab=overview).

After a successful migration, post-migration tasks include:

- Review of migrated space workflows identified in the CCMA precheck as not fully cloud-compatible. If required, these need to be edited to ensure the workflow elements are cloud-compatible and the workflow functionality meets your needs
- If multiple workflows are active in a space, review the order in which the workflows are applied to ensure the correct workflow is applied to each document

You can also edit pages to add the [Document metadata macro](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CDMC&title=Document%20Metadata) to retrieve and display migrated metadata

## Prerequisites

You must have completed

- **CCMA migration task** - [Step 2 - Migrate your data using the Migration Assistant](/cms_trial/space/CDMC/2193130034/Step+2+-+Migrate+your+data+using+the+Confluence+Cloud+Migration+Assistant/)

## Post-migration

### **Edit workflows for cloud compatibility**

Some workflows might have been identified as not fully cloud-compatible during the **Migration Assistant** vendor app checks or when using the Workflow Translator for Cloud tool.

You might also need to update [workflow trigger events](/cms_trial/space/CDMC/2193950329/Trigger+events/) or [workflow trigger actions](/cms_trial/space/CDMC/2193950329/Trigger+events/).

These must be reviewed and edited using the workflow builder visual editor or code editor to ensure the functionality meets your needs in Confluence Cloud.

After migration, all workflows transferred from the server will have access to their **original server markup** within the **Cloud Workflow Builder**. This information will be available in a dedicated section for migrated workflows only.

### **Review enabled workflows**

Reapply workflows in each space using the app space settings.

- [Apply workflows at the space level](/cms_trial/space/CDMC/2193033075/At+space+level/)

![contentId-2193097068](/cms_trial/assets/91509f70-96e3-4ae3-89d7-a6a7f5cd4605.png)

When [multiple workflows are active in a space](/cms_trial/space/CDMC/2193033075/At+space+level/), you should review their order and any labels to ensure they are applied in the required order.

If the migration included a hosted app global scope workflow in the space, this is enabled by default in the cloud space. You might also need to review the space workflow names if a global-scope workflow was included in a migrated space, as space-scope workflows are migrated with a "~" prefix in the cloud to preserve the workflow order from the hosted instance.

Image — asset pipeline pending  
contentId-2360967230

Hosted app page workflows are consolidated as space workflows before migration and are included in the space.

### **Adjust workflow states**

You can manually update any mismatched workflow states:

- On a page-by-page basis, using the workflow state dialog box on each document, or
- Initialize states for all documents with an active workflow using the app space settings.

![contentId-2193097068](/cms_trial/assets/a9e7dff9-07e3-4d1e-8dd0-19980bb1300f.png)

See: [Space administration](/cms_trial/space/CDMC/2192776249/Space+administration/)

### Retrieve and display metadata

Metadata is automatically migrated through the Confluence Cloud Migration Assistant (CCMA).

The macro retrieves only the metadata and values included in the migrated document. This includes:

- Metadata from the **Comala Metadata** app
- Metadata set using the **set-metadata** macro in the hosted Comala Document Management app
- **Page-level workflow parameters** are defined in the workflow

The macro can be added to a page, and a migrated metadata value can be displayed by adding the name.

![contentId-2193097068](/cms_trial/assets/5e833493-7c94-4857-867c-304f1fbf0cbf.png)

### **Hosted workflow markup view for migrated workflows**

The [Migrated workflow view](https://appfire.atlassian.net/wiki/spaces/CDMC/pages/2570355695) in the workflow editor lets users access the **hosted app workflow markup** for a migrated workflow.

It can be accessed via the **Migrated workflow** button next to the two existing options ([visual builder editor](https://appfire.atlassian.net/wiki/spaces/CDMCD/pages/614009868) and [JSON code editor](https://appfire.atlassian.net/wiki/spaces/CDMCD/pages/614010155)).

![contentId-2193097068](/cms_trial/assets/5016e99d-701f-4b4a-b622-bf4a80117b67.png)

The view is only visible for workflows that have been migrated from a **DC instance**, providing better insight into the original hosted app workflow configuration post-migration.