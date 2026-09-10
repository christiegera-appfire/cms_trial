# getProjectRoleIdByName

## Description

Retrieves the id for the project role with the given name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getProjectRoleIdByName(projectRoleName) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectRoleName | String | Yes | Project role name. |

## Return Type

**Number**

The return value is a number representing the project role id.

## Example

Project role with id "10200" has the name "programmers".

```javascript
return getProjectRoleIdByName("programmers");
```

Result: 10200

## See also