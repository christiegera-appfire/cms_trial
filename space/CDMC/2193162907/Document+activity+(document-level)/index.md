# Document activity (document-level)

## Overview

The Document Activity report tracks all workflow events for a page or blog post and provides a full audit trail of state changes, approvals, rejections, and other workflow actions.

The [workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/) includes a **Document Activity** option that displays the document’s workflow history.

In the *Workflow State* dialog, click the **three-dot (…) menu** > **Document Activity** to view the activity report.

![Workflow State dialog with the Document Activity option selected from the More actions menu.](/cms_trial/assets/b6f342a0-15f2-45e8-9372-232cc9443d1e.png)

The Document Activity report is displayed, showing the document's workflow history.

![Document Activity report](/cms_trial/assets/5628b2b3-8356-45aa-a0d3-2c0987507020.png)

## Activity events

The Document Activity report records the following events:

- **State transitions**: Show both the origin and destination states, for example, Changed state from Draft to Review.
- **Approvals**: Records the reviewer, their decision (approved/rejected), and the approval name.
- **Multi-approver transitions**: All approvers in a transition are listed as contributors, with the final approver shown as the actor.
- **Manual state overrides**: Flagged in the log, for example, `Changed state from Review to Approved (manual state override)`.
- **Bulk state overrides**: Recorded when states are initialized in bulk using app space settings.
- **State expirations**: Recorded as `Document state expired`. The add-on account is shown as the actor for expirations only.
- **Page created**: Recorded when a page is created with an active workflow.

All other actions are attributed to the user who performed them.

## Document Activity in a full page view

You can view the Document Activity report in a full Confluence page, making it easy to bookmark or share a direct link to it.

1. To navigate to the full Confluence page, click **Open in full page**.

   ![Document Activity_full page view.png](/cms_trial/assets/06dc3c67-1715-4e3d-980c-c452b1926ba4.png)
2. This opens the Document Activity in a new browser tab. To return to the original Confluence content page, click **Back to page**.

   ![Document Activity_Full page view_Back to page.png](/cms_trial/assets/3c074062-ae12-450c-a58b-d43a4701223b.png)

## Export to CSV

Document Activity can be exported as a CSV file for offline analysis or reporting.

Click the **Export to CSV** button in the Document Activity dialog to download the full activity log for the document.

![Document Activity_Export to CSV.png](/cms_trial/assets/afc522df-b105-4fa7-a6b0-74308d6ab69f.png)

## View historical activity (migrated pages)

For pages migrated from Data Center, the Document Activity report includes a **View Historical Activity** option. This displays the full workflow history that was migrated from the DC instance.

Migrated historical activity is viewable for audit purposes and does not merge with the Cloud document activity.

Document Activity records are retained for compliance and audit purposes. Records are automatically removed only when the associated page or space is deleted.