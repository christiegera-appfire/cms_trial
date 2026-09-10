# arrayFindBinary

## Description

Binary search on sorted array. If the element is not found, returns -1.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayFindBinary(arrayName, element) | **Package** | array |
| **Alias** |  | **Pkg Usage** | binaryFind(arrayName, element) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| arrayName | Array | Yes | Array. |
| element | type of array element | Yes | Element to find in the array. |

## Return Type

**Number**

## Example

```javascript
return arrayFindBinary(arraySort(usersInGroups({"jira-users"}), false), "admin");
```

The result of the function is the index of the searched element in the array returned by [arraySort()](/cms_trial/space/PSJC/434733352/arraySort/). If the array contains duplicates, the function returns the index of the first occurrence of the searched element.

Binary search should be used only for sorted arrays.

## See also