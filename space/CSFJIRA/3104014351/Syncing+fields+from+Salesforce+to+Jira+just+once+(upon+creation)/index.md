# Syncing fields from Salesforce to Jira just once (upon creation)

## Purpose

How can I sync fields from Salesforce to Jira just once? (upon creation)

## Answer

If you need to add a specific field to appear in "Required Fields" and "More fields to review" on the **Review & Create** screen but don't want to add it to your mappings, you will need to add the field in your Jira Project's settings under **Screens** as shown in the screenshot below:

![Jira project Screens settings for Connector for Salesforce field configuration](/cms_trial/assets/bc2a0209-f619-4053-b689-d62adaff99d3.png)

The connector will pull the [supported fields](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754283/Creating+a+Jira+Issue+from+Salesforce) from the created screen to display them in Salesforce.

So there is no need to map those fields if you just need to update them once because they will synchronize only at the time of creation if they aren't set in your mappings.