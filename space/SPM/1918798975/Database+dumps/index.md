# Database dumps

A backup of the app creates a dump of only the application database.It does not include Jira issue data (Jira backup is a separate process that creates a Jira backup file).

**Limitations**:

- Data from the [Priorities module](/cms_trial/space/SPM/1918504313/Priorities/) is not included in a backup. It cannot be restored using a database dump.
- Data from the [OKR module](/cms_trial/space/SPM/1918405440/Objectives+%26+Key+Results+(OKR+module)/) is not included in the backup. It cannot be restored using a database dump. The OKR [import](/cms_trial/space/SPM/1918406659/Import+OKRs/)/[export](/cms_trial/space/SPM/1918668919/Export+OKRs/) functionality can be used for OKRs.

![contentId-1918798975](/cms_trial/assets/1ebb11d9-9734-4fcc-96e7-eb8c1f20cf41.png)

## Jira backup vs App restore

Jira and BigPicture store their data separately.

Creating a dump of the app data is not a Jira backup.

BigPicture **App Configuration** > **Advanced** > **Database dumps** lets you create (and download) a backup of the state of the BigPicture app.

![image2022-1-3_13-17-32.png](/cms_trial/assets/b704d386-bd11-42b9-84f3-822eccaeedfd.png)

## How does an app restore work?

An app restore overwrites current app data and replaces it with the state saved in the dump. There is no possibility of merging two different states of the app:

- You can't combine two dumps
- You can't amend an existing state

![contentId-1918798975](/cms_trial/assets/42bcf102-2947-4d0f-8e14-b8c97aa98d9d.png)