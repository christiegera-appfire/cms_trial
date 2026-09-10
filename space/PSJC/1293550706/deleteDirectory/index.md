# deleteDirectory

## Description

Deletes a dir. It also returns "true" if the directory was deleted successfully and "false" otherwise. Directory must be empty.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteDirectory(path\_to\_dir) | **Package** | file |
| **Alias** |  | **Pkg Usage** | deleteDir(path\_to\_dir) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_dir | string | Yes | Specifies the directory to delete. |

## Return Type

**boolean (true/false)**

## Example

```javascript
deleteDirectory("C:/tmp/MYDIR");
```

It is recommended that you use forward slashes ( / ) for file paths.

## See also