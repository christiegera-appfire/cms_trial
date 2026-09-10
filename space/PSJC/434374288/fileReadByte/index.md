# fileReadByte

## Description

Reads a byte from an open file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileReadByte(fid) | **Package** | file |
| **Alias** |  | **Pkg Usage** | readByte(fid) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fid | String | Yes | The id of the open file to read from. |

## Return Type

**Byte**

## Error Handling

Throws **String**

Error: "read\_error": followed by the error message if the read fails

## Example

### Example 1

```javascript
use "file";
int fid = fileOpen("C:\myData.dat");
runnerLog(fileReadByte(fid));
close(fid);
```

Returns: 61

## See also