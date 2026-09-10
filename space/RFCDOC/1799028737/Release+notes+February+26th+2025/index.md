# Release notes February 26th 2025

**Release date**: February 26, 2025

Our team is thrilled to announce the latest release of Rich Filters for Jira Dashboards.

---

## New features

## Restore rich filters from backup

[Rich filter export and import](/cms_trial/space/RFCDOC/1723924660/Export+and+import+of+rich+filters+data/) is still in beta. Your feedback is welcome and appreciated.

The [bulk operation](/cms_trial/space/RFCDOC/1723596949/Bulk+operations/) *Export to backup* allows you to create backup files containing the configuration of multiple rich filters. Jira admins can import backup files into the same Jira instance or a copy of it.

In the previous release, we added an import method, *Create with new IDs*, which creates rich filters from a backup while assigning new IDs to the rich filters and their sub-objects (such as static filters). This allows you to clone rich filters within a Jira instance or transfer them between instances (e.g., from staging to production).

This release introduces a second import method: *Restore as exported*. It works only on the same Jira instance and restores rich filters while keeping their original IDs from the backup. This ensures that existing rich filter gadgets continue working with the restored rich filters. The primary use case for this feature is backup and restore scenarios—allowing you to create backups under your control and restore rich filters in case they are lost, corrupted, or modified unintentionally.

Jira admins can access the *Import from backup* screen from the `...` menu at the top-right of the rich filters list screen.

---

## Enhancements

## Rich filters limit enforcement logic

Previously, all rich filters in an instance counted toward the limit on the number of rich filters per instance. This meant that to free up space, you had to permanently delete rich filters.

Starting with this release, only *active and archived rich filters* count toward the limit. *Trashed rich filters no longer count*, so you can free up space by simply moving rich filters to the trash. This operation is easily reversible (including in bulk), so you don’t have to worry as much about making mistakes.

Together with automatic archival and bulk operations on rich filters, this change allows you to regularly remove unused rich filters by establishing a simple cleanup process that works for your organization.

## Visual indicator for status of dependencies in Gantt chart

The *Rich Filter Results* gadget can display Gantt charts, where dependencies between issues are represented by badges on each side of the bar.

Clicking on a badge opens the dependencies dialog, which already allows you to identify scheduling errors or conflicts. This enhancement adds *color coding* to the badges: red for errors and green for correct dependencies. This way, you can easily identify problematic dependencies at a glance, without needing to open each dialog.

## Other enhancements

- **Sort rich filters by** ***Last used date***: Added the ability to sort by *Last used date* in rich filter lists.
- **Import/export of trashed rich filters**: Trashed rich filters can now be exported and imported.
- **Increased column limit in views**: You can now configure up to *70 columns per view*.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. <https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview>
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think here. <https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=reviews>

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in [unmapped inline: placeholder]!