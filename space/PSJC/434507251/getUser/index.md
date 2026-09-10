# getUser

## Description

Gets the user by account id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getUser(accountId, [forceIncludeEmail]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| accountId | String | Yes | The account id of the user that needs to be retrieved. |
| forceIncludeEmail | boolean | No | Optional boolean flag which, if true, is used to force the extraction of the user's email in the result. |

## Return Type

[**JUser**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the user.

## Example

```javascript
JUser usr = getUser("john.doe");
```

## See also