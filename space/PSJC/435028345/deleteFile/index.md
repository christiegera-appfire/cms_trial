# deleteFile

## Description

Deletes a file. It also returns "true" if the file was deleted successfully and "false" otherwise. If returned "false" check the log for a detailed reason on why it failed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteFile(path\_to\_file) | **Package** | file |
| **Alias** |  | **Pkg Usage** | delete(path\_to\_file) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_file | String | Yes | Specifies the file name to delete. |

## Return Type

**Boolean (true/false)**

## Example

```javascript
deleteFile("C:/fileToDelete.txt");
```

It is recommended that you use forward slashes ( / ) for file paths.

## See also