# fileRead

## Description

Reads a byte array from a file until it reaches the specified length or until the EOF is reached.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileRead(fid, len) | **Package** | file |
| **Alias** |  | **Pkg Usage** | read(fid, len) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fid | String | Yes | The id of the open file to read from. |
| len | Integer | Yes | The number of bytes that should be read. |

## Return Type

**Byte []**

## Error Handling

Throws **String**

**Errors:**

- "eof": if you read past the end of the file
- "read\_error": followed by the actual error if read fails

## Example

### Example 1

```javascript
use "file";
int fid = open("C:\myData.dat");
runnerLog(read(fid, 10));
close(fid);
```

Returns: 61|54|32|85|45|33|21|11|40|06 (a byte array)

## See also