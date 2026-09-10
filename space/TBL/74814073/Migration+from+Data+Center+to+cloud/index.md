# Migration from Data Center to cloud

This page explains the migration support details for the Advanced Tables for Confluence app data from the Data Center to the cloud.

Before migrating your Advanced Tables for Confluence app content from Data Center to the cloud, we recommend reading the [Cloud migration guide](https://www.atlassian.com/migration/plan/cloud-guide) to plan your migration.

## Prerequisites

- Install the latest version of the Advanced Tables for Confluence app on the Data Center instance. (Migration is supported from Advanced Tables for Confluence, Data Center version 8.8.7.)
- Install the latest version of the Advanced Tables for Confluence app on your cloud instance.
- Install [Confluence Cloud Migration Assistant](https://marketplace.atlassian.com/apps/1219672/confluence-cloud-migration-assistant?hosting=datacenter&tab=overview) on the Data Center instance from which you intend to migrate the Advanced Tables for Confluence app configurations.

Data Center version 8.8.7 is compatible with Confluence versions < 9.5.4.

- To migrate from the Data Center to the **Forge** version of the app on the cloud, your app version requirements depend on your Confluence Data Center version:

  - **For Confluence Data Center < 9.5.4:** If you are migrating to the Forge version on the cloud, you must use app version **8.8.7**.
  - **For Confluence Data Center 10.0+:** If you are migrating to the Forge version on the cloud, you must use the **latest available version** of the Data Center app.

## Migration process

- Before you begin, ensure all the required applications are installed on the Data Center and the cloud. Refer to [Prerequisites](/cms_trial/space/TBL/74814073/Migration+from+Data+Center+to+cloud/).
- On the Data Center instance, navigate to the **Migration Assistant home** screen: **General Configuration** > **Atlassian Cloud** > **Migration Assistant**.
- With the help of Migration Assistant, you can migrate global app configurations, users, and groups as required. For more information, refer to [Confluence Cloud Migration Assistant](https://confluence.atlassian.com/cloud/cloud-migration-assistant-for-confluence-973486571.html).

## Limitations

The following fields are not supported after migration:

**Global Configuration:**The configuration values for the parameters Allow JavaScript and Help us improve the product are not se*t.*

- The Site administrator can edit the Global Configuration and configure the parameter values.

## Differences between the Data Center and cloud versions

- All macros available in the Data Center version, except the **JQL Table macro**, are supported in the Cloud version.
- The cloud version includes an additional macro, the [Advanced Table Viewer](/cms_trial/space/TBL/1531117698/Advanced+Table+Viewer+macro/).
- To know the difference between the Data Center and cloud version of the app, refer to [Difference between Advanced Tables for Confluence Data Center and cloud version](/cms_trial/space/TBL/74812510/Difference+between+Advanced+Tables+for+Confluence+Data+Center+and+cloud+version/).

## Problem reporting

If you experience any unexpected problems or behavior changes, [create a support request](https://appf.re/support). This helps us identify and prioritize fixes and improvements.

## References

- [Migration best practices for Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/SUPPORT/pages/2180808876)
- [Data residency and Advanced Tables for Confluence](/cms_trial/space/TBL/3529933064/Data+residency+and+Advanced+Tables+for+Confluence/)