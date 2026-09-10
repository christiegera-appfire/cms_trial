# admDeleteFilter

## Description

Deletes a filter. Returns true if deletion succeeds

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeleteFilter(filterId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; updateFilter(filterId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filterId | int | Yes | The filter id to be deleted |

## Return Type

**boolean**

## Example

```javascript
admDeleteFilter(10017);
```

Deletes the filter with the id 10017

## See also