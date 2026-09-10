# deleteCustomerDetailField

## Description

Deletes a customer detail field and all values stored for it for all customers. You cannot restore a detail field once it has been deleted.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteCustomerDetailField(fieldName) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldName | string | Yes | The name of the detail field |

## Return Type

**boolean**

True if the customer detail field is deleted, false otherwise.

## Example

```javascript
return deleteCustomerDetailField("Projects");
```

## See also