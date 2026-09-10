# admRemoveUserFromGroup

## Description

Removes a single user from a group if the user is in that group.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admRemoveUserFromGroup(user, group) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | removeUserFromGroup(user, group) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| User | String | Yes | Username or userkey. |
| Group | String | Yes | Name of the group. |

## Return Type

**Boolean**

Returns "true" if operation succeeded.

## Example

```javascript
admRemoveUserFromGroup("user.3", "Senior Developers");
```

The look-up is first made after the userkey, then after the username.

## See also