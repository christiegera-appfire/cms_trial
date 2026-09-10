# I am getting "an unknown error occurred while trying to perform a search" when doing JQL queries

## Summary

On some of my JQL queries, I am getting this error

"An unknown error occurred while trying to perform a search ."

![Connector for Salesforce & Jira unknown error message when performing JQL search](/cms_trial/assets/3b81b3ec-9a41-4ec2-abc9-c3a96f77b7ab.png)![Connector for Salesforce & Jira JQL query error detail view](/cms_trial/assets/4b453833-f4f5-46bf-85cc-6a9e4533c58c.png)

## Environment

- JIRA
- Connector for Salesforce & Jira (Cloud)

## Cause

This issue usually only affects projects with a very large number of Jira issues (around 5,000 or more).

## Resolution

Enable the **Optimize the association JQL query** option under **Query Optimization** in the connector settings.

![Connector for Salesforce & Jira Query Optimization settings with Optimize association JQL query option](/cms_trial/assets/7cd4837c-a6de-453c-8241-061b78371bf5.png)

If enabled, this option can help improve performance and reduce the "unknown error" messages by fine-tuning the JQL query that retrieves Salesforce and Jira associations, where it will be limited to projects with active binding. This option is disabled by default.

## Accessing the configuration settings

1. Go to

   [Unmapped macro: inline-media-image — no content to fall back on]

   **> Apps**, and then in the sidebar, under **Salesforce**, choose **Connections.**
2. Choose your connection, then click **Configure**.