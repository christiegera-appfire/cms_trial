# Standard JIRA Fields

This page explains how to access the value of Standard Jira fields using Nunjucks. Each field's structure is explained with examples. To understand how to *write* values into these fields see, [Text input for fields](/cms_trial/space/JMWEC/466289528/Text+input+for+fields/) and [JSON input for fields](/cms_trial/space/JMWEC/466225769/JSON+input+for+fields/).

It is now possible to access the standard fields of an issue by its *Field name* or *Key*.

**Example:**

`{{ issue.fields.watches.watchCount }}` and `{{ issue.fields.Watchers.watchCount }},` both return the number of watchers.

When the field *name* contains a space or any special character, you need to use the array syntax to access the field :

**Example:**

`{{ issue.fields['Issue Type'].name }}`

`{{ issue.fields['Component/s'][0].name }}`

## Affects Version/s

- **Field name :** `Affects Version/s`
- **Key:** `versions`
- **Description** : The Affects Version/s field is an array of objects. Each object represents a single version.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Affects version/s*** **field** :

  - First Affects Version name : `{{issue.fields.versions[0].name}}`
  - Last Affects Version name:

    ```text
    {{ issue.fields.versions | last | field("name")}}
    ```

    where '|' is the pipe operator, 'last' and 'field' are filters. See [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations for more filters.
  - Join the *names* of the Affects Version/s, separated by commas: `{{issue.fields.versions | join("," , "name")}}`
  - Return all the Affects Version/s, in a format that can be used to set the Fix Version/s field : `{{issue.fields.versions | dump(2)}}`
  - Test whether "1.0" is in the Affects Version/s: `{{ issue.fields.versions | find({name:"1.0"}) }}`

## Assignee

- **Field name :** `Assignee`
- **Key:** `assignee`
- **Description** : The Assignee field is an object that represents the user who this issue is assigned to.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Assignee*** **field** :

  - AccountId of the Assignee : `{{issue.fields.assignee.accountId}}`
  - Timezone of the assignee : `{{issue.fields.assignee.timeZone}}`

## Attachments

- **Field name :** `Attachment`
- **Key:** `attachment`
- **Description** : Attachment is an array of objects. Each object represents a single attachment.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Attachment*** **field**:

  - Size of the last attachment :

    ```text
    {{ issue.fields.attachment | last | field("size")%}
    ```

    where '|' is the pipe operator, 'last' and 'field' are filters. See [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations for more filters.
  - Name of the Author of the first attachment : `{{ issue.fields.attachment[0].author.accountId}}`

## Created

- **Field name :** `Created`
- **Key:** `created`
- **Description** : The Created field is a string representation of a date.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Created*** **fields** :
- - Created date of the issue : `{{ issue.fields.created }}`
  - Format the created date : `{{ issue.fields.created | date('fromNow') }}`

You can use the [date](/cms_trial/space/JMWEC/466323491/date+filter/) filter to manipulate and/or format the value

## Creator

- **Field name :** `Creator`
- **Key:** `creator`
- **Description** : The Creator field is an object that represents the user who created this issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Creator*** **field** :

  - Name of the Creator of the issue : `{{ issue.fields.creator.accountId }}`
  - Display name of the creator : `{{ issue.fields.creator.displayName }}`

## Comments

- **Field name :** `Comment`
- **Key:** `comment`
- **Description** : The Comments field is an object with two fields:

  - `comments`, containing an array of objects. Each object represents a single comment.
  - `total`, showing the number of comments
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Comments*** **field**:

  - Number of comments on the issue : `{{issue.fields.comment.total}}`
  - Last Comment body :

    ```text
    {{ issue.fields.comment.comments | last | field("body") }}
    ```

    where '|' is the pipe operator, 'last' and 'field' are filters. See [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations for more filters.
  - AccountId of the author of the first comment on the issue :

    ```text
    {{ issue.fields.comment.comments | first | field("author.accountId") }}
    ```

    where '|' is the pipe operator, 'first' and 'field' are filters. See [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations for more filters.
  - Email address of the author of the last comment on the issue :

    ```text
    {{ issue.fields.comment.comments | last | field("author.emailAddress") }}
    ```

    where '|' is the pipe operator, 'last' and 'field' are filters. See [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations for more filters.
  - Display all the comments in a text field : `{{ issue.fields.comment.comments | join("\n" , "body") }}`

## Component/s

- **Field name :** `Component/s`
- **Key:** `components`
- **Description** : The Components field is an array of objects. Each object represents one component.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Components*** **field** :

  - First component name : `{{issue.fields.components[0].name}}`
  - Last component description :

    ```text
    {{ issue.fields.components | last | field("description") }}
    ```

    where '|' is the pipe operator, 'last' and 'field' are filters. See [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations for more filters.
  - All components of the current issue:

    ```text
    {{issue.fields.components | join ("," , "name") }}
    ```
  - Test whether "UI" is in the Components: `{{ issue.fields.components | find({name:"UI"}) }}`

## Description

- **Field name :** `Description`
- **Key:** `description`
- **Description** : The Description field is a string representation of a multi-line text describing the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Description*** **field** :

  - Description of the issue : `{{issue.fields.description}}`

## Due Date

- **Field name :** `Due Date`
- **Key:** `duedate`
- **Description** : The Due Date field is a string representation of a date.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Due date*** **field** :
- - The Due date of the issue : `{{issue.fields.duedate}}`
  - Set the Due date to Created + 2 days if the priority of the issue is "Highest". Ignore it, if it is already less than or equal to 2 days (using the "Ignore empty value" option) :

    ```text
    {% set duedate = issue.fields.duedate %}
    {% set newdate = issue.fields.created | dateadd(2,"d") %}
    {% if issue.fields.priority.name == "Highest" %}
    	{% if duedate >= newdate or duedate == null%}
    		{{newdate}}
    	{%else%}
    		{{duedate}}
    	{%endif%}
    {%endif%}
    ```
  - Format the due date and add it as a comment on the issue, once the issue is transitioned to In Progress state :

    ```text
    This issue is due on : {{ issue.fields.duedate | date('dddd, MMMM Do YYYY, h:mm:ss a') }}
    ```

    where, *date* is the date filter. See [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations for more filters.

You can use the [date](/cms_trial/space/JMWEC/466323491/date+filter/) filter to manipulate and/or format the value

## Environment

- **Field name :** `Environment`
- **Key:** `environment`
- **Description** : The Environment field is a string representation of a multi-line text describing the environment of the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Environment*** **field** :

  - The Environment of the issue : `{{issue.fields.environment}}`

## FixVersion/s

- **Field name : Fix Version/s**
- **Key:** `fixVersions`
- **Description** : The Fix Version/s field is an array of objects. Each object represents a single version.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Fix** ***Version/s*** **field** :

  - First Fix Version/s name : `{{issue.fields.fixVersions[0].name}}`
  - Last Fix Version/s name:

    ```text
    {{ issue.fields.fixVersions | last | field("name") }}
    ```

    where '|' is the pipe operator, 'first' and 'field' are filters. See [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations for more filters.
  - Return only Fix Versions that are not released, separated by commas:

    ```text
    {% set versions = issue.fields.fixVersions %}
    {% set comma = joiner() %}
    {% for version in versions -%}
    	{% if not version.released %}
    		{{ comma() }}{{ version.name }}
    	{%endif%}
    {%- endfor %}
    ```

    The `joiner` function is a global Nunjucks function describe [here](https://mozilla.github.io/nunjucks/fr/templating.html#joiner-separator).
  - Join the *names* of the Fix Version/s, separated by commas : `{{issue.fields.fixVersions | join("," , "name")}}`
  - Test whether "1.0" is in the Fix Version/s: `{{ issue.fields.fixVersions | find({name:"1.0"}) }}`

## Issue links

- **Field name :** `Linked Issues`
- **Key:** `issuelinks`
- **Description** : Issue links is an array of objects. Each object represents one link.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]

  Note that only one of `inwardIssue` or `outwardIssue` will be present in each issue link. Also, note that only a small subset of the linked issues' fields will be present. A much easier way to access linked issues is through the use of the [linkedIssues, epic, stories, parentIssue and subtasks filters](https://appfire.atlassian.net/wiki/display/JMWEC/How+to+insert+information+using+Nunjucks+annotations#HowtoinsertinformationusingNunjucksannotations-Filters).

- **Accessing the** ***Issue links*** **field**: use the [linkedIssues, epic, stories, parentIssue and subtasks filters](https://appfire.atlassian.net/wiki/display/JMWEC/How+to+insert+information+using+Nunjucks+annotations#HowtoinsertinformationusingNunjucksannotations-Filters) instead.

## Issue type

- **Field name :** `Issue Type`
- **Key:** `issuetype`
- **Description** : The Issue Type field is an object describing the issue type.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Issue type field** :

  - Name of the issue type : `{{issue.fields.issuetype.name}}`
  - Set a text field to `"This issue is a sub-task"` if the issue is a sub-task :

    ```text
    {% if issue.fields.issuetype.subtask == true %}
    	This issue is a sub-task
    {% else %}
    	This issue is not a sub-task
    {% endif %}
    ```

## Key

- **Key:** `key`
- **Description** : The Key of the issue is a string that represents the key of the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Key of the issue** :

  - Key of the issue : `{{issue.key}}`

## Labels

- **Field name :** `Labels`
- **Key:** `labels`
- **Description** : Labels is an array of values representing the labels of the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Labels field** :

  - First label : `{{ issue.fields.labels[0] }}`
  - Last label : `{{ issue.fields.labels | last }}`
  - All the labels of the issue separated by a space : `{{issue.fields.labels | join(" ")}}`
  - Test whether "myLabel" is in the labels: `{{ issue.fields.labels | find("myLabel") }}`

## Last Viewed

- **Key:** `lastViewed`
- **Description** : Last Viewed field is a string representation of a date.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the LastViewed field** :
- - Last viewed time stamp : `{{issue.fields.lastViewed}}`

You can use the [date](/cms_trial/space/JMWEC/466323491/date+filter/) filter to manipulate and/or format the value.

You cannot use this field's value in 'Set field value' or 'Set field value of linked issues' post-functions because this field is special. Its value is user-specific. Since these post-functions are run as the add-on user the field value fetched will always be empty.

However, you can use this field in the 'Comment [linked] issue' post-functions, since it is run as the current user.

## Original Estimate

- **Field name :** `Original Estimate`
- **Key:** `timeoriginalestimate`
- **Description** : The Original Estimate field is a string representation of a number representing the original time estimate in seconds.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Original Estimate field** :

  - Original Estimate of the issue in seconds : `{{ issue.fields.timeoriginalestimate }}`
  - You can access the Original estimate from the Standard JIRA Fields Time tracking field as well.

## Parent

- **Field name :** `Parent`
- **Key:** `parent`
- **Description** : The Parent field is an object representing the parent of the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Parent field** :

  - Summary of the parent issue : `{{ issue.fields.parent.fields.summary }}`
  - Key of the parent issue : `{{ issue.fields.parent.key }}`
  - Id of the parent issue : `{{ issue.fields.parent.id }}`

## Priority

- **Field name :** `Priority`
- **Key:** `priority`
- **Description** : The Priority field is an object describing the priority of the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Priority field** :

  - Name of the Priority of the issue : `{{ issue.fields.priority.name }}`
  - ID of the Priority of the issue : `{{ issue.fields.priority.id }}`

## Progress

- **Field name :** `Progress`
- **Key:** `progress`
- **Description** : The Progress field is an object describing the progress on the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Progress field** :

  - Progress on the issue in seconds : `{{ issue.fields.progress.progress }}`
  - Total progress on the issue in seconds : `{{ issue.fields.progress.total }}`
  - Percentage of progress on the issue : `{{ issue.fields.progress.percent }}`

## Project

- **Field name :** `Project`
- **Key:** `project`
- **Description** : The Project field is an object describing the selected project.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Project field** :

  - Name of the project the issue belongs to : `{{ issue.fields.project.name }}`
  - Key of the project the issue belongs to : `{{ issue.fields.project.key}}`

## Remaining Estimate

- **Field name :** `Remaining Estimate`
- **Key:** `timeestimate`
- **Description** : The Remaining Estimate field is a string representation of a number representing the remaining time estimate in seconds.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Remaining Estimate field** :

  - Remaining Estimate of the issue in seconds : `{{ issue.fields.timeestimate }}`
  - You can access the Remaining estimate from the Standard JIRA Fields Time tracking field as well.

## Reporter

- **Field name :** `Reporter`
- **Key:** `reporter`
- **Description** : The Reporter field is an object that represents the user by whom this issue is reported.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the Reporter field** :

  - AccountId of the reporter of the issue : `{{ issue.fields.reporter.accountId}}`
  - Email address of the reporter : `{{ issue.fields.reporter.emailAddress }}`

## Resolution

- **Field name :** `Resolution`
- **Key:** `resolution`
- **Description** : The Resolution field is an object describing the resolution of the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Resolution*** **field** :

  - Name of the Resolution of the issue : `{{ issue.fields.resolution.name }}`
  - Description of the resolution : `{{ issue.fields.resolution.description }}`

## Resolved

- **Field name :** `Resolved`
- **Key:** `resolutiondate`
- **Description** : The Resolved field is a string representation of a date.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Resolved*** **field** :
- - Time stamp of resolution : `{{ issue.fields.resolutiondate }}`

You can use the [date](/cms_trial/space/JMWEC/466323491/date+filter/) filter to manipulate and/or format the value

## Security level

- **Field name :** `Security Level`
- **Key:** `security`
- **Description** : The Security level field is an object describing the security level of the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Security level*** **field** :

  - Name of the security level of the issue : `{{ issue.fields.security.name }}`
  - Description of the security level of the issue : `{{ issue.fields.security.description }}`

## Status

- **Field name :** `Status`
- **Key:** `status`
- **Description** : The Status field is an object describing the status of the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Status*** **field** :

  - Name of the status of the issue : `{{ issue.fields.status.name }}`
  - Name of the status category of the status : `{{ issue.fields.status.statusCategory.name }}`

## Subtasks

- **Field name :** `Sub-tasks`
- **Key:** `subtasks`
- **Description** : Sub-tasks is an array of objects. Each object represents a single sub-task.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Subtasks*****field**: Only a small subset of the subtasks' fields (see the structure above) will be available from the subtasks field. To access all the fields of the subtasks use the [subtasks filter](https://appfire.atlassian.net/wiki/display/JMWEC/How+to+insert+information+using+Nunjucks+annotations#HowtoinsertinformationusingNunjucksannotations-Filters) instead.

## Summary

- **Field name :** `Summary`
- **Key:** `summary`
- **Description** : The Summary field is a string representation of a single-line text describing the summary of the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Summary*** **field** :

  - Summary of the issue : `{{ issue.fields.summary }}`

## Time spent

- **Field name :** `Time Spent`
- **Key:** `timespent`
- **Description** : The Time spent field is a number representing the time spent on the issue in seconds.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Time spent*** **field** :

  - Time spent on the issue in seconds : `{{ issue.fields.timespent }}`
  - You can access the time spent from the Standard JIRA Fields Time tracking field as well.

## Time tracking

- **Field name :** `Time Tracking`
- **Key:** `timetracking`
- **Description** : The Time tracking field is an object describing the time spent working on the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Time tracking*** **field** :

  - Original Estimate of the issue as duration string : `{{ issue.fields.timetracking.originalEstimate }}`
  - Original Estimate of the issue in seconds : `{{ issue.fields.timetracking.originalEstimateSeconds }}`
  - Remaining Estimate of the issue as duration string : `{{ issue.fields.timetracking.remainingEstimate }}`
  - Remaining Estimate of the issue in seconds : `{{ issue.fields.timetracking.remainingEstimateSeconds }}`
  - Time Spent on the issue as a duration string : `{{ issue.fields.timetracking.timeSpent }}`
  - Time Spent on the issue in seconds : `{{ issue.fields.timetracking.timeSpentSeconds }}`

## Updated

- **Field name :** `Updated`
- **Key:** `updated`
- **Description** : The Updated field is a string representation of a date.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Updated*** **field** :
- - Updated time stamp of the issue : `{{ issue.fields.updated }}`

You can use the [date](/cms_trial/space/JMWEC/466323491/date+filter/) filter to manipulate and/or format the value

## Votes

- **Field name :** `Votes`
- **Key:** `votes`
- **Description** : The Votes field is an object describing the votes on the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Votes***:

  - Number of votes on the issue : `{{issue.fields.votes.votes}}`

## Watchers

- **Field name :** `Watchers`
- **Key:** `watches`
- **Description** : The Watchers field is an object describing the watches on an issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Watchers*** **field** :

  - Number of users watching the issue : `{{ issue.fields.watches.watchcount }}`

## Work log

- **Field name :** `Log Work`
- **Key:** `worklog`
- **Description** : The Work log field is an object with two fields:

  - `worklog`, containing an array of objects. Each object represents a single work log.
  - `total`, showing the total number of work logs.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Worklog***:

  - Total number of work logs : `{{issue.fields.worklog.total}}`

## Work Ratio

- **Field name :** `Work Ratio`
- **Key:** `workratio`
- **Description** : The Work Ratio field is a number representing the ratio of work done on the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***Work Ratio*** **field** :

  - Work ratio of the issue : `{{ issue.fields.workratio }}`

## ∑ Original Estimate

- **Field name :** `Σ Original Estimate`
- **Key:** `aggregatetimeoriginalestimate`
- **Description** : The aggregate original Estimate field is a number representing the total original estimate of the issue and its sub-tasks, if the issue has any.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the ∑ Original Estimate field** :

  - Aggregate original estimate of the issue in seconds : `{{ issue.fields.aggregatetimeoriginalestimate }}`

## ∑ Remaining Estimate

- **Field name :** `Σ Remaining Estimate`
- **Key:** `aggregatetimeestimate`
- **Description** : The aggregate remaining Estimate field is a number representing the total remaining estimate of the issue and its sub-tasks, if the issue has any.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the ∑ Remaining Estimate field** :

  - Aggregate remaining estimate of the issue in seconds : `{{ issue.fields.aggregatetimeestimate }}`

## ∑ Progress

- **Field name :** `Σ Progress`
- **Key:** `aggregateprogress`
- **Description** : The Aggregate Progress field is an object describing the aggregate progress on the issue.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the ∑ Progress field** :

  - Aggregate Progress on the issue in seconds : `{{ issue.fields.aggregateprogress.progress }}`
  - Total progress on the issue in seconds : `{{ issue.fields.aggregateprogress.total }}`
  - Percentage of progress on the issue : `{{ issue.fields.aggregateprogress.percent }}`

## ∑ Time Spent

- **Field name :** `Σ Time Spent`
- **Key:** `aggregatetimespent`
- **Description** : The Aggregate time spent field is a number representing the total time spent on the issue and its sub-tasks, if the issue has any.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the ∑ Time spent field** :

  - Aggregate time spent on the issue in seconds : `{{ issue.fields.aggregatetimespent }}`