# Variables in Nunjucks Templates

A variable looks up a value from the template context. This documents details on the variables available in JMWE and how to create custom variables.

If you want to insert the value of a variable in your template, you can use the following syntax: `{{ myVar }}`. This looks up for the `myVar` variable from the context and displays it. Variable names can have dots in them which look up properties, just like in javascript.

## Variables available in JMWE

JMWE makes the `issue, transition, linkedIssue, parentIssue, now`and`currentUser`variables available to templates. You can access their properties using "." or "[ ]". For example, you can access the current issue key using `{{issue.key}}`.

### **issue variable**

The `issue`variable is used to insert data of the issue being transitioned. You can access the issue data by looking up at its properties.

**For example:**

`{{issue.fields.labels}}` returns an array of label values, e.g. `[ "1","2" ]`

`{{issue.fields.reporter.accountId}}` returns the `accountId` of the reporter, e.g. `carter`

Click here to see some properties of the issue variable

| Properties | Description |
| --- | --- |
| `issue.id` | Internal Id number of the issue |
| `issue.key` | Issue key |
| `issue.fields.summary` | Issue summary |
| `issue.fields.description` | Issue description |
| `issue.fields.issuetype.name` | Issue type |
| `issue.fields.issuetype.description` | Issue type description |
| `issue.fields.creator.name` | Username of the person who created the issue |
| `issue.fields.creator.emailAddress` | Email address of the person who created the issue |
| `issue.fields.creator.displayName` | Displays name of the person who created the issue |
| `issue.fields.creator.timeZone` | Time zone of the creator |
| `issue.fields.reporter.accountId` | AccountId of the person who reported the issue |
| `issue.fields.reporter.emailAddress` | Email address of the person who reported the issue |
| `issue.fields.reporter.displayName` | Display name of the person who reported the issue |
| `issue.fields.reporter.timeZone` | Time zone of the reporter |
| `issue.fields.assignee.accountId` | AccountId of the person assigned to the issue |
| `issue.fields.assignee.emailAddress` | Email address of the person assigned to the issue |
| `issue.fields.assignee.displayName` | Display name of the person assigned to the issue |
| `issue.fields.assignee.timeZone` | Time zone of the assignee |
| `issue.fields.created` | Date and time the issue was created |
| `issue.fields.updated` | Date and time the issue was last updated |
| `issue.fields.priority.name` | Issue priority name |
| `issue.fields.project.name` | Issue project name |
| `issue.fields.project.key` | Issue project key |
| `issue.fields.lastViewed` | Date and time the issue was last viewed by the current user |
| `issue.fields.fixVersions[0].name` | Name of the first fix Version/s |
| `issue.fields.fixVersions[0].description` | Description of the first fix Version/s |
| `issue.fields.fixVersions[0].releaseDate` | Release date of the first Fix Version/s |
| `issue.fields.versions[0].name` | Name of the first Affects Version/s |
| `issue.fields.versions[0].description` | Description of the first Affects Version/s |
| `issue.fields.versions[0].releaseDate` | Release date of the first Affects Version/s |
| `issue.fields.components[0].name` | Name of the first component |
| `issue.fields.components[0].description` | Description of the first component |
| `issue.fields.duedate` | Due date of the issue |
| `issue.fields.timespent` | Time spent on the issue |
| `issue.fields.timeoriginalestimate` | The original estimate of the time required to resolve the issue |
| `issue.fields.resolution.name` | Resolution of the issue |
| `issue.fields.watches.watchcount` | The number of people watching the issue |
| `issue.fields.labels` | Labels the issue relates to |
| `issue.fields.environment` | The hardware or software environment the issue relates to |
| `issue.fields.votes` | The number of votes an issue has |

### **transition variable**

The `transition`variable is used to insert information of the transition being executed.

**For example:**

`{{transition.transitionName}}` returns the name of the transition, e.g. `Start Progress`

`{{transition.to_status}}` returns the status of the transition, e.g. I`n Progress`

Click here to see the properties of the transition variable

| Properties | Description |
| --- | --- |
| `transition.transitionName` | Name of the current transition |
| `transition.transitionId` | Numerical ID of the current transition |
| `transition.from_status` | Source status of the transition |
| `transition.to_status` | Destination status of the transition |
| `transition.workflowName` | Name of the current workflow |
| `transition.workflowId` | Numerical ID of the current workflow |

### context variable

The `context` variable holds information passed around between post-functions in the same Shared, Scheduled, or Event-based Action, or in the same Sequence of post-functions. It can contain information provided by post-functions such as the Create Issue(s) post-function, as well as information added by Nunjucks templates using the `{% setContextVar %}` Nunjucks tag. See [passing variables within a sequence](/cms_trial/space/JMWEC/466288975/Shared+actions/) for more information.

#### The following properties are available by default, after a Create Issue(s) post-function runs in a sequence or Action:

`context.newIssueKey`: stores the issue key of the *last* issue created by a Create Issue(s) post-function in the action.

`context.newIssueKeys`: stores an array of the keys of all the issues created by any Create Issue(s) post-function in the action.

#### The following property is only available from post functions that belong to a shared action or Sequence of post-functions post function:

`context.currentIssue`: if the post-function belongs to a Sequence of post-functions or a Shared Action, this variable contains the original issue being transitioned or modified.

#### The following property is available when the user modified at least one field on the transition screen (in a post-function), or the event-based action is triggered following a change to a field:

`context.changelog`: returns a single changelog entry, in the format for a single entry in the `values` property of the *response* documented [here](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-issueidorkey-changelog-get). For example:

```text
{
      "id": "10001",
      "author": {
        "self": "https://your-domain.atlassian.net/rest/api/2/user?accountId=5b10a2844c20165700ede21g",
        "accountId": "5b10a2844c20165700ede21g",
        "emailAddress": "mia@example.com",
        "avatarUrls": {
          "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48",
          "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24",
          "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16",
          "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32"
        },
        "displayName": "Mia Krystof",
        "active": true,
        "timeZone": "Australia/Sydney"
      },
      "created": "1970-01-18T06:27:50.429+0000",
      "items": [
        {
          "field": "fields",
          "fieldtype": "jira",
          "fieldId": "fieldId",
          "from": null,
          "fromString": "",
          "to": null,
          "toString": "label-1"
        }
      ]
    }
```

#### The following property is available when the user provided a comment on the transition screen (in a post-function), or the event-based action is triggered following the posting of a new comment:

`context.comment`: the comment being added, in the format described in the *response* section [here](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issue-comments/#api-rest-api-2-issue-issueidorkey-comment-id-get).

### newIssueKey

The `newIssueKey` variable holds the key of the newly created issue. This is applicable only in the [Create issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function.

**For example:**

`{{newIssueKey}}` returns the key of the newly created issue.

`Issue {{newIssueKey}} has been created.`

### **linkedIssue variable**

The `linkedIssue` variable, which is only available from post-functions that work on linked issues, is used to insert data of the linked issue being processed by the post-function.

**For example:**

`{{linkedIssue.fields.description}}` returns the description of the linked issue being processed.

Click here to see the properties of the linkedIssue variable

| Properties | Description |
| --- | --- |
| `linkedIssue.id` | Internal Id number of the linked issue |
| `linkedIssue.key` | Linked issue key |
| `linkedIssue.fields.summary` | Linked issue summary |
| `linkedIssue.fields.description` | Linked issue description |
| `linkedIssue.fields.issuetype.name` | Linked issue type |
| `linkedIssue.fields.issuetype.description` | Linked issue Issue type description |
| `linkedIssue.fields.creator.accountId` | Account Id of the person who created the linked issue |
| `linkedIssue.fields.creator.emailAddress` | Email address of the person who created the linked issue |
| `linkedIssue.fields.creator.displayName` | Displays name of the person who created the linked issue |
| `linkedIssue.fields.creator.timeZone` | Time zone of the creator |
| `linkedIssue.fields.reporter.accountId` | Account Id of the person who reported the linked issue |
| `linkedIssue.fields.reporter.emailAddress` | Email address of the person who reported the linked issue |
| `linkedIssue.fields.reporter.displayName` | Display name of the person who reported the linked issue |
| `linkedIssue.fields.reporter.timeZone` | Time zone of the reporter |
| `linkedIssue.fields.assignee.accountId` | Account Id of the person assigned to the linked issue |
| `linkedIssue.fields.assignee.emailAddress` | Email address of the person assigned to the linked issue |
| `linkedIssue.fields.assignee.displayName` | Display name of the person assigned to the linked issue |
| `linkedIssue.fields.assignee.timeZone` | Time zone of the assignee |
| `linkedIssue.fields.created` | Date and time the linked issue was created |
| `linkedIssue.fields.updated` | Date and time the linked issue was last updated |
| `linkedIssue.fields.priority.name` | Linked Issue priority name |
| `linkedIssue.fields.project.name` | Linked Issue project name |
| `linkedIssue.fields.project.key` | Linked Issue project key |
| `linkedIssue.fields.lastViewed` | Date and time the linked issue was last viewed by the current user |
| `linkedIssue.fields.fixVersions[0].name` | Name of the first Fix Version/s |
| `linkedIssue.fields.fixVersions[0].description` | Description of the first Fix Version/s |
| `linkedIssue.fields.fixVersions[0].releaseDate` | Release date of the first Fix Version/s |
| `linkedIssue.fields.versions[0].name` | Name of the first Affects Version/s |
| `linkedIssue.fields.versions[0].description` | Description of the first Affects Version/s |
| `linkedIssue.fields.versions[0].releaseDate` | Release date of the first Affects Version/s |
| `linkedIssue.fields.components[0].name` | Name of the first component |
| `linkedIssue.fields.components[0].description` | Description of the first component |
| `linkedIssue.fields.duedate` | Due date |
| `linkedIssue.fields.timespent` | Time spent |
| `linkedIssue.fields.timeoriginalestimate` | The original estimate of the time required to resolve the linked issue |
| `linkedIssue.fields.resolution.name` | Resolution of the issue |
| `linkedIssue.fields.watches.watchcount` | The number of people watching the linked issue |
| `linkedIssue.fields.labels` | Labels the linked issue relates to |
| `linkedIssue.fields.environment` | The hardware or software environment the linked issue relates to |
| `linkedIssue.fields.votes` | The number of votes a linked issue has |

### **targetIssue variable**

The `targetIssue` variable, which is only available from post-functions that allow specifying the issues to operate on, is used to insert data of each target issue being processed by the post-function.

**For example:**

`{{targetIssue.fields.description}}` returns the description of the target issue being processed.

Click here to see the properties of the linkedIssue variable

| Properties | Description |
| --- | --- |
| `targetIssue.id` | Internal Id number of the related issue |
| `targetIssue.key` | Target issue key |
| `targetIssue.fields.summary` | Target issue summary |
| `targetIssue.fields.description` | Target issue description |
| `targetIssue.fields.issuetype.name` | Target issue type |
| `targetIssue.fields.issuetype.description` | Target issue Issue type description |
| `targetIssue.fields.creator.accountId` | Account Id of the person who created the target issue |
| `targetIssue.fields.creator.emailAddress` | Email address of the person who created the target issue |
| `targetIssue.fields.creator.displayName` | Displays name of the person who created the target issue |
| `targetIssue.fields.creator.timeZone` | Time zone of the creator |
| `targetIssue.fields.reporter.accountId` | Account Id of the person who reported the target issue |
| `targetIssue.fields.reporter.emailAddress` | Email address of the person who reported the target issue |
| `targetIssue.fields.reporter.displayName` | Display name of the person who reported the target issue |
| `targetIssue.fields.reporter.timeZone` | Time zone of the reporter |
| `targetIssue.fields.assignee.accountId` | Account Id of the person assigned to the target issue |
| `targetIssue.fields.assignee.emailAddress` | Email address of the person assigned to the target issue |
| `targetIssue.fields.assignee.displayName` | Display name of the person assigned to the target issue |
| `targetIssue.fields.assignee.timeZone` | Time zone of the assignee |
| `targetIssue.fields.created` | Date and time the target issue was created |
| `targetIssue.fields.updated` | Date and time the target issue was last updated |
| `targetIssue.fields.priority.name` | Target Issue priority name |
| `targetIssue.fields.project.name` | Target Issue project name |
| `targetIssue.fields.project.key` | Target Issue project key |
| `targetIssue.fields.lastViewed` | Date and time the target issue was last viewed by the current user |
| `targetIssue.fields.fixVersions[0].name` | Name of the first Fix Version/s |
| `targetIssue.fields.fixVersions[0].description` | Description of the first Fix Version/s |
| `targetIssue.fields.fixVersions[0].releaseDate` | Release date of the first Fix Version/s |
| `targetIssue.fields.versions[0].name` | Name of the first Affects Version/s |
| `targetIssue.fields.versions[0].description` | Description of the first Affects Version/s |
| `targetIssue.fields.versions[0].releaseDate` | Release date of the first Affects Version/s |
| `targetIssue.fields.components[0].name` | Name of the first component |
| `targetIssue.fields.components[0].description` | Description of the first component |
| `targetIssue.fields.duedate` | Due date |
| `targetIssue.fields.timespent` | Time spent |
| `targetIssue.fields.timeoriginalestimate` | The original estimate of the time required to resolve the linked issue |
| `targetIssue.fields.resolution.name` | Resolution of the issue |
| `targetIssue.fields.watches.watchcount` | The number of people watching the target issue |
| `targetIssue.fields.labels` | Labels the target issue relates to |
| `targetIssue.fields.environment` | The hardware or software environment the target issue relates to |
| `targetIssue.fields.votes` | The number of votes a target issue has |

### **parentIssue variable**

The `parentIssue`variable, which is only available from post-functions that work on the parent issue, is used to insert data of the parent issue being processed by the post-function.

**For example:**

`{{parentIssue.fields.priority.name}}` returns the priority of the parent issue being processed.

Click here to see the properties of the parentIssue variable

| Properties | Description |
| --- | --- |
| `parentIssue.id` | Internal Id number of the parent issue |
| `parentIssue.key` | Parent issue key |
| `parentIssue.fields.summary` | Parent issue summary |
| `parentIssue.fields.description` | Parent issue description |
| `parentIssue.fields.issuetype.name` | Parent issue type |
| `parentIssue.fields.issuetype.description` | Parent issue Issue type description |
| `parentIssue.fields.creator.accountId` | Account Id of the person who created the parent issue |
| `parentIssue.fields.creator.emailAddress` | Email address of the person who created the parent issue |
| `parentIssue.fields.creator.displayName` | Displays name of the person who created the parent issue |
| `parentIssue.fields.creator.timeZone` | Time zone of the creator |
| `parentIssue.fields.reporter.accountId` | Account Id of the person who reported the parent issue |
| `parentIssue.fields.reporter.emailAddress` | Email address of the person who reported the parent issue |
| `parentIssue.fields.reporter.displayName` | Display name of the person who reported the parent issue |
| `parentIssue.fields.reporter.timeZone` | Time zone of the reporter of the parent issue |
| `parentIssue.fields.assignee.accountId` | Account Id of the person assigned to the parent issue |
| `parentIssue.fields.assignee.emailAddress` | Email address of the person assigned to the parent issue |
| `parentIssue.fields.assignee.displayName` | Display name of the person assigned to the parent issue |
| `parentIssue.fields.assignee.timeZone` | Time zone of the assignee of the parent issue |
| `parentIssue.fields.created` | Date and time the parent issue was created |
| `parentIssue.fields.updated` | Date and time the parent issue was last updated |
| `parentIssue.fields.priority.name` | Parent Issue priority name |
| `parentIssue.fields.project.name` | Parent Issue project name |
| `parentIssue.fields.project.key` | Parent Issue project key |
| `parentIssue.fields.lastViewed` | Date and time the parent issue was last viewed by the current user |
| `parentIssue.fields.fixVersions[0].name` | Name of the first Fix Version/s |
| `parentIssue.fields.fixVersions[0].description` | Description of the first Fix Version/s |
| `parentIssue.fields.fixVersions[0].releaseDate` | Release date of the first Fix Version/s |
| `parentIssue.fields.versions[0].name` | Name of the first Affects Version/s |
| `parentIssue.fields.versions[0].description` | Description of the first Affects Version/s |
| `parentIssue.fields.versions[0].releaseDate` | Release date of the first Affects Version/s |
| `parentIssue.fields.components[0].name` | Name of the first component |
| `parentIssue.fields.components[0].description` | Description of the first component |
| `parentIssue.fields.duedate` | Due date |
| `parentIssue.fields.timespent` | Time spent |
| `parentIssue.fields.timeoriginalestimate` | The original estimate of the time required to resolve the parent issue |
| `parentIssue.fields.resolution.name` | Resolution of the parent issue |
| `parentIssue.fields.watches.watchcount` | The number of people watching the parent issue |
| `parentIssue.fields.labels` | Labels the parent issue relates to |
| `parentIssue.fields.environment` | The hardware or software environment the parent issue relates to |
| `parentIssue.fields.votes` | The number of votes a parent issue has |

### **currentUser variable**

The `currentUser` variable is used to insert information about the current user, i.e. the user triggering the transition. Only one property of the current user is available: *accountId.* To set a user-type field (such as Assignee, Reporter, or any custom User-picker field), use the *accountId*property.

**For example:**

`{{currentUser.accountId}}` returns the accountId of the user triggering the transition, e.g. `accountId:5ca5b1469a000c1180956957.`Use this to set a user-type field (such as Assignee, Reporter, or any custom User-picker field)

### **now variable**

The `now`variable is used to insert the current date and time. This is useful to save a transition's execution date/time in a custom field.

**For example:**

`{{now}}` returns the current date and time, e.g. `2016-09-30T13:57:23.608Z`

### nowObj

The nowObj variable represents [*Variables used in Nunjucks templates#now*](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449642802/Variables+in+Nunjucks+Templates#VariablesusedinNunjuckstemplates-now) as a Moment.js object.

For example:

`{{ nowObj }}` returns [Variables used in Nunjucks templates#now](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449642802/Variables+in+Nunjucks+Templates#VariablesusedinNunjuckstemplates-now) as a [Moment.js](/cms_trial/space/JMWEC/466323491/date+filter/) object.

`{{ nowObj | date }}` returns current date as a date Object

`{{ issue.fields.duedate | date('clone') <= nowObj }}` returns `true` if the ticket is overdue.

## User-defined variables

In addition to the above variables, you can also create your own variables within the template using the **set** Nunjucks tag.

**For example:**

`{% set x = "High" %}` sets the value of the variable *x* to High. You can also set the variable to an object. For example: `{% set assignee = issue.fields.assignee %}`