# admRemoveITSSMapping

## Description

Assigns an Issue Type Screen Scheme (ITSS) to a project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAssignITSSToProject(issueTypeScreenSchemeId, projectKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | assignITSSToProject(issueTypeScreenSchemeId, projectKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueTypeScreenSchemeId | integer | Yes | The ID of the issue type screen scheme. |
| projectKey | string | Yes | The project key |

## Return Type

**boolean**

Returns true if the issue type screen scheme is assigned to that project.

## See also