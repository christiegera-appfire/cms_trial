# Issue and Transition Data in Nunjucks

This document explains how to access the details of *issue* and *transition* objects, such as those available through the [issue](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) and [transition](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) variables. To see an example of the structure of an issue go to **<base\_URL\_of\_Jira>/rest/api/latest/issue/{issueKey}**. The fields displayed through this REST API actually depend on the fields set on the issue.

Structure of an issue object

An issue object consists of the issue key and a collection of fields. The structure of the issue object (such as those available through the `issue`, `sourceIssue` and `linkedIssue` variables) is the same as that returned by the **/rest/api/latest/issue** REST resource documented [**here**](https://docs.atlassian.com/jira/REST/cloud/#api/2/issue-getIssue).

#### issue object

- **Description**: The *issue* object is an object with the following fields.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]

**Accessing issue details using Nunjucks**:

- Key of the issue : `{{issue.key}}`
- ID of the issue : `{{issue.id}}`
- [Standard Jira fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)
- [Predefined Custom Fields](/cms_trial/space/JMWEC/465242312/Predefined+Custom+Fields/)
- [User-created custom fields](/cms_trial/space/JMWEC/465505179/User-created+Custom+Fields/)

## Structure of the `transition` variable

The `transition` variable describes the current workflow transition. You might want to look at the log entries of a post-function execution to see the structure. The transition of an issue consists of the following fields :

#### transitionName

- **Description** : The name of the current transition.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Access the** ***transitionName*** **field** :

  - Name of the transition - `{{transition.transitionName}}`

#### transitionId

- **Description** : The ID of the current transition.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***transitionId*** **field** :

  - `{{transition.transitionId}}`

#### from\_status

- **Description** : The status from which the current transition starts.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***from\_status*** **field** :

  - `{{transition.from_status}}`

#### to\_status

- **Description** : The status to which the current transition leads
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***to\_status*** **field** :

  - `{{transition.to_status}}`

#### workflowName

- **Description** : The name of the workflow the transition belongs to.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]

  **Accessing the** ***workflowName*** **field** :

  - `{{transition.workflowName}}`

#### workflowId

- **Description** : The ID of the workflow the transition belongs to.
- **Structure** :

  [Unmapped macro: legacy-content — no content to fall back on]
- **Accessing the** ***workflowID*** **field** :

  - `{{transition.workflowId}}`