# JQL functions reference

 Use this JQL functions reference to learn how to use the advanced search functions provided by **JQL Search Extensions**. This page explains the available functions, their syntax, and example queries to find Jira issues by project, field, attachment, comment, version, link, update, and other issue details.

The instructions on this page describe how to use the functions from [JQL Search Extensions](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira-the-jql-extensions?hosting=datacenter&tab=overview).

JQL Search Extensions are accessed from Jira’s [Advanced search](https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-939938733.html).

## Projects

### **movedIssues(projectKey)**

Finds issues which moved from the project in argument. For instance:

```text
project = SEARCHSERVER AND issue in movedIssues("SEARCHCLOUD")
```

Will find all issues which are in project SEARCHSERVER and moved from project SEARCHCLOUD.

## Fields

### **fieldMatch(jql-subquery, field-name, regexp)**

FieldMatch can be used to find issues with field matching the regular expression in the argument. For instance:

```text
issue in fieldMatch("project = SEARCH", "description", "find issues mat*")
```

Will find all issues with description field matching the regular expression `find issues mat*`.

The `asterisk *` matches any alphanumeric characters. It is also possible to use all regular expression constructs, such as

```text
issue in fieldMatch("project = SEARCH", "description", "find issu[a-z]{2} mat*") 
issue in fieldMatch("project = SEARCH", "my custom field", "f[a-z]{5}
```

This function can be used with any system or custom field.

For documentation of of regular expression constructs, refer to the [documentation](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) from Oracle.

### **fieldsHaveSameValue(jql-subquery, field-name1, field-name2,...,field-name-x)**

FieldsHaveSameValue can be used to find issues with fields having the same value. For instance:

```text
issue in fieldsHaveSameValue("version", "my-custom-field-with-version")
```

It is possible to use multiple fields in the expression, such as below:

```text
issue in fieldsHaveSameValue("version", "my-custom-field-with-version", "one-more-field-with-version")
```

It is also possible to add JQL subquery to the expression. It will narrow the search only to those issues which match the subquery (in the example below, are in the project DEMO and have the same value of fields version and my-custom-field-with-version).

```text
issue in fieldsHaveSameValue("project = SEARCH", "version", "my-custom-field-with-version")
```

In case fields contain multiple values (for instance, there are many values of field version) the function will expect all values to be equal (but doesn't expect the same order).

## Attachments

### **AttachedAfter**

AttachedAfter can be used to find issues with attachments added after particular date. Expected date format is yyyy-MM-dd (year dash month dash day of the month) or dd-MM-YYYY

```text
issue in attachedAfter("2018-05-26")
```

### **AttachedBefore**

AttachedBefore can be used to find issues with attachments added before particular date. Expected date format is yyyy-MM-dd (year dash month dash day of the month) or dd-MM-YYYY

```text
issue in attachedBefore("2018-05-26")
```

### **AttachedBetween**

AttachedBetween can be used to find issues with attachments added between particular dates. Expected date format is yyyy-MM-dd (year dash month dash day of the month) or dd-MM-YYYY

```text
issue in attachedBetween("2018-05-26", "2018-07-01")
```

### **AttachedOnDate**

AttachedOnDate can be used to find issues with attachments added on particular dates. Expected date format is yyyy-MM-dd (year dash month dash day of the month) or dd-MM-YYYY

```text
issue in attachedOnDate("2018-05-26")
```

### **AttachedByUser**

AttachedByUser can be used to find issues with attachments added by a particular user (username is expected)

```text
issue in attachedByUser("filip")
```

This function can be used together with membersOf to find issues attached by users who are members of a particular group.

```text
issue in attachedByUser("membersOf(employees)")
```

### **AttachmentExtension**

AttachmentExtension can be used to find issues with attachments with particular extension.

```text
issue in attachmentExtension("pdf")
```

### **AttachmentName**

AttachmentName can used to find issues with attachments with particular name.

```text
issue in attachedName("documentation")
```

### **AttachmentsCountEqualTo**

AttachmentsCountEqualTo can be used to find issues with particular number of attachments.

```text
issue in attachmentsCountEqualTo(2)
```

### **AttachmentsCountGreaterThan**

AttachmentsCountGreaterThan can be used to find issues with number of attachments greater than provided number

```text
issue in attachmentsCountGreaterThan(1)
```

### **AttachmentsCountLessThan**

AttachmentsCountLessThan can be used to find issues with number of attachments lesser than provided number

```text
issue in attachmentsCountLessThan(2)
```

## Comments

### **CommentedAfter**

CommentedAfter can be used to find issues with comments added after particular date. Expected date format is yyyy-MM-dd (year dash month dash day of the month) or dd-MM-YYYY

```text
issue in commentedAfter("2018-05-26")
```

### **CommentedBefore**

CommentedBefore can be used to find issues with comments added before particular date. Expected date format is yyyy-MM-dd (year dash month dash day of the month) or dd-MM-YYYY

```text
issue in commentedBefore("2018-05-26")
```

### **CommentedBetween**

CommentedBetween can be used to find issues with comments added between particular dates. Expected date format is yyyy-MM-dd (year dash month dash day of the month) or dd-MM-YYYY

```text
issue in commentedBetween("2018-05-26", "2018-07-01")
```

### **CommentedOnDate**

CommentedOnDate can be used to find issues with comments added on particular dates. Expected date format is yyyy-MM-dd (year dash month dash day of the month) or dd-MM-YYYY

```text
issue in commentedOnDate("2018-05-26")
```

### **CommentedByUser**

CommentedByUser can be used to find issues with comments added by a particular user (username is expected)

```text
issue in commentedByUser("filip")
```

This function can be used together with membersOf to find issues commented by users who are members of a particular group.

```text
issue in commentedByUser("membersOf(employees)")
```

### **CommentsCountEqualTo**

CommentsCountEqualTo can be used to find issues with particular number of comments.

```text
issue in commentsCountEqualTo(2)
```

### **CommentsCountGreaterThan**

CommentsCountGreaterThan can be used to find issues with number of comments greater than provided number

```text
issue in commentsCountGreaterThan(2)
```

### **CommentsCountLessThan**

CommentsCountLessThan can be used to find issues with number of comments lesser than provided number

```text
issue in commentsCountLessThan(2)
```

## Versions

### **AffectedVersionsArchivedCountLessThan**

### **FixVersionsArchivedCountLessThan**

AffectedVersionsArchivedCountLessThan and FixVersionsArchivedCountLessThan can be used to find issues with number of archived versions less than provided number.

```text
issue in affectedVersionsArchivedCountLessThan(2) OR issue in fixVersionsArchivedCountLessThan(2)
```

### **AffectedVersionsArchivedCountEqualTo**

### **FixVersionsArchivedCountEqualTo**

AffectedVersionsArchivedCountEqualTo and FixVersionsArchivedCountEqualTo can be used to find issues with number of archived versions equal to provided number.

```text
issue in affectedVersionsArchivedCountEqualTo(2) OR issue in fixVersionsArchivedCountEqualTo(2)
```

### **AffectedVersionsArchivedCountGreaterThan**

### **FixVersionsArchivedCountGreaterThan**

AffectedVersionsArchivedCountGreaterThan and FixVersionsArchivedCountGreaterThan can be used to find issues with number of archived versions greater than provided number.

```text
issue in affectedVersionsArchivedCountGreaterThan(2) OR issue in fixVersionsArchivedCountGreaterThan(2)
```

### **AffectedVersionsCountLessThan**

### **FixVersionsCountLessThan**

AffectedVersionsCountLessThan and FixVersionsCountLessThan can be used to find issues with number of versions less than provided number.

```text
issue in affectedVersionsCountLessThan(2) OR issue in fixVersionsCountLessThan(2)
```

### **AffectedVersionsCountEqualTo**

### **FixVersionsCountEqualTo**

AffectedVersionsCountEqualTo and FixVersionsCountEqualTo can be used to find issues with number of versions equal to provided number.

```text
issue in affectedVersionsCountEqualTo(2) OR issue in fixVersionsCountEqualTo(2)
```

### **AffectedVersionsCountGreaterThan**

### **FixVersionsCountGreaterThan**

AffectedVersionsCountGreaterThan and FixVersionsCountGreaterThan can be used to find issues with number of versions greater than provided number.

```text
issue in affectedVersionsCountGreaterThan(2) OR issue in fixVersionsCountGreaterThan(2)
```

### **AffectedVersionsOpenedCountLessThan**

### **FixVersionsOpenedCountLessThan**

AffectedVersionsOpenedCountLessThan and FixVersionsOpenedCountLessThan can be used to find issues with number of opened versions less than provided number.

```text
issue in affectedVersionsOpenedCountLessThan(2) OR issue in fixVersionsOpenedCountLessThan(2)
```

### **AffectedVersionsOpenedCountEqualTo**

### **FixVersionsOpenedCountEqualTo**

AffectedVersionsOpenedCountEqualTo and FixVersionsOpenedCountEqualTo can be used to find issues with number of opened versions equal to provided number.

```text
issue in affectedVersionsOpenedCountEqualTo(2) OR issue in fixVersionsOpenedCountEqualTo(2)
```

### **AffectedVersionsOpenedCountGreaterThan**

### **FixVersionsOpenedCountGreaterThan**

AffectedVersionsOpenedCountGreaterThan and FixVersionsOpenedCountGreaterThan can be used to find issues with number of opened versions greater than provided number.

```text
issue in affectedVersionsOpenedCountGreaterThan(2) OR issue in fixVersionsOpenedCountGreaterThan(2)
```

### **AffectedVersionsReleasedCountLessThan**

### **FixVersionsReleasedCountLessThan**

AffectedVersionsReleasedCountLessThan and FixVersionsReleasedCountLessThan can be used to find issues with number of released versions less than provided number.

```text
issue in affectedVersionsReleasedCountLessThan(2) OR issue in fixVersionsReleasedCountLessThan(2)
```

### **AffectedVersionsReleasedCountEqualTo**

### **FixVersionsReleasedCountEqualTo**

AffectedVersionsReleasedCountEqualTo and FixVersionsReleasedCountEqualTo can be used to find issues with number of released versions equal to provided number.

```text
issue in affectedVersionsReleasedCountEqualTo(2) OR issue in fixVersionsReleasedCountEqualTo(2)
```

### **AffectedVersionsReleasedCountGreaterThan**

### **FixVersionsReleasedCountGreaterThan**

AffectedVersionsReleasedCountGreaterThan and FixVersionsReleasedCountGreaterThan can be used to find issues with number of released versions greater than provided number.

```text
issue in affectedVersionsReleasedCountGreaterThan(2) OR issue in fixVersionsReleasedCountGreaterThan(2)
```

### **FixVersionReleasedOnDate**

### **AffectedVersionReleasedOnDate**

FixVersionReleasedOnDate and AffectedVersionReleasedOnDate can be used to find issues with versions released on particular date.

```text
issue in fixVersionReleasedOnDate("2018-05-26") OR issue in affectedVersionReleasedOnDate("2018-05-26")
```

### **FixVersionReleasedBetweenDates**

### **AffectedVersionReleasedBetweenDates**

FixVersionReleasedBetweenDates and AffectedVersionReleasedBetweenDates can be used to find issues with versions released between provided dates.

```text
issue in fixVersionReleasedBetweenDates("2018-05-26", "2018-07-01") OR issue in affectedVersionReleasedBetweenDates("2018-05-26", "2018-07-01")
```

### **FixVersionReleasedAfterDate**

### **AffectedVersionReleasedAfterDate**

FixVersionReleasedAfterDate and AffectedVersionReleasedAfterDate can be used to find issues with versions released after particular date.

```text
issue in fixVersionReleasedAfterDate("2018-05-26") OR issue in affectedVersionReleasedAfterDate("2018-05-26")
```

### **FixVersionReleasedBeforeDate**

### **AffectedVersionReleasedBeforeDate**

FixVersionReleasedBeforeDate and AffectedVersionReleasedBeforeDate can be used to find issues with versions released before particular date.

```text
issue in fixVersionReleasedBeforeDate("2018-05-26") OR issue in affectedVersionReleasedBeforeDate("2018-05-26")
```

### **LatestReleaseVersionForProject**

LatestReleaseVersionForProject can be used to find issues with versions which are the most recently released version for the project.

```text
fixVersion in latestReleaseVersionForProject("SEARCH")
```

## Links

### **LinksCountLessThan**

LinksCountLessThan can be used to find issues with number of links less than provided number.

```text
issue in linksCountLessThan(2)
```

### **LinksCountGreaterThan**

LinksCountGreaterThan can be used to find issues with number of links greater than provided number.

```text
issue in linksCountGreaterThan(2)
```

### **LinksCountEqualTo**

LinksCountEqualTo can be used to find issues with number of links equal to the provided number.

```text
issue in linksCountEqualTo(2)
```

### **LinkedBy([linktype], jql-query or issuekeys)**

Search for issues that are linked by given issues or by issues matched by the given JQL. Link type can be provided to limit the search to particular link type or types. Many link types can be specified in a single function call.

The first optional list of arguments specifies link types. They are followed by either JQL or a list of issue keys.

**EXAMPLES**

Find issues which are linked by JQL-3 or JQL-5.

```text
issue in linkedBy(JQL-3, JQL-5)
```

Find issues which are linked by issues from project JQL with priority = Highest.

```text
issue in linkedBy("project = JQL AND priority = Highest")
```

Find issues which are blocked by issue JQL-3 or JQL-5.

```text
issue in linkedBy("is blocked by", "JQL-3", JQL-5)
```

Find issues which are blocked by issues from project JQL with priority = Highest.

```text
issue in linkedBy("is blocked by", "is related to", "project = JQL AND priority = Highest")
```

### **Links(jql-query, link type)**

Search for issues which links issues matched by JQL. Link type can be provided to limit the search to particular link type or types. Many link types can be specified in single function call.

**EXAMPLES**

Find issues which link at least one issue from project JQL.

```text
issue in links("project = JQL")
```

**EXAMPLES**

Find issues which "blocks" at least one issue from project JQL.

```text
issue in links("blocks", "project = JQL")
```

### **LinksIssue**

Search for issues which links a particular issue.

**EXAMPLES**

Find issues which link JQL-3 or JQL-5

```text
issue in linksIssue(JQL-3, JQL-5)
```

### **LinkType**

Search for issues which have a particular link type.

**EXAMPLES**

Find all issues which are blocked by another issue

```text
issue in linkType("is blocked by")
```

### **LinkedIssueStatus**

Search for issues which are linked or link issues with a particular status.

**EXAMPLES**

Find all issues which are linked by issues in "To Do" status.

```text
issue in linkedIssueStatus("To Do")
```

### **LinkedIssueStatusCategory**

Search for issues which are linked or link issues with a particular status category.

**EXAMPLES**

Find all issues which are linked or link issues in status category "Done"

```text
issue in linkedIssueStatusCategory("Done")
```

### **LinkedIssueType**

Search for issues which are linked or link issue with a particular issue type.

**EXAMPLES**

Find all issues which are linked by Bugs.

```text
issue in linkedIssueType("Bug")
```

### **LinkedIssuePriority**

Search for issues which are linked or links issues with a particular priority.

**EXAMPLES**

Find all issues which are linked by "blockers"

```text
issue in linkedIssuePriority("Blocker")
```

### **LinkedByIssueProject**

Search for issues which are linked or links issues from a particular project.

**EXAMPLES**

Find all issues which are linked or links project JQL

```text
issue in linkedByIssueProject("JQL")
```

## Updated

### **UpdatedByUserCountLessThan**

UpdatedByUserCountLessThan can be used to find issues updated by less than provided number of users.

```text
issue in updatedByUserCountLessThan(2)
```

### **UpdatedByUserCountGreaterThan**

UpdatedByUserCountGreaterThan can be used to find issues updated by greater than provided number of users.

```text
issue in updatedByUserCountGreaterThan(2)
```

### **UpdatedByUserCountEqualTo**

UpdatedByUserCountEqualTo can be used to find issues updated by particular number of users.

```text
issue in updatedByUserCountEqualTo(2)
```

### **UpdatedByUser**

Search for issues which were updated by a particular user/users.

**EXAMPLES**

Find issues which were updated by Helen or Daniel:

```text
issue in updatedByUser("helen", "daniel")
issue in updatedByUser("membersOf(employees)")
```

### **TransitionedByUser**

Search for issues which were transitioned by a particular user/users.

**EXAMPLES**

Find issues which were transitioned by Helen or Daniel:

```text
issue in transitionedBy in ("daniel", "helen")
issue in transitionedBy("membersOf(employees)")
```

### **LoggedTimeByUser**

Search for issues on which particular users reported time.

**EXAMPLES**

Find issues on which Helen or Daniel reported time.

```text
issue in loggedTimeByUser("daniel", "helen")
issue in loggedTimeByUser("membersOf(employees)"
```

## Subtasks

### **SubTaskOf(jql-query)**

Search for subtasks of issues matching JQL.

**EXAMPLES**  
Find subtasks of parents with priority = Blocker.

```text
issue in subtaskOf("priority = Blocker")
```

### **ParentOf(jql-query)**

Search for parents of issues matching JQL.

**EXAMPLES**

Find parents of subtasks with issue type = Bug.

```text
issue in parentOf("issueType = Bug")
```

### **SubtaskCountLessThan**

SubtaskCountGreaterThan can be used to find issues with number of subtasks lesser than provided number.

```text
issue in subtaskCountLessThan(2)
```

### **SubtaskCountGreaterThan**

SubtaskCountGreaterThan can be used to find issues with number of subtasks greater than provided number.

```text
issue in subtaskCountGreaterThan(2)
```

### **SubtaskCountEqualTo**

SubtaskCountEqualTo can be used to find issues with a particular number of subtasks.

```text
issue in subtaskCountEqualTo(2)
```

### **SubTaskKey**

Search for issues that have subtasks with a particular key.

**EXAMPLES**

Find issues with subtask with key ABC-123

```text
issue in subtaskKey("ABC-123")
```

### **SubtaskPriority**

Search for issues that have subtasks with a particular [Priority](https://confluence.atlassian.com/jira/what-is-an-issue-270829373.html).

**EXAMPLES**

Find issues with subtasks which have a "Blocker" priority.

```text
issue in subTaskPriority("Blocker")
```

### **SubTaskType**

Search for issues that have subtasks with a particular [Issue Type](https://confluence.atlassian.com/jira/what-is-an-issue-270829373.html).

**EXAMPLES**

Find issues which have "Test" issue type.

```text
issue in subTaskType("Test")
```

### **SubTaskStatus**

Search for issues that have subtasks with a particular [Status](https://confluence.atlassian.com/jira/what-is-an-issue-270829373.html).

**EXAMPLES**

Find issues which have subtasks "In Progress".

```text
issue in subTaskStatus("In Progress")
```

### **SubTaskStatusCategory**

Search for issues that have subtasks with a particular [Status Category](https://confluence.atlassian.com/adminjiraserver070/defining-status-field-values-749382903.html).

**EXAMPLES**

Find issues which have "To Do" status category.

```text
issue in subTaskStatusCategory("To Do")
```

## Software Development

### **OpenPullRequestsCount**

Search for issues that have particular number of open pull requests. This value is present if JIRA is connected to Bitbucket.

**SUPPORTED OPERATORS**

| **=** | **!=** | **~** | **!~** | **>** | **>=** | **<** | **<=** | **IS** | **IS NOT** | **IN** | **NOT IN** | **WAS** | **WAS IN** | **WAS NOT** | **WAS NOT IN** | **CHANGED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**EXAMPLES**

Find issues with open pull requests.

```text
openPullRequestsCount > 0
```

### **CommitsCount**

Search for issues that have particular number of commits. This value is present if JIRA is connected to Bitbucket or Crucible/Fisheye.

**SUPPORTED OPERATORS**

| **=** | **!=** | **~** | **!~** | **>** | **>=** | **<** | **<=** | **IS** | **IS NOT** | **IN** | **NOT IN** | **WAS** | **WAS IN** | **WAS NOT** | **WAS NOT IN** | **CHANGED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**EXAMPLES**

Find issues with commits.

```text
commitsCount > 0
```

### **FailingBuildsCount**

Search for issues that have particular number of failed builds. This value is present if JIRA is connected to Bamboo.

**SUPPORTED OPERATORS**

| **=** | **!=** | **~** | **!~** | **>** | **>=** | **<** | **<=** | **IS** | **IS NOT** | **IN** | **NOT IN** | **WAS** | **WAS IN** | **WAS NOT** | **WAS NOT IN** | **CHANGED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**EXAMPLES**

Find issues with failing builds.

```text
failingBuildsCount > 0
```

### **OpenReviewsCount**

Search for issues that have particular number of open reviews. This value is present if JIRA is connected to Bitbucket or Crucible/Fisheye.

**SUPPORTED OPERATORS**

| **=** | **!=** | **~** | **!~** | **>** | **>=** | **<** | **<=** | **IS** | **IS NOT** | **IN** | **NOT IN** | **WAS** | **WAS IN** | **WAS NOT** | **WAS NOT IN** | **CHANGED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**EXAMPLES**

Find issues with failing builds.

```text
openReviewsCount > 0
```

### **PullRequestsCount**

Search for issues that have particular number of pull requests. This value is present if JIRA is connected to Bitbucket.

**SUPPORTED OPERATORS**

| **=** | **!=** | **~** | **!~** | **>** | **>=** | **<** | **<=** | **IS** | **IS NOT** | **IN** | **NOT IN** | **WAS** | **WAS IN** | **WAS NOT** | **WAS NOT IN** | **CHANGED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**EXAMPLES**

Find issues with pull requests.

```text
pullRequestsCount > 0
```

### **ReviewsCount**

Search for issues that have particular number of reviews. This value is present if JIRA is connected to Bitbucket or Crucible/Fisheye.

**SUPPORTED OPERATORS**

| **=** | **!=** | **~** | **!~** | **>** | **>=** | **<** | **<=** | **IS** | **IS NOT** | **IN** | **NOT IN** | **WAS** | **WAS IN** | **WAS NOT** | **WAS NOT IN** | **CHANGED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**EXAMPLES**

Find issues with pull requests.

```text
reviewsCount > 0
```

## Issue hierarchy

### **AllIssuesInEpic(jql-query or issuekey)**

Search for all epics, issues in epics and subtasks of these issues.

**SUPPORTED OPERATORS**

| **=** | **!=** | **~** | **!~** | **>** | **>=** | **<** | **<=** | **IS** | **IS NOT** | **IN** | **NOT IN** | **WAS** | **WAS IN** | **WAS NOT** | **WAS NOT IN** | **CHANGED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**EXAMPLES**

Find issues and subtasks of epic "SEARCH-12"

```text
issue in allIssuesInEpic(SEARCH-12)
```

Find issues and subtasks of epics "SEARCH-12, SEARCH-13"

```text
issue in allIssuesInEpic(SEARCH-12, SEARCH-13)
```

Find issues and subtasks of epics and issues for fixVersion = 1.0 in project SEARCH

```text
issue in allIssuesInEpic("fixVersion = 1.0 AND project = SEARCH")
```

### **EpicOf(jql-query)**

Find all epics which have issues matching JQL query.

**SUPPORTED OPERATORS**

| **=** | **!=** | **~** | **!~** | **>** | **>=** | **<** | **<=** | **IS** | **IS NOT** | **IN** | **NOT IN** | **WAS** | **WAS IN** | **WAS NOT** | **WAS NOT IN** | **CHANGED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**EXAMPLES**

Find all epics with unresolved, high-priority stories

```text
issue in epicOf("issuetype = Story and resolution is empty and priority = High")
```

Find all epics for the fixVersion 1.0 in project SEARCH

```text
issue in epicOf("fixVersion = 1.0 and project = SEARCH")
```

## User

### **UserMatch(regular-expression)**

UserMatch can be used to find issues with user fields matching the regular expression in the argument. For instance:

```text
assignee in userMatch("danie*")
```

Will find all issues with assignee username matching the regular expression danie\*, such as daniel, danied, danie3 etc.

The asterisk **'\*'** matches any alphanumeric characters. It is also possible to use all regular expression constructs, such as

```text
assignee in userMatch("danie[a-z]") // matching danie followed by a single lowercase alphabet character
assignee in userMatch("dan[a-z]{3}") // matching dan followed by three lowercase alphabet characters
```

This function can be used for any user field. For documentation of regular expression constructs, please follow [this link](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html)

Write a comment…