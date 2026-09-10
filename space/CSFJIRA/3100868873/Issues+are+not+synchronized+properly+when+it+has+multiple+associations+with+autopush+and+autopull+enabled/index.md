# Issues are not synchronized properly when it has multiple associations with autopush and autopull enabled

## Summary

Issues are not being synchronized when an issue has multiple associations with both autopush and autopull enabled.

## Environment

Jira Server

## Diagnostics Steps

Not applicable.

## Cause

When a user updates a Salesforce record with an association, the record will be synchronized to Jira automatically.

Once the Jira issue is updated by the Connector, it will trigger an auto-push event to push the changes to all associated records, but this action will not actually be performed.

## Workaround

Most likely the integration user is not a Jira user account that is dedicated for this purpose.

The Jira admin must [create a dedicated Jira user for an integration user](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754191) to avoid further synchronization problems.

## Resolution

Not applicable.