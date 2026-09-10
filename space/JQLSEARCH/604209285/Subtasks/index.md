# Subtasks

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Subtasks JQL functions

**JQL functions** are accessible from the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page or [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in Jira advanced search. When using functions, the issues returned are based on the subquery defined in parentheses.

### subtasksOfParentsInQuery()

For a given JQL subquery, it finds subtasks of the resulting parent issues.

**Examples**

`issue in subtasksOfParentsInQuery("status='Done'") and status='To Do'` finds subtasks that are in progress and have finished parents  
`issue in subtasksOfParentsInQuery("assignee=currentUser()")` finds subtasks of my issues

## Subtasks JQL keywords

### parentSummary

Search for subtasks with a parent's summary containing a particular text.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**:

Find subtasks where the parent summary contains the text `Test`.

```text
parentSummary ~ "Test"
```

### parentPriority

Search for subtasks with a parent that has a particular priority.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find subtasks where the parent has the Blocker priority.

```text
parentPriority = Blocker
```

### parentIssueType

Search for subtasks with a parent of a particular issue type.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find subtasks with a parent of issue type "Test".

```text
parentIssueType = "Test"
```

### parentStatus

Search for subtasks with a parent of a particular status.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find subtasks with a parent that is in the In Progress status.

```text
parentStatus = "In Progress"
```

### parentStatusCategory

Search for subtasks with a parent of a particular status.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find subtasks with a parent in the To Do status.

```text
parentStatusCategory= "To Do"
```