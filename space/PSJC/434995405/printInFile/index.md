# printInFile

## Description

Prints in the specified file the provided value. It appends the value to the file. For best results, use absolute paths, since relative paths are resolved starting with the current working directory.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | printInFile(filepath, var[, charset]) | **Package** | file |
| **Alias** |  | **Pkg Usage** | print(filepath, var[, charset]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filepath | String | Yes | Specifies the file name to write in. |
| var | String | Yes | Specifies the character expression to write into the file filepath. |
| charset | String | No | Specifies the charset used to write that file. |

## Return Type

**None**

The returned value has no meaning.

## Example

```javascript
printInFile("C:/story.txt", "Once upon a time...");
```

Prints to the **story.txt** file the record **Once upon a time...**

It is recommended that you use forward slashes ( / ) for file paths. As a general observation use the silEnv() function to create an absolute path.

## See also