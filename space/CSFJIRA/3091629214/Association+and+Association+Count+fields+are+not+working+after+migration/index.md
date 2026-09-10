# Association and Association Count fields are not working after migration

## Problem

The *Association* and *Association Count* fields don’t update and can’t be edited after a migration. The fields seem to be locked, and they are to be used for reporting purposes or easier access to the associations related to the Jira issue.

## Solution

The *Association* and *Association Count* fields are custom fields created by the connector on each instance and only for that instance. These fields are locked after a migration and aren’t updated by the Connector. Instead, the Connector installed in the new instance creates its own set of fields, which need to be added to the *Edit Issue* screen *or View Issue* screen to be updated for the Connector.

Add the **Associations**and **Associations Count** fields to the *Edit Issue* Screen to allow the application to populate and update them. An administrator must configure the fields in the project settings.

- If the fields are not added to the *Edit Issue* screen, they cannot be updated.
- If the fields are added to the *View Issue* screen, they are editable and can be edited manually. We recommend removing these fields from the *View Issue* screen and avoiding updating them manually.
- If the fields are updated manually, the app synchronizes them again when the next association-related action occurs.

For more information regarding screen configuration, refer to [Configure the issue detail view](https://support.atlassian.com/jira-software-cloud/docs/configure-the-issue-detail-view/).

## \uD83D\uDCCE Related articles

- [Use JQL to report on Jira issues with associations](/cms_trial/space/CSFJIRA/3092219354/Use+JQL+to+report+on+Jira+issues+with+associations/)