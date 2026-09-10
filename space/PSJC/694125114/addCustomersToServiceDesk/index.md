# addCustomersToServiceDesk

## Description

Adds an existing customer or a list of customers to a specified service desk.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addCustomersToServiceDesk(serviceDeskId, customersAccountIds) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | Integer | Yes | Add customer/s to that service desk. |
| customersAccountIds | String [] | Yes | The customer(s) id/s |

## Return Type

**Boolean**

Returns "true" if the operation succeeded.

## Examples

### Example 1

Add multiple customers to a a service desk with id of 1.

```javascript
return addCustomersToServiceDesk(1, {"customer1","customer2"});
```

### Example 2

Add a single customer to a a service desk with id of 1.

```javascript
return addCustomersToServiceDesk(1, "customer");
```

## See also