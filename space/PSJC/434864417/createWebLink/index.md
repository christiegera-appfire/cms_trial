# createWebLink

## Description

Creates a web link on the issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createWebLink(issueKey, url, title) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | Key of the selected issue. |
| url | String | Yes | URL of the link. |
| title | String | Yes | Name/title of the link as it should appear on the issue. |

## Return Type

**None**

The returned value has no meaning.

## Example

```javascript
createWebLink(key, "http://www.google.com", "Super-duper search");
```

## See also