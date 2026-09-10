# Migrate Service Management projects to the Cloud

## Streamlining your workflow: Migrating Jira Service Management projects from Cloud to Cloud

Configuration Manager for Jira (CMJ) Cloud now allows you to migrate your Jira Service Management projects. Our app automates and streamlines the migration process, ensuring a smooth transition.

### How service management projects are migrated

Configuration Manager for Jira (CMJ) Cloud can:

- add a source service project as a new one to the destination site, and
- merge a source service project with an existing destination service project.

The [Analyze Changes](/cms_trial/space/CMJC/193626781/Analyze+changes/) document explains how CMJ Cloud migrates and reports projects. The information there applies to *Jira Software* and *Service Management* projects.

### Case-sensitivity in SLA names

The source and destination SLA fields may use different letter capitalizations, which can affect mapping. For instance, a source SLA called "Time to resolution" won't match a destination SLA labeled "TIME TO RESOLUTION." In such cases, CMJ Cloud will not map these SLAs. Instead, it will create a new destination SLA that exactly matches the name and capitalization of the source field.

### Supported Service Management configuration

| **Jira Service Management configuration** | **Supported configuration** |
| --- | --- |
| Service Management project basics | available |
| Organizations | Partially  *Organization membership isn’t migrated.* |
| Request types | available |
| Portal groups | available |
| Portal settings | available |
| SLAs | available |
| Queues | available |
| Calendars | available |
| Work categories | available |
| Forms | available |
| JQL querries | available |
| Satisfaction settings | available |
| Customer permissions | available |
| Customer notifications | available |
| Email requests | Future |
| Language settings | Future |
| Knowledge base | Future |
| Reports | TBD |
| Widgets | TBD |