# isUserInRole

## Description

Returns "true" if the user has a certain role on the specified project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isUserInRole(user,project, role) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| User | String | Yes | Username or userkey of the user in question. |
| Project key | String | Yes | Key of the selected project. |
| Role name | String | Yes | Name of the role that is verified. |

## Return Type

**Boolean**

Returns "true" if the user has the role on a project and "false" otherwise.

## Example

```javascript
return isUserInRole("mike", "PRJ", "Developers");
```

The look-up is first made after the userkey, then after the username.

## See also