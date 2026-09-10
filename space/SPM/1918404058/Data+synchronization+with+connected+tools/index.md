# Data synchronization with connected tools

## Types of synchronization

Initial sync happens only during the plugin's first startup. When the plugin starts up for the first time, synchronization does not occur because there are no boxes in BigPicture/BigGantt yet. At this stage, the parent-child relations do not influence the synchronization process. Synchronization does not consider the configuration of the box, i.e.,the Work Breakdown Structure hierarchy (because those things don't exist yet).

All cases of synchronization take into account the following:

- Task modes
- Jira permissions of the user who initialized the change

For more information about the synchronization settings, check [the Performance related settings page](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spmdraft&title=Performance-related%20settings&linkCreation=true&fromPageId=1839104057).

| **Types of Synchronization** | **When does it occur** | **Who is the author of a change?** |
| --- | --- | --- |
| Full sync (re-sync) | User actions can trigger a request for data synchronization when a user:   - Opens a box (e.g., enters any box module such as the Gantt, Resources, or Roadmap module) - Enters Jira Issue Details page with the 'Work Breakdown Structure' panel of either BigPicture or BigGantt enabled.   An Admin user can manually trigger a re-sync of a box by:   - Clicking 'Re-sync' in the Data drop-down menu of Gantt's header - Typing the 'R' key twice on the keyboard while having the Gantt or Roadmap module open   Full sync is in all boxes after:   - Turning off the plugin (restarting the plugin) - clearing cache - Plugin update | The user who triggers a request for box data synchronization or the Scope Owner |
| Partial sync (task synchronization) | Partial sync happens when changes are made:   - In the App - In the connected tool   If a user changes a connected tool (such as Jira or Trello), the events related to these changes are queued inside the app. If a number of changes are applied to the same issue within the interval, the last person who updated the issue will be the author of the last queued change.  When the following Jira events are received:   - Issue Updated, - Issue Created, - Issue Deleted.   When the user made any of the following changes in the app:   - The user moved a task on the Gantt's timeline. - The user moved a task from one Cadence to another in the Roadmap module. - The user-linked tasks in the Gantt.   If a user tries to perform an action for which they have insufficient Jira permissions, they can't do it, so no sync is necessary. | The author of the change in Jira or the app. |

## Authors of changes

Three types of users can be listed as authors of changes:

- Current user (the logged-in person who makes a change; full sync is an exception)
- Scope Owner
- Technical user (in the Jira server, changes may be listed without any users assigned to a change)

## Corrupted Jira index

Full synchronization is not run when BigPicture gets information about the corrupted index from the Jira API. A user can perform a Jira re-index. This should solve the corrupted index problem. Users can also continue without reindexing, which can cause irreversible and unintended changes in Box scope.

## Resync of all boxes

It is not possible to trigger the synchronization of all boxes at the same time for two following reasons:

1. We are avoiding a negative impact on BigPicture and Jira performance.
2. Full re-sync happens when entering a box to ensure you work with the current data.

If you turn the plugin on and off, such action flags all Program boxes, and a full resync is performed when entering each box. This lets us avoid triggering the resync of boxes that are not being used.

## Resynchronize (Gantt and Scope modules)

If your data seems out of date, you can manually trigger resynchronization.

Resynchronization might take up to several minutes, during which you and your team can work in read-only mode.

Box data is stored in the App's cache. If the box is not opened for more than 24 hours, the cache will be automatically cleared, and a full synchronization will be triggered when you open the box.

### Security

Available to:

- Box Admin

### Resynchronization

- Incremental sync takes into account the last updated timestamp in the task source. If changes are made that do not affect that timestamp (for example, using direct database edit), they won't be covered by incremental sync.
- The sync is performed with a two-stage approach - it runs for each box but takes into account the last update time of individual tasks
- If the last update of a task is known to be the same in the app and in the task source, then the incremental sync doesn't run on that task.
- Incremental sync excludes the same tasks that are excluded from partial sync (for example, from boxes that are closed, have corrupted scope, or are waiting for a full sync)

#### Steps

1. Try to reload the page first and wait a few seconds.
2. Go to **Data** > **Resynchronization**.

   ![Screenshot of the Resynchronize button in the Gantt module.](/cms_trial/assets/b5e9d4bc-80be-4d30-9582-16a768405122.png)
3. Click **Resynchronize**to confirm.

   ![Screenshot of confirming the resynchronize action. ](/cms_trial/assets/798b896d-8736-466d-b951-2fa095deef03.png)
4. Task synchronization progress is indicated in the box icon. A green checkmark indicates the process is complete.

   ![Screenshot of the green checkmark indicating that the resynchronization is completed. ](/cms_trial/assets/82faff00-d31d-4bc7-a731-914b973f6f7f.png)

### Gantt live sync

To activate the live sync of the Gantt module, go to **App Configuration** > **General** > **Live sync**.

### Schedule

An incremental sync is scheduled daily at a randomized hour: between 20:00 and 3:00 in the tenant's timezone.

### Constraints

#### Portfolio boxes (non-scope boxes)

- The **Resynchronize** feature is not available for portfolio boxes (non-scope boxes).

  ![Screenshot of the portfolio box in the Gantt module.](/cms_trial/assets/61797c9f-7811-46a6-b20b-c703f7347650.png)

## OKRs data sync across modules

When a user changes a task status and the task is linked to a Key Result, the status change is automatically reflected in the OKR module.

To learn more about task data synchronization in the OKR module, see the [OKR linked work items data sync (and auto-progress update)](/cms_trial/space/SPM/2173109245/OKR+linked+work+items+data+sync+(and+auto-progress+update)/) page.