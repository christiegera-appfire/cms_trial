# admDeleteCustomField

## Description

Deletes a custom field.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeleteCustomField(cfId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deleteCustomField(cfId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| cfId | String | Yes | The custom field id. |

## Return Type

**boolean**

Returns true if the custom field is deleted and false otherwise.

## Example

### Example

Deleting the customfield\_10000

```javascript
admDeleteCustomField("customfield_10000");
```

## See also