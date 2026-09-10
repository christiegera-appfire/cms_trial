# Data residency and Advanced Tables for Confluence

Atlassian data residency gives you control over where your in-scope app data, such as data stored by apps like Advanced Tables for Confluence, is stored geographically, for example, in Europe or the US. This helps you meet data management and compliance requirements.

Atlassian provides data residency support for apps that use [persistent Forge hosted storage](https://developer.atlassian.com/platform/forge/storage-reference/#persistent), as well as allowing realm pinning for apps that use [Forge Remote](https://developer.atlassian.com/platform/forge/remote/).

The **Advanced Tables for Confluence** app is built on **Atlassian Forge** and adheres to the same data residency policies as the host Confluence Cloud site.

- Persistent app data is retained in Atlassian Forge-hosted storage (Key-Value Store).
- When a customer's Confluence site is pinned to a supported region, Forge-hosted storage for the app is hosted, pinned, and migrated in accordance with the site's data residency policies.

- For general information, see [Data residency](https://developer.atlassian.com/platform/forge/data-residency/) and [Understand data residency](https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/).
- To view and configure data residency, see [Manage data residency](https://support.atlassian.com/security-and-access-policies/docs/manage-data-residency-for-products/).

## Frequently asked questions

The FAQ below answers common questions about data residency and migration of the Advanced Tables for Confluence app.

Does the Advanced Tables for Confluence app support data residency?

Yes. The Advanced Tables for Confluenceapp is built on Atlassian Forge and therefore operates under the same data residency policies as the host Confluence Cloud site.

Does Appfire have any externally managed data residency requirement for app data on Atlassian Cloud?

No. Appfire does not directly manage or store customer data — the app's data is stored in Atlassian Forge-hosted storage, and residency is governed by Atlassian's data residency policies for the host Confluence Cloud site.

Why does the Advanced Tables for Confluence app not have the Runs on Atlassian badge?

The Advanced Tables for Confluence app operates under Atlassian data residency because the app has been migrated to Forge.

The app does not currently have the Runs on Atlassian badge for two reasons:

1. **Legacy Connect support:** The app manifest file still supports legacy Connect apps for customers who have not migrated yet. We are actively working to migrate the remaining customers off Connect.
2. **Fetch allowlisting**: Supporting external files as a data source requires us to allowlist specific URLs in the manifest, which is incompatible with the Runs on Atlassian badge. There are no plans to remove support for external files as a data source in the Advanced Tables macros.
Where is the app configuration data stored?

The configuration data is stored in the macro body.

Does the Advanced Tables for Confluence app support CCMA (Confluence Cloud Migration Assistant) migration?

- Yes, the app supports Atlassian's Confluence Cloud Migration Assistant.
- Migration using CCMA is required only when the Profiles feature is actively used.
- For more information, refer to:

  - [Migration from Data Center to Cloud](https://support.appfire.com/space/TBL/74814073/Migration+from+Data+Center+to+cloud?utm_source=htmlredirect&utm_medium=confluence).
  - [Migration best practices for Advanced Tables for Confluence from Data Center to Cloud](https://support.appfire.com/space/SUPPORT/2180808876/Migration+best+practices+for+Advanced+Tables+for+Confluence+from+Data+Center+to+Cloud).
  - [Difference between Advanced Tables for Confluence Data Center and Cloud version](https://support.appfire.com/space/TBL/74812510/Difference+between+Advanced+Tables+for+Confluence+Data+Center+and+cloud+version?utm_source=htmlredirect&utm_medium=confluence).