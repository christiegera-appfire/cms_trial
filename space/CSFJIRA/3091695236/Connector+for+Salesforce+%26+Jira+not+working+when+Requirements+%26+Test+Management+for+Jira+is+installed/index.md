# Connector for Salesforce & Jira not working when Requirements & Test Management for Jira is installed

## Summary

After installing [Connector for Salesforce & Jira](https://marketplace.atlassian.com/apps/1214214?tab=overview&hosting=cloud) and [Requirements & Test Management for Jira](https://marketplace.atlassian.com/apps/1220294/requirements-test-management-for-jira?hosting=datacenter&tab=overview), the Connector app does not work as expected and while browsing the project issues, the screen becomes frozen (greyed out) for Jira projects that have no [Bindings](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754674/Binding+a+Project+to+a+Connection).

## Environment

- Jira Server / Data Center
- [Connector for Salesforce & Jira](https://marketplace.atlassian.com/apps/1214214?tab=overview&hosting=server)
- [Requirements & Test Management for Jira](https://marketplace.atlassian.com/apps/1220294/requirements-test-management-for-jira?hosting=datacenter&tab=overview)

## Diagnostics Steps

Not applicable.

## Cause

The root cause of this issue is due to a bug in [Requirements & Test Management for Jira](https://marketplace.atlassian.com/apps/1220294/requirements-test-management-for-jira?hosting=datacenter&tab=overview) where it causes a conflict with our Connector app.

## Workaround

Not applicable.

## Resolution

Upgrade [Requirements & Test Management for Jira](https://marketplace.atlassian.com/apps/1220294/requirements-test-management-for-jira?hosting=datacenter&tab=overview) to version [7.4.2](https://marketplace.atlassian.com/apps/1220294/requirements-test-management-for-jira/version-history) and above where this issue does not occur anymore.