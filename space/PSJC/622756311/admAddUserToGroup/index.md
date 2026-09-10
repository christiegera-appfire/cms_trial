# admAddUserToGroup

## Description

Adds a single user to a group if the user is not already in that group.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddUserToGroup(user, group) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addUserToGroup(user, group) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| User | String | Yes | Username or userkey. |
| Group | String | Yes | Group name. |

## Return Type

**Boolean**

Returns "true" if operation succeeded.

## Example

```javascript
admAddUserToGroup("user.3", "Senior Developers");
```

The look-up is first made after the userkey, then after the username.

## See also