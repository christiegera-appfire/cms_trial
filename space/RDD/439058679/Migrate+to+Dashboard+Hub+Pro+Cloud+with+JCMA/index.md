# Migrate to Dashboard Hub Pro Cloud with JCMA

## Overview

This page explains the migration support details for the *Dashboard Hub Pro* app content from Data Center (DC) to Cloud using Jira Cloud Migration Assistant (JCMA).

## Prerequisites

### Data Center

- Install the latest version of [*Dashboard Hub Pro*](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-for-jira-reports-charts?tab=overview&hosting=cloud)app (migration is supported from version 3.2.0).
- Install [Jira Cloud Migration Assistant](https://marketplace.atlassian.com/apps/1222010/jira-cloud-migration-assistant?hosting=datacenter&tab=overview). For more information, refer to [What is Jira Cloud Migration Assistant?](https://support.atlassian.com/migration/docs/what-is-jira-cloud-migration-assistant/)

### Cloud

- Install Dashboard Hub on your Cloud instance using JMCA.
- **Use the supported integrations on the cloud after migration:** If you are using any of the supported integrations in the DC instance and plan to use them on the Cloud instance, then install the required applications on the Cloud instance.

## Migration process

1. Before you begin, ensure you have all the required applications installed on the DC and Cloud. Refer to [Prerequisites](/cms_trial/space/RDD/439058679/Migrate+to+Dashboard+Hub+Pro+Cloud+with+JCMA/).
2. Navigate to the *Migration Assistant*home screen: **System** > **IMPORT AND EXPORT** > **Migrate to Cloud***.*  
   With the help of Migration Assistant, you can migrate global app configurations, users, and groups, as required. For more information, refer to [this page](https://confluence.atlassian.com/cloud/use-the-jira-cloud-migration-assistant-to-migrate-from-server-to-cloud-993925215.html).

## Limitations

There aren’t any limitations on the data that can be migrated.

## Problem reporting

If you experience any unexpected problems or changes in behavior, [create a support request](https://appf.re/support). It helps us identify and prioritize fixes and improvements.

### "SUCCESS WITH WARNINGS" Status

In the **DC** instance, these statuses are set by Atlassian and can’t be modified. To improve clarity on the **Cloud** instance side, we provide an additional status, **“SUCCESS WITH WARNINGS.”** This status indicates a mostly successful migration with minor issues that didn’t prevent completion (e.g., a custom field).

### Interpret migration statuses in your reports

Refer to the following as a guide for interpreting these statuses:

| **Status in Dataplane DC** | **Status in Dashboard Hub Cloud** | **Description** |
| --- | --- | --- |
| **SUCCESS** | **SUCCESS** | All items migrated successfully without issues. |
| **SUCCESS** | **SUCCESS WITH WARNINGS** | The app did migrate whatever is possible to migrate in an automated way.  But there are some warnings, which require attention and maybe some manual post processing. The user can find information about this in the post-migration report in Dashboard Hub Cloud.  However, there is no point to re-run the migration, as it will not improve anything. |
| **INCOMPLETE** | **INCOMPLETE** | Not all data was processed. The user should check the post migration report, try to resolve any problems mentioned and eventually re-run the migration of the app. If the problem persists, contact Appfire’s support. |
| **FAILED** | **ERROR** (or nothing) | Migration was unsuccessful due to significant issues.  The user should try to re-run the migration of the app. If the problem persists, contact Appfire’s support. |
| **IN\_PROGRESS** | **IN\_PROGRESS** | Migration is ongoing. |

If you encounter **“SUCCESS WITH WARNINGS”** statuses, review the affected elements and verify that critical data was transferred correctly.