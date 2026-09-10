# fileTruncate

## Description

Clears the content of the specified file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | truncate(path\_to\_file) | **Package** | file |
| **Alias** |  | **Pkg Usage** | truncate(path\_to\_file) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_file | String | Yes | Name of the file you want to truncate. |

## Return Type

**Boolean**

Returns true if the file is truncated.

## Example

### Example 1

```javascript
use "file";
truncate("fileToTruncate.txt");
```

## See also