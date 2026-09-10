# admDeletePermissionGrant

## Description

Deletes the permission grant indicated in the grantId parameter from the permission scheme with the provided schemeId.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeletePermissionGrant(schemeId, grantId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deletePermissionGrant(schemeId, grantId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | integer | Yes | The id of the scheme from which the grant will be deleted. |
| grantId | integer | Yes | The id grant that will be deleted. |

## Return Type

**Boolean**

Returns true if the grant has been deleted.

## Example

### Example

```javascript
return admDeletePermissionGrant(10012, 11308);
```

## See also