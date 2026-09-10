# admSetProjectCategory

## Description

Returns true if the category of a project has been updated.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetProjectCategory(pkey, categoryName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | setProjectCategory(pkey, categoryName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | String | Yes | The project key. The value must be unique. |
| categoryName | String | Yes | The project category name. Leave blank if no category is available. |

## Return Type

**boolean**

Returns true if the category was set to the project and false otherwise.

## Examples

```javascript
admSetProjectCategory("T3", "Thunderbolt3");
```

```javascript
use "adm";
setProjectCategory("CX1", "Cat");
```

## See also