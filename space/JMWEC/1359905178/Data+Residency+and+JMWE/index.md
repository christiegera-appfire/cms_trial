# Data Residency and JMWE

**Data Residency** for Atlassian products allow you to configure your instances to store long-term data in specific geographical regions, or **realms** as Atlassian labels them; these features help in fulfilling local and regional data storage requirements as well as enable organizations to store their user-generated content only in regions with which they are comfortable.

**Note**: The number of locations (AWS regions) Jira offers is currently limited, with more locations being made available. See the Atlassian [cloud roadmap](https://www.atlassian.com/roadmap/cloud?category=dataManagement&) for more information.

The FAQ below addresses Data Residency as it applies to JMWE as well as a few other specific questions. For more information on Data Residency in general, see this page: <https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/>.

For detailed information on configuring data residency, see this page: <https://developer.atlassian.com/cloud/jira/platform/data-residency/>.

[Unmapped macro: rw-expand — no content to fall back on]

Atlassian considers third-party apps data residency compliant if the app supports both **realm pinning** and **realm migration**.

**Note**: only specific Atlassian data, and therefore JMWE data, can be pinned. Atlassian defines this data as **in-scope** data. See this page for more information about which data can be pinned and which cannot: <https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/#In-scope-product-data>

[Unmapped macro: rw-expand — no content to fall back on]

**JMWE** is data residency compliant in respects to Atlassian’s definition of compliance; *data-at-rest and user-generated content are stored in the data residency realm for which your Jira instance is configured.* Because JMWE stores all of its configurations and data inside of Jira, it is compliant with data residency without any additional configuration or actions. When you pin your Jira instance to a specific realm and complete the migration to that realm, JMWE is pinned and migrated as a part of your Jira instance.

However, currently some data does not meet full data residency compliance. Similar to Atlassian, JMWE needs to store some data in the Global Realm (the AWS US Region). This currently applies to:

- Log files (retained for 14 days only)
- Cached data, which is used to improve computation throughput (retained for variable lengths)
- JMWE license status

All of the above data contains no confidential information or Personally Identifiable Information (PII), and is used for performance improvement and analytic purposes only.

[Unmapped macro: rw-expand — no content to fall back on]

Yes, JMWE will move to full data residency compliance at some point in the near future. Logs, cached data, and data processing will be offered in each of the Atlassian realms so that when your instance is pinned to a specific realm, all JMWE-related data and processes will be migrated to match. **There is currently no release date available for full compliance**.