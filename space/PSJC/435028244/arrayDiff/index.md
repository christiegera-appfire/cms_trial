# arrayDiff

## Description

Difference between two arrays. Returns the elements from the first array that do not exist in the second array.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayDiff(arrayName1, arrayName2) | **Package** | array |
| **Alias** |  | **Pkg Usage** | diff(arrayName1, arrayName2) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| arrayName1 | Array | Yes | First array. |
| arrayName2 | Array | Yes | Second array. |

## Return Type

**Array**

## Examples

### Example 1

```javascript
string[] array1 = {"a", "b", "c"};
string[] array2 = {"c", "d"};
return arrayDiff(array1, array2);
```

The result will be an array containing elements "a" and "b".

### Example 2

```javascript
string[] developers= usersInGroups({"jira -developers"});
string[] administrators = usersInGroups({"jira-administrators"});
return arrayDiff (developers, administrators );
```

The result is an array that contains only developers that are not also administrators.

If the array types are incompatible, the function returns error.

## See also