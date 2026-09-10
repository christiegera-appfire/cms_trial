# arrayDeleteElement

## Description

If **elem** is an element of the array type, returns a new array without the specified element.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayDeleteElement(arrayName, elem) | **Package** | array |
| **Alias** | deleteElement(arrayName, elem) | **Pkg Usage** | deleteElement(arrayName, elem) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| arrayName | Array | Yes | Array the new element is deleted from. |
| elem | Any | Yes | Element to be deleted. Must be the same type as the array type. |

## Return Type

**Array**

## Example

```javascript
watchers = deleteElement(watchers, currentUser());
```

The result returned by the function is assigned to the the same array **watchers**, so the initial array **watchers** will be modified.

1. If **array** is not defined as an array, the function returns error.
2. If **elem**  is not the same type as declared in the array definition, the function returns error.

Starting with version 2.5, there is a more powerful way to express these operations: **array = array - element;** or even better **array -= element;**

## See also