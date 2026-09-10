# admGetProjectPermissionScheme

## Description

Returns the name of the permission scheme name for the given project key or id

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetProjectPermissionScheme(projectKeyOrId) | **Package** | adm |
| **Alias** | getProjectPermissionScheme | **Pkg Usage** | projectPermsScheme(projectKeyOrId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKeyOrId | string | Yes | The key or the id of the project |

## Return Type

**string**

Returns the name of the permission scheme for the project.

## Example

```javascript
return admGetProjectPermissionScheme("TEST");
```

Default Permission Scheme

## See also