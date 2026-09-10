# admRemoveGroupFromProjectRole

## Description

Removes a single group from a project role if the group is in that role.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admRemoveGroupFromProjectRole(group, project, role) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | removeGroupFromProjectRole(group, project, role) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Group | String | Yes | Group name. |
| Project key | String | Yes | Key of the selected project. |
| Role name | String | Yes | Name of the role to add the user to. |

## Return Type

**Boolean**

Returns "true" if operation succeeded.

## Example

```javascript
removeGroupFromProjectRole("dev-group, "TEST", "Developers");
```

## See also