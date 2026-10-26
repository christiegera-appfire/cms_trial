# At space level

## Overview

In Comala Document Management, workflows can be applied at the space level so that every page and blog post in a Confluence space follows a consistent review and approval process.

This page covers how to apply a space workflow, set evaluation priority, and use label-based conditions.

## Apply a space workflow

A workflow can be applied across all documents in a space. Only space administrators can enable and apply space workflows.

To apply a workflow at the space level:

1. Go to **Space apps** > **Comala Document Management**.
2. In the *Space Workflows* tab, enable the required workflow using the toggle next to its name.

The workflow is applied to all pages and blog posts in the space.

![Space Workflows tab showing an enabled workflow toggle.](/cms_trial/assets/3b4ba707-c3d9-47e9-ac78-a1a1b0cd6989.png)

Workflows can’t be added to a space homepage. Confluence Cloud restricts the use of certain properties, like the workflow content byline, on the homepage.

An active space workflow takes priority over any page-level workflow applied to the same document.

## Multiple active workflows

If you’re a space administrator, you can enable multiple workflows and set the order in which workflows are evaluated using the drag-and-drop option.

- Enabled workflows are evaluated from top to bottom, and evaluation stops at the first match.
- Disabled workflows are skipped.
- Only one workflow can be applied to a document at a time.
- Changes take effect after you save the new order.

For example, if two workflows are active in this order:

1. Legal Review (label: `legal`) - applies to documents with the `legal` label.
2. General Approval (no labels) - applies to all other documents.

A page with the `legal` label gets the Legal Review workflow. A page without any labels gets the General Approval workflow.

![Space Workflows tab showing Content Expiry Workflow.](/cms_trial/assets/55b776e1-1f3d-4b68-a469-db75b4f186bf.png)![Drag-and-drop workflow ordering controls in the Space Workflows tab.](/cms_trial/assets/31a68a09-099a-4ac9-8b62-9dad78c0d064.png)

If a document doesn’t meet the conditions for any active workflow, no workflow is applied, and a **No Applicable Workflow** byline is displayed on the page.

## Label-based workflows

Workflows can be assigned to specific content labels. They apply only to pages with those labels, or exclude pages with certain labels. Labels and workflows stay in sync in both directions: applying a label to a page activates the corresponding workflow, and selecting a workflow from the *Workflow State Dialog* adds the required label to the page.

### Apply a workflow with labels

To add labels to your workflow,

1. Open the required custom workflow from Space Settings and click **Edit Workflow**.
2. Add one or more labels to a workflow using the visual editor under the **Labels** option.   
   The added labels are displayed in the *Space Workflows* tab.

![Edit Workflow dialog and Space Workflows screen showing how to apply a workflow with labels.](/cms_trial/assets/16e5c09c-fba7-4733-9c38-b6d893fb8c7c.png)

When a workflow has labels configured:

- The workflow applies only to documents that have at least one of the specified labels.
- If multiple workflows are active, the first matching workflow in the evaluation order is applied.
- When you add more than one label, the workflow applies to any document with at least one of the specified labels.

For example, if a workflow is configured with the labels `compliance` and `audit`, the workflow applies to any document that has at least one of these labels.

### Exclude labels

Use the **Exclude labels** option to prevent a workflow from applying to pages with specific labels. All other pages in the space get the workflow.

For example, if a workflow is set to exclude the label `draft`, the workflow applies to all pages in the space that don’t have the `draft` label. Pages with the `draft` label are skipped.

To exclude labels,

1. Open the required custom workflow from space settings and click **Edit Workflow**.
2. In the *Labels* option, select the **Exclude labels** checkbox. This applies the workflow only to documents that don’t have any of the specified labels. When the **Exclude labels** option is selected, the labels are displayed as **Excluding** in the *Space Workflows* tab.

![Workflow editor with the Exclude labels option enabled.](/cms_trial/assets/b513ff3b-f522-49ef-adf7-b032fb77219e.png)

### Sticky labels

Sticky labels ensure that essential labels remain consistently applied to a workflow. When sticky labels are added, only administrators can remove them. Non-admin users can still manage regular labels.

For example, if the label `regulated` is set to sticky, only administrators can remove it from a page. Non-admin users can still add or remove other labels on that page.

To add sticky labels:

1. Open the required custom workflow from space settings and click **Edit Workflow**.
2. Under *Advanced* options, add the required sticky labels.

![Advanced settings showing sticky label configuration.](/cms_trial/assets/da7e47e5-5d13-4bd6-9eb5-ceca0fae45aa.png)

## Bulk apply workflows

Administrators can bulk apply workflows to scan all pages and blog posts in a space, apply the appropriate workflow, and initialize their workflow status. This ensures all documents appear correctly in the Document Report.

See [Space Administration](/cms_trial/space/CDMC/2192776249/Space+administration/) for detailed steps on **Apply Workflow Updates** and **Initialize States.**

**Related topics**

- [Space administration](/cms_trial/space/CDMC/2192776249/Space+administration/)
- [Apply workflows at page level](/cms_trial/space/CDMC/2192838126/At+page%2Fblog+level/)
- [Global workflows](/cms_trial/space/CDMC/2276786309/Global+workflows/)
- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)
- [Visual builder editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/)