# Release notes November 2026

**Release date**: November 18, 2026

This page outlines the updates included in the latest release of Configuration Manager for Jira (CMJ) Cloud.

---

## New features

### View migrated audit history

You can now access the audit history of Configuration Manager for Jira (CMJ) and Project Configurator for Jira (PCJ) from Jira Data Center after migrating to Jira Cloud.

CMJ Cloud preserves historical audit records transferred through the Jira Cloud Migration Assistant (JCMA). You can view these records in the new Data Center audit log section in CMJ Cloud.

The audit log provides a read-only history of migration-related events, including the date, severity, user, operation type, event description, app, and source instance.

This lets you review previous configuration activities and maintain access to your historical audit records after migration.

[Read more about migrated audit history](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/3824943152/View+migrated+audit+history?utm_source=chatgpt.com).

### Deploy automation flows with CMJ Cloud

You can now include Jira automation flows in configuration snapshots and deploy them between Jira Cloud instances using CMJ Cloud.

Automation flows are automatically included based on the snapshot scope:

- Everything supported: Includes global, project-type-scoped, and project-scoped automation flows.
- Specific elements: Includes project-scoped automation flows associated with the selected projects.

During deployment analysis, you can review which automation flows will be added or modified on the destination instance. CMJ Cloud creates new flows, updates matching existing flows, and adjusts references to supported Jira configuration elements.

Some flows can require additional configuration after deployment. Flows affected by unsupported components or references may be deployed as disabled.

[Read more about automation flows with CMJ Cloud](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/3784900898/Deploy+automation+flows+with+CMJ+Cloud?utm_source=chatgpt.com).

For known limitations and post-deployment actions, see [Automation flows: Limitations and considerations](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/3784704330/Automation+flows+Limitations+and+considerations?utm_source=chatgpt.com).

---

## Enhancements

### Improved table functionality

CMJ Cloud snapshot and deployment tables now more closely follow Jira's design and interaction patterns and make it easier to navigate and work with them.

The updates improve table headers, borders, and scrolling behavior. Where enabled, users can scroll within tables without scrolling the entire page. The Configure columns option also lets users choose which columns to display.

### User interface improvements

We've made several interface improvements to provide a more consistent experience across CMJ Cloud.

These include clearer visual indicators for configuration items with warnings and errors, improved icons for transformed objects in light and dark themes, clearer terminology for snapshot scope information, and better feedback during reanalysis and when operation limits are reached.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue that could cause snapshot creation or deployment analysis to fail when processing JMWE workflow post-functions configured with the Clear Field(s) option.
- Fixed an issue that could cause snapshot creation to fail when processing Jira Service Management request type fields.
- Fixed an issue that could cause errors when remapping spaces in custom field contexts.
- Fixed an issue that caused the items-per-page control to become misaligned when users selected All.
- Fixed an issue that prevented the selected notification method from being displayed correctly after the initial snapshot was created.
- Fixed an issue that prevented scheduled snapshots from using the configured Slack notification method.
- Fixed an issue that caused the snapshot details page to display incorrectly when access, permission, or licensing banners were present.
- Fixed an issue that could cause configuration deployment to fail when updating field scheme associations for system fields such as Epic Name.
- Fixed an issue that could cause migrations using custom mapping to fail during the preparation stage.
- Fixed an issue that could cause configuration deployment to fail when creating custom field contexts.
- Fixed an issue that caused deployment to fail when processing cascading options for custom fields that do not support cascading options.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Configuration Manager for Jira (CMJ) Cloud!