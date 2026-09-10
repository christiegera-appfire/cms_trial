# admGetIssueTypeScreenScheme

## Description

Creates an Issue Type Screen Scheme (ITSS)

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateIssueTypeScreenScheme(name, description, defaultScreenSchemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createIssueTypeScreenScheme(name, description, defaultScreenSchemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the scheme. |
| description | string | Yes | The description of the scheme. |
| defaultScreenSchemeId | integer | Yes | The ID of the screen scheme to be used as the default screen scheme (i.e. mapping not specified). |

## Return Type

[**JIssueTypeScreenScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an issue type screen scheme.

## See also