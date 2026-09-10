# arraySetElement

## Description

If **elem** is an element of the array type, returns a new array with the specified element on position **index1**. If **index1** is greater than the array size, it will add empty elements on the missing positions.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arraySetElement(array, index1, elem) | **Package** | array |
| **Alias** | setElement(array, index1, elem) | **Pkg Usage** | setElement(array, index1, elem) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array | Array | Yes | Array where to add the element. |
| index1 | Number | Yes | Position where to add the element. |
| elem | Matches type of array element to be set | Yes | Element to add to the array. |

## Return Type

**Element of the array type**

## Example

```javascript
watchers = setElement(watchers, 12, currentUser());
```

Sets the value **currentUser** for the 13 th element of the array **watchers.**

1. If **array** is not defined as an array, the function returns error.
2. If **index** is not number the function returns error.

Starting with version 2.5 we added the indexing operator. It will work on arrays, strings, dates and interval.  
You can simply write in your programs **watchers[12] = currentUser()** to refer to the 13 th element in the watchers array.

## See also