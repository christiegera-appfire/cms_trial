# fileWrite

## Description

Writes text or byte data to an open file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileWrite(fid, string\_byte\_or\_bytearray) | **Package** | file |
| **Alias** |  | **Pkg Usage** | open(fid, string\_byte\_or\_bytearray) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fid | String | Yes | The id of the open file to write to. |
| string\_byte\_or\_bytearray | String/Byten | Yes | The text string or byte data to write to the file. |

## Return Type

**None**

Return value has no meaning.

## Error Handling

Throws **String**

Error: "write\_error": followed by the actual error

## Example

### Example 1

```javascript
use "file";
int fid = open(filename); //fileOpen
fileWrite(fid, "First line is here
"); //full name of the function
write(fid, "Second line is here
");
close(fid); //fileClose
```

## See also