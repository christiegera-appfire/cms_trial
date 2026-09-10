# arrayAddElement

## Description

If **elem** is an element of the array type, returns a new array that includes the specified element at the end.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayAddElement(arrayName, elem) | **Package** | array |
| **Alias** | addElement(arrayName, elem) | **Pkg Usage** | addElement(arrayName, elem) |

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
watchers2 = addElement(watchers, currentUser());
```

The result returned by the function is assigned to a new array **watchers2**, so the initial array **watchers**  will not be modified.

### Example 2

```javascript
watchers = addElement(watchers, currentUser());
```

The result returned by the function is assigned to the same array **watchers**, so the initial array **watchers**  will be modified.

If **elem** is not the same type as declared in the array definition, the function returns error.

Starting with version 2.5, it is easier for you to just use the '+' operator to add elements to an array. **array = array + element** it is a simple and more meaningful way to express it. **array += element** is even better.

## See also