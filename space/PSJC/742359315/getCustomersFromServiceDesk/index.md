# getCustomersFromServiceDesk

## Description

Returns a list of customers accounts ids

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomersFromServiceDesk(serviceDeskId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The ID of the service desk for which the customers will be retrieved |

## Return Type

**String[]**

## Example

```javascript
return getCustomersFromServiceDesk(1);
```

Returns a list of customers accountIds.

## See also