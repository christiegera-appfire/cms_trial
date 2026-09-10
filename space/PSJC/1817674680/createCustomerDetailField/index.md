# createCustomerDetailField

## Description

Creates a customer detail field.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createCustomerDetailField(fieldName, fieldType[, options]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldName | string | Yes | The name of the detail field |
| fieldType | string | Yes | The field type. Valid values: TEXT, EMAIL, URL, DATE, NUMBER, BOOLEAN, PHONE, SELECT, MULTISELECT. |
| options | string[] | No | Field value options |

## Return Type

**boolean**

True if the customer detail field is created, false otherwise.

## Example

```javascript
return createCustomerDetailField("Projects", "MULTISELECT", {"TEST", "DEMO", "NEW"});
```

## See also