# getOrganizationPropertyValues

## Description

Get the organization properties keys the provided organization id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getOrganizationPropertyValues(organizationId, propertyKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| organizationId | number | Yes | Id of the organization for which to get the property value. |
| propertyKey | string | Yes | The property key for which to get the property value. |

## Return Type

**string []**

Returns null if the organization or the property can not be found.

## Example

```javascript
return getOrganizationPropertyValues(13, "TestProperty1");
```

Result: The string [] "Property1TestValue|AnotherPropertyValue" will be return.

## See also