# admUpdateITSSDefaultScreenScheme

## Description

Updates an Issue Type Screen Scheme (ITSS), default screen scheme

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateITSSDefaultScreenScheme(issueTypeScreenSchemeId, defaultScreenSchemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updateITSSDefaultScreenScheme(issueTypeScreenSchemeId, defaultScreenSchemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueTypeScreenSchemeId | integer | Yes | The ID of the issue type screen scheme. |
| defaultScreenSchemeId | string | Yes | The ID of the screen scheme to be used as the default screen scheme (i.e. mapping not specified) |

## Return Type

[**JIssueTypeScreenScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an issue type screen scheme.

## See also