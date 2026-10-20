# admGetITSSMappings

## Description

Gets the mappings between the screen schemes and issue types for an Issue Type Screen Scheme (ITSS)

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetITSSMappings(issueTypeScreenSchemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getITSSMappings(issueTypeScreenSchemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueTypeScreenSchemeId | integer | Yes | The ID of the issue type screen scheme. |

## Return Type

[**JIssueTypeScreenMapping []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Array of mappings between the issue type id and screen scheme id. If the issue type is zero (0) it's the default mapping

## See also