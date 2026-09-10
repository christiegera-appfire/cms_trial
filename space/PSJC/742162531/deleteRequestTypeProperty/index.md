# deleteRequestTypeProperty

## Description

Removes the property with the property key, from a specified request type and service desk.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteRequestTypeProperty(serviceDeskId, requestTypeId, propertyKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The servicedesk id from which to remove the property. |
| requestTypeId | number | Yes | The request type id from which to remove the property. |
| propertyKey | string | Yes | The key of the property to be deleted. |

## Return Type

**boolean**

True if the property is deleted, false otherwise.

## Example

```javascript
return deleteRequestTypeProperty(1, 2, "propKey");
```

## See also