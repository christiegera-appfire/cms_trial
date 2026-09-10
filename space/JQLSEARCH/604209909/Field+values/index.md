# Field values

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Field value comparisons JQL functions

**JQL functions** are accessible from the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page or [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in Jira advanced search. When using functions, the issues returned are based on the subquery defined in parentheses.

### dateCompare()

Find issues with dates that match an expression.

The expression consists of two date fields connected by a comparison operator: <, <=, >, >=, =. You can add units using +/- m,h,d,w, M, or y to the expression to compare a date to a floating date instead of a fixed date.

**Examples**

```text
issue in dateCompare("duedate < resolved")
```

```text
issue in dateCompare("'Target date' >= 'Start date'")
```

```text
issue in dateCompare(“resolutiondate +1d < duedate +1w”) AND project = DEV
```

### dateCompareIgnoreTime()

Find issues with dates that match an expression. This function considers only the date portion of the timestamps.

The expression consists of two date fields connected by a comparison operator: <, <=, >, >=, =. You can add units using +/- m,h,d,w, M, or y to the expression to compare a date to a floating date instead of a fixed date.

**Examples**

`issue in dateCompareIgnoreTime("duedate < resolved")`

`issue in dateCompareIgnoreTime("'Target date' >= 'Start date'")`

```text
issue in dateCompareIgnoreTime (“resolutiondate +1d < duedate +1w”) AND project = DEV
```

## Field value comparisons JQL keywords

### hasSameUpdatedAndCreatedDate

Search for issues that have not been updated since their creation date.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

```text
hasSameUpdatedAndCreatedDate = "true"
```

### hasSameAssigneeAndReporter

Search for issues with the same assignee and reporter.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

```text
hasSameAssigneeAndReporter = "true"
```

### hasSameVersions

Search for issues with the same fix and affected versions.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

```text
hasSameVersions = "true"
```