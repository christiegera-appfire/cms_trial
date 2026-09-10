# admDeleteProjectCategory

## Description

Deletes the project category with the provided name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeleteProjectCategory(categoryName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deleteProjectCategory(categoryName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| categoryName | String | Yes | Project category name. |

## Return Type

**Boolean (true/false)**

Returns true if the category was deleted and false otherwise.

## Example

```javascript
admDeleteProjectCategory("T3");
```

## See also