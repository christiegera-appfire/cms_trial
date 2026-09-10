# userLanguage

## Description

Returns the language for an user.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | userLanguage(user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| user | String | Yes | Username or key of the user. |

## Return Type

**String**

The return value represents the language for the specified user.

## Example

```javascript
userLanguage("Administrator");
```

Returns: The language of user Administrator.

The look-up is first made after the userkey, then after the username.

## See also