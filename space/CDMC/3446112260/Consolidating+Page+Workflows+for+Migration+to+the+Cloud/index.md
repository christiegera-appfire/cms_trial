# Consolidating Page Workflows for Migration to the Cloud

## Overview

Page workflows are not migrated to the Cloud. If you need to preserve them, consolidate each page workflow into a labeled space workflow before migration.

You can consolidate page workflows in two ways:

- **Manually** - consolidate the page workflow in each space using the Page Workflows dashboard (see the manual consolidation section below)
- **Scripted** - bulk consolidation across multiple spaces using a script (see the [bulk consolidation](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/3404955773/Consolidating+Page+Workflows+for+Migration+to+the+Cloud#Scripted-bulk-consolidation) section)

## Moving your page workflows

Go to **Confluence Global Administration** > **Comala Document Management** > **Migration CDM Usage** and generate the **Page Workflows Report**.

This CSV file lists all active page workflows across your instance.

If the report is empty, you can skip this step.

## Manual consolidation (per space)

Use the Page Workflows dashboard in each space to consolidate workflows one at a time.

1. Go to **Space tools** > **Page Workflows dashboard**
2. All active page workflows in the space are listed, even if a space workflow is also active on the page
3. For each page workflow, open the **Actions** menu and select **Consolidate**
4. In the **Consolidate Page Workflow** dialog, enter a label string. This string will be used as the content label filter when the workflow is converted to a space workflow.
5. Click **Transform** to complete the consolidation

This does the following:

- Removes the page workflow from the linked pages and blog posts
- Adds the label to those pages and blog posts
- Creates a new space workflow with the label condition
- Applies the workflow to the labeled pages as a space workflow

The consolidated workflow is now included in the space's workflow list and will be migrated.

## Scripted bulk consolidation

For Confluence instances with many page workflows across multiple spaces, you can use the consolidation script.

### Prerequisites

- The **Page Workflows Report** CSV file from the Workflow Usage screen
- Python 3 installed
- Access to the Confluence REST API

### Run the script

**Script**: ▢

consolidate\_page\_workflows.py  
**How to run it:**`python3 consolidate_page_workflows.py page-workflows.csv`  
**Description**: This script reads the CSV file containing page workflows from the **Workflows Usage Report** and consolidates them into space-level workflows using the Confluence REST API. When run, the script:

1. Prompts you to choose the grouping logic:

   - `1`: Group by Space Key + Workflow Name
   - `2`: Group by Space Key + Workflow Name + Workflow Markup
2. Automatically generates a unique label for each group:  
   `WorkflowName` (cleaned) + incremental number (e.g., `SimpleApproval1`)
3. Sends a `curl` request per group to the Confluence REST API to perform the consolidation.

In both cases, page workflows are consolidated as a label space workflow.

### Verification

After running the script:

- Check the **Space Workflows** dashboard in each affected space to confirm that the consolidated workflows appear
- Verify that the content labels have been applied to the correct pages
- Run a test migration on a non-production space to confirm that the consolidated workflows migrate correctly

## Related pages

- [Migrate from Data Center to Cloud (Forge)](/cms_trial/space/CDMC/3446079850/Migrate+from+Data+Center+to+Cloud+(Forge)/)
- [Moving your workflows to the cloud](/cms_trial/space/CDMC/2192902721/Moving+your+workflows+to+the+cloud/)