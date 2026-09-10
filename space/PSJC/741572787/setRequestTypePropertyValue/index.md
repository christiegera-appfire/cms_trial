# setRequestTypePropertyValue

## Description

Sets a property value for the provided property key, from a specified request type and service desk.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | setRequestTypePropertyValue(serviceDeskId, requestTypeId, propertyKey, propertyValue) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The servicedesk id in which to set the property. |
| requestTypeId | number | Yes | The request type id in which to set the property. |
| propertyKey | string | Yes | The name of the property for which we'll set the values. |
| propertyValue | number/string | Yes | The value to be set. |

## Return Type

**boolean**

True if the property value is set, false otherwise.

## Example

```javascript
return setRequestTypePropertyValue(1, 2, "propKey", {1, 2, 3});
```

## See also