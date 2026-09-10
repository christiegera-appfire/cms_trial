# getCustomerDetail

## Description

Returns the value of a given detail field for a customer.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomerDetail(customerId, fieldName) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customerId | string | Yes | The customer id |
| fieldName | string | Yes | The customer detail field name |

## Return Type

**string[]**

The array contains one value for single-value fields and multiple values for multi-value fields.

## Example

```javascript
return getCustomerDetail("qm:afdc53a9-551b-c5f4c08de195:16ce414a-e682a47faccc", "Projects");
```

Returns the value of the Projects detail field for the specified customer.

## See also