# admAddProjectCategory

## Description

Adds new project category.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddProjectCategory(categoryName[, description]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addProjectCategory(categoryName[, description]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| categoryName | String | Yes | Project category name. |
| description | String | No | Description of the category being added |

## Return Type

**Boolean (true/false)**

Returns true if the new category was added and false otherwise.

## Example

```javascript
admAddProjectCategory("T3", "Thunderbolt Category");
```

## See also