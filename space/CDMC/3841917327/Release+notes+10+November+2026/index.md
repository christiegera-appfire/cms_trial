# Release notes 10 November 2026

**Release date**: November 10, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**Release Version:** 54.0.0

---

**Important: Manual app update required**

This release requires additional app permissions and does not upgrade automatically. A Confluence site administrator must manually approve the update to enable the new features and enhancements. Until the update is approved, your site continues to use the previous version of Comala Document Management.

## New features and enhancements

## Native publishing: Copy page trigger improvements

The **Copy page** action in the workflow builder now lets you configure the destination, choose what content to copy, and set the title and owner of the copied page . You can configure multiple destinations in one action instead of creating a separate action for each destination.

## Workflow variables

Workflow variables are now fully available in Comala Document Management Cloud.

Use variables to reference page, space, workflow, approval, event, and user information in your workflows. You can also reference supported values from other pages or spaces, reducing the need to enter the same information in multiple places.

Cross-references use the app's Confluence permissions. A variable can retrieve information from a page that the person triggering the workflow cannot access directly. Configure references only to sources authorized for your workflow.

For more configuration details and supported values, see [Variables in Comala Document Management workflows](/cms_trial/space/CDMC/3842114162/Variables/).

## Advanced approvals

You now have more control over who can review content and manage reviewer assignments in your workflows.

Configure eligibility and exclusion rules for individual users, Confluence groups, and teams:

- **Eligible reviewers:** Specify who can be assigned to an approval and approve or reject content.
- **Excluded reviewers:** Prevent selected users, groups, or teams from being assigned to an approval or submitting a decision.
- **Eligible assigners:** Specify who can assign or remove reviewers.
- **Excluded assigners:** Prevent selected users, groups, or teams from managing reviewer assignments.

For more details, see [Approvals](/cms_trial/space/CDMC/2193195490/Approvals/).

## `on-reject-completed` trigger event

The new `on-reject-completed` trigger event lets you run workflow actions when an approval is completely rejected by all its reviewers.

---

## Bug fixes

The following bugs are fixed in this release:

- Automatic reviewer pre-assignment is limited to 400 assignments across all approvals when a page enters a workflow state. If the limit is reached, the workflow continues with the selected reviewers; additional reviewers aren’t assigned automatically.

- Fixed an issue where pages with extensive approval histories could display an outdated workflow state in the page byline or Confluence search results.
- State descriptions now preserve the line breaks and paragraphs configured in the workflow builder.
- The **Document Activity** macro now renders when pages are exported with K15t Scroll PDF Exporter or through `export_view`.
- Restored workflow state information for **Updated content** entries in Document Activity and CSV exports, including historical entries.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!