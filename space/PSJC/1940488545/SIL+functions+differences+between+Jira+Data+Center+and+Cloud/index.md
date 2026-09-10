# SIL functions differences between Jira Data Center and Cloud

Power Scripts will be unavailable during scheduled maintenance on August 8-9, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

This reference document details the differences in Simple Issue Language (SIL) functions between Jira Data Center (DC) and Cloud environments. It provides a comprehensive comparison of function parameters, impact levels, and required modifications to help developers adapt their SIL routines during Jira DC to Cloud migration.

## Impact Key

The following impact levels indicate the extent of changes required when migrating SIL functions from Data Center to Cloud:

|  |  |
| --- | --- |
| none | While syntax differences exist between environments, the function will work in JIRA Cloud without requiring code changes. |
| minor | A code change may be required, with all necessary information documented and easily accessible. |
| moderate | Additional lines of code (1 to 3) may be needed to resolve the differences in functionality. |
| major | Significant code modification (additional 5 to 10 lines) may be needed to resolve the differences in functionality; in some cases, equivalent functionality may not be available in Jira Cloud. |

The ZIP file provided below contains a migration analysis script that works in both Data Center and Cloud environments.  When executed, it scans your existing scripts and identifies SIL functions that require modifications during the migration from Data Center to Cloud..

[Unmapped macro: attachments — no content to fall back on]

---

## Removed parameters

When comparing Jira DC and Cloud functions syntax, some parameters available in Jira DC have been removed in Jira Cloud. These removals can significantly impact function behavior.

| **Function name** | **Data Center syntax** | **Cloud syntax** | **Impact** | **Notes/Comment** |
| --- | --- | --- | --- | --- |
| `admChangeFilterOwner` | `admChangeFilterOwner(oldOwnerName, newOwnerName, filterName)` | `admChangeFilterOwner(filterId, newOwner)` | moderate | While the removal of `oldOwnerName` is minor, changing from `filterName` to `filterId` may take additional code. |
| `admGetCustomFieldOptions` | `admGetCustomFieldOptions(fieldName, projectKeys, issueTypes[, filterDisabled])` | `admGetCustomFieldOptions(fieldName[, projectIssueTypesNames[, filterDisabled]])` | moderate | `projectKeys` parameter has been removed. Additional code may be required to filter options by project. |
| `admGetFiltersForProject` | `admGetFiltersForProject(user, projectKey)` | `admGetFiltersForProject(projectKey)` | moderate | Since the `user` parameter is removed in Jira Cloud, additional code is needed to filter results for a specific user. |
| `admUpdateCustomFieldOptions` | `admUpdateCustomFieldOptions(fieldName, pathToFile, charset, actionForOldFieldValues, actionForExistingFieldValues, projectKeys, issueTypes, useDefaultScheme, reorder, updateExistingOptionsValues, applyActionsOnParentOptions)` | `admUpdateCustomFieldOptions(fieldName, options[, projectIssueTypesNames])` | major | Missing parameters like `pathToFile` significantly change how this function operates in the cloud. |
| `getIssueEntityPropertyValue` | `getIssueEntityPropertyValue(issueKey, entityName, propertyKey)` | `getIssueEntityPropertyValue(issueKey, propertyKey)` | minor |  |
| `getRequestsTypes` | `getRequestsTypes(portalId)` | `getRequestsTypes([searchQuery[, serviceDesksIds]])` | minor | Minor changes are needed to convert from `portalId` to `searchQuery`. |

---

## Additional parameters

These functions have additional parameters when comparing between DC and cloud. The functionality of the function should not change dramatically but additional code may be required to get the information to supply as the parameter.

When comparing Jira DC and Cloud functions, some Cloud functions have additional parameters. While the basic functionality remains largely unchanged, additional code may be needed to gather the information for these new parameters.

| **Function name** | **Data Center syntax** | **Cloud syntax** | **Impact** | **Notes/Comment** |
| --- | --- | --- | --- | --- |
| `admCreateProject` | `admCreateProject(pkey, pname, description, lead, url, categoryName, defaultIsUnassigned, avatarId[, projectTypeKey])` | `admCreateProject(key, name, description, projectType, url, category, defaultUser, assign_to_def_user[,permissionScheme, issueSecurityScheme, notificationScheme, fieldConfigScheme, issueTypeScheme, issueTypeScreenScheme, workflowScheme])` | MODERATE | Projects in Jira Cloud have different types; the project creation API is also different. |
| `admReindex` | `admReindex([useBackgroundReindexing])` | `admReindex(jqlQuery[, async])` | minor | In Jira Cloud, you must provide a JQL query to determine which issues to reindex; you can still use a query that includes all issues. |
| `admSetProjectWorkflowScheme` | `admSetProjectWorkflowScheme(pkey, schemeName)` | `admSetProjectWorkflowScheme(projectKey, propertyKey, propertyName, value)` |  |  |
| `cloneIssue` | `cloneIssue(issueKey, [issueLinkTypeName [, newParentKey]])` | `cloneIssue(issueKey, project_key, [issueLinkTypeName [, newParentKey]])` | minor | `project_key` is a required parameter in Jira Cloud. |
| `getAllOpenSprints` | `getAllOpenSprints()` | `getAllOpenSprints(boardId)` | minor | `boardId` is a required parameter in Jira Cloud. |
| `issueInBacklog` | `issueInBacklog(issue key[, boardName])` | `issueInBacklog(boardId, issue_key)` | minor | `boardId` is a required parameter in Jira Cloud. |
| `issueInEpic` | `issueInEpic(issue key, epic key)` | `issueInEpic(boardId, epicId, issueKey)` | minor | `boardId` is a required parameter in Jira Cloud. |

---

## Changed parameters

Parameters differ between Jira DC and Cloud functions. These differences can range from minor changes (like username versus user ID) to more significant modifications.

| **Function name** | **Data Center syntax** | **Cloud syntax** | **Impact** | **Notes/Comment** |
| --- | --- | --- | --- | --- |
| `accountIdToDisplayName` | `accountIdToDisplayName(userKey)` | `accountIdToDisplayName(accountId)` | minor | Switching from `userKey` to `accountId`is required in Jira Cloud. |
| `admCreateScreen` | `admCreateScreen(name, description)` | `admCreateScreen(screen)` | minor |  |
| `admGetIssueTypeScheme` | `admGetIssueTypeScheme(pkey)` | `admGetIssueTypeScheme(name, id)` | minor |  |
| `admGetIssueTypesFromScheme` | `admGetIssueTypesFromScheme(issueTypeSchemeName)` | `admGetIssueTypesFromScheme(id)` | minor | In Jira DC, functions accept `issueTypeSchemeName`; in Jira Cloud `id` is required. |
| `admSetIssueTypeScheme` | `admSetIssueTypeScheme(pkey, schemeName)` | `admSetIssueTypeScheme(pKey, schemeId)` | minor | `schemeName` is accepted in Jira DC, while `schemeId` must be used in Jira Cloud. |
| `admShareFilter` | `admShareFilter(filterId, shareType, [ shareRight [, shareName [,roleName ]]])` | `admShareFilter(filterId, rights, sharePerm)` | moderate | Additional code can be needed to determine appropriate values. |
| `createWebLink` | `createWebLink(issueKey, url, title)` | `createWebLink(issueKey, remoteLinkStruct)` | minor |  |
| `filterForBoard` | `filterForBoard(boardName)` | `filterForBoard(boardId)` | minor | `boardName` is accepted in Jira DC; `boardId`must be used in Jira Cloud. |
| `getUserOrganizations` | `getUserOrganizations(username)` | `getUserOrganizations(userAccountId)` | minor | `username` is accepted in Jira DC, `userAccountId` must be used in Jira Cloud. |
| `projectsForBoard` | `projectsForBoard(board)` | `projectsForBoard(boardId)` | minor | Parameter name changed from `board` in Jira DC to `boardId` in Cloud. |
| `userHasAccessToComment` | `userHasAccessToComment(user, comment_id)` | `userHasAccessToComment(accountId, issueKey, comment_id)` | minor | Parameter changed from `user` in Jira DC to `accountId` in Cloud; `issueKey` parameter added in Cloud. |
| `userKeyToUsername` | `userKeyToUsername(userKey)` | `userKeyToUsername(accountID)` | minor | Switching from `userKey` to `accountId`is required in Jira Cloud. |

---

## Addition of issue parameter

The following functions require an additional issue parameter in Jira Cloud. Since the issue parameter (`issue` or `issueKey`) is consistently placed first in Cloud functions, automated script updates are possible.

| **Function name** | **Data Center syntax** | **Cloud syntax** | **Impact** | **Notes/Comment** |
| --- | --- | --- | --- | --- |
| `deleteComment` | `deleteComment(commentId_or_mode[, issue, dispatchEvent])` | `deleteComment(issue, commentId_or_mode)` | minor |  |
| `editComment` | `editComment(commentId, comment[, securityLevel, dispatchEvent])` | `editComment(issueKey, comment_id, comment[, securityLevel])` | minor |  |
| `getCommentById` | `getCommentById(id)` | `getCommentById(issueKey, id)` | minor |  |
| `getWorklogAuthor` | `getWorklogAuthor(worklog)` | `getWorklogAuthor(issue, worklog)` | minor |  |
| `getWorklogComment(worklog)` | `getWorklogComment(worklog)` | `getWorklogComment(issue, worklog)` | minor |  |
| `getWorklogLoggedHours` | `getWorklogLoggedHours(worklog)` | `getWorklogLoggedHours(issue, worklog)` | minor |  |
| `getWorklogStartDate` | `getWorklogStartDate(worklog)` | `getWorklogStartDate(issue, worklog)` | minor |  |
| `getWorklogUpdateAuthor` | `getWorklogUpdateAuthor(worklog)` | `getWorklogUpdateAuthor(issue, worklog)` | minor |  |
| `getWorklogUpdatedDate` | `getWorklogUpdatedDate(worklog)` | `getWorklogUpdatedDate(issue, worklog)` | minor |  |
| `removeWorklogAdjustEstimate` | `removeWorklogAdjustEstimate(worklog)` | `removeWorklogAdjustEstimate(issue, worklog)` | minor |  |
| `removeWorklogExistingEstimate` | `removeWorklogExistingEstimate(worklog)` | `removeWorklogExistingEstimate(issue, worklog)` | minor |  |
| `removeWorklogIncreaseEstimateBy(worklog, increaseBy)` | `removeWorklogIncreaseEstimateBy(worklog, increaseBy)` | `removeWorklogIncreaseEstimateBy(issue, worklog, increaseBy)` | minor |  |
| `removeWorklogSetEstimateTo` | `removeWorklogSetEstimateTo(worklog, setTo)` | `removeWorklogSetEstimateTo(issue, worklog, setTo)` | minor |  |
| `isPublicJSDComment` | `isPublicJSDComment(jsdCommentId)` | `isPublicJSDComment(requestId_or_Key, commentId)` | minor | `requestId_or_Key` is required in Jira Cloud. |
| `updateWorklogAdjustEstimate` | `updateWorklogAdjustEstimate(worklog, interval, startDate, comment)` | `updateWorklogAdjustEstimate(issue, worklog, interval, startDate, comment)` | minor |  |
| `updateWorklogExistingEstimate` | `updateWorklogExistingEstimate(worklog, interval, startDate, comment)` | `updateWorklogExistingEstimate(issue, worklog, interval, startDate, comment)` | minor |  |
| `updateWorklogSetEstimateTo` | `updateWorklogSetEstimateTo(worklog, interval, startDate, comment, setTo)` | `updateWorklogSetEstimateTo(issue, worklog, interval, startDate, comment, setTo)` | minor |  |

---

## Optional parameters change

These functions have changes to their optional parameters through additions, removals, or modifications. Since these parameters are optional, your code will most likely continue to work without changes.

| **Function name** | **Data Center syntax** | **Cloud syntax** | **Impact** | **Notes/Comment** |
| --- | --- | --- | --- | --- |
| `autotransition` | `autotransition(transition, issueKey, [skipStateCheck, [skipConditions, skipValidators]])` | `autotransition(transition, issueKey)` | MAJOR | The Jira Cloud version of this function no longer has the optional `skip` parameters, so transitions will likely be blocked until conditions and validators are satisfied. |
| `createIssue` | `createIssue(projectKey, parentIssueKey, issueType, summary[, priority, description, components, due date, estimate, security_level, field_mappings])` | `createIssue(projectKey, parentIssueKey, issueType, summary[, priority, description, components, due date, security_level, field_mappings])` | minor | `estimate` is not available in Jira Cloud. |
| `getAllBoardNames` | `getAllBoardNames([user])` | `getAllBoardNames()` | moderate |  |
| `getAllBoards` | `getAllBoards([username])` | `getAllBoards()` | moderate |  |
| `getAllUsers` | `getAllUsers([maxResults])` | `getAllUsers()` | minor |  |
| `getBoardName` | `getBoardName(id, [user])` | `getBoardName(boardId)` | minor |  |
| `getComponents` | `getComponents(pkey [, filterArchived])` | `getComponents(pkey)` | minor |  |
| `getIncomingEmail` | `getIncomingEmail([prefer_html, strip_whitespace])` | `getIncomingEmail()` | moderate |  |
| `issuesInBoard` | `issuesInBoard(board[, filterVisible])` | `issuesInBoard(boardId [, jql])` | moderate |  |
| `usersInGroups` | `usersInGroups(groups[, activeUsersOnly])` | `usersInGroups(groups)` | minor | Additional code can be required to filter active users. |

---

## Dispatch events

The optional `dispatchEvent` parameter, which triggered Jira notifications, is not available in Jira Cloud functions.

| **Function name** | **Data Center syntax** | **Cloud syntax** | **Impact** | **Notes/Comment** |
| --- | --- | --- | --- | --- |
| `addComment` | `addComment(issue, username, comment[, securityLevel, dispatchEvent])` | `addComment(issue, username, comment[, securityLevel])` | minor |  |
| `deleteComment` | `deleteComment(commentId_or_mode[, issue, dispatchEvent])` | `deleteComment(issue, commentId_or_mode)` | minor |  |
| `editComment` | `editComment(commentId, comment[, securityLevel, dispatchEvent])` | `editComment(issueKey, comment_id, comment[, securityLevel])` | minor |  |

---

## Parameter changes with no impact

Although these functions differ between Jira DC and Cloud, the differences will not affect migration.

| **Function name** | **Data Center syntax** | **Cloud syntax** | **Impact** | **Notes/Comment** |
| --- | --- | --- | --- | --- |
| `admCreateCustomField` | `admCreateCustomField(fieldName, description, fieldType, fieldSearcher, projects, issueTypes)` | `admCreateCustomField(fieldName, description, fieldType[, fieldSearcher, [projects, issueTypes]])` | none | Since the `projects` and `issueType` parameters exist as optional in the Jira Cloud version of the function, the code will migrate without changes. |
| `admGetProjectIssueSecurityScheme` | `admGetProjectIssueSecurityScheme(pkey)` | `admGetProjectIssueSecurityScheme(projectKeyOrId)` | none | Jira Cloud can accept either the project key or the project ID. |
| `admGetProjectNotificationScheme` | `admGetProjectNotificationScheme(pkey)` | `admGetProjectNotificationScheme(projectKeyOrId)` | none | Jira Cloud can accept either the project key or the project ID. |
| `admGetProjectPermissionScheme` | `admGetProjectPermissionScheme(pkey)` | `admGetProjectPermissionScheme(projectKeyOrId)` | none | Jira Cloud can accept either the project key or the project ID. |
| `admGetProjectWorkflowScheme` | `admGetProjectWorkflowScheme(pkey)` | `admGetProjectWorkflowScheme(projectKeyOrId)` | none | Jira Cloud can accept either the project key or the project ID. |
| `createSprint` | `createSprint(rapidViewId, sprintName)` | `createSprint(boardId, sprintName [,goal [,startDate, endDate]])` | none | Additional sprint fields can be set in Jira Cloud. |
| `linkIssue` | `linkIssue(issueKey1, issueKey2_or_url, issueLinkTypeName)` | `linkissue(inwardIssueKey, outwardIssueKey, issueLinkTypeName [, comment, securityLevel])` | none | `comment` and `securityLevel` are optional parameters in Jira Cloud. |