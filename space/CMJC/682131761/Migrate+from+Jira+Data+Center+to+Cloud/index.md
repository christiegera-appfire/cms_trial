# Migrate from Jira Data Center to Cloud

Moving from Jira Data Center to Jira Cloud involves more than installing Configuration Manager for Jira (CMJ) Cloud. If you’ve been using CMJ Data Center, you can bring your CMJ audit history to Cloud using the Jira Cloud Migration Assistant (JCMA).

## Migrate CMJ app data

When you migrate with JCMA, CMJ transfers your Data Center audit history to CMJ Cloud. Other CMJ data, such as snapshots, is not migrated. Once migrated, the records are available in CMJ Cloud through the **Data center audit log** page.

To include your audit history in the migration:

1. Open the **Jira Cloud Migration Assistant** on your Jira Data Center instance.
2. On the **Assess and prepare apps** screen, locate Configuration Manager for Jira.
3. Set the app's status to **Needed in cloud**.
4. Continue with the migration process in JCMA.

The imported audit history is read-only and contains only records from Data Center. New CMJ Cloud activities are not recorded in this log.

For more information about accessing and reviewing your historical records, see [**View migrated audit history**](/cms_trial/space/CMJC/3862233113/View+migrated+audit+history/).

To move your Jira projects, configurations, and issue data from Data Center to Cloud, use the Jira Cloud Migration Assistant (JCMA). Uploading CMJ snapshots to CMJ Cloud is not available by default. If you need to upload a DC snapshot, for example, for compliance reasons, please open a ticket with [Appfire Support](https://appf.re/support), and we’ll review your case.

## What changes when moving to CMJ Cloud?

CMJ Cloud and CMJ Data Center share configuration-management capabilities, but they don't support exactly the same features.

Before migrating, review [**Differences between CMJ Data Center and CMJ Cloud**](/cms_trial/space/CMJC/681903694/Differences+between+CMJ+Data+Center+and+CMJ+Cloud/) to understand which capabilities are available and how the Cloud experience differs.

### Do I need a new license?

Yes. CMJ Cloud requires a separate Atlassian Marketplace license from CMJ Data Center.

For more information, see [**Purchasing from the Atlassian Marketplace**](https://www.atlassian.com/licensing/marketplace#general-faqs).

## Need help?

If you have questions about migrating your configurations or preserving your audit history, contact [**Appfire Support**](https://appf.re/support) for assistance.