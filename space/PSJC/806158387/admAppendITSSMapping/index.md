# admAppendITSSMapping

## Description

Adds a mapping into an Issue Type Screen Scheme (ITSS) between an issue type and a screen scheme id

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAppendITSSMapping(issueTypeScreenSchemeId, issueTypeId, screenSchemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | appendITSSMapping(issueTypeScreenSchemeId, issueTypeId, screenSchemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueTypeScreenSchemeId | integer | Yes | The ID of the issue type screen scheme. |
| issueTypeId | integer | Yes | The ID of the issue type. |
| screenSchemeId | integer | Yes | The ID of the screen scheme. |

## Return Type

**boolean**

Returns true if the issue type screen scheme is updated.

## See also