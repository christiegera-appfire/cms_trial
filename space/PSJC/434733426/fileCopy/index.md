# fileCopy

## Description

Copy a file from one location to another. Returns "true" if the file was copied successfully and "false" otherwise. If "false" is returned check the log for a detailed reason on why it failed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileCopy(path\_to\_source, path\_to\_destination) | **Package** | file |
| **Alias** |  | **Pkg Usage** | copy(path\_to\_source, path\_to\_destination) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_source | String | Yes | Specifies the source file name. |
| path\_to\_destination | String | Yes | Specifies the destination file name. |

## Return Type

**Boolean (true/false)**

## Example

```javascript
fileCopy("C:/source.txt", "C:/destination.txt");
```

Returns 'true' if the **source.txt** file was copied to the **destination.txt** file.

It is recommended that you use forward slashes ( / ) for file paths.

## See also