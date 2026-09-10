# fileReadLine

## Description

Reads a line of text from an open file until it reaches the end of the line (\n or \r\n).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileReadLine(fid) | **Package** | file |
| **Alias** |  | **Pkg Usage** | readLine(fid) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fid | String | Yes | The id of the open file to read from. |

## Return Type

**String**

## Error Handling

Throws **String**

**Errors:**

- "eof": if you read past the end of the file
- "read\_error": followed by the actual error if read fails

## Example

### Example 1

```javascript
use "file";
int fid = fileOpen("C:\alphabet.txt");
runnerLog(fileReadLine(fid));
close(fid);
```

Returns: ABCDEFGHIJKLMNOPQRSTUVWXYZ

## See also