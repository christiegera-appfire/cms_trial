# Standard variables reference

These standard variables represent core issue data like summary, description, and status. They are already pre-declared in SIL. When your script runs in an issue context, you can use these variables directly without specifying an issue. However, outside of issue context, you must explicitly reference the [issue context](/cms_trial/space/PSJC/491001721/Contexts+and+scope+in+SIL/).

Never redefine Jira's built-in field names as variables in your code, as this will override their original functionality and cause hard-to-detect errors in your scripts.

| **Variable** | **Aliases** | **SIL type** | **Read-only** | **Explanation** |
| --- | --- | --- | --- | --- |
| `affectedVersions` | `affectedVersion` `affectedVers` `affectedVer` `affVers` `affVer` | `string []` | ❌ | The affected versions field of the issue  Attempts to add an invalid value are ignored. |
| `assignee` | none | `string` | ❌ | Username of the assignee of the issue  Represents the user key, not the real name. |
| `argv` | none | `string []` | ❌ | This standard variable is used to pass information from one script to another. |
| `attachments` | `attach` | `string []` | ✅ | The filenames of the attachments |
| `components` | `component` `comps` `comp` | `string []` | ❌ | The components of the issue  Attempts to add an invalid value are ignored. |
| `created` | none | `date` | ✅ | Timestamp of the date when the issue was created |
| `description` | `desc` | `string` | ❌ | The description of the issue |
| `dueDate` | `due` | `date` | ❌ | The due date of the issue |
| `estimate` | `est` `remaining` | `interval` | ❌ | Remaining estimate  Only works if Time Tracking is enabled at the project level in Jira. |
| `environment` | `env` | `string` | ❌ | The environment of the issue |
| `fixVersions` | `fixVersion` `fixVers` `fixVer` | `string []` | ❌ | Target fix versions of the issue  Attempts to add an invalid value are ignored. |
| `id` | none | `integer` | ✅ | Internal issue ID |
| `issueCreator` | none | `string` | ✅ | Username of the creator  Represents the user key, not the real name. |
| `issueType` | `type` | `string` | ✅ | The name of the issue type |
| `issueTypeId` | none | `string` | ✅ | The ID of the issue type |
| `key` | none | `string` | ✅ | The issue key |
| `labels` | none | `string []` | ❌ | The labels of the issue |
| `originalEstimate` | `origEstimate` `origEst` | `interval` | ❌ | The original estimate of the issue  Only works if Time Tracking is enabled at the project level in Jira. |
| `parent` | none | `string` | ❌ | The parent issue key |
| `parentId` | none | `integer` | ❌ | The ID of the parent issue |
| `priority` | `prio` | `string` | ❌ | The name of the issue priority level |
| `priorityId` | none | `string` | ❌ | The ID of the issue priority level |
| `project` | `prj` | `string` | ✅ | The project key |
| `projectId` | none | `integer` | ✅ | The internal ID of the project |
| `reporter` | none | `string` | ❌ | Username of the reporter  Represents the user key, not the real name. |
| `resolution` | `res`  `resol` | `string` | ❌ | The name of the resolution state  When set, it will also modify the resolution date. |
| `resolutionId` | `resId`  `resolId` | `string` | ❌ | The ID of the resolution state  When set, it will also modify the resolution date. |
| `resolutionDate` | none | `date` | ✅ | The current resolution date  If the resolution is modified, the date will also be updated. |
| `securityLevel` | `security` | `string` | ❌ | The name of the security level |
| `securityLevelId` | `securityId` | `integer` | ❌ | The ID of the security level |
| `status` | none | `string` | ✅ | The name of the current status |
| `statusId` | none | `string` | ✅ | The ID of the current status |
| `summary` | none | `string` | ❌ | The summary of the issue |
| `timeSpent` | `spent` | `interval` | ❌ | Total logged time on the issue  Only works if Time Tracking is enabled at the project level in Jira. |
| `updated` | none | `date` | ✅ | Last update timestamp  The value changes automatically when:   - Issue fields are modified - Comments are added - Workflows are transitioned - Attachments are added/removed - Links are created/removed  It will update automatically after the current transition. |
| `votes` | none | `integer` | ❌ | The number of votes this issue has |
| `watchers` | none | `string []` | ❌ | The usernames of the watchers of the issue |
| `workflow` | `wrkflw` `wf` | `string` | ❌ | The workflow scheme name applied to the issue |
| `workflowId` | none | `integer` | ❌ | The workflow Scheme ID applied to the issue |