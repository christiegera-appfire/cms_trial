# setOrganizationPropertyValue

## Description

Set the organization property value for the provided organization id, property key.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | setOrganizationPropertyValue(organizationId, propertyKey, propertyValue) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| organizationId | number | Yes | Id of the organization for which to get the property value. |
| propertyKey | string | Yes | The property key for which to set the property value. |
| propertyValue | null | Yes | The value to be set for he provided propertyKey. |

## Return Type

**boolean**

Returns true if the property was set and false otherwise.

## Example

```javascript
return setOrganizationPropertyValue(13, "TestProperty1", "TestValue");
```

Result: true

## See also