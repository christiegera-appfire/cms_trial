# JQL functions and keywords reference

This page lists the JQL functions and keywords available in JQL Search Extensions for Jira Cloud. Use it as a starting point to explore the available query functions by category, including issue hierarchy, epics, sprints, comments, links, attachments, and field values. Each category page includes detailed descriptions, syntax, and examples to help you build advanced JQL queries in Jira Cloud.

For details on using functions with Jira Data Center, see the Data Center [documentation](/cms_trial/space/JQLSEARCH/1865482654/JQL+functions+reference/).

Refer to the category pages for complete descriptions and examples.

## Issue hierarchy

See [Issue hierarchy](/cms_trial/space/JQLSEARCH/604209353/Issue+hierarchy/) for complete descriptions and examples.

- parentsOfIssuesInQuery()
- parentsOfIssuesInQueryRecursive()
- childrenOfIssuesInQuery()
- childrenOfIssuesInQueryRecursive()

## Epics

See [Epics](/cms_trial/space/JQLSEARCH/604209425/Epics/) for complete descriptions and examples.

- epicsOfChildrenInQuery()
- childrenOfEpicsInQuery()
- issuesInEpicCount
- bugsInEpicCount
- storiesInEpicCount
- issuesInEpicToDoCount
- issuesInEpicInProgressCount
- issuesInEpicDoneCount
- bugsInEpicToDoCount
- bugsInEpicInProgressCount
- bugsInEpicDoneCount
- storiesInEpicToDoCount
- storiesInEpicInProgressCount
- storiesInEpicDoneCount

## Text matches

See [Text matches](/cms_trial/space/JQLSEARCH/604209903/Text+matches/) for complete descriptions and examples.

- exactTextMatch()
- exactTextMatchCaseInsensitive()
- wildcardMatch()
- regex()

## Agile sprints

See [Agile sprints](/cms_trial/space/JQLSEARCH/604209345/Agile+sprints/) for complete descriptions and examples.

- nextSprint()
- previousSprint()
- addedToSprintAfterStart()

## Attachments

See [Attachments](/cms_trial/space/JQLSEARCH/604209221/Attachments/) for complete descriptions and examples.

- attachmentContent
- attachmentsCount
- attachedByUser
- attachedOnDate
- attachmentExtension
- attachmentName

## Subtasks

See [Subtasks](/cms_trial/space/JQLSEARCH/604209285/Subtasks/) for complete descriptions and examples.

- subtasksOfParentsInQuery()
- parentSummary
- parentPriority
- parentIssueType
- parentStatus
- parentStatusCategory

## Issues with subtasks

See [Issues with subtasks](/cms_trial/space/JQLSEARCH/1348927877/Issues+with+subtasks/) for complete descriptions and examples.

- parentsOfSubtasksInQuery()
- subtasksCount
- subtaskSummary
- subtaskKey
- subtaskPriority
- subtaskIssueType
- subtaskStatus
- subtaskStatusCategory

## Comments

See [Comments](/cms_trial/space/JQLSEARCH/604209943/Comments/) for complete descriptions and examples.

- commentsCount
- commentedByUser
- commentLastCreatedBy
- commentLastCreatedOnDate
- commentLastUpdatedBy
- commentLastUpdatedOnDate
- commentedOnDate
- commentUpdatedOnDate

## Versions

See [Versions](/cms_trial/space/JQLSEARCH/604209229/Versions/) for complete descriptions and examples.

- affectedVersionsArchived
- affectedVersionsReleased
- affectedVersionsOpened
- affectedVersionsCount
- affectedVersionReleaseDate
- fixVersionsArchived
- fixVersionsReleased
- fixVersionsOpened
- fixVersionsCount
- fixVersionReleaseDate

## Links

See [issue links](/cms_trial/space/JQLSEARCH/604209269/Issue+links/) for complete descriptions and examples.

- linkedIssuesOfQuery()
- linkedIssuesOfQueryRecursive()
- linksCount
- linkedBy
- linksIssue
- linkType
- linkedIssueStatus
- linkedIssueStatusCategory
- linkedIssueType
- linkedIssuePriority
- linksIssuesCount
- linkedByIssuesCount
- linkedByIssueProject
- linksIssueProject

## Web links

*Formerly called remote links*

See [Web links](/cms_trial/space/JQLSEARCH/604209213/Web+links/) for complete descriptions and examples.

- remoteLinkUrl
- remoteLinkUrlPartialMatch
- remoteLinkApplicationName
- remoteLinkApplicationType
- remoteLinkHost
- remoteLinkQuery
- remoteLinkPath
- remoteLinkTitle
- remoteLinkTitlePartialMatch
- remoteLinkRelationship
- remoteLinksCount

## Issue updates

See [Issue updates](/cms_trial/space/JQLSEARCH/604209933/Issue+updates/) for complete descriptions and examples.

- updatedByUsersCount
- updatedBy
- transitionedBy
- loggedTimeBy
- updatedOnDates
- lastUpdatedBy
- movedProjects
- movedProjectsCount

## Field values

See [Field values](/cms_trial/space/JQLSEARCH/604209909/Field+values/) for complete descriptions and examples.

- dateCompare()
- dateCompareIgnoreTime()
- hasSameUpdatedAndCreatedDate
- hasSameAssigneeAndReporter
- hasSameVersions

## Using dates in JQL

- [Aggregation of dates](/cms_trial/space/JQLSEARCH/604209257/Aggregation+of+dates/)
- [Dates with time](/cms_trial/space/JQLSEARCH/604209245/Dates+with+time/)

## Using standard JQL in Jira Cloud

- [What is Advanced Search](https://support.atlassian.com/jira-software-cloud/docs/what-is-advanced-searching-in-jira-cloud/)
- Standard JQL [functions](https://support.atlassian.com/jira-software-cloud/docs/advanced-search-reference-jql-functions/), [fields](https://support.atlassian.com/jira-software-cloud/docs/advanced-search-reference-jql-fields/), [keywords](https://support.atlassian.com/jira-software-cloud/docs/advanced-search-reference-jql-keywords/), [operators](https://support.atlassian.com/jira-software-cloud/docs/advanced-search-reference-jql-operators/)
- [Development functions](https://support.atlassian.com/jira-software-cloud/docs/advanced-search-reference-jql-developer-status/)
- [Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/advanced-search-reference-jql-fields/) - JSM specific fields and functions, especially around SLA
- [Advanced Roadmaps functions](https://support.atlassian.com/jira-software-cloud/docs/search-for-advanced-roadmaps-custom-fields-in-jql/)