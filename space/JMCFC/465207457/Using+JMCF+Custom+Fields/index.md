# Using JMCF Custom Fields

Custom fields created with **JMCF for Jira Cloud** can be used to create fields quickly and without code. These custom fields can not only provide necessary information not included by default in Jira - your custom fields can also be used to enhance search, reports, and dashboards.

## Enhanced Reporting and Dashboards

JMCF custom fields can add additional points of data to your Jira data, which can be used for enhanced reporting and dashboards. Whether you use them in filters for your boards or in dashboard gadgets, you can use custom fields in JQL queries to filter your issues as needed by your workflow.

## Searching with custom fields

Currently, there are no specific search templates for custom fields created with JMCF; currently the only search template available is **Forge custom field searcher**, the default search template for Jira Forge apps. Because JMCF uses native data types, the fields are generally searchable using JQL and basic search. However, there are some limitations:

- **Time in Status** can only be searched by number of seconds.

Search template flexibility will be expanded in later versions of **JMCF for Jira Cloud** as the Forge team introduces more capabilities for search.

You are viewing the documentation for **Jira Cloud**.