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

![image-20261021-123932.png](/cms_trial/assets/c203f8b8-138f-4406-9459-c69af490797d.png)

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

![Global Document Report showing multiple reviewer status icons for a document requiring multiple approvals.](/cms_trial/assets/266ca7cc-2cc6-43b3-8ba0-b86ee1d62323.png)

Click a **reviewer** icon to see that reviewer's details. The list of approvers is read-only.

![Reviewer details displayed after selecting a reviewer status icon in the Global Document Report.](/cms_trial/assets/67081e33-cf4f-47e6-8b43-25459c8f6891.png)

### Show or hide columns

Use the **Show or hide columns** menu in the table header to choose which columns appear.

- You can't hide **Title**.
- Your column choices are remembered in your browser.

![image-20261021-131717.png](/cms_trial/assets/75ce6876-ae5e-4737-b67a-2d5c3e491268.png)

### Load more

When there are more results than the report shows, select **Load more** to load the next set of documents.

## Filter the report

You can filter the report by space, workflow, state, assigned reviewers, and pending reviewers, and you can combine filters.

![Filter controls available in the Global Document Report.](/cms_trial/assets/48f1af3e-efe1-40a1-bcc2-b8e5729c4a53.png)

### Filter by space

Select one or more spaces to show only their documents. Use the search box in the dropdown to find a space quickly.

![Space filter showing available Confluence spaces with a search field.](/cms_trial/assets/a9510765-0c6f-4d75-8a24-c37a17ebe2ea.png)

### Filter by workflow

Select one or more workflows to show only their documents. Use the search box in the dropdown to find a workflow quickly.

![Workflow filter showing available workflows with a search field.](/cms_trial/assets/91063f16-a541-4d87-8d2d-0e421a82a042.png)

### Filter by state

Select one or more workflow states to show only documents in those states. Use the search box in the dropdown to find a state quickly.

![State filter showing available workflow states with a search field.](/cms_trial/assets/c8063159-43a7-489b-95a8-b303bc61777f.png)

### Filter by assigned reviewers

Select one or more users to show documents assigned to them as reviewers. Search for reviewers by name.

![Assigned reviewers filter showing users available for selection.](/cms_trial/assets/2fb5de67-feef-4ce7-a585-2f2912dafc59.png)

### Filter by pending reviewers

Select one or more users to show documents with pending approvals. They're assigned as reviewers but haven't approved or rejected the document yet. Search for reviewers by name.

![Pending reviewers filter showing reviewers with outstanding approvals.](/cms_trial/assets/12014e08-b852-4dd1-a2de-0bcfef56bae9.png)

### Clear filters

- **Clear selection** inside a filter removes only that filter.
- **Clear filters** resets all active filters at once.

![Global Document Report with the Clear filters option for resetting all active filters.](/cms_trial/assets/b7476c37-31b4-48c2-b40e-5cf64c838d4f.png)

### No results

When your filters return no matching documents, the report shows a no-results message. Adjust or clear the filters to see documents again.

![Global Document Report displaying a no-results message after filters return no matching documents.](/cms_trial/assets/87ec28e3-33eb-4675-b31a-60f33d67971c.png)

## Export to CSV

You can export the **Global** **Document Report** as a CSV file for offline analysis.

Select **Export to CSV** under the *Global Document Report* tab.

![image-20261021-124430.png](/cms_trial/assets/4582b21e-f8f9-4bfe-82fd-1356b769d0c8.png)

The exported file includes the following for each document:

- Space name and space key
- Content type and title
- Content ID and version
- Creator
- Owner
- Created at
- Last updated by
- Last updated at
- Workflow scope (space or page)
- Workflow name
- Workflow version
- Workflow state
- Expiration
- Approval name
- Approval reviewers
- Review state

The file is named using this format:

`global_document_report_[user_name]_[YYYYMMDD]_[HHMM].csv`