# admDeletePermissionScheme

## Description

Deletes the permission scheme indicated in the schemeId parameter.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeletePermissionScheme(schemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deletePermissionScheme(schemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | integer | Yes | The id o the scheme to be deleted. |

## Return Type

**Boolean**

Returns true if the scheme has been deleted.

## Example

### Example

```javascript
return admDeletePermissionScheme(10011);
```

## See also