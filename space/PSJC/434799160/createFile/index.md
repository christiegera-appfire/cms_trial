# createFile

## Description

Creates an empty file. It also returns "true" if the file was created successfully and "false" otherwise. If returned "false" check the log for a detailed reason on why it failed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createFile(path\_to\_file) | **Package** | file |
| **Alias** |  | **Pkg Usage** | create(path\_to\_file) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_file | String | Yes | Specifies the file name to create. |

## Return Type

**Boolean (true/false)**

## Example

```javascript
createFile("C:/fileToCreate.txt");
```

It is recommended that you use forward slashes ( / ) for file paths.

## See also