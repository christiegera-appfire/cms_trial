# zipFiles

## Description

Adds a file or an array of files to a zip file. If the zip file doesn't exist, it will be created, otherwise it will be appended with all files that exist.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | zipFiles(files, zipFileName) | **Package** | file |
| **Alias** |  | **Pkg Usage** | zip(files, zipFileName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| files | string[] | Yes | List of files. |
| zipFileName | String | Yes | Name of the zip file. |

## Return Type

**Boolean (true/false)**

The function returns 'true' if at least one file was added to the zip file and 'false' otherwise.

## Example

```javascript
zipFiles({"C:/file1.txt", "C:/file2.txt"}, "nameOfZip");
```

It is recommended that you use forward slashes ( / ) for file paths.

## See also