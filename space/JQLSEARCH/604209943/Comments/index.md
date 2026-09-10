# Comments

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Comments JQL keywords

### commentsCount

Find issues with a specific number of comments.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues with comments.

```text
commentsCount > 0 
```

### commentedByUser

Search for issues that were commented on by a particular user.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were commented on by Jane Potter.

```text
commentedByUser = "Jane Potter"
```

### commentLastCreatedBy

Search for issues that were last commented on by a particular user.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were last commented on by admin.

```text
commentLastCreatedBy= "admin"
```

### commentLastUpdatedBy

Search for issues with a comment last updated by a particular user.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues with a comment last updated by admin.

```text
commentLastUpdatedBy= "admin"
```

### commentedOnDate

Search for issues that were commented on a particular date. This keyword works with date-related JQL functions:

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

**See also**

- [Note on aggregation of dates](/cms_trial/space/JQLSEARCH/604209257/Aggregation+of+dates/)
- [Note on dates with time](/cms_trial/space/JQLSEARCH/604209245/Dates+with+time/)

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues that were commented on the 13th or 14th of March, 2016.

```text
commentedOnDate >= "2016/03/13" AND commentedOnDate < "2016/03/15"
```

Find issues that were commented on at any time in the past.

```text
commentedOnDate < now()
```

### commentUpdatedOnDate

Search for issues in which a comment was updated on a particular date. This keyword works with date-related JQL functions.

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

**Examples**

Find issues with comments updated on 13th or 14th of March, 2016.

```text
commentUpdatedOnDate >= "2016/03/13" AND commentUpdatedOnDate < "2016/03/15" 
commentUpdatedOnDate < now()
```

### commentLastCreatedOnDate

Search for issues that were last commented on a particular date. This keyword works with date-related JQL functions.

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

**See also**

- [Note on aggregation of dates](/cms_trial/space/JQLSEARCH/604209257/Aggregation+of+dates/)
- [Note on dates with time](/cms_trial/space/JQLSEARCH/604209245/Dates+with+time/)

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were commented on more than 2 days ago.

```text
commentLastCreatedOnDate < -2d
```

### commentLastUpdatedOnDate

Search for issues with comments updated on a particular date. This keyword works with date-related JQL functions.

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

**See also**

- [Note on aggregation of dates](/cms_trial/space/JQLSEARCH/604209257/Aggregation+of+dates/)
- [Note on dates with time](/cms_trial/space/JQLSEARCH/604209245/Dates+with+time/)

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were commented on more than 2 days ago.

```text
commentLastUpdatedOnDate < -2d
```

### userMentionedInComment

Find issues where a specified user is mentioned (@mentioned) in a comment.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues where ‘Kai Clarke’ is mentioned in a comment.

```text
userMentionedInComment = Kai Clark
```

Find issues where the current user is mentioned in a comment.

```text
userMentionedInComment = currentUser()
```

Find issues where specified team members are mentioned recently.

```text
userMentionedInComment in (Kai Clark, Lee Carter) AND commendedOnDate > startOfWeek()
```

### userMentionedInLastComment

Find issues where a specified user is mentioned in the latest comment.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Examples**

Find issues where ‘Kai Clarke’ is mentioned in the last comment.

```text
userMentionedInLastComment = Kai Clark
```

Find issues where the current user is mentioned in the last comment.

```text
userMentionedInLastComment = currentUser()
```