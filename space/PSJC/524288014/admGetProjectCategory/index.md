# admGetProjectCategory

## Description

Get project category of the project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetProjectCategory(pkey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getProjectCategory(pkey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | String | Yes | Project key. |

## Return Type

**String**

Returns the name of the project category associated with the project.

## Example

```javascript
admGetProjectCategory("T3");
```

## See also