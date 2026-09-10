# Release notes 3rd September 2026

**Release date**: September 3, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**App version:** 50.20.0

**Release version:** 5.0.27

---

## Enhancements

### Page creation recorded in Document Activity

Document Activity now records a **Page created** event when a workflow is first applied to a page. The entry captures the original author, creation date, and contributors, providing a complete history from the moment the content enters a workflow.

### Page created entry shown across Document Activity views

The new **Page created** entry appears in the Document Activity modal, macro, and CSV export, labeled *created page*, so the page origin is visible wherever you review activity.

### Clearer messages for workflow changes

Document Activity messages now show more detail when a page’s workflow is changed or updated to a new version. Entries display the previous and new workflow names or version numbers, so it’s easy to track what changed.

### Clearer activity for bulk admin actions

Bulk state override activity is now split into four distinct event types covering space and workflow initialization and state override. These clearer event types make bulk administrative actions easier to identify and understand in Document Activity.

---

## Bug fixes

- Fixed missing rejection notifications on the first workflow iteration. You now see the rejected message flag after content is rejected.
- Fixed background and automated workflow operations, such as scheduled expiration, on pages with restricted access. System actions now run correctly without being blocked by incorrect permission checks.

---

## Maintenance

- Improved the reliability of our internal testing process. Tests now run more consistently, which helps us identify and resolve issues before release.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!