# Issue updates

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Issue Updates JQL keywords

### updatedByUsersCount

Search for issues that were updated by a particular number of users.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues updated by more than 5 users.

```text
updatedByUsersCount > 5
```

### updatedBy

Search for issues that were updated by a particular user/users.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were updated by Helen or Daniel.

```text
updatedBy in ("helen", "daniel")
```

### transitionedBy

Search for issues that were transitioned by a particular user/users.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were transitioned by Helen or Daniel.

```text
transitionedBy in ("daniel", "helen")
```

### loggedTimeBy

Search for issues on which particular users reported time.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues on which Helen or Daniel reported time.

```text
loggedTimeBy in ("daniel", "helen")
```

### updatedOnDates

Search for issues that were updated on a particular date. This keyword works with date-related JQL functions:

- endOfDay()
- endOfMonth()
- endOfWeek()
- endOfYear()
- lastLogin()
- now()
- startOfDay()
- startOfMonth()
- startOfWeek()
- startOfYear()

**Also see**

- [Note on aggregation of dates](/cms_trial/space/JQLSEARCH/604209257/Aggregation+of+dates/)
- [Note on dates with time](/cms_trial/space/JQLSEARCH/604209245/Dates+with+time/)

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were updated between midnight 1 June and midnight 2 June.

```text
updatedOnDates>="2020/06/01" AND updatedOnDates<"2020/06/02" 
updatedOnDates < now()
```

### lastUpdatedBy

Search for issues that were last updated by a particular user.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were last updated by admin.

```text
lastUpdatedBy="admin"
```

### movedProjects

Search for issues that were moved between projects.

From September 30, 2024 , `movedProjects` is not supported for new customers. The keyword will not be indexed, and using it in a query will not return and issue. Customers who installed the app prior to this date are not affected by this change. See the [deprecation notice](/cms_trial/space/JQLSEARCH/1243480091/Deprecation+notices+2024/) to learn more.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that belonged to a different project and were moved. For instance, the following query finds issues that were in projects SEARCH and DATA.

```text
movedProjects in ("SEARCH", "DATA")
```

Due to a Jira system limitation, it is impossible to build a command that supports searching from/to. The query will find all issues that were in SEARCH or DATA at some point.

### movedProjectsCount

Search for issues that were moved between a number of projects.

From September 30, 2024 , `movedProjectsCount` is not available to new customers. The keyword will not be indexed, and using it in a query will not return and issue. Customers who installed the app prior to this date are not affected by this change. See the [deprecation notice](/cms_trial/space/JQLSEARCH/1243480091/Deprecation+notices+2024/) to learn more.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were moved between 2 or more projects.

```text
movedProjectsCount >= 2 
```