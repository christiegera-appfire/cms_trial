# fileExists

## Description

Returns 'true' if the file exists and 'false' otherwise.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileExists(path\_to\_file) | **Package** | file |
| **Alias** |  | **Pkg Usage** | exists(path\_to\_file) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_file | String | Yes | Specifies the file name you want to search for. |

## Return Type

**Boolean (true/false)**

## Example

```javascript
if(fileExists("C:/someFile.txt")){
    print("The file exists!");
} else {
    print("The file does not exist!");
}
```

It is recommended that you use forward slashes ( / ) for file paths.

## See also