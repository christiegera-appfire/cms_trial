# Why does my association not auto-push back to other associated Salesforce Objects after pulling to Jira

## Summary

If you have multiple associations between a Jira Issue and multiple Salesforce Objects, and more than one associations are configured to auto-push and auto-pull, upon updating a Salesforce Object the Connector will update the associated Jira Issue but will not automatically push back to the other associated Salesforce Objects.

## Environment

- Jira Cloud
- Jira DC

## Diagnostics Steps

Not applicable.

## Cause

This is due to a known issue regarding loop prevention upon auto-push and auto-pull. The Connector checks whether the issue is being updated by itself (by verifying the Account ID of the issue updated event), and if so, it will stop the auto-push event.

## Workaround

Not applicable.

## Resolution

Our developers are currently aware of this issue and are working on a more permanent solution which will ensure data coherence.

If you need more help, contact our [Support Team](https://apps.appf.re/support). We've got your back.