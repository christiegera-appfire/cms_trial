# readFromTextFile

## Description

Read the text of the file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | readFromTextFile(path[, charset]) | **Package** | file |
| **Alias** |  | **Pkg Usage** | readText(path[, charset]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path | String | Yes | Specifies the file name to read from. |
| charset | String | No | Specifies the charset used to read that file. Available starting with **SIL Engine 4.0.0.** |

## Return Type

**String**

The text of the file

## Example

```javascript
string fileContent = readFromTextFile("C:/story.txt");
```

1. You can use absolute paths and relative paths to "sil.home".
2. If the file is not found, an error will be raised.

## See also