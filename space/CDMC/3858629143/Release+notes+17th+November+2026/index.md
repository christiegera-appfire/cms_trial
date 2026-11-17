# Release notes 17th November 2026

**Release date**: November 17, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**Release Version:** 55.0.0

---

**Important: Manual app update required**

This release requires additional app permissions and does not upgrade automatically. A Confluence site administrator must manually approve the update to enable the new features and enhancements. Until the update is approved, your site continues to use the previous version of Comala Document Management.

## New features

### `on-attachment-added`trigger

The new **Attachment added** trigger event lets you automate workflow actions when an attachment is uploaded or restored to a page.

### Trigger condition: File name

The new **File name** trigger condition lets you run workflow actions based on the name of an attachment. You can specify one or more file names to match attachment events.

## Enhancements

### Variables

#### Improved handling of restricted values

Variable cross-references no longer resolve values that are restricted from access.

---

## Bug fixes

The following bugs are fixed in this release:

- - **Metadata values:** Fixed an issue where the Get Metadata macro displayed blank values after a workflow reached its final approved state when using the `increment-metadata` action with workflow-scoped parameters.
  - **Page publishing:** Fixed an issue where the `copy-page` action failed to retain published pages in destination spaces without a homepage. Published copies are now retained at the root of the destination space and updated when republished.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!