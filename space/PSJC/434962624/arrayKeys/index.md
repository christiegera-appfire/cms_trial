# arrayKeys

## Description

Returns the keys of the array. Keys are not sorted and index in the returned array does not correspond to index in the original array. The function only returns a list of added keys. If the array contains no keys an empty array is returned.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayKeys(array) | **Package** | array |
| **Alias** |  | **Pkg Usage** | keys(array) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array | Array | Yes | Array. |

## Return Type

**String []**

## Example

```javascript
number []arr;
arr["one"] = 1;
arr["two"] = 2;
arr["three"] = 3;
arr[3] = 4;
string [] arrkeys = arrayKeys(arr); // contains strings 'one', 'two', 'three' but not necessary in that order !
```

## See also