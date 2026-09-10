# Issues with subtasks

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Issues with subtasks JQL functions

**JQL functions** are accessible from the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page or [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in Jira advanced search. When using functions, the issues returned are based on the subquery defined in parentheses.

### parentsOfSubtasksInQuery()

For a given JQL subquery, it finds the parents of the resulting subtasks.

**Examples**

`issue in parentsOfSubtasksInQuery("status='To Do'") and status='Done'` finds finished issues that have unfinished subtasks  
`issue in parentsOfSubtasksInQuery("assignee=currentUser()")` finds parents of my subtasksSubtasks JQL keywords

## Issues with subtasks JQL keywords

### subtasksCount

Search for issues that have a particular number of subtasks.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with subtasks.

```text
subtasksCount > 0 
```

### subtaskSummary

Search for issues that have subtasks where the summary contains particular text.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**:

Find issues in which the subtask summary contains the text `Test`.

```text
subtaskSummary ~ "Test"
```

### subtaskKey

Search for issues that have subtasks with a particular key.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with a subtask with key ABC-123.

```text
subtaskKey = ABC-123
```

### subtaskPriority

Search for issues that have subtasks with a particular priority.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with subtasks that have a Blocker priority.

```text
subtaskPriority = Blocker
```

### subtaskIssueType

Search for issues that have subtasks with a particular issue type.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues with subtasks with the issue type Spike.

```text
subtaskIssueType = Spike
```

### subtaskStatus

Search for issues that have subtasks with a particular status.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues that have subtasks in progress.

```text
subtaskStatus = "In Progress"
```

### subtaskStatusCategory

Search for issues that have subtasks with a particular status category.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues that have subtasks in the To Do status.

```text
subtaskStatusCategory = "To Do"
```