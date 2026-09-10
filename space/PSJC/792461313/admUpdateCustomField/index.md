# admUpdateCustomField

## Description

Updates a custom field, the searcher can also be updated.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateCustomField(cfId, fieldName, description[, fieldSearcher]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updateCustomField(cfId, fieldName, description[, fieldSearcher]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| cfId | String | Yes | The id of the custom field. |
| fieldName | String | Yes | Custom field name. |
| description | String | Yes | Custom field description (can be blank). |
| fieldSearcher | String | No | Custom field searcher (either key or name). If blank, the default custom field searcher for the given type will be considered. |

## Return Type

**boolean**

Returns true if the custom field is updated and false otherwise.

## Example

### Example

Changing the name of the customfield\_10000 and make it use a free text searcher

```javascript
admUpdateCustomField("customfield_10000", "New Custom Field Name", "test description", "Free Text Searcher");
```

If the provided custom field searcher key or name is wrong, it will be ignored and the custom field will be updated with no searcher configured.

## See also