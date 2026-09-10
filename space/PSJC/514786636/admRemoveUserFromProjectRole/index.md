# admRemoveUserFromProjectRole

## Description

Removes a single user from a project role if the user is in that role.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admRemoveUserFromProjectRole(user, project, role) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | removeUserFromProjectRole(user, project, role) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| User | String | Yes | Username or userkey. |
| Project key | String | Yes | Key of the selected project. |
| Role name | String | Yes | Name of the role to add the user to. |

## Return Type

**Boolean**

Returns "true" if operation succeeded.

## Example

```javascript
removeUserFromProjectRole("user.3", "TEST", "Developers");
```

The look-up is first made after the userkey, then after the username.

## See also