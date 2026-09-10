# renameFile

## Description

Renames a file. Returns "true" if the file was renamed successfully and "false" otherwise. If "false" is returned check the log for a detailed reason on why it failed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | renameFile(path\_to\_source, path\_to\_destination) | **Package** | file |
| **Alias** |  | **Pkg Usage** | rename(path\_to\_source, path\_to\_destination) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_source | String | Yes | Specifies the source file name. |
| path\_to\_destination | String | Yes | Specifies the new file name for the source file. |

## Return Type

**Boolean (true/false)**

## Example

```javascript
renameFile("C:/source.txt", "C:/destination.txt");
```

It returns 'true' if the **source.txt** file was renamed to **destination.txt**.

It is recommended that you use forward slashes ( / ) for file paths.

## See also