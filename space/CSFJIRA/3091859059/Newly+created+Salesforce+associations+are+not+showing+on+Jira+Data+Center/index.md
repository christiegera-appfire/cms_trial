# Newly created Salesforce associations are not showing on Jira Data Center

## Summary

Jira will sometimes not display Salesforce associations that were recently created. This is usually caused by latency and related issues with the "Affected Versions" field values. The underlying cause is usually the “session stickiness” setting is not correctly configured in the Data Center environment.

## Environment

- Jira DC

## Diagnostics Steps

Not applicable.

## Cause

We have found index replication lag can occur between multiple nodes, in which the **create request** was first sent to **node A**, followed by the **fetch request** sent to **node B**, just before the changes on node A get replicated onto node B. This situation is also [stated](https://confluence.atlassian.com/jirakb/index-replication-jira-data-center-troubleshooting-966676040.html?__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1618305633998.1618333033010.201&__hssc=72543820.11.1618333033010&__hsfp=1964150784) by Atlassian as one of the common problems using DC.

## Workaround

We currently have tested both workarounds below and they have helped

- Workaround 1

  - Please configure session stickiness on your load balancers based on Atlassian’s [documentation](https://confluence.atlassian.com/enterprise/jira-data-center-load-balancer-examples-781200827.html).
- Workaround 2

  - Please ensure that you update to  [Jira 8.12.0](https://confluence.atlassian.com/jirasoftware/jira-software-8-12-x-release-notes-1019380834.html?__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1618305633998.1618333033010.201&__hssc=72543820.11.1618333033010&__hsfp=1964150784) and above, as Jira has introduced [**Document Based Replication**](https://confluence.atlassian.com/enterprise/document-based-replication-in-jira-data-center-1021214730.html?__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1618305633998.1618333033010.201&__hssc=72543820.11.1618333033010&__hsfp=1964150784) which helps to speed up replication across multiple nodes.

Restart Jira server and clearing all browser related cache usually is a good practice when working with cache related updates. Do ensure these are completed as well.

## Resolution

Not applicable.