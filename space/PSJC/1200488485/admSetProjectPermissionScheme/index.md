# admSetProjectPermissionScheme

## Description

Updates the permission scheme to the given one. Return true if success, false otherwise

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetProjectPermissionScheme(projectKey, schemeName) | **Package** | adm |
| **Alias** | setProjectPermissionScheme | **Pkg Usage** | setProjectPermissionScheme(projectKey, schemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | The project key |
| schemeName | string | Yes | The name of the scheme to be set |

## Return Type

**Boolean (true/false)**

Returns true if the scheme was set and false otherwise.

## Example

```javascript
admSetProjectPermissionScheme("ITSD","Permission sch");
```

## See also