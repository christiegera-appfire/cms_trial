# admGetAllPermissionGrants

## Description

Retrieves a list of permissions for the provided scheme id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllPermissionGrants(schemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | allPermissionGrants(schemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | integer | Yes | The id for which the grants will be get. |

## Return Type

[**JPermissionGrant []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of permission grant structures.

## Example

```javascript
JPermissionGrant [] allPermGrants = admGetAllPermissionGrants(10012);
return allPermGrants;}
```

## See also