# arrayAddElementIfNotExist

## Description

If **elem** is an element of the array type, returns a **new** array that includes the specified element at the end. The element is added **only if it is not already** in the array.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayAddElementIfNotExist(arrayName, elem) | **Package** | array |
| **Alias** | addElementIfNotExist(arrayName, elem) | **Pkg Usage** | addElementIfNotExist(arrayName, elem) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| arrayName | Array | Yes | Array the new element is added to. |
| elem | Any | Yes | Element to be added. Must be the same type as the array type. |

## Return Type

**Array**

## Examples

### Example 1

```javascript
watchers2 = addElementIfNotExist(watchers, currentUser());
```

Adds **currentUser** to the **watchers** array if **currentUser** is not already present. The function returns a new array **watchers2**, so the initial array will not be modified.

### Example 2

```javascript
watchers = addElementIfNotExist(watchers, currentUser());
```

The initial array will be modified as a result of the **=** operator and **NOT of the function call**.

1. If **arrayName**  is not defined as an array, the function returns error.
2. If **elem**  is not the same type as declared in the array definition, the function returns error.

## See also