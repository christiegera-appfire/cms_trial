# updateCustomerDetailField

## Description

Renames a customer detail field and/or changes the available options for SELECT or MULTISELECT fields.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | updateCustomerDetailField(fieldName, name[, options]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldName | string | Yes | The name of the detail field to update |
| name | string | Yes | The name of the detail field |
| options | string[] | No | Field value options |

## Return Type

**boolean**

True if the customer detail field is updated, false otherwise.

## Example

```javascript
return updateCustomerDetailField("Projects", "New Projects", {"TEST", "DEMO", "NEW"});
```

## See also