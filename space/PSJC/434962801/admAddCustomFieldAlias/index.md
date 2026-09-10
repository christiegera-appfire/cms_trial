# admAddCustomFieldAlias

## Description

Adds a custom field alias in the sil.aliases file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddCustomFieldAlias(customField, alias) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addCFAlias(customField, alias) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customField | String | Yes | Custom field string id, name or existing alias. |
| alias | String | Yes | New custom field alias to set. |

## Return Type

**Boolean (true/false)**

Returns 'true' if the custom field alias was added successfully in the sil.aliases file or already exists and 'false' otherwise.

## Examples

### Example 1

Setting a custom field alias using custom field id:

```javascript
admAddCustomFieldAlias("customfield_10000", "TestAlias");
```

### Example 2

Setting a custom field alias using custom field name:

```javascript
admAddCustomFieldAlias("Text Field", "TestAlias");
```

## See also