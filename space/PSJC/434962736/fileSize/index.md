# fileSize

## Description

Returns the size for a given file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileSize(file) | **Package** | file |
| **Alias** |  | **Pkg Usage** | size(file) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| file | String | Yes | Path depicting a file. |

## Return Type

**Number**

## Example

```javascript
number len = fileSize("C:/file1.txt");
```

It is recommended that you use forward slashes ( / ) for file paths.

## See also