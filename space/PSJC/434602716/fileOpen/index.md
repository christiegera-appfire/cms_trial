# fileOpen

## Description

Opens a file in memory so that it may be read from. Note that the file is seen as an octet stream, encoding doesn’t matter from this point of view. File may be read and written at random locations.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileOpen(path\_to\_file, mode) | **Package** | file |
| **Alias** |  | **Pkg Usage** | open(path\_to\_file, mode) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_file | String | Yes | Specifies the path to the file that should be opened. |
| mode | Boolean | Yes | If 'true' the file will be opened in read only mode. If 'false' the file will be editable. |

## Return Type

**Integer**

The id of the file that was opened. The id has no meaning beyond the script.

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