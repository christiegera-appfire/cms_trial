# Keyword Syncing

## Initial Synchronization

When you first decide to use the JQL feature, you must trigger an initial synchronization. First, you need to decide what to index: projects, project categories, or the global level. It’s recommended to index only what you need, so you may want to add projects and project categories to meet your needs:

![Power Scripts for Jira Cloud JQL project configuration dialog](/cms_trial/assets/77e09cfc-0805-4eb2-b05f-47ba93cfc425.png)

After defining what to index, click **Save & Synchronize**.  
If you need to synchronize the entire Jira instance, ensure that you don't have any projects or project categories added, then click **Synchronize**.

After beginning the synchronization, the progress bar under **Synchronize** will display the synchronization completion percentage and the number of process issues, relative to the total number of issues to be indexed.

![Power Scripts for Jira Cloud JQL keyword synchronization interface](/cms_trial/assets/9eb6a4a0-83c4-4fc4-9eb4-53b35e0aea1a.png)

Depending on the number of issues and the complexity of your search scripts, synchronization may take some time.

## Automatic Synchronization

Since a JQL keyword is metadata for an issue that has been evaluated and saved before a JQL search, there must be a way to keep those keywords up to date with the issue data. This is done automatically using system event listeners when **auto-synchronization is turned on**. The keywords get updated when events are triggered for an issue, including:

- Issue created event
- Issue updated event
- Issue deleted event
- Issue link created event
- Issue link deleted event
- Issue commented event
- Issue comment updated event
- Issue comment deleted event

For example, the issue link keywords will be updated when an issue link creation/update event is triggered. Power Scripts attempts to keep the keywords up to date; however, keep in mind that Jira and Power Scripts are separate products with a network in between.

![Power Scripts for Jira Cloud keyword sync status display](/cms_trial/assets/286aa382-44d6-4ad8-9240-24d481693736.png)

## Manual Synchronization

Keywords may become unsynchronized when:

- There is a network failure between Jira and Power Scripts.
- Power Scripts was performing maintenance tasks (booting, reconfiguring, or installing a new version) when Jira triggered events. As a result, those events are lost.
- Jira was unavailable to publish the results of the keyword calculation, for any given reason, and therefore, the updates Power Scripts pushes are lost.

It is therefore recommended to run a manually triggered synchronization (using the **Synchronize** button) from time to time to avoid incorrect results for your users. The update will not block users from working, and Jira will continue to operate normally. Updates are processed as they become available to Power Scripts.