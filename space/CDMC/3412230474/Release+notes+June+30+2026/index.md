# Release notes June 30 2026

**Release date**: June 30, 2026

This page outlines the updates included in the latest release of Comala Document Management for Cloud.

---

Comala Document Management is now built on the Atlassian Forge platform. This release brings unified navigation, a redesigned Workflow State Dialog, workflow version control, advanced approvals, richer reporting with CSV exports, new governance controls, and improved Data Center migration tools.

## New features

## UI and navigation

### Unified left-side navigation

**Global and space settings are now accessible through a new left-hand menu.** You can find global settings under the top **Apps** menu, now organized into three tabs: *Global Workflows*, *E-Signatures*, and *Settings*.

![Comala 2026 release notes feature update](/cms_trial/assets/3ad072f0-f5d8-410e-a622-d685e0421492.png)

**Space settings** follow the same tabbed structure, with *Document Report* available under the *Space Settings* tab.

![Comala 2026 release notes workflow enhancement](/cms_trial/assets/8d4fcc1c-00c5-49e4-b0da-ec50cb206420.png)

### Workflow state dialog

**Now manage all workflow actions from a single dialog.** The dialog handles state transitions, approvals, rejections, the View Approved Version link, Document Activity, manual state overrides, and workflow parameter updates. Open it from the **Document Management** status indicator in the page byline.

![Workflow State dialog showing document actions, approvals, and workflow controls.](/cms_trial/assets/79b64a22-03d1-4758-8934-ae7ceb2bbbce.png)

The dialog now displays the title of the applied workflow. You can click the title to view the workflow details.

![orkflow State dialog displaying the applied workflow name with a link to workflow details.](/cms_trial/assets/1ecb37cc-83c2-45f8-88d5-616ac753b5cf.png)

New dialog enhancements include:

- A **visual state-flow diagram** now shows the current state and available transitions. Hover over any state to see a tooltip with the transition name.

  ![Workflow State dialog showing the workflow state-flow diagram and available transitions.](/cms_trial/assets/b43c5a5a-d345-4292-8585-d5aa055013ac.png)
- For multi-approval workflows, approvals now appear as a **carousel** below the states diagram.

  ![Animated approval carousel showing multiple approvals in the Workflow State dialog.](/cms_trial/assets/e975b561-ee90-4605-9af0-fde0c7d4ab56.gif)
- The **comment section** is now accessible through a button at the bottom left of the dialog, which opens a text field when clicked.

  ![Workflow State dialog with the comment panel opened.](/cms_trial/assets/6f2d6654-b411-4a93-81d3-517a6df6d2ee.png)

[Learn more](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/) about the workflow state dialog.

### Drag-and-drop workflow prioritization

**You can now reorder space workflows using drag-and-drop.** Enabled workflows are evaluated from top to bottom, and evaluation stops at the first match. Disabled workflows are skipped, and changes take effect only after you save the new order.

![Comala 2026 release notes new feature interface](/cms_trial/assets/0fefd297-ebc3-4a9c-bdec-98356fdd6f9e.png)![Comala 2026 release notes updated settings view](/cms_trial/assets/708ae4ca-b186-47eb-9bf6-40376b2a2695.png)

### Updated workflows list design

Workflow actions and parameters are now grouped under a three-dot menu for each workflow in the list. Newly created workflows appear at the end of the list by default.

![Comala 2026 release notes workflow change](/cms_trial/assets/c83cc869-9afe-4277-9d4c-bb1c72ac342b.png)

---

## Workflow management

### New workflow version control

You can now track the version history and revert changes for **Global Workflows**. Every edit is saved as a new version. View any previous version's definition (as JSON) and revert to it if needed.

To access, open **Global Workflows** > **Three-dot menu (⋯) on any workflow** > **View History**.

![Workflow version history showing saved workflow versions and available actions.](/cms_trial/assets/76a42739-1fd3-4f19-b190-c20d7c9fde8b.png)

- Reverting creates a new version entry, but no history is lost.
- Reverts apply globally to all pages and spaces using that workflow.

[Learn more](/cms_trial/space/CDMC/2276786309/Global+workflows/) about Global Workflows.

### New manual state overrides

In addition to existing bulk state override operations, administrators can now override a document’s workflow state for individual pages directly from the *Workflow State* dialog*.* This bypasses standard transitions (for example, moving a page from *Review* directly to *Approved*).

![Manual state override dialog for changing a document workflow state.](/cms_trial/assets/f1540987-29c2-4b53-8aa9-85d020ac452a.png)

Every override is also recorded in the **Document Activity** log.

![Document Activity log showing a recorded manual state override.](/cms_trial/assets/d1c3b3d9-254e-4454-9acc-a922b5e3c5b8.png)

### Labels and workflows stay in sync

Labels and workflows are now linked in both directions. When a workflow is configured to match a specific label, applying that label to a page automatically activates the matching workflow. Similarly, selecting a workflow from the *Workflow State* dialog automatically applies the required label to the page.

[Learn more](/cms_trial/space/CDMC/2193033075/At+space+level/) about applying workflows.

### Edit and delete built-in workflows

Built-in global workflow templates (Basic Approval Workflow, Content Expiry Workflow, Quality Management System Workflow) are now fully editable. You can customize or delete them to match your process. Deleted workflows cannot be restored through the app, so make sure to consider the impact on existing space configurations before deleting them.

## Advanced approvals

### Redesigned approvals builder

The approvals builder now features three organized sections:

![Add approval showing General Settings, Outcome Criteria, and Reviewers sections.](/cms_trial/assets/3e89542e-a5c9-4994-8a07-3391104389a4.png)

1. **General Settings**

- **Approval Name:** a descriptive name for the approval (e.g., `Legal Review)`. Special characters such as **? ! @ #** are not allowed in the name.
- **Custom Action Labels:** Rename the default **Approve** and **Reject** buttons to fit each team's vocabulary (for example, "Sign off" / "Send back").
- **Authentication Method:** Optionally require reviewers to authenticate their decision, including via OTP. The default is "Not required”.

1. **Outcome Criteria**

Define required participation and the decision type:

- **Required participation:** Defines the minimum level of reviewer participation required before a decision is finalized.

  - *All or default*: If reviewers are assigned, all must record a decision. If no reviewers are assigned, at least one reviewer must participate.
  - *Minimum participants*: A specified minimum number of reviewers must record a decision before the outcome can be finalized.
- **Decision type**: Choose how reviewer decisions are evaluated to determine the approval outcome.

  - *Unanimity*: All participating reviewers must agree (all approve or all reject) for the decision to pass.
  - *Majority*: The decision follows the **majority** vote among reviewers who actively participated, not the total number assigned.
  - *Minimum approvals/rejections*: Set explicit **Minimum approvals** and **Minimum rejections** thresholds. The outcome is finalized when either threshold is reached first.

1. **Reviewers**

Control who can participate, enable manual assignment during active approvals, pre-assign users or groups, and use **Remember reviewers** to carry over manually added reviewers to future rounds.

You can now add or remove reviewers at any point during the approval process from the *Workflow State Dialog*.

[Learn more](https://support.appfire.com/space/CDMC/2193195490/Approvals) about Approvals.

### Document Approvals macro: New Version column

**The Document Approvals macro now includes a ‘Show version’ option.** When enabled, a Version column is added to the approvals table, showing the page version at the time each reviewer approved or rejected.

![Document Approvals macro showing the Version column in the approvals table.](/cms_trial/assets/047eccfc-f7ea-4665-bdf3-a7484c6d691c.png)

[Learn more](/cms_trial/space/CDMC/2192777118/Document+Approvals/) about the Document Approvals macro.

## Reporting and document activity

### New CSV data export

**You can now export data from both the Document Report and Document Activity directly to CSV.**

- **Document Report CSV** includes space name, space key, content type, title, content ID, version, creator, owner, creation date, last update date, workflow scope, workflow name, and applied workflow version.
- **Document Activity CSV** exports the full activity log for a document. Use the CSV exports to merge reports across spaces and build custom dashboards.

![Export options for Document Report and Document Activity CSV files.](/cms_trial/assets/803f9f81-6de5-41aa-8cc3-7c3f91782a37.png)

### Updated Document Activity

Document activity now captures a richer set of events:

- State transitions display both the origin and destination states: for example, they display ‘*Changed state from Draft to Review’*.
- Manual state overrides and bulk overrides are flagged in the activity log: for example, *Changed state from Review* to *Approved (manual state override)*.
- New page-created and state-expiration events are recorded.
- All approvers in a multi-approver transition are listed as contributors.
- All actions are attributed to the person who performed them. The add-on account appears as the actor only for state expirations.

![Updated Document Activity log displaying detailed workflow events.](/cms_trial/assets/32c8ee53-ddb2-4c32-823e-d6fa4d1dfe64.png)

## Governance and administration

### Content restriction controls

**Configure how CDM handles restricted pages** from the *Content Restrictions* section under *Settings*. Two toggles are available:

- **Grant Automatic Add-on User Access**: Automatically grants the add-on edit access when users restrict a document. Turn this off to prevent the add-on from accessing restricted pages (workflows stop functioning on those pages).
- **Enforce & Lock Space-Level Override**: Enforces the above setting globally and locks it for space admins, preventing them from overriding it at the space level.

![Comala 2026 release notes dialog update](/cms_trial/assets/615b6a3c-ad50-4768-9706-5ed46de0e62c.png)

### Role-based settings visibility

Settings visibility is now based on user permissions. Each tab in Space Settings and Global Settings is shown or hidden depending on the user’s role:

- **Non-admin users** see only the *Document Report* tab in *Space Settings*.
- **Space admins** can access the *Space Workflows* and *Settings* tabs.
- **Site admins** can access *Global Settings*.

---

## Enhancements

### Simplified OTP authentication

**OTP setup and signing now occur in a pop-up window**. You’re no longer required to open a new browser tab. Your email address is also pre-filled when signing in with OTP.

![Comala 2026 release notes feature improvement](/cms_trial/assets/7b7a9b0d-671b-4a98-8e6c-79556b24af36.png)

Learn more about [E-signatures](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/).

### Clearer batch error handling

Bulk operation errors display a clear summary. Each failed page is now listed by name with a direct link and the reason for failure, making it easy to diagnose and fix issues.

### Dark mode support

All views, including the Workflow Builder, now fully adapt to Confluence's dark mode theme.

![Workflow Builder displayed in Confluence dark mode.](/cms_trial/assets/214f12d3-32da-4fde-bd79-8de94eef076c.png)

### Page workflow scoping

To apply a workflow to a page, the workflow must be listed in the space's workflow list. This ensures workflows are consistently managed at the space level. Existing page workflows are not affected.

Learn more about [apply workflows at page-level](/cms_trial/space/CDMC/2192838126/At+page%2Fblog+level/).

### New localization support

**CDM now supports English (en-US) and Spanish (es-ES).** When you access Confluence in a supported language, CDM displays in that language. Additional locales are planned for future releases.

---

## Migration Enhancements

### Faster Data Center to Cloud migrations

Backend optimizations improve performance for bulk data transfers from the Data Center to the Cloud.

### New Migration Dashboard

A new administrative dashboard now lets you monitor your migration in real time. Available to Confluence administrators, it lets you view each batch, inspect its migration type and outcome, and retry only the failed batches. You don’t need to restart the entire migration.

### Resilient migration retries

Successfully migrated data is now retained when a batch fails. Retries process only the failed records. You don’t need to clear the cloud data first.

### Migrate without removing page restrictions

You can now run your migration with page restrictions in place. Restricted pages in the Data Center are migrated as-is, with no manual restriction removal or restoration steps required.

### Automatic Document Activity after migration

Migrated Document Activity is now available immediately without any manual retrieval steps.

---

## Important changes

The following changes apply to the Forge platform version of CDM.

| **Feature** | **Changes** |
| --- | --- |
| Workflow actions location | All workflow actions are now in the *Workflow State Dialog*, accessed from the page byline. They are not available in Confluence's three-dot page menu. |
| Configuration export and import | Manual backup, export, or import of workflow configurations at the space or instance level is not supported. |
| Document Activity history | There's no option to clear Document Activity. |
| Page copying | Copying a page does not carry over its workflow state or page-level workflow assignment. Apply the workflow separately after copying. |
| Page workflow scoping | Workflows applied to a page must now exist in that space's workflow list. |
| View Approved Version | The **View Approved Version** link is now in the *Workflow State Dialog*. |
| Workflow versioning | Version history is available for Global Workflows only. Reverts apply globally to all pages using the workflow. |

---

## Known Atlassian Forge platform limitations

The following behaviors are caused by the Atlassian Forge platform and are not specific to CDM.

| **Behavior** | **Impact** |
| --- | --- |
| App uninstallation data policy | Uninstalling CDM removes your app data from Forge storage. Data can only be recovered within a limited window by contacting Atlassian Support directly. |
| Multiple macro rendering | Pages containing multiple Forge macros may occasionally fail to render some, causing certain macros to appear blank. |
| Historical page versions | Viewing historical versions of a page displays the current active workflow state in the byline and macros, not the state at the time of that version. |
| Page navigation byline | When navigating between pages, the workflow status in the byline may briefly show a loading state or the previous page's status for a few seconds before updating. |

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!