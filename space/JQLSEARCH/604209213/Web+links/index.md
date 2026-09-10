# Web links

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Web links JQL keywords

Web links were called Remote links in previous versions of Jira.

### remoteLinkUrl

Find issues that contain the remote link with the URL.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that contain both URLs.

```text
remoteLinkUrl in ("http://digitaltoucan.com/our-products/jql-search-extensions/", "https://google.com")
```

### remoteLinkUrlPartialMatch

This keyword is similar to `remoteLinkUrl` but supports partial match. All the slashes are replaced with spaces. Word match will differ depending on your [word stemming](https://confluence.atlassian.com/jirasoftwarecloud/search-syntax-for-text-fields-764478343.html#Searchsyntaxfortextfields-stemmingWordstemming) configuration in Jira.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that contain `appfire` in the URL.

```text
remoteLinkUrlPartialMatch ~ appfire
```

### remoteLinkApplicationName

Find issues that contain the remote link to an application, such as Confluence.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that link to Confluence:

```text
remoteLinkApplicationName="Confluence"
```

### remoteLinkApplicationType

It is similar to `remoteLinkApplicationName` but matches the application identifier.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that link to Confluence.

```text
remoteLinkApplicationType="com.atlassian.confluence"
```

### remoteLinkHost

Matches the host part of the remote link.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that link to `jqlsearchextensions.atlassian.net`.

```text
remoteLinkHost="jqlsearchextensions.atlassian.net"
```

### remoteLinkQuery

Matches the query part of the remote link.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that link to URLs, for example, `http://host.com/path?pageId=1234`.

```text
remoteLinkQuery="pageId=1234"
```

### remoteLinkPath

Matches the path part of the remote link.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that link to URLs such as `http://host.com/path?pageId=1234`.

```text
remoteLinkPath="/path"
```

### remoteLinkTitle

Find issues with a remote link title.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues with the title `My Page`.

```text
remoteLinkTitle="My Page"
```

### remoteLinkTitlePartialMatch

Find issues that contain text in the remote link title. Word matches will differ depending on your [word stemming](https://confluence.atlassian.com/jirasoftwarecloud/search-syntax-for-text-fields-764478343.html#Searchsyntaxfortextfields-stemmingWordstemming) configuration in Jira.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that contain `Appfire` in the remote link title.

```text
remoteLinkTitlePartialMatch ~ "Appfire"
```

### remoteLinkRelationship

Find issues with a remote link of a particular type.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues that were mentioned in Confluence.

```text
remoteLinkRelationship="mentioned in"
```

### remoteLinksCount

Find issues that contain a particular number of remote links.

**Supported operators**

| = | != | ~ | !~ | > | >= | < | <= | IS | IS NOT | IN | NOT IN | WAS | WAS IN | WAS NOT | WAS NOT IN | CHANGED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Example**

Find issues with more than 5 remote links.

```text
remoteLinksCount > 5
```