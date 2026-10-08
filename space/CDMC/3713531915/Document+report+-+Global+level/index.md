# Document report - Global level

## Overview

The **Global Document Report** lists approval activity for documents across *all spaces in your Confluence instance* in a single view. It also shows the workflow applied to each document, even when several workflows are active at once.

Unlike the space-level Document Report, which shows one space at a time, the Global Document Report brings every space together in one place.

You can filter the report by:

- **Space**
- **Workflow**
- **State**
- **Assigned reviewers**
- **Pending reviewers**

## View the Global Document Report

To view the Global Document Report:

1. Go to **Apps** and select **Comala Document Management**.
2. Open the *Global Document Report* tab.

The report opens and shows approval activity across every space in the instance.

![Global Document Report showing approval activity for documents across multiple Confluence spaces.](/cms_trial/assets/f55fb154-d916-475f-85c1-5e378079ca37.png)

Pages without an active workflow do not appear in the report.

### Report columns

The report table includes the following columns:

| **Column** | **Description** |
| --- | --- |
| **Title** | The document name, shown with a Page or Blog post icon. Click the title to open the content in Confluence. |
| **Space** | The space the document belongs to. |
| **Workflow** | The workflow applied to the document. |
| **Scope** | Whether the workflow applies to a **Page** or a **Space**, shown with an icon. |
| **State** | The current workflow state. |
| **Reviewers** | Approval status icons. Click an icon to see reviewer details. |
| **Creator** | The user who created the content. |
| **Owner** | The page owner. This is empty for blog posts. |
| **Updated By** | The user who last updated the content. |
| **Updated** | The date the content was last updated. |

If a page is in a workflow state that needs **multiple approvals**, each approval shows as a separate icon in the **Reviewers** column.

![Global Document Report showing multiple reviewer status icons for a document requiring multiple approvals.](/cms_trial/assets/63d133cb-aa5f-4b44-b4b0-2fcdbf8e7a75.png)

Click a **reviewer** icon to see that reviewer's details. The list of approvers is read-only.

![Reviewer details displayed after selecting a reviewer status icon in the Global Document Report.](/cms_trial/assets/519183c7-4930-4d82-aae0-9d1870080fa6.png)

### Show or hide columns

Use the **Show or hide columns** menu in the table header to choose which columns appear.

- You can't hide **Title**.
- Your column choices are remembered in your browser.

![Show or hide columns menu for selecting which report columns are displayed.](/cms_trial/assets/4a040276-fde1-4013-9bb1-27b096decf2c.png)

### Load more

When there are more results than the report shows, select **Load more** to load the next set of documents.

## Filter the report

You can filter the report by space, workflow, state, assigned reviewers, and pending reviewers, and you can combine filters.

![Filter controls available in the Global Document Report.](/cms_trial/assets/4735e4d3-c8cf-4075-bdd6-233af76aff89.png)

### Filter by space

Select one or more spaces to show only their documents. Use the search box in the dropdown to find a space quickly.

![Space filter showing available Confluence spaces with a search field.](/cms_trial/assets/00e6f64e-fd8f-43cb-848d-2d8f23fde143.png)

### Filter by workflow

Select one or more workflows to show only their documents. Use the search box in the dropdown to find a workflow quickly.

![Workflow filter showing available workflows with a search field.](/cms_trial/assets/91ade043-78d9-4da4-b0ac-1fb8d53fc53c.png)

### Filter by state

Select one or more workflow states to show only documents in those states. Use the search box in the dropdown to find a state quickly.

![State filter showing available workflow states with a search field.](/cms_trial/assets/bf68d7ff-219f-46c4-9f4c-51c0ece31e08.png)

### Filter by assigned reviewers

Select one or more users to show documents assigned to them as reviewers. Search for reviewers by name.

![Assigned reviewers filter showing users available for selection.](/cms_trial/assets/6e735824-8e49-4793-945e-d499fd2616e9.png)

### Filter by pending reviewers

Select one or more users to show documents with pending approvals. They're assigned as reviewers but haven't approved or rejected the document yet. Search for reviewers by name.

![Pending reviewers filter showing reviewers with outstanding approvals.](/cms_trial/assets/17a5cd12-a211-4ee6-8006-165fbee9fdd1.png)

### Clear filters

- **Clear selection** inside a filter removes only that filter.
- **Clear filters** resets all active filters at once.

![Global Document Report with the Clear filters option for resetting all active filters.](/cms_trial/assets/96630020-4542-4b62-9215-c3ba43761290.png)

### No results

When your filters return no matching documents, the report shows a no-results message. Adjust or clear the filters to see documents again.

![Global Document Report displaying a no-results message after filters return no matching documents.](/cms_trial/assets/cb92f3cd-6710-459e-b3e0-ce3a65705332.png)