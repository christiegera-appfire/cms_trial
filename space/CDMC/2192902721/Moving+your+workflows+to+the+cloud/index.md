# Moving your workflows to the cloud

## Overview

Existing **global workflows** and **space workflows** are included in the migration. A **global workflow** in a space is migrated to the cloud as an **active space workflow**. If a global-scope workflow was included in a migrated space, space-scope workflows are migrated with a "~" prefix in the cloud to preserve the workflow order from the hosted instance.

![contentId-2192902721](/cms_trial/assets/e6a85442-7dc0-4a98-9e91-0dbf11d50ffd.png)

**Page workflows** are not migrated, but you can use the [Page Workflows dashboard](https://appfire.atlassian.net/wiki/spaces/CDML/pages/1639157765) to review active page workflows in your data center instance and consolidate them into a space workflow before migration.

A global administrator can run [Workflow Usage Reports](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649957481) as part of the pre-migration assessment to generate CSV files listing the global and space workflows and page workflows in spaces across the instance.

Some workflow features function differently in the cloud (see the [Product comparison](/cms_trial/space/CDMC/2192677102/Product+comparison/) page for details). Space workflows that are not fully cloud-compatible are flagged in the **Atlassian CCMA app vendor pre-migration checks**, along with a list of global and page workflows for each space.

The Atlassian Confluence cloud and Confluence-hosted platforms work differently, so exact feature parity between the environments is not possible. Because of these functional differences, it is recommended that you review each workflow's functionality in the cloud.

Before migration, you can also use the [Workflow Translator for Cloud](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649924970) tool in your Data Center app to convert hosted app workflows into cloud-compatible workflow templates. Adding these templates to Confluence Cloud lets you review workflow functionality and make any necessary adjustments. For example, our cloud app supports a different set of workflow trigger events and actions.

## Workflow usage

Before migration, you can review your current usage of Comala Document Management workflows in your hosted instance to check your [workflow usage](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649957481).

Go to Confluence **Global Administration** > **Comala Document Management** > **Migration CDM Usage** to generate the following reports as downloadable CSV files:

- **Space Workflows and Linked Global Workflows Report**
- **Page Workflows Report**

![contentId-2192902721](/cms_trial/assets/c319a43f-f53b-44e1-b2f7-34d9f0c6bcb4.png)

Global workflows and space workflows, including linked global workflows, are migrated to the cloud. Page workflows are not migrated, but before migration, you can [consolidate a page workflow](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/1996619783/Moving+your+workflows+to+the+cloud#Consolidate-page-workflows) as a labeled space workflow to include in the migration.

## Global workflows and space workflows

A migration includes all global and space workflows, including global workflows linked to a space as global-scope workflows. These workflows are translated into their cloud-compatible equivalents. Global workflows are added to the app global workflows screen, and space workflows are added to the related app space settings in Confluence Cloud.

![contentId-2192902721](/cms_trial/assets/11fe4759-963d-4654-8a13-5c0b8ef63871.png)

Each migrated workflow includes the following:

- Label workflow conditions
- Invert labels as the Exclude labels option
- Workflow triggers with supported trigger events in the cloud
- The values of the workflow parameters that are defined at the space level

If the space workflows in your hosted instance include a linked global workflow, they are migrated and added as active space workflows in the cloud space. When a global scope workflow is migrated for a space, the space scope workflows are appended with a "~" to ensure the migrated global scope workflows are ordered at the top of the app space settings.

In Confluence Cloud, all the workflow users and user groups (in any macro that uses them) are replaced with the cloud IDs created in the cloud spaces.

After migration, the hosted app workflow template markup can be accessed from the app visual editor in Confluence Cloud. This option is only accessible and visible for a migrated workflow.

## Consolidate page workflows

Page workflows are not included in the migration. However, these can be consolidated as a space workflow before migration.

The active page workflows on a page or blog post in a space in your data center instance are displayed in the [Page Workflows dashboard](https://appfire.atlassian.net/wiki/spaces/CDML/pages/1639157765).

![contentId-2192902721](/cms_trial/assets/0eb30d85-16cb-4d96-8a1d-a273e2366e69.png)

All active page workflows are listed, even if a space workflow is currently active and applied to the page.

You can use the **Page Workflows dashboard** to consolidate a page workflow using the **Consolidate** option in the **Actions** menu.

![contentId-2192902721](/cms_trial/assets/b4985849-9616-48d1-9103-453cf33a19f5.png)

You must add a text string in the **Consolidate Page Workflow** dialog box. This string is used as a content label filter when you **Transform** the workflow into a space workflow.

![contentId-2192902721](/cms_trial/assets/0c678263-e50e-4dc0-b22e-d6e2a5310b49.png)

The workflow is added to the **Space Workflows** dashboard in your hosted instance as an active space workflow with a content label filter and is included in a migration as a space workflow with a label condition.

In the data center instance, consolidating the workflow:

- Removes it as a page workflow from the linked pages and blog posts.
- Adds the label to the linked pages and blog posts.
- Applies it as a space workflow to the labeled pages, subject to other existing active workflows.

You can also run a [bulk consolidation of your page workflows using a script](/cms_trial/space/CDMC/2193130141/Support+and+troubleshooting+for+migration/).

## CCMA Pre-Migration Workflow Assessment

The Atlassian Confluence Cloud Migration Assistant includes a vendor app and a **pre-migration workflow assessment** that checks the cloud compatibility of workflows in the migration plan.

![contentId-2192902721](/cms_trial/assets/d6c9d624-7cc2-419d-8328-f036c293113c.png)

You should use the [Workflows Usage reports](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649957481) in your hosted app global administration to identify where workflows are configured.

Global and space workflows are automatically recreated in the cloud as part of the migration, but you need to review any incompatible elements that may be changed or removed during migration.

- See: [Workflow elements translated from data center](/cms_trial/space/CDMC/2232485018/Workflow+elements+translated+from+data+center/)

Page workflows are not migrated. Before migrating, you can consolidate these as space label workflows to include them in the migration.

## Moving an individual workflow to the cloud

You translate a hosted app workflow to a cloud-compatible workflow template using the [Workflow Translator for Cloud](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649924970) tool.

![contentId-2192902721](/cms_trial/assets/cfceb73a-909f-40b1-b1d5-df28dd5bf802.png)

We recommend reviewing your workflows' functionality in the cloud as part of your preparation for migrating to Confluence Cloud.

The translated workflow template code can be copied and pasted into the [code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/) in the document management app space settings or the global workflows screen in Confluence Cloud

![contentId-2192902721](/cms_trial/assets/30fcb3e8-af00-472e-a68c-2a874d532015.png)

Saving the copied workflow adds it to the document management app space settings or the global workflows screen.

![contentId-2192902721](/cms_trial/assets/7bd50330-c24c-4a0b-9257-0c02f9561e87.png)

The tool cannot to translate all workflow elements into a cloud-compatible workflow.

## Unsupported workflow elements

Migrated workflows and the [Workflow Translator for Cloud](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649924970) tool are not able to translate all workflow elements into a cloud-compatible workflow.

- The [Workflow Translator for Cloud](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649924970) tool workflow template markup highlights unsupported workflow elements
- The **Unsupported Macros** message box provides further details

![contentId-2192902721](/cms_trial/assets/77e382f8-b6fc-4c0e-b9c3-df209cacb0dd.png)

Some workflow elements, such as layout parameters for adding footers, headers, or workflow instructions, are not supported in Confluence Cloud.

Translation of a workflow trigger is supported when the trigger has an equivalent workflow trigger event in the cloud.

Details of the workflow elements translated to the cloud are available on the [Workflow elements translated from data center](/cms_trial/space/CDMC/2232485018/Workflow+elements+translated+from+data+center/) page.

A trigger with a supported event might be translated without some trigger actions if the action is unavailable in the cloud. When this occurs, the workflow trigger in the translated cloud-compatible workflow template can have empty trigger actions.

These triggers must be edited or recreated using the [code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/) or the [visual editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/) in the cloud app.

![contentId-2192902721](/cms_trial/assets/ca6bee2e-86e8-453a-b742-1bc1f0d5eb2c.png)

## Changes in workflow functionality

Some [workflow elements are translated](/cms_trial/space/CDMC/2232485018/Workflow+elements+translated+from+data+center/), but there can be functional differences that need you to review. For example:

- **Assignment of approval reviewers**

  - No option in the workflow in the cloud to limit the users who can assign reviewers.
  - View-only users can be assigned as a reviewer to an approval. Whilst assigned, they can assign other users as a reviewer.
- **Workflow final state and draft view restriction**

  - Users are directed to the latest version of the page.
  - View-only users are not restricted by the workflow to the latest approved (final state) version.

To manage access to the latest approved pages in the cloud, you should consider using the integration with [Comala Publishing Cloud](https://marketplace.atlassian.com/apps/143/comala-publishing?hosting=cloud&tab=overview) to publish and sync pages to a separate space and manage user permissions separately from the space with your draft pages.

It is recommended to undertake a test migration and explore the workflow functionality in Confluence Cloud. This can help identify functional differences in Confluence Cloud and the required apps.

## Related pages

- [Workflow elements translated from data center](/cms_trial/space/CDMC/2232485018/Workflow+elements+translated+from+data+center/)
- <https://appfire.atlassian.net/wiki/spaces/CDML/pages/649957481>
- <https://appfire.atlassian.net/wiki/spaces/CDML/pages/649924970>
- [Product comparison](/cms_trial/space/CDMC/2192677102/Product+comparison/)