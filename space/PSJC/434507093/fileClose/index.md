# fileClose

## Description

Closes a previously opened file and removes it from memory.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileClose(fid) | **Package** | file |
| **Alias** |  | **Pkg Usage** | close(fid) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| file id | Integer | Yes | The id of a file opened from a previous step that should be closed. |

## Return Type

**None**

Return value has no meaning.

## Error Handling

Throws **String**

**Errors:**

- "invalid": if the path is invalid
- "cannot\_work\_on\_directory": if the path is a directory, in fact, and not a file
- "unresolvable": if the file cannot be resolved
- "notfound": if the file is not found

## Example

### Example 1

```javascript
use "file";
int fid = open(filename); //fileOpen
fileClose(fid);//full name of the function
```

## See also