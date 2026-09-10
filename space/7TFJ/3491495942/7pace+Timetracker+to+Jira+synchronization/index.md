# 7pace Timetracker to Jira synchronization

![7pace-to-jira-sync.png](/cms_trial/assets/bd18fee3-2a96-4827-b759-108dc2161274.png)

The Jira synchronization settings allow administrators to control whether time logged within 7pace Timetracker automatically exports to Jira worklogs.

## Overview and Business Use Case

By default, 7pace Timetracker synchronizes all logged time to native Jira worklogs on corresponding Jira issues. However, Jira and 7pace handle permission models differently:

- **Jira Permissions:** Any user who has permission to view a Jira issue can also see all native Jira worklogs attached to it, including who logged the time and the duration.
- **7pace Permissions:** 7pace allows fine-grained role management (for example, the **Individual** role) to restrict users from seeing other team members' logged hours.

### Why Disable Synchronization?

Turning off the 7pace to Jira export is ideal when:

- **Privacy and Granular Visibility:** You want to restrict logged time visibility. When sync is disabled, users without 7pace access (or users with restricted 7pace roles like **Individual)** cannot see logged hours using native Jira issue views.
- **Milestone-Based Reporting:** You prefer to keep time logs internal during an active phase or project, only syncing them to Jira after project completion or approval.

## How It Works

### When Active (Sync Enabled)

- Time logged in 7pace is immediately exported to native Jira worklogs.
- Native Jira worklog fields reflect 7pace entries.

### When Inactive (Sync Disabled)

- Users can still use **Add Time**, select work items, and log hours normally within 7pace.
- **No worklogs are pushed to Jira.** The logged time remains strictly inside 7pace Timetracker.
- Once the toggle is switched back to **Active**, queued or pending worklogs will synchronize to Jira.