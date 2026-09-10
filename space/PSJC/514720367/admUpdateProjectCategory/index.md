# admUpdateProjectCategory

## Description

Updates project category description with the provided text.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateProjectCategory(categoryName, description) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updateProjectCategory(categoryName, description) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| categoryName | String | Yes | Project category name. |
| description | String | Yes | Description of the category being updated |

## Return Type

**Boolean (true/false)**

Returns true if the category was updated and false otherwise.

## Example

```javascript
admUpdateProjectCategory("T3", "Thunderbolt Category Updated");
```

## See also