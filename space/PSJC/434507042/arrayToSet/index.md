# arrayToSet

## Description

Converts an array to a set of unique elements.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayToSet(arrayName) | **Package** | array |
| **Alias** |  | **Pkg Usage** | toSet(arrayName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| arrayName | Array | Yes | Array to be converted to a set of elements. |

## Return Type

**Array**

## Example

```javascript
watchers = arrayToSet(watchers);
```

The result returned by the function is an array that contains the elements from watchers without duplicates.

## See also