# fileSeek

## Description

Moves the file pointer to a specific spot in an already open file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileSeek(fid, pos) | **Package** | file |
| **Alias** |  | **Pkg Usage** | seek(fid, pos) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fid | String | Yes | The id of the open file to read from. |
| pos | Integer | Yes | The new position of the cursor. |

## Return Type

**Integer**

Returns the current position of the file pointer.

## Error Handling

Throws **String**

Error: "seek\_error": followed by the actual error

## Example

### Example 1

```javascript
use "file";
int fid = open("C:\alphabet.txt");
seek(fid, 10);
runnerLog(fileReadLine(fid));
close(fid);
```

Returns: KLMNOPQRSTUVWXYZ

## See also