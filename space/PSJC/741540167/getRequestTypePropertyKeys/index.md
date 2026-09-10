# getRequestTypePropertyKeys

## Description

Gets a list of property keys for the specified request type from the provided service desk.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getRequestTypePropertyKeys(serviceDeskId, requestTypeId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The servicedesk id for which to retrieve the properties. |
| requestTypeId | number | Yes | The request type id for which to retrieve the properties. |

## Return Type

**string[]**

## Example

```javascript
return getRequestTypePropertyKeys(1, 2);
```

Returns: "propKey|propKey2|propKey3"

## See also