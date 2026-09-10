# arrayDeleteElementAt

## Description

If index is less than the array size, returns a new array without the element at the specified index.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayDeleteElementAt(array, index) | **Package** | array |
| **Alias** | deleteElementAt(array, index) | **Pkg Usage** | deleteElementAt(array, index) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array | Array | Yes | Array the element at the specified index is deleted from. |
| index | Number | Yes | Index of the element to be deleted. |

## Return Type

**Array**

## Examples

### Example 1

```javascript
if(size(watchers)>= 2){
	watchers2 = deleteElementAt(watchers, 1);
}
```

The result returned by the function is assigned to a new array **watchers2**, so the initial array **watchers** will not be modified.

### Example 2

```javascript
if(size(watchers)>= 2){
	watchers = deleteElementAt(watchers, 1);
}
```

The result returned by the function is assigned to the the same array **watchers**, so the initial array **watchers** will be modified.

## See also