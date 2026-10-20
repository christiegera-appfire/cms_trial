# admGetITSSProjects

## Description

Returns the projects that use the Issue Type Screen Scheme (ITSS).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetITSSProjects(issueTypeScreenSchemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getITSSProjects(issueTypeScreenSchemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueTypeScreenSchemeId | integer | Yes | The ID of the issue type screen scheme. |

## Return Type

**string []**

Returns the project keys that are associated with this ITSS.

## See also