# Document report - Space level

## Overview

The **Document Report** lists the approval activity for documents in a space. It also shows the workflow applied to each document, even when several workflows are active at once.

You can filter the report by:

- **Workflow**
- **State**
- **Assigned reviewers**
- **Pending reviewers**

No entries appear if no active workflow exists on a page or in the space.

**Non-admin users** see only the *Document Report* tab. *Space Workflows* and *Settings* tabs require space-admin permissions.

## View the Document Report

To view the Document Report:

1. Log in to your Confluence space.
2. Under **Space Apps**, select **Comala Document Management**.
3. Go to the **Document Report** tab.

The report opens and shows the approval activity for the space.

![image-20260918-140217.png](/cms_trial/assets/8b618708-16aa-458e-9d0b-a8d81c863ddb.png)

### Report columns

The report table includes the following columns:

| **Column** | **Description** |
| --- | --- |
| **Title** | The document name, shown with a Page or Blog post icon. Click the title to open the content in Confluence. |
| **Workflow** | The workflow applied to the document. |
| **Scope** | Whether the workflow applies to a **Page** or a **Space**, shown with an icon. |
| **State** | The current workflow state. |
| **Expiration** | The due date for the current state, shown next to **State**. It appears when at least one active workflow includes a state with a due date, and only while the workflow is in that state. |
| **Reviewers** | Approval status icons. Click an icon to see reviewer details. |
| **Creator** | The user who created the content. |
| **Owner** | The page owner. This is empty for blog posts. |
| **Updated By** | The user who last updated the content. |
| **Updated** | The date the content was last updated. |

If a page is in a workflow state that needs **multiple approvals**, each approval shows as a separate icon in the **Reviewers** column.

![image-20260918-140930.png](/cms_trial/assets/d338f8d7-0263-4dad-9564-bc3480800784.png)

Click a **reviewer** icon to see that reviewer’s details. The list of approvers is read-only.

![image-20260918-141150.png](/cms_trial/assets/3d2fb2ad-ad95-42f3-a586-63ddd74b19af.png)

### Show or hide columns

Use the **Show or hide columns** menu in the table header to choose which columns appear.

- You can’t hide **Title** or **Expiration** (while Expiration is shown).
- Your column choices are remembered in your browser.

![image-20260918-142135.png](/cms_trial/assets/9e0d7fb6-a0d2-49fa-9f5e-b5c658b71089.png)

### Load more

When there are more results than the report shows, select **Load more** to load the next set of documents.

![image-20260921-050810.png](/cms_trial/assets/7bf4f411-9d53-4d8c-8fc4-4f50c7742032.png)

### Refresh data

If you’re a space administrator and a record seems to be missing, select **Refresh Data** to update the report.

![document-report-refresh-data.png](/cms_trial/assets/b67e7dc9-c8e6-41eb-beb4-a2e28baa9ab7.png)

## Filter the report

You can filter the report by workflow, state, assigned reviewers, and pending reviewers, and you can combine filters.

![image-20260921-054932.png](/cms_trial/assets/3668df14-ec0a-4685-b1e5-a734af5adc52.png)

### Filter by workflow

Select one or more workflows to show only their documents. Use the search box in the dropdown to find a workflow quickly.

![image-20260921-055020.png](/cms_trial/assets/5ca6a878-da31-47aa-92d1-a46dc5e3e31b.png)

### Filter by state

Select one or more workflow states to show only documents in those states. Use the search box in the dropdown to find a state quickly.

![image-20260921-055044.png](/cms_trial/assets/97e2f468-f4be-4132-9ece-ce0cb327fe5e.png)

### Filter by assigned reviewers

Select one or more users to show documents where they’re assigned as reviewers. Search for reviewers by name.

![image-20260921-055118.png](/cms_trial/assets/40b47c5b-a7cf-4d6d-86c4-ddc10cf4e79f.png)

### Filter by pending reviewers

Select one or more users to show documents with pending approvals. They’re assigned as a reviewer but haven’t approved or rejected the document yet. Search for reviewers by name.

![image-20260921-055153.png](/cms_trial/assets/0796156c-d587-4f28-bd08-8664efde88c4.png)

### Clear filters

- **Clear selection** inside a filter removes only that filter.
- **Clear filters** resets all active filters at once.

![image-20260921-055417.png](/cms_trial/assets/f87d9fc9-53a2-48e9-828e-27b05aa88e3e.png)

### No results

When your filters return no matching documents, the report shows a no-results message. Adjust or clear the filters to see documents again.

![image-20260921-055455.png](/cms_trial/assets/be426fda-7f09-4a9b-b89f-e9bc2fc0840f.png)

## Export to CSV

You can export the **Document Report** as a CSV file for offline analysis.

Select **Export to CSV** in the *Document Report* toolbar.

![image-20260921-053959.png](/cms_trial/assets/997af599-cd6c-408c-a473-b8fc6d3c7151.png)

The exported file includes the following for each document:

- Space name and space key
- Content type and title
- Content ID and version
- Creator
- Owner
- Last updated by
- Last updated at
- Workflow scope (space or page)
- Workflow name
- Workflow version
- Workflow state
- Approval name
- Approval reviewers
- Review state

The file is named using this format:

`space_document_report_[space_name]_[YYYYMMDD]_[HHMM].csv`

![image-20260921-101155.png](/cms_trial/assets/dff35a4f-fe2a-4605-8273-a80d340ec05e.png)

The report shows one space at a time. To combine data across spaces and build custom dashboards, use the CSV export.