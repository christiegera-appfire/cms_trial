# Backup, restore, and migrate

A backup of the app creates a dump of only the application database**.**

It does not include Jira issue data (Jira backup is a separate process that creates a Jira backup file).

Looking for information about migrating from Data Center to Cloud? Visit the [Backup, restore, and migrate](https://support.appfire.com/space/DLP/2212266044/Backup,+restore,+and+migrate) page for Data Center.

## Step-by-step instructions

- [Staging (migration between instances of the same type)](/cms_trial/space/SPM/1918862176/Staging+(migration+between+instances+of+the+same+type)/)
- [Backup and restore BigPicture using database dump](/cms_trial/space/SPM/1918502531/Backup+and+restore+BigPicture+using+database+dump/)
- [Backup and restore BigPicture using CSV file](/cms_trial/space/SPM/1918698918/Backup+and+restore+BigPicture+using+CSV+file/)
- [Upgrade (migration from BigGantt to BigPicture)](/cms_trial/space/SPM/3488121777/Upgrade+(migration+from+BigGantt+to+BigPicture)/)
- [Restore (on the same instance)](/cms_trial/space/SPM/3487925169/Restore+(on+the+same+instance)/)

## Jira backup vs. app restore

Jira and BigPicture store their data separately.

Creating a dump of the app data IS NOT a Jira backup.

BigPicture app Configuration > Advanced > **Database dumps** allow you to create (and download) a backup of the state of the BigPicture app.

![image2022-1-3_13-17-32.png](/cms_trial/assets/237773e0-01dd-46f5-a519-5c85fa38bf96.png)

## Server/Data center to Cloud migration (Jira)

BigPicture migration from Jira On-premise to Jira Cloud can be run using:

- [Jira XML + BigPicture snapshot](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Migration%20using%20Jira%20XML%20%2B%20BigPicture%20snapshot&linkCreation=true&fromPageId=3488285408)
- [Jira Cloud Migration Assistant (JCMA)](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Migration%20using%20Jira%20Cloud%20Migration%20Assistant%20%28JCMA%29&linkCreation=true&fromPageId=3488285408)

### Post-migration issues when the issue security settings are set

If there are **issue security** settings set for issues on the Jira Server, BigPicture will lose access to such issues after migrating **company-managed** and **team-managed** projects to Jira Cloud.

In such a situation, perform the following steps after migration.

**For company-managed projects:**

1. Open Jira Cloud.
2. Navigate to the **Project settings > Issues > Issue security** page.
3. For each **issue security level** that is defined, add the following **project role**: ***atlassian-addons-project-access***

   ![image2023-4-27_9-1-4.png](/cms_trial/assets/2531350c-4cea-4058-ab8c-ae415ee3ca98.png)
4. Click **Add** to confirm.
5. BigPicture now has access to issues.

**For team-managed projects:**

Currently, it is impossible to add roles on the **Issue Security** page due to [limitations on the Atlassian side](https://jira.atlassian.com/browse/JRACLOUD-79918).

## How does an app "restore" work?

An app restore **overwrites current app data** and replaces it with the state saved in the dump. There is no possibility of merging two different states of the app:

- you can't combine two dumps
- you can't amend an existing state

![contentId-3488285408](/cms_trial/assets/ccd9872d-ffa0-4653-8446-19589a1cbaf6.png)