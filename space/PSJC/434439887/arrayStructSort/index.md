# arrayStructSort

## Description

Sorts the elements from an array by their specified field. Works only with arrays that contain structures.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayStructSort(arr, field) | **Package** | array |
| **Alias** |  | **Pkg Usage** | structSort(arr, field) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| arr | Array | Yes | Array, must be a struct array. |
| field | String | Yes | Field to be sorted by. |

## Return Type

**Array**

## Example

```javascript
struct Person {
    string id;
    string name;
}

Person p1; 
p1.name = "John Doe";
p1.id = "1234567";
Person p2; 
p2.name = "Jane Doe";
p2.id = "1234568";
Person p3; 
p3.name = "Jimmy Doe";
p3.id = "1234565";
Person[] persons = {p1, p2, p3};
runnerLog("Array before sort: " + persons);
persons = arrayStructSort(persons, "id");
runnerLog("Array after sort: " + persons);
```

The output will be:  
  
Array before sort: 1234567|John Doe|1234568|Jane Doe|1234565|Jimmy Doe  
Array after sort: 1234565|Jimmy Doe|1234567|John Doe|1234568|Jane Doe

## See also