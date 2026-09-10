# Space administration

## Overview

Space administration in Comala Document Management gives space administrators centralized control over workflows, settings, and reporting within a space.

To access space settings, go to **Space apps** > **Comala Document Management**.

Space settings are organized into three tabs:

- **Space Workflows** - view, create, enable, and manage workflows for the space. You can also link or copy global workflows, reorder workflow priorities, and run bulk operations such as initializing states.
- **Settings** - configure space-level preferences, such as how restrictions are handled when a document reaches a final state.
- **Document Report** - view a report of all approval activities in the space, filter by status, and export to CSV.

![Comala Document Management space administration page showing the Space Workflows, Settings, and Document Report tabs.](/cms_trial/assets/76d85847-e0be-493f-abce-36d70a468e74.png)

## Space workflows

### Workflows list

The *Space Workflows* tab displays all workflows in the space, including built-in templates, linked global workflows, copied workflows, and custom workflows.

- Built-in workflow templates are fully editable. You can customize or delete them to match your process. Deleted workflows can't be restored through the app, so consider the impact on existing configurations before deleting.
- Workflow actions (edit, duplicate, delete, initialize states, view details) are grouped under the **three-dot menu** (⋯) for each workflow.

  ![Comala Document Management space administration page showing the Space Workflows, Settings, and Document Report tabs.](/cms_trial/assets/76d85847-e0be-493f-abce-36d70a468e74.png)![Space workflow list with the More actions menu open for a workflow.](/cms_trial/assets/8b15d0e1-65df-43c4-b062-07e6bcf911bf.png)
- Drag and drop workflows to set evaluation priority. Enabled workflows are evaluated from top to bottom, and evaluation stops at the first match. Disabled workflows are skipped. Changes take effect after you save the new order.

![Comala 2026 release notes updated settings view](/cms_trial/assets/529fd8b2-da5e-4dcf-96f2-3ab94dfb1956.png)

See [Apply workflows](/cms_trial/space/CDMC/2192870271/Apply+workflows/) for detailed steps on enabling and applying workflows to your space.

### Link or copy a global workflow

You can link or copy a global workflow to your space from the *Space Workflows* tab. Click **Link/Copy Workflow** to view available global workflows.

- **Link** - creates a reference to the global workflow. A linked workflow can't be edited at the space level and automatically syncs future updates.
- **Copy** - creates an independent copy of the workflow that you can edit without affecting the original.

![Link or Copy Workflow dialog listing available global workflows.](/cms_trial/assets/93d08968-8345-448a-9c22-7aa204362418.png)

See [Global workflows](/cms_trial/space/CDMC/2276786309/Global+workflows/) for more details.

## Space utilities

### Apply workflow updates

Applies all current space-level workflows to uninitialized documents in the space. This scans every page and blog post to assign the correct workflow and state based on your current configuration.

![Space utilities page showing the Apply workflow updates option.](/cms_trial/assets/e2a29eed-da97-4136-aaca-3a28ce19ebfa.png)

### Initialize states

Set a specific workflow state across all pages and blog posts for an active workflow.

1. In the **three-dot menu** (**⋯**) for the active workflow, click **Initialize States**.
2. In the *Bulk State Override* dialog, select a state from the **State** dropdown.
3. Select **Override existing states** to apply the state to all pages, including those already processed. Leave it unchecked to set the state only for unprocessed pages.

Unprocessed pages are pages with an applied workflow where no workflow events or actions have occurred since the workflow was applied. The progress of the bulk state override is displayed in the dialog. You can click **Stop** to exit the process, but this doesn't undo changes to pages already processed.

![Initialize states dialog for selecting a workflow state and overriding existing states.](/cms_trial/assets/c61831a1-9b94-492d-8089-ad041e5e9da4.png)

### Reindex workflows

Use **Reindex workflows** after importing a space from one cloud to another to ensure the workflows function correctly. This updates the document states for pages you haven't visited yet.

Reindex workflows is only used for cloud-to-cloud imports. It isn't required when migrating content from a server or data center instance.

## Settings tab

### Remove restrictions

Enable this setting to automatically remove page-level restrictions when a document reaches a final workflow state.

1. In the *Settings* tab, enable the **Remove restrictions** toggle.
2. Confirm the setting in the dialog. Once enabled, restrictions are automatically removed when any workflow in the space transitions to a final state. This setting can only be changed when a workflow is active in the space.

![Settings tab showing the Remove restrictions toggle.](/cms_trial/assets/06b04239-a45b-413b-b123-fec8fd5f3082.png)

### Content restrictions

Configure how CDM handles restricted pages from the *Content Restrictions* section under the *Settings* tab.

Two toggles are available:

- **Grant Automatic Add-on User Access**: automatically grants the add-on edit access when you restrict a document. This ensures workflows continue to function on restricted pages. Turn this off to prevent the add-on from accessing restricted pages. When disabled, workflows stop functioning on those pages.
- **Enforce & Lock Space-Level Override**: enforces the above setting globally and locks it for space admins, preventing them from overriding it at the space level. When this toggle is enabled, the **Grant Automatic Add-on User Access** setting can’t be changed from the space settings.

![Content Restrictions settings showing Grant Automatic Add-on User Access and Remove Restrictions options.](/cms_trial/assets/219e7518-4490-424a-99ca-e05923e7e86a.png)

These settings are configured at the global level by site administrators. Space admins can adjust the **Grant Automatic Add-on User Access** toggle at the space level only if the **Enforce & Lock Space-Level Override** toggle is disabled in [Global administration](/cms_trial/space/CDMC/2193129643/Global+administration/).

## Document report

The *Document Report* tab displays a report of all approval activities in the space. You can export the report to CSV, filter by status, and view your assigned or pending approvals.

![Document Report tab displaying approval activity with filtering and export options.](/cms_trial/assets/64c053dd-dbd8-4bc9-801f-6f6b6da72c09.png)

## Set workflow parameter values

When a workflow with parameters is active in the space, you can edit parameter values from the **three-dot menu** (**⋯**) for that workflow. See [Parameters](/cms_trial/space/CDMC/2192837939/Parameters/) for details.

### **Related topics**

- [Apply workflows](/cms_trial/space/CDMC/2192870271/Apply+workflows/)
- [Global workflows](/cms_trial/space/CDMC/2276786309/Global+workflows/)
- [Global administration](/cms_trial/space/CDMC/2193129643/Global+administration/)
- [Parameters](/cms_trial/space/CDMC/2192837939/Parameters/)
- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)