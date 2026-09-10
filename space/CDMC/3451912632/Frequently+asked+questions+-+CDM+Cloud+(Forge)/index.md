# Frequently asked questions - CDM Cloud (Forge)

Common questions about Comala Document Management for Cloud built on the Atlassian Forge platform.

---

## Where are the workflow actions that used to appear in the page menu?

Workflow actions are no longer available from Confluence's three-dot page menu. All workflow actions, including approve, reject, assign, add/remove workflow, view activity, and update parameters, are accessed from the **Workflow State Dialog**, opened via **Document Management** in the page byline.

## Why doesn't the workflow state appear when I'm editing a page?

When a page is in edit mode or is a live doc, the byline does not display the workflow state. Workflow status is only shown for published pages in view mode.

## Why does a previous page version show the current workflow state?

When viewing a historical page version, the workflow byline and Document State macro display the **current** workflow state, not the state at the time of that version. This is expected behavior in the current Cloud version and is not a data issue.

The Document Approval macro has partial historical-version awareness for approval activity rows.

## Why isn't the workflow copied when I duplicate a page?

When a page is copied, the workflow state and page workflow assignment are not carried over. The workflow must be applied separately to the new page, either manually or via triggers (for example, label-based initialization).

## Why can't I find my workflow where I expect it?

The Cloud version uses a different workflow scoping than the Data Center version. Here's where to look:

| Type | Where it's defined | How it gets applied |
| --- | --- | --- |
| **Global workflow** (CDM only) | Global Settings > Global Workflows | Linked and enabled in a space via Space Settings > Workflows |
| **Space workflow** (label-based) | Space Settings > Workflows | Applied automatically to pages with matching labels. Must be enabled with labels defined. |
| **Page workflow** (single page) | Space Settings > Workflows (same list) | The workflow must be **disabled** and have **no labels**. Only then does it appear as an option in the Workflow State Dialog. |

## Why can I edit or delete the built-in workflow templates?

Built-in workflow templates (BAW, CEW, QMSW) can now be modified and deleted. This was not possible in the previous version and is intentional.

**Caution:** Deleting a built-in workflow may break space configurations that rely on it. Recovery may require engineering assistance.

## Why can't I clear Document Activity records?

The "Clear Document Activity" feature has been permanently removed. Document activity records are retained for compliance and audit purposes. Records are only removed when the associated page or space is deleted.

## Why can't I export or import workflow configurations?

Manual workflow configuration export/import (instance-level or space-level backup and restore of workflow definitions) is not supported in the current Cloud version.

**What still exists:**

- **Confluence space backup/restore** - handled by Confluence itself. Workflow data may be re-linked asynchronously after a space import.
- **Copy-paste via code editor** - workflow JSON can be copied from one space and pasted into another using the code editor.

## What happens if the app is uninstalled?

Uninstalling the app **removes application data** stored in Forge SQL. Atlassian may retain data for a limited recovery period (approximately 90 days). Recovery requests must be handled through **Atlassian Support**, not Appfire Support.

**Do not uninstall the app as a troubleshooting step.**

## Why are some macros blank on my page?

Pages containing multiple Forge app macros may display some macros as blank. This is a known limitation of the Atlassian Forge platform affecting pages with multiple Forge macros. It is not specific to any single macro type.

## Why does the workflow state briefly show incorrect information when navigating between pages?

When navigating between pages, the workflow byline may temporarily display a loading state or information from the previously viewed page. The correct state appears once initialization completes. This is a known behavior on the Forge platform.

If the incorrect state persists and does not self-correct within a few seconds, [contact Appfire Support](https://appfire.atlassian.net/servicedesk/customer/portal/11).

---

## Need help?

- [Contact Appfire Support](https://appfire.atlassian.net/servicedesk/customer/portal/11)