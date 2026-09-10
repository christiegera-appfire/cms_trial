# arrayGetElement

## Description

Returns the element at the specified **index**.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayGetElement(array, index) | **Package** | array |
| **Alias** | getElement(array, index) | **Pkg Usage** | getElement(array, index) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array | Array | Yes | Array where the element at the specified index is searched. |
| index | Number | Yes | Index of the element to be returned. |

## Return Type

**Element of the array type.**

## Example

```javascript
for(number i = 0; i < size(watchers); i = i + 1){
    print(getElement(watchers, i) + " is watching this issue.");
}
```

Prints all the elements of the array **watchers.**

1. If **index** is not number or has negative value the function returns error.
2. If **index** is greater than the size of the array, the function will return an empty value of the respective type.

Starting with version 2.5 we added the indexing operator. It will work on arrays, strings, dates and interval.  
  
You can simply write in your programs **watchers[0]** to refer to the first element in the watchers array.

## See also