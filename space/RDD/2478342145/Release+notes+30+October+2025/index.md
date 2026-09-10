# Release notes 30 October 2025

**Release date**: October 30, 2025

Our team is thrilled to announce the latest release of the Dashboard Hub family of apps for Jira, Confluence, Bitbucket and <http://monday.com> .

[unmapped inline: placeholder]

---

## New features

## Bulk delete dashboards

To save time when managing multiple dashboards, you can now bulk delete dashboards. This new feature lets you sort your dashboards by creation date, last update date, or owner. You can then select multiple dashboards to delete instead of deleting dashboards one at a time. See our [documentation](/cms_trial/space/RDD/146310002/How+to+create%2C+edit%2C+clone%2C+delete%2C+and+export+your+dashboard/) to learn more about managing dashboards.

![Dashboard Hub Manage Dashboards page showing bulk delete](/cms_trial/assets/f549716a-9d58-47e7-b78f-a6676a23f1b5.png)

---

## Enhancements

The following improvements are included in this release:

- Updated the Bitbucket Add datasource UI to align with Atlassian’s deprecation of app passwords in favor of API tokens.
- The default permission for new dashboards is now *Only specific people can view or edit.* This ensures that new dashboards are private on creation. Dashboard owners must explicitly configure the dashboard to change these permissions.

---

## Bug fixes

The following bug fixes are included in this release:

- Resolved an issue where Dashboard Hub incorrectly displayed hours instead of minutes in the Time Spent field.
- Default datasources were not created if a datasource was shared with a new user. Now, default datasources are always created unless a datasource for the same user and instance already exists.