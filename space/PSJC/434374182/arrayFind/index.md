# arrayFind

## Description

Finds an element inside the collection and returns its index. If the element is not found, it returns -1.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayFind(arrayName, element) | **Package** | array |
| **Alias** |  | **Pkg Usage** | find(arrayName, element) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| arrayName | Array | Yes | Array. |
| element | Type must match element that is to be found. | Yes | Element to be found in the array. |

## Return Type

**Number**

## Example

```javascript
return arrayFind(usersInGroups({"jira-users"}), "admin");
```

The result of the function is the index of the searched element in the array returned by usersInGroups(). If the array contains duplicates, the function returns the index of the first occurrence of the searched element.

## See also