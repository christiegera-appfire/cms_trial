# Migrations

Are you using JQL Search Extensions for Jira Data Center and want to continue using JQL Search Extensions on Jira Cloud? This page describes the key feature and syntax differences. You can also find a list of the additional [Cloud-only extensions](https://appfire.atlassian.net/wiki/spaces/JQLSEARCH/pages/edit-v2/604209729#Cloud-only-features) that are available to you with JQL Search Extensions for Jira Cloud.

See our full list of Cloud extensions with examples: [JQL functions and keywords reference](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/).

## Platform differences

### JQL syntax

The implementation of JQL Search Extensions (JSE) differs between Jira Data Center and Jira Cloud.

For Jira Data Center, all extensions are implemented as JQL **functions** that perform calculations using the values specified in `()`.

All functions are preceded by `issue in`, for example, `issue in commentedBefore("2022-09-11")`.

For Jira Cloud, most JQL extensions are implemented as JQL **keywords** as references to issue metadata, resulting in indexed searches. Keywords are followed by operators, for example, `commentedOnDate < "2018-05-26"`. Other, more complex searches are implemented as JQL functions. Refer to the [syntax table](/cms_trial/space/JQLSEARCH/604209729/Migrations/) on this page for the complete list.

### Usage

You can use the extensions in JQL Search Extensions for Jira Data Center in Jira’s advanced search.

In JQL Search Extensions for Jira Cloud, the app provides JQL keywords that can be used in Jira’s advanced search and the Extended Search page. JQL functions are accessible from the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page or by using [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in Jira’s advanced search.

#### Examples

| **Jira Data Center** |
| --- |
| Jira advanced search showing a JQL Search Extensions Data Center function query in the search field. |
| **Jira Cloud** |
| JQL Search Extensions Extended Search page showing a Cloud keyword query in the search field. |

### Execution model

With the Data Center version, the search queries are executed in the same Java Virtual Machine (JVM) as Jira. In the Cloud version, the JQL Search Extensions service is a separate deployment communicating with Jira over the REST API. As a result, all operations in the cloud are indexed [asynchronously](/cms_trial/space/JQLSEARCH/604209683/Asynchronous+execution/), and updates to issues in Jira can be reflected in the JQL with a slight delay.

## Migration pathway

Queries are not migrated. If you want to use any saved queries from your Data instance in Jira Cloud, the first step is to identify queries that use JQL Search Extensions. You should especially look at:

- Filters
- Board filters
- Automation rules
- Dashboard gadgets
- Other apps that accept filters and JQL queries, for example, JSU, JMWE, Power Scripts, or BigPicture

Once you have identified where the saved queries are used, translate them to the Cloud-equivalent JQL extension using the [syntax table](/cms_trial/space/JQLSEARCH/604209729/Migrations/) below. You can also build new queries using the [additional extensions](/cms_trial/space/JQLSEARCH/604209729/Migrations/) provided by JQL Search Extensions for Jira Cloud. If you require additional assistance, please contact our [support team](https://appf.re/support).

## Feature parity comparison

The table below lists the query parity between JQL Search Extensions for Jira Data Center and Jira Cloud.

Last updated November 4, 2025

| **Keyword/function type** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Projects | ✅ | ✅ | `movedProjects` was deprecated September 30, 2024 |
| Fields | ✅ | ✅ |  |
| Attachments | ✅ | ✅ |  |
| Comments | ✅ | ✅ |  |
| Versions | ✅ | ✅ |  |
| Links | ✅ | ✅ |  |
| Issue Updates | ✅ | ✅ |  |
| Subtasks | ✅ | ✅ |  |
| Software Development | ✅ | ❌ | If you linked your development tools, refer to Atlassian’s Jira Cloud JQL [documentation](https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-development-fields-reference-973491363.html). |
| Issue Hierarchy | ✅ | ✅ |  |
| User | ✅ | ❌ |  |

## Cloud-only features

JQL Search Extensions for Jira Cloud provides the following additional extensions that are not unavailable with the Data Center app.

|  |
| --- |
| **Agile** |
| nextSprint()  previousSprint()  addedToSprintAfterStart() |
| **Attachments** |
| attachmentContent |
| **Comments** |
| commentUpdatedOnDate  commentLastUpdatedOnDate |
| **Epics** |
| epicsOfChildrenInQuery()  childrenOfEpicsInQuery()  issuesInEpicCount  bugsInEpicCount  storiesInEpicCount  issuesInEpicToDoCount  issuesInEpicInProgressCount  issuesInEpicDoneCount  bugsInEpicToDoCount  bugsInEpicInProgressCount  bugsInEpicDoneCount  storiesInEpicToDoCount  storiesInEpicInProgressCount  storiesInEpicDoneCount |
| **Field Comparison** |
| dateCompare()  dateCompareIgnoreTime() |
| **Issue & Project Updates** |
| updatedOnDates  lastUpdatedBy  movedProjectsCount (deprecated September 30, 2024 ) |
| **Jira Hierarchy and Advanced Roadmaps** |
| parentsOfIssuesInQuery()  parentsOfIssuesInQueryRecursive()  childrenOfIssuesInQuery()  childrenOfIssuesInQueryRecursive() |
| **Links** |
| linksIssueProject |
| **Subtasks** |
| parentSummary  parentPriority  parentIssueType  parentStatus  parentStatusCategory |
| **Text** |
| exactTextMatch()  exactTextMatchCaseInsensitive() |
| **Web Links (Remote Links)** |
| remoteLinkUrl  remoteLinkUrlPartialMatch  remoteLinkApplicationName  remoteLinkApplicationType  remoteLinkHost  remoteLinkQuery  remoteLinkPath  remoteLinkTitle  remoteLinkTitlePartialMatch  remoteLinkRelationship  remoteLinksCount |

## Syntax differences between JSE Data Center and JSE Cloud

Most JQL functions are written as keywords in JSE Cloud. Refer to this table when converting saved queries if you migrate from the Data Center version of our app.

| **Data Center** | **Cloud** | **Notes** |
| --- | --- | --- |
| movedIssues() | `movedProjects` | `movedProjects` was deprecated September 30, 2024 |
| fieldMatch() | `regex()`, or `wildcardMatch()` |  |
| fieldsHaveSameValue() | `hasSameUpdatedAndCreatedDate`  `hasSameAssigneeAndReporter`  `hasSameVersions` |  |
| attachedAfter() | `attachedOnDate` |  |
| attachedBefore() | `attachedOnDate` |  |
| attachedBetween() | `attachedOnDate` |  |
| attachedOnDate() | `attachedOnDate` |  |
| attachedByUser() | `attachedByUser` |  |
| attachmentExtension() | `attachmentExtension` |  |
| attachmentName() | `attachedByUser` |  |
| attachmentsCountEqualTo() | `attachmentsCount` |  |
| attachmentsCountGreaterThan() | `attachmentsCount` |  |
| attachmentsCountLessThan() | `attachmentsCount` |  |
| commentedAfter() | `commentedOnDate` |  |
| commentedBefore() | `commentedOnDate` |  |
| commentedBetween() | `commentedOnDate` |  |
| commentedOnDate() | `commentedOnDate` |  |
| commentedByUser() | `commentedByUser`  `commentLastCreatedBy`  `commentLastUpdatedBy` |  |
| commentsCountEqualTo() | `commentsCount` |  |
| commentsCountGreaterThan() | `commentsCount` |  |
| commentsCountLessThan() | `commentsCount` |  |
| affectedVersionsArchivedCountLessThan() | `affectedVersionsArchived` |  |
| affectedVersionsArchivedCountEqualTo() | `affectedVersionsArchived` |  |
| affectedVersionsArchivedCountGreaterThan() | `affectedVersionsArchived` |  |
| affectedVersionsCountLessThan() | `affectedVersionsCount` |  |
| affectedVersionsCountEqualTo() | `affectedVersionsCount` |  |
| affectedVersionsCountGreaterThan() | `affectedVersionsCount` |  |
| affectedVersionsOpenedCountLessThan() | `affectedVersionsOpened` |  |
| affectedVersionsOpenedCountEqualTo() | `affectedVersionsOpened` |  |
| affectedVersionsOpenedCountGreaterThan() | `affectedVersionsOpened` |  |
| affectedVersionsReleasedCountLessThan() | `affectedVersionsReleased` |  |
| affectedVersionsReleasedCountEqualTo() | `affectedVersionsReleased` |  |
| affectedVersionsReleasedCountGreaterThan() | `affectedVersionsReleased` |  |
| affectedVersionReleasedOnDate() | `affectedVersionReleasedDate` |  |
| affectedVersionReleasedBetweenDates() | `affectedVersionReleasedDate` |  |
| affectedVersionReleasedAfterDate() | `affectedVersionReleasedDate` |  |
| affectedVersionReleasedBeforeDate() | `affectedVersionReleasedDate` |  |
| fixVersionsArchivedCountLessThan() | `fixVersionsArchived` |  |
| fixVersionsArchivedCountEqualTo() | `fixVersionsArchived` |  |
| fixVersionsArchivedCountGreaterThan() | `fixVersionsArchived` |  |
| fixVersionsCountLessThan() | `fixVersionsCount` |  |
| fixVersionsCountEqualTo() | `fixVersionsCount` |  |
| fixVersionsCountGreaterThan() | `fixVersionsCount` |  |
| fixVersionsOpenedCountLessThan() | `fixVersionsOpened` |  |
| fixVersionsOpenedCountEqualTo() | `fixVersionsOpened` |  |
| fixVersionsOpenedCountGreaterThan() | `fixVersionsOpened` |  |
| fixVersionsReleasedCountLessThan() | `fixVersionsReleased` |  |
| fixVersionsReleasedCountEqualTo() | `fixVersionsReleased` |  |
| fixVersionsReleasedCountGreaterThan() | `fixVersionsReleased` |  |
| fixVersionReleasedOnDate() | `fixVersionReleaseDate` |  |
| fixVersionReleasedBetweenDates() | `fixVersionReleaseDate` |  |
| fixVersionReleasedAfterDate() | `fixVersionReleaseDate` |  |
| fixVersionReleasedBeforeDate() | `fixVersionReleaseDate` |  |
| latestReleaseVersionForProject() | No direct cloud equivalent |  |
| linksCountLessThan() | `linksCount` |  |
| linksCountGreaterThan() | `linksCount` |  |
| linksCountEqualTo() | `linksCount` |  |
| linkedBy([linktype], jql-query or issuekeys) | function `linkedIssuesOfQuery()` |  |
| links(jql-query, link type) | function `linkedIssuesOfQuery()` |  |
| linksIssue() | `linkedBy`  `linksIssue` |  |
| linkType() | `linkType` |  |
| linkedIssueStatus() | `linkedIssueStatus` |  |
| linkedIssueStatusCategory() | `linkedIssueStatusCategory` |  |
| linkedIssueType() | `linkedIssueType` |  |
| linkedIssuePriority() | `linkedIssuePriority` |  |
| linkedByIssueProject() | `linkedByIssueProject` |  |
| updatedByUserCountLessThan() | `updatedByUsersCount` |  |
| updatedByUserCountGreaterThan() | `updatedByUsersCount` |  |
| updatedByUserCountEqualTo() | `updatedByUsersCount` |  |
| updatedByUser() | `updatedBy` |  |
| transitionedByUser() | `transitionedBy` |  |
| loggedTimeByUser() | `loggedTimeBy` |  |
| subTaskOf(jql-query) | function `subtasksOfParentsInQuery()` |  |
| parentOf(jql-query) | functions  `parentsOfIssuesInQuery()`  `parentsOfIssuesInQueryRecursive()` |  |
| subtaskCountLessThan() | `subtasksCount` |  |
| subtaskCountGreaterThan() | `subtasksCount` |  |
| subtaskCountEqualTo() | `subtasksCount` |  |
| subTaskKey() | `subtaskKey` |  |
| subtaskPriority() | `subtaskPriority` |  |
| subTaskType() | `subtaskIssueType` |  |
| subTaskStatus() | `subtaskStatus` |  |
| subTaskStatusCategory() | `subtaskStatusCategory` |  |
| openPullRequestsCount() commitsCount() failingBuildsCount() openReviewsCount() pullRequestsCount() reviewsCount() | There is no support in JQL Search Extensions Cloud | If you linked your development tools, refer to the native Jira Cloud JQL documentation <https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-development-fields-reference-973491363.html> |
| allIssuesInEpic(jql-query or issuekey) | function `childrenOfEpicsInQuery()` |  |
| epicOf(jql-query) | function `epicsOfChildrenInQuery()` |  |
| `userMatch` | No direct cloud equivalent |  |

See the full list of Cloud JQL extensions with examples: [JQL functions and keywords reference](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/).