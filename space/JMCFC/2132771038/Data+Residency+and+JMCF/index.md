# Data Residency and JMCF

**JMCF for Jira Cloud** supports Data residency; all app data and log files are stored within Atlassian data centers, and all data can be pinned to a specific realm. It is possible to share execution log data with Appfire for the purposes of troubleshooting and support if you so choose.

**Data Residency** for Atlassian products allow you to configure your instances to store long-term data in specific geographical regions, or **realms** as Atlassian labels them; these features help in fulfilling local and regional data storage requirements as well as enable organizations to store their user-generated content only in regions with which they are comfortable.

**Note**: The number of locations (AWS regions) Jira offers is currently limited, with more locations being made available. See the Atlassian [cloud roadmap](https://www.atlassian.com/roadmap/cloud?category=dataManagement&) for more information.

The FAQ below addresses Data Residency as it applies to JMCF as well as a few other specific questions. For more information on Data Residency in general, see this page: <https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/>.

For detailed information on configuring data residency, see this page: <https://developer.atlassian.com/cloud/jira/platform/data-residency/>.

How does Atlassian define data residency compliance?

Atlassian considers third-party apps data residency compliant if the app supports both **realm pinning** and **realm migration**.

**Note**: only specific Atlassian data, and therefore JMCF data, can be pinned. Atlassian defines this data as **in-scope** data. See this page for more information about which data can be pinned and which cannot: <https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/#In-scope-product-data>

Is JMCF compliant with data residency? Does JMCF support Realm Pinning and Realm Migration?

**JMCF** is data residency compliant in respects to Atlassian’s definition of compliance; *data-at-rest and user-generated content are stored in the data residency realm for which your Jira instance is configured.* Because JMCF stores all of its configurations and data inside Jira, it is compliant with data residency without any additional configuration or actions. When you pin your Jira instance to a specific realm and complete the migration to that realm, JMCF is pinned and migrated as a part of your Jira instance.

You are viewing the documentation for **Jira Cloud**.