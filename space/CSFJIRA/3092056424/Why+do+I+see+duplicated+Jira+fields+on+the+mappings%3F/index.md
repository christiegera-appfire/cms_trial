# Why do I see duplicated Jira fields on the mappings?

## Purpose

When you click **Mappings** in the Salesforce configuration page to map Jira fields with Salesforce fields, you may see a duplicate field option to choose from.

When checking for the duplicate field in the [Custom field](https://support.atlassian.com/jira-software-cloud/docs/customize-an-issues-fields-in-team-managed-projects/?__hstc=72543820.f6d28dbcf919a81908b4de18f3e84150.1659559279276.1671207991541.1671221421386.153&__hssc=72543820.28.1671221421386&__hsfp=4274870856) section, the same field shows up only once.

![contentId-3092056424](/cms_trial/assets/f210effd-9f24-41b6-a7cb-cfc244608dd8.png?version=1&modificationDate=1678857316466&cacheVersion=1&api=v2)

## Answer

This happens in a [team-managed](https://support.atlassian.com/jira-software-cloud/docs/get-started-with-team-managed-projects/?__hstc=72543820.f6d28dbcf919a81908b4de18f3e84150.1659559279276.1671207991541.1671221421386.153&__hssc=72543820.28.1671221421386&__hsfp=4274870856) project. These duplicate fields will not appear in the [Custom Fields](https://support.atlassian.com/jira-software-cloud/docs/customize-an-issues-fields-in-team-managed-projects/?__hstc=72543820.f6d28dbcf919a81908b4de18f3e84150.1659559279276.1671207991541.1671221421386.153&__hssc=72543820.28.1671221421386&__hsfp=4274870856) page.

The Jira administrator has to change the team-managed custom field name to differentiate the fields.