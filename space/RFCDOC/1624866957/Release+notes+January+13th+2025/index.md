# Release notes January 13th 2025

**Release date**: January 13, 2025

Our team is thrilled to announce the latest release of Rich Filters for Jira Dashboards.

---

## New features

## [Bulk operations on rich filters](/cms_trial/space/RFCDOC/1723596949/Bulk+operations/)

This release introduces bulk operations on rich filters. The available bulk operations are:

- Move to trash
- Restore from trash
- Delete forever
- Download usage data (see below)
- Export to backup (beta, see below)

You can access the bulk operations screen from the  `...`  menu at the top-right of the rich filters list screen.

By default, only Jira admins have the permission to perform bulk operations on rich filters. You can change this permission from the *Permissions* tab of the [App Configuration](/cms_trial/space/RFCDOC/783943002/App+configuration/) page. Authorized users can only perform bulk operations on the rich filters for which they have the admin permission.

## Rich filter usage data

You can now download an Excel file with usage data for the rich filters you administer:

- for a particular rich filter, from the `...` menu in the rich filter list or on the *General* configuration page,
- for a set of rich filters, with the *Download usage data* bulk operation.

The usage data contains details about the rich filter changes (create, modify, trash) and access (view, use in dashboards).

## Export and import of rich filters

This feature is in beta. We will make improvements in future releases. Your feedback on it is welcome and appreciated.

The bulk operation *Export to backup* allows you to create backup files with the configuration of a set of rich filters. Jira admins can import backup files on the same Jira instance or on a copy of it. This is necessary because the IDs of the Jira objects referenced in the rich filters must be identical in both the source and destination instances.

Currently, one import method is available that creates the rich filters with the configuration from the backup, but *with new IDs* for the rich filters and their sub-objects (static filters, etc.). This import method allows you to clone rich filters on a Jira instance, or to transfer rich filters from a Jira instance to a copy of it (e.g., from staging to prod). Note that the rich filter transfer use case doesn’t cover dashboards that use the rich filters – any rich filter gadgets in the destination instance (existing or transferred by other means) will not automatically reference the transferred rich filters.

We will soon add a second import method that works only on the same Jira instance and restores the rich filters as exported, *keeping the IDs* from the backup. This means that existing rich filter gadgets will keep working with the restored rich filters.

Jira admins can access the *import from backup* screen from the  `...`  menu at the top-right of the rich filters list screen.

---

## Enhancements

## Support for images in Rich Filter Text Panel gadgets

The *Rich Filter Text Panel* gadgets can now display images stored on the web (accessible with a URL). To insert an image, in the config of the gadget, add a tag formatted like this:

`{{IMG width=250 align=left https://picsum.photos/id/237/200/300 }}`

The `width` and `align` attributes are optional and the URL must be simple text (not hyperlink). Note the space before the closing `}}` – it is necessary for the image tag to work.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. <https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview>
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think here. <https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=reviews>

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in [unmapped inline: placeholder]!