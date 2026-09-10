# I am having problems with the Connector while Jira Service Management is installed

## Summary

This issue has been resolved.

Ensure that you have **BOTH** Connector for Salesforce & Jira Server version 0.4.0-BETA **and** Salesforce Package version 2.0 installed.

You may experience problems with the Connector for Salesforce & Jira when you have Jira Service Management installed on Jira 7.

Problems include:

- Failure to authenticate API token from Jira into Salesforce
- Failure to synchronize from Salesforce to Jira

## Environment

- Jira 7 with Jira Service Management installed.

## Diagnostics Steps

Not applicable.

## Cause

An authentication component in Jira Service Management is conflicting with our app.

## Workaround

At the moment you may upgrade your Jira 7 instance to Jira 8 and your Jira Service Management to a version that supports Jira 8.

If this is not feasible at the moment, then please be assured that we are working on a fix for Jira 7.

We're collecting more information from our affected customers. If you're affected by this issue, contact our [Support Team](https://apps.appf.re/support).

## Resolution

Not applicable.