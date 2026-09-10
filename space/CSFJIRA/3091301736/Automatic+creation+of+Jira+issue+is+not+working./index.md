# Automatic creation of Jira issue is not working.

## Problem

You deployed an Apex trigger to automatically create Jira work items. However, the trigger doesn't work as expected, and the system displays no errors.

## Solution

To enable automatic work item creation, you must first ensure manual creation works without manually adding information. This means that mapping configuration is used to create work items, which is the same process that the Apex trigger follows.

However, if the LWC components are used to manually create work items, the system may not display some errors that will block automatic creation. Before solving the issue, please check the following:

1. Mapping configuration - Ensure all fields are [compatible](/cms_trial/space/CSFJIRA/1522369149/Jira+field+type+to+Salesforce+field+type+compatibility/) between Salesforce and Jira.
2. Make sure all fields required for Jira issue creation exist in your mapping configuration
3. Verify that all mapped fields appear on the **Create** work item screen in Jira.

If any of these requirements are missing, automatic issue creation will fail.

## Related articles

[Attachments are not synchronizing to Jira autmatically only manually when a push is done](https://appfire.atlassian.net/wiki/spaces/470745117/pages/2377515009/Attachments+are+not+synchronizing+to+Jira+autmatically+only+manually+when+a+push+is+done?atlOrigin=eyJpIjoiMzgyOTgxMjdlYTFjNDQxMGFjMDhkNTBlZjM3MGQ5NjQiLCJwIjoiYyJ9)