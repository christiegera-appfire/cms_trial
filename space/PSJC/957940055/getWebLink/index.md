# getWebLink

## Description

Gets a web link structure.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWebLink(issueKey, linkId) or getWebLink(issueKey, globalId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | string | Yes | Key of the selected issue. |
| linkId | integer | Yes | the id of the remote web link. |

### Or

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | string | Yes | Key of the selected issue. |
| globalId | string | Yes | the global id of the remote web link. |

## Return Type

[**JRemoteIssueLink**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

The returned value is the full structure of the link

## See also