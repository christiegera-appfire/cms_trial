# removeCustomersFromServiceDesk

## Description

Removes a customer or a list of customers from a specified service desk.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeCustomersFromServiceDesk(serviceDeskId, customersAccountIds) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The servicedesk id from here to remove the customer/s. |
| customersAccountIds | String [] | Yes | The customers' account id/s |

## Return Type

**Boolean**

The returned value has no meaning.

## Example

```javascript
removeCustomersFromServiceDesk(1, currentUserKey());
```

## See also