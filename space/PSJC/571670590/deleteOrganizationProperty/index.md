# deleteOrganizationProperty

## Description

Delete the organization property with the provided propertyKey for the organizationId.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteOrganizationProperty(organizationId, propertyKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| organizationId | number | Yes | Id of the organization for which to delete the property. |
| propertyKey | string | Yes | The property key of the property to be deleted. |

## Return Type

**boolean**

Returns true if the property was deleted and false otherwise.

## Example

```javascript
return deleteOrganizationProperty(13, "TestProperty1");
```

Result: true

## See also