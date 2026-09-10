# arraysConcat

## Description

Adds the elements of the second array to the first one.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arraysConcat(array1, array2) | **Package** | array |
| **Alias** |  | **Pkg Usage** | concat(array1, array2) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array1 | Array | Yes | First array to be added. |
| array2 | Array | Yes | Second array to be added. |

## Return Type

**Array**

## Example

```javascript
group={"user1", "user2"};
watchers += arraysConcat(watchers, group);
```

Adds the elements of the **group** array to the **watchers** array.

If the array types are incompatible, the function returns error.

## See also