# getUserByEmail

## Description

Gets the user by email address.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getUserByEmail(email) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| email | String | Yes | Email address. |

## Return Type

[**JUser**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

If there are more users with the same email address, the function does not guarantee that it will always return the same user.

## See also