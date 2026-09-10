# setCustomerDetail

## Description

Sets a detail field value for a specified customer.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | setCustomerDetail(customerId, fieldName, fieldValue) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customerId | string | Yes | The customer id |
| fieldName | string | Yes | The customer detail field name |
| fieldValue | string[] | Yes | The array contains one value for single-value fields and multiple values for multi-value fields |

## Return Type

**boolean**

True if the customer detail field value is set, false otherwise.

## Examples

```javascript
return setCustomerDetail("qm:afdc53a9-551b-c5f4c08de195:16ce414a-b51d-e682a47faccc", "Email", "test@mail.com");
```

```javascript
return setCustomerDetail("qm:afdc53a9-551b-c5f4c08de195:16ce414a-b51d-e682a47faccc", "Projects", {"IT", "DEMO"};
```

```javascript
return setCustomerDetail("qm:afdc53a9-551b-c5f4c08de195:16ce414a-b51d-e682a47faccc", "New Date", formatDate(currentDate(), "yyyy-MM-dd");
```

## See also