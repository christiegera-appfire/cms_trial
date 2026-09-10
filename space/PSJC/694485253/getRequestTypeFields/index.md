# getRequestTypeFields

## Description

Returns a string array of custom fields ids that match the provided parameters.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getRequestTypeFields(serviceDeskId, requestTypeId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | Integer | Yes | The service desk id. |
| requestTypeId | Integer | Yes | The request type id |

## Return Type

**String []**

## Example

```javascript
return getRequestTypeFields(1, 2);
```

## See also