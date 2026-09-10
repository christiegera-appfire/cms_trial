# Document report - Space level

## Overview

The document report provides a list of all the approval activities in a space. The report can be filtered by one or more workflow states and assigned approvals for the current user. The report also includes the workflow applied to each document, including cases where multiple workflows are active in a space.

No entries are displayed if there is no active workflow on a page or in the space.

**Non-admin users** see only the *Document Report* tab. *Space Workflows* and *Settings* tabs require space-admin permissions.

## View the document report

To view the **Document Report**:

1. Log in to your Confluence space.
2. Choose **Comala document management** under *Space Apps*.
3. Go to the *Document Report* tab.

The document report displays workflow activities.

![Space apps menu showing the Document Report tab.](/cms_trial/assets/3ea6277b-4dd6-4645-bdd4-5de6b7120918.png)![Document Report listing documents, workflow status, reviewers, and approvals.](/cms_trial/assets/dd2f257b-3f40-49e5-afe4-ca68a1c85e1b.png)

The Expiration column appears in the document report when at least one active workflow in the report includes a state with a due date. The due date is shown only when the workflow is currently in that state.

![Document Report showing the Expiration column for workflow states with due dates.](/cms_trial/assets/099e95e9-aed2-4057-ab63-8b04ad1fd004.png)

1. If a page is in a workflow state that requires **multiple approvals**, each approval is shown as a separate icon in the **Reviewers** column.

![Document Report showing multiple reviewer icons in the Reviewers column.](/cms_trial/assets/4421a42c-7ba0-4f51-9fbc-5fb6af668e97.png)

5. Click a reviewer icon to view the details of the reviewer.

![Reviewer details pop-up showing approval information.](/cms_trial/assets/df290f98-d033-4084-b4f9-651cbe8bd68c.png)

The list of approvers is read-only.

### Document Status - Obsolete

When a workflow applied to a document is changed, and **no further workflow activity** has occurred since the change, the **Document Activity Report** shows the document’s status with a **grey state indicator**.

The state name is marked as **(Obsolete)** to indicate that it belonged to the previous workflow and is no longer active.

### Document Status - Not initialized

If a page has not yet entered a state in the currently applied workflow, its **Status** may appear as **Not Initialized** in the report.

These pages can be initialized into a valid state in one of two ways:

- Directly on the page using the **workflow** **state dialog**.
- Through a **space initialization** for the applied workflow under **App Space Settings**.

This can be displayed for the document when either:

- A workflow is first applied, but there has not yet been a workflow event or activity.
- Multiple space workflows are active, and no applicable workflow for the document exists.

## Filter the report

### Filter by status

The **Document Report** can be filtered by one or more workflow states using the **Filter by status** option.

![Filter by status menu in the Document Report.](/cms_trial/assets/6bb0ba45-c072-485e-a229-da78c1800578.png)

### My assigned approvals

Click **My assigned approvals** to display the approvals assigned to you as the current user.

![Document Report filtered to My assigned approvals.](/cms_trial/assets/3dc54ef0-c0f4-4512-8739-5f93276d9f6b.png)

### My pending approvals

Click **My pending approvals** to find the approvals for which you are assigned as a reviewer, but haven’t approved or rejected the document yet.

![Document Report filtered to My pending approvals.](/cms_trial/assets/f37bcd22-5730-402c-9dca-807d20af98e0.png)

When an approval is not complete, such as when multiple reviewers are assigned or a minimum number of approvals is required, your decision status is shown for this approval.

## Export to CSV

The Document Report can be exported as a CSV file for offline analysis.

Click the **Export to CSV** button in the Document Report toolbar.

![Document Report toolbar showing the Export to CSV button.](/cms_trial/assets/63b7ac67-f3d0-47eb-b23c-4cee3502d24e.png)

The exported file includes the following metadata for each document:

- Space name and space key
- Content type and title
- Content ID and version
- Creator and owner
- Creation date and last update date
- Workflow scope (space or page)
- Workflow name and applied workflow version

The Document Report UI is limited to a single space at a time. Use CSV export to merge reports across multiple spaces and build custom dashboards.