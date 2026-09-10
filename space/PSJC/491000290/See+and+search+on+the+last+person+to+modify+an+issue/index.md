# See and search on the last person to modify an issue

## Scenario

- "I'd like to easily see the last person to interact with an issue, in any way, on an issue's page"
- "I'd like to create a filter or dashboard gadget based on the user who last interacted with an issue"

We'll show you how to do all of this using [Power Scripts™ for Jira](https://marketplace.atlassian.com/plugins/com.keplerrominfo.jira.plugins.jjupin/server/overview); a powerful scripting tool to help automate your Jira.

## What these scripts do

This is another simple one-scripter. The script runs whenever a specified system event occurs and sets the "Last Modified By" user picker custom field to the user who invoked the event.

## Prerequisites

1. You have Jira Core or Jira Software installed
2. You have Power Scripts™ for Jira installed
3. You have mapped the Last Modified By user picker custom field to its customfield ID in the "sil.aliases" file.

## The script

This script will run on any issue interaction that causes a modification to the issue and set the Last Modified By field to the user who invoked  
the modification.

Script assumes you have a single user picker custom field available called "Last Modified By" and that it is mapped to a custom field ID in sil.aliases.

```text
lastModifiedBy=currentUser();
```

## Configure event listeners

In this case, you will want to execute this script when any of the following events occur:

- Generic Event
- Issue Assigned
- Issue Closed
- Issue Comment Deleted
- Issue Comment Edited
- Issue Commented
- Issue Created
- Issue Moved
- Issue Reopened
- Issue Resolved
- Issue Updated
- Issue Worklog Deleted
- Issue Worklog Updated
- Work Logged On Issue
- Work Started On Issue
- Work Stopped On Issue

You may also want to run this script **asynchronously** because you don't necessarily care if the value gets set immediately and you can save some load on Jira application performance.