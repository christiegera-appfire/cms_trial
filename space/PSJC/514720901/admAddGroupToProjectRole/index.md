# admAddGroupToProjectRole

## Description

Adds a single group to a project role if the group is not already in that role.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddGroupToProjectRole(group, project, role) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addGroupToProjectRole(group, project, role) |

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
addGroupToProjectRole("dev-group", "TEST", "Developers");
```

## See also