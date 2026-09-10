# Issue links

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Links JQL functions

**JQL functions** are accessible from the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page or via [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in Jira advanced search. When using functions, the issues returned are based on the subquery defined in parentheses.

### linkedIssuesOfQuery()

For a given JQL subquery (content in parentheses) and an optional link type, it finds issues linked to the resulting issues.

`issue in linkedIssuesOfQuery("project=ACME", "is blocked by")` finds issues that my project ACME is blocked by  
`issue in linkedIssuesOfQuery("project=ACME", "blocks")` finds issues that the project ACME blocks  
`issue in linkedIssuesOfQuery("type=Epic AND status='To Do'")` finds issues that are linked in any way with epics that are in progress

### linkedIssuesOfQueryRecursive()

For a given JQL subquery (content in parentheses), it finds issues linked to the resulting issues, and those recursively linked to those issues up to a defined depth, or until no additional linked issues remain. You can set the depth from one to five. If you don’t set a depth, it defaults to five. To refine the results, you can add the link type, for example, `blocks` or `relates to`, using the following syntax: `linkedIssuesOfQueryRecursive("JQL", "linkType", depth)`

**Examples**

Find issues linked to issues with fix version 2.1, to a depth of four.

`issue in linkedIssuesOfQueryRecursive("fixVersion=2.1",4)`

Find issues that *block* the issues in version 2.1 (and issues that block those, recursively).

`issue in linkedIssuesOfQueryRecursive("fixVersion=2.1", "blocks")`

To preserve system performance, the `linkedIssuesOfQueryRecursive()` function is available to use only after the initial indexing process completes.

## Links JQL keywords

### linksCount

Find issues with a particular number of links.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that have links.

```text
linksCount > 0
```

### linkedBy

Find issues that are linked by particular issues.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were linked by JQL-3 or JQL-5.

```text
linkedBy in (JQL-3, JQL-5)
```

### linksIssue

Find issues with links to a particular issue.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that link JQL-3 or JQL-5.

```text
linksIssue in (JQL-3, JQL-5)
```

### linkType

Find issues that have a particular link type.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that are blocked by another issue.

```text
linkType = "is blocked by"
```

### linkedIssueStatus

Find issues that are linked or link issues with a particular status.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find all issues that are linked by issues in the To Do status.

```text
linkedIssueStatus = "To Do"
```

### linkedIssueStatusCategory

Find issues that are linked or link issues with a particular status category.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find all issues that are linked or link issues in the Done status.

```text
linkedIssueStatusCategory = Done
```

### linkedIssueType

Find issues that are linked or link issues with a specific issue type.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find all issues that are linked by bugs.

```text
linkedIssueType = Bug
```

### linkedIssuePriority

Find issues that are linked or link issues with a specific priority.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that are linked to high-priority issues.

```text
linkedIssuePriority = "High" 
```

### linksIssuesCount

Find issues that link to a specific number of issues.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that link more than 5 issues.

```text
linksIssuesCount > 5
```

### linkedByIssuesCount

Find issues that are linked by a specific number of issues.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that are linked by more than 10 issues.

```text
linkedByIssueCount > 10 
```

### linkedByIssueProject

Find issues that are linked by issues from a specific project.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find all issues that are linked by issues from project JQL.

```text
linkedByIssueProject = JQL
```

### linksIssueProject

Find issues that link to issues from a specific project.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find all issues that link to issues from project JQL.

```text
linksIssueProject= JQL
```