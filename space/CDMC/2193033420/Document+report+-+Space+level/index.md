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

![image-20260918-140217.png](/cms_trial/assets/44f06c4d-2141-4f7d-95eb-11a22ac2429e.png)

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

![image-20260918-140930.png](/cms_trial/assets/cad04ce5-ea71-4290-b2e4-684ea3f18946.png)

Click a **reviewer** icon to see that reviewer’s details. The list of approvers is read-only.

![image-20260918-141150.png](/cms_trial/assets/ffaeccfb-d85c-4a5b-939a-dfcda6dd8b87.png)

### Show or hide columns

Use the **Show or hide columns** menu in the table header to choose which columns appear.

- You can’t hide **Title** or **Expiration** (while Expiration is shown).
- Your column choices are remembered in your browser.

![image-20260918-142135.png](/cms_trial/assets/466124ba-9c7c-436b-baea-2837a0209582.png)

### Load more

When there are more results than the report shows, select **Load more** to load the next set of documents.

![image-20260921-050810.png](/cms_trial/assets/cfffc645-1a58-4eda-9b66-354298324958.png)

### Refresh data

If you’re a space administrator and a record seems to be missing, select **Refresh Data** to update the report.

![document-report-refresh-data.png](/cms_trial/assets/74fe488e-703f-4b75-b76d-e374921fced5.png)

## Filter the report

You can filter the report by workflow, state, assigned reviewers, and pending reviewers, and you can combine filters.

![image-20260921-054932.png](/cms_trial/assets/8da391f6-d851-469c-9ada-1f05c2773061.png)

### Filter by workflow

Select one or more workflows to show only their documents. Use the search box in the dropdown to find a workflow quickly.

![image-20260921-055020.png](/cms_trial/assets/2519752b-40e3-44e3-b944-5605db019b93.png)

### Filter by state

Select one or more workflow states to show only documents in those states. Use the search box in the dropdown to find a state quickly.

![image-20260921-055044.png](/cms_trial/assets/3f8f524c-c6da-49c5-bb94-75ec35cc989e.png)

### Filter by assigned reviewers

Select one or more users to show documents where they’re assigned as reviewers. Search for reviewers by name.

![image-20260921-055118.png](/cms_trial/assets/cd0022f8-f7e2-41ec-b6fe-bfc8d6360a6e.png)

### Filter by pending reviewers

Select one or more users to show documents with pending approvals. They’re assigned as a reviewer but haven’t approved or rejected the document yet. Search for reviewers by name.

![image-20260921-055153.png](/cms_trial/assets/413c6294-f5a9-465a-8da7-43bfed907628.png)

### Clear filters

- **Clear selection** inside a filter removes only that filter.
- **Clear filters** resets all active filters at once.

![image-20260921-055417.png](/cms_trial/assets/ebb5217e-34b2-45ab-a065-e2b41cf57187.png)

### No results

When your filters return no matching documents, the report shows a no-results message. Adjust or clear the filters to see documents again.

![image-20260921-055455.png](/cms_trial/assets/bb49602f-c1b2-4341-b203-c46e4c15d2b3.png)

## Export to CSV

You can export the **Document Report** as a CSV file for offline analysis.

Select **Export to CSV** in the *Document Report* toolbar.

![image-20260921-053959.png](/cms_trial/assets/477ac40c-8ca4-4572-9396-c9fe21e97887.png)

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

![image-20260921-101155.png](/cms_trial/assets/8ba4ee45-e635-42eb-90be-a6b60b3ce633.png)

The report shows one space at a time. To combine data across spaces and build custom dashboards, use the CSV export.