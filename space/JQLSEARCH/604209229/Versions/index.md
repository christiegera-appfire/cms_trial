# Versions

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Versions JQL keywords

### affectedVersionsArchived

Find issues with [affected version archived](https://confluence.atlassian.com/jira/managing-versions-185729543.html).

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues which affected version is archived.

```text
affectedVersionsArchived > 0
```

### affectedVersionsReleased

Find issues with [affected version released](https://confluence.atlassian.com/jira/managing-versions-185729543.html).

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues which affected version is released.

```text
affectedVersionsReleased > 0
```

Find issues in which no affected version is released.

```text
affectedVersionsReleased = 0
```

### affectedVersionsOpened

Find issues with [affected version opened](https://confluence.atlassian.com/jira/managing-versions-185729543.html).

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues which affected version is opened.

```text
affectedVersionsOpened > 0
```

### affectedVersionsCount

Find issues with a particular number of [affected versions](https://confluence.atlassian.com/jira/managing-versions-185729543.html).

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that have affected versions.

```text
affectedVersionsCount > 0
```

### affectedVersionReleaseDate

Search for issues which affected version was released on a particular date. This keyword works with date-related JQL functions:

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

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues which affected version was released on the 13th or 14th of March, 2016.

```text
affectedVersionReleaseDate = "2016/03/14" OR affectedVersionReleaseDate = "2016/03/13" 
affectedVersionReleaseDate in ("2016/03/14", "2016/03/13") 
affectedVersionReleaseDate < now()
```

### fixVersionsArchived

Find issues with [fix version archived](https://confluence.atlassian.com/jira/managing-versions-185729543.html).

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues which affected version is archived.

```text
fixVersionsArchived > 0
```

### fixVersionsReleased

Find issues with [fix version released](https://confluence.atlassian.com/jira/managing-versions-185729543.html).

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues which fix version is released.

```text
fixVersionsReleased > 0
```

Find issues with no fix version released.

```text
fixVersionsReleased = 0
```

### fixVersionsOpened

Search for issues with [fix version opened](https://confluence.atlassian.com/jira/managing-versions-185729543.html).

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues with fix version opened.

```text
fixVersionsOpened > 0
```

### fixVersionsCount

Find issues with a particular number of [fix versions](https://confluence.atlassian.com/jira/managing-versions-185729543.html).

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that have fix versions.

```text
fixVersionsCount > 0
```

### fixVersionReleaseDate

Search for issues which fix version was released on a particular date. This keyword works with date-related JQL functions:

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

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues which fix version was released on the 13th or 14th of March, 2016.

```text
fixVersionReleaseDate = "2016/03/14" OR fixVersionReleaseDate = "2016/03/13" 
fixVersionReleaseDate in ("2016/03/14", "2016/03/13")
fixVersionReleaseDate < now()
```