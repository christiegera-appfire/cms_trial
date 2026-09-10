# updateWebLink

## Description

Updates a web link on the issue. If the link struct has no id, updates based on global id

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | updateWebLink(issueKey, remoteLinkStruct) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | string | Yes | Key of the selected issue. |
| remoteLinkStruct | JRemoteIssueLink | Yes | Link structure, including icons and status. |

## Return Type

**integer**

The returned value represents the id of the web link updated.

## Example

```javascript
JRemoteIssueLink ret = getWebLink("TEST-1", 10000);
ret.globalId = "mylink2=https://duckduckgo.com";
ret.url="https://duckduckgo.com";
ret.title="Duck Duck";
updateWebLink("TEST-1", ret);
```

## See also