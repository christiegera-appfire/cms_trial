# writeToBinaryFile

## Description

Prints bytes to a specified file. The file can be overwritten or appended to.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | writeToBinaryFile(filepath, bytes [, append]) | **Package** | file |
| **Alias** |  | **Pkg Usage** | writeBinary(filepath, bytes [, append]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filepath | String | Yes | Specifies the file name to write in. |
| bytes | Byte [] (Array of bytes) | Yes | Specifies the bytes to be written to the file. |
| append | Boolean | No | 'true' if new bytes are added to the end of the file, otherwise 'false' (default) the whole file will be overwritten. |

## Return Type

**Integer**

Return value represents the number of bytes written to the file.

## Example

### Example 1

```javascript
writeToBinaryFile("C:/myData.dat", dataBytes[], true)
```

Writes (appends) the data from the dataBytes variable to the file "myData.dat".

It is recommended that you use forward slashes ( / ) for file paths. As a general observation use the silEnv() function to create an absolute path.

## See also