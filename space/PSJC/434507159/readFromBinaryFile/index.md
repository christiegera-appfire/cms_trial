# readFromBinaryFile

## Description

Read the bytes of a binary file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | readFromBinaryFile(path) | **Package** | file |
| **Alias** |  | **Pkg Usage** | readBinary(path) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Path | String | Yes | Specifies the file name to read from. |

## Return Type

**Byte []**

An array of bytes read from the binary file.

## Example

### Example 1

```javascript
byte [] fileContent = readFromTextFile("C:/icon.jpg");
```

It is recommended that you use forward slashes () for file paths. As a general observation use the silEnv() function to create an absolute path.

## See also