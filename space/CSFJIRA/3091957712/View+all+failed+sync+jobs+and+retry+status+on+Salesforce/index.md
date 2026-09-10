# View all failed sync jobs and retry status on Salesforce

## Summary

Salesforce auto-sync jobs may occasionally fail due to service disruptions or other factors. As a result, it can be hard to determine if the associated Salesforce records are in sync after the disruption.

A sync feature is available that automatically retries failed auto-sync jobs. Failed jobs are automatically retried up to five times, at approximately 5, 10, 30, 60, and 90 minutes from the first failure.

Admins can also view the status of failed sync jobs, as shown in the diagnostic steps below.

This feature is disabled by default and can only be enabled by a Salesforce administrator. Refer to this page for instructions to enable it:

- [Automatically retry failed sync jobs](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754407/Automatically+retry+failed+sync+jobs+Cloud)

## Environment

- Jira Cloud
- Jira Data Center
- Connector for Salesforce & Jira

## Diagnostics Steps

Salesforce admins can view a list of failed and pending sync jobs with this URL:

`{_SALESFORCE_HOST_}/lightning/o/JCFS__AutoSyncJob__c/list`

In the list, failed jobs are shown under the *Job Status* column with the status of *MAX\_RETRIES*, along with relevant info in the other columns like *Attempts*, *First Try*, *Next Try*, and *Last Try*. If the retry succeeds, the sync job will no longer appear on this list.

![contentId-3091957712](/cms_trial/assets/c7ebe9e6-6914-4c5c-b39f-0a2e17883593.png?version=1&modificationDate=1678858813027&cacheVersion=1&api=v2)

You can also click on the ID numbers under the *Job ID* column to get additional details:

![contentId-3091957712](/cms_trial/assets/a3582065-4b8a-4122-b8ad-b7c2b99654a6.png?version=1&modificationDate=1678858813241&cacheVersion=1&api=v2)

## Cause

Auto-sync jobs may occasionally fail due to factors like service disruptions (for example, Internet outage or server downtime).

## Workaround

Not applicable.

## Resolution

The connector can be set to automatically retry failed auto-sync jobs. Failed jobs will be automatically retried up to five times, approximately 5, 10, 30, 60, and 90 minutes after the first failure.

Salesforce admins can track failed and pending sync jobs using the URL provided above.

This feature is disabled by default and can only be enabled by a Salesforce administrator. Refer to this page for instructions to enable it:

- [Automatically retry failed sync jobs](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754407/Automatically+retry+failed+sync+jobs+Cloud)