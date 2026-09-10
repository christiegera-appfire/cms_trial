# admGetPermissionGrant

## Description

Retrieves a permissions by its id for the provided scheme id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetPermissionGrant(schemeId, grantId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | permissionGrant(schemeId, grantId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | integer | Yes | The id of the scheme for which the grant will be get. |
| grantId | integer | Yes | The id grant that will be get. |

## Return Type

[**JPermissionGrant**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a permission grant structures.

## Example

```javascript
JPermissionGrant permGrant = admGetPermissionGrant(10012, 11344);
return permGrant;}
```

## See also