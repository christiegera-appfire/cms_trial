# arrayUnion

## Description

Union between two arrays.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayUnion(arrayName1, arrayName2) | **Package** | array |
| **Alias** |  | **Pkg Usage** | union(arrayName1, arrayName2) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| arrayName1 | Array | Yes | First array. |
| arrayName2 | Array | Yes | Second array. |

## Return Type

**Array**

## Example

```javascript
string[] developers= usersInGroups({"jira-developers"});
string[] administrators = usersInGroups({"jira-administrators"});
return arrayUnion(developers, administrators);
```

The result returned by the function is an array that contains the unique elements from developers and administrators.

## See also