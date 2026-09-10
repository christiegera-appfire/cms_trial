# removeRequestTypeByIdFromServiceDesk

## Description

Removes a request type from the provided service desk.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeRequestTypeByIdFromServiceDesk(serviceDeskId, requestTypeId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The ID of the service desk where the customer request type is to be created. |
| requestTypeId | number | Yes | The ID of the request type to be removed. |

## Return Type

**boolean**

The returned value has no meaning.

## Example

```javascript
removeRequestTypeByIdFromServiceDesk(1, 44);
```

## See also