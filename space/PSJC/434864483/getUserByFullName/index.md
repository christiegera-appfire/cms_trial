# getUserByFullName

## Description

Gets the user by full name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getUserByFullName(fullName, [forceIncludeEmail]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fullName | String | Yes | Full name. |
| forceIncludeEmail | boolean | No | Optional boolean flag which, if true, is used to force the extraction of the user's email in the result. |

## Return Type

[**JUser**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the first user found with the specified full name.

## See also