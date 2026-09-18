# Release notes 15th September 2026

**Release date**: September 15, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**App version:** 51.0.0

**Release version:** 5.0.29

---

## Enhancements

### **Space Document Report enhancements**

We’ve enhanced the Space Document Report to give more context at a glance and greater control over what you see.

#### **Richer content details**

- Added content type icons (Page or Blog post) in the **Title** column, with a tooltip on hover.
- Added scope icons in the Scope column to distinguish between Space and Page workflows.
- Added **Creator** and **Owner** columns to show the content author and page owner for each item.

#### **More powerful filtering**

- Added **Assigned Reviewers** and **Pending Reviewers** filters to help you find content by review status.
- Added a **More filters** dropdown for filtering by Creator and Owner.
- Added a **Clear filters** option to reset all applied filters at once.

#### **Better customization and consistency**

- Added a column **show/hide** menu so you can choose which columns are visible.
- Standardized the file naming convention for CSV exports.
- Refined the overall UI, including the table, filters, avatars, and workflow filter search.

### **Document Activity enhancements**

- Page update activity now records the version author and contributors.
- Comments added to workflow-enabled pages are now recorded in Document Activity.
- The Document Activity view displays the ‘Added comment’ action along with the comment text.

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where labels were not removed when a page update trigger ran a remove-labels action with state conditions.
- Fixed workflow filter errors that occurred when applying workflows containing SELECT transitions and labels.

## Security updates

- Loading or modifying workflows in the Workflow Builder requires space or instance administrator permissions.
- Space Settings workflow operations are scoped to the relevant space through space-level authorization.
- Reading or exporting Document Activity requires content view permissions.
- Document Report filter options are limited to the current space context.
- State Dialog history and disabled-workflow queries include additional permission checks.
- Updating metadata through the Set Metadata macro requires content edit permissions.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!