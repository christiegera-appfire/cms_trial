# admAddUserToProjectRole

## Description

Adds a single user to a project role if the user is not already in that role.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddUserToProjectRole(user, project, role) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addUserToProjectRole(user, project, role) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| User | String | Yes | Username or userkey. |
| Project key | String | Yes | Key of the selected project. |
| Role name | String | Yes | Name of the role to add the user to. |

## Return Type

**Boolean**

## Example

```javascript
addUserToProjectRole("user.3", "TEST", "Developers");
```

## See also