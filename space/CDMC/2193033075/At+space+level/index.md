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

![Space Workflows tab showing an enabled workflow toggle.](/cms_trial/assets/34b6154e-a9e6-4d53-8e36-19d90589d9f2.png)

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

![Space Workflows tab showing Content Expiry Workflow.](/cms_trial/assets/6b64b275-dba7-47ec-8032-8d9bbd49c4c6.png)![Drag-and-drop workflow ordering controls in the Space Workflows tab.](/cms_trial/assets/7f59fe47-9b5e-4131-a52f-327b3fd23834.png)

If a document doesn’t meet the conditions for any active workflow, no workflow is applied, and a **No Applicable Workflow** byline is displayed on the page.

## Label-based workflows

Workflows can be assigned to specific content labels. They apply only to pages with those labels, or exclude pages with certain labels. Labels and workflows stay in sync in both directions: applying a label to a page activates the corresponding workflow, and selecting a workflow from the *Workflow State Dialog* adds the required label to the page.

### Apply a workflow with labels

To add labels to your workflow,

1. Open the required custom workflow from Space Settings and click **Edit Workflow**.
2. Add one or more labels to a workflow using the visual editor under the **Labels** option.   
   The added labels are displayed in the *Space Workflows* tab.

![Edit Workflow dialog and Space Workflows screen showing how to apply a workflow with labels.](/cms_trial/assets/bdbe8957-4265-44a7-8b21-1c07c15404e3.png)

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

![Workflow editor with the Exclude labels option enabled.](/cms_trial/assets/60600d83-ba2a-4c4a-9d70-abcb26c400f4.png)

### Sticky labels

Sticky labels ensure that essential labels remain consistently applied to a workflow. When sticky labels are added, only administrators can remove them. Non-admin users can still manage regular labels.

For example, if the label `regulated` is set to sticky, only administrators can remove it from a page. Non-admin users can still add or remove other labels on that page.

To add sticky labels:

1. Open the required custom workflow from space settings and click **Edit Workflow**.
2. Under *Advanced* options, add the required sticky labels.

![Advanced settings showing sticky label configuration.](/cms_trial/assets/20600af0-4b06-453a-9a32-e7c4c938d028.png)

## Bulk apply workflows

Administrators can bulk apply workflows to scan all pages and blog posts in a space, apply the appropriate workflow, and initialize their workflow status. This ensures all documents appear correctly in the Document Report.

See [Space Administration](/cms_trial/space/CDMC/2192776249/Space+administration/) for detailed steps on **Apply Workflow Updates** and **Initialize States.**

**Related topics**

- [Space administration](/cms_trial/space/CDMC/2192776249/Space+administration/)
- [Apply workflows at page level](/cms_trial/space/CDMC/2192838126/At+page%2Fblog+level/)
- [Global workflows](/cms_trial/space/CDMC/2276786309/Global+workflows/)
- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)
- [Visual builder editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/)