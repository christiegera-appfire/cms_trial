# At page/blog level

## Overview

Page-level workflows in Comala Document Management let you apply a workflow to an individual page or blog post instead of applying it across the entire space.

For a workflow to be available as a page-level workflow, it must meet the following conditions:

- The workflow must be listed in the space’s workflow list.
- All workflows on the *Space Workflows* page must be **disabled** (if enabled, they’re treated as space workflows).
- The workflow must have **no labels** configured (if labels are defined, they are used for automatic label-based initialization).
- Page-level workflows can’t be applied when a space-level workflow is active. Space-level workflows take priority over page-level workflows.

## Add a workflow to a page

1. Go to the page where you want to apply the workflow.
2. Click the **Document Management** status indicator in the page byline to open the *Workflow State* dialog.
3. Select **Apply to Content** in the *Workflow State* dialog to apply the workflow to that page.

![Workflow State Dialog with the Apply to Content and Apply to Space options.](/cms_trial/assets/e26c1979-52db-4b2b-a729-9c4a6f9b2733.png)

1. The available page workflows are displayed in the dialog. Select the required workflow.
2. Click **Apply Workflow**.

   ![Apply Workflow dialog showing the list of available page workflows.](/cms_trial/assets/c22b12db-6cec-4179-baa6-37cf8c68dec1.png)

The initial state of the workflow is displayed in the page byline. For example, the page transitions to the *Review* state as defined in the workflow.

![Workflow state dialog displaying the applied workflow and current Review state.](/cms_trial/assets/33b27baa-0ae9-4174-a1c8-ad14522cf2c5.png)

- Only one workflow can be active on a page at a time. Remove the existing workflow before adding a new one.
- Copying a page doesn’t carry over its workflow state or page-level workflow assignment. Apply the workflow separately after copying.
- To remove a page workflow, open the *Workflow State* dialog and select **Remove Workflow** from the **Actions** menu.

See the [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/) page for more details on managing workflows from the dialog.