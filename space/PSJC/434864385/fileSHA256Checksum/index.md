# fileSHA256Checksum

## Description

Returns the SHA256 checksum of the file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileSHA256Checksum(file) | **Package** | file |
| **Alias** |  | **Pkg Usage** | checksum(file) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| file | String | Yes | Specifies the file name to read from. |

## Return Type

**String**

## Example

```javascript
fileSHA256Checksum("C:/story.txt");
```

1. You can use absolute paths and relative paths to "sil.home".
2. If the file is not found, an error will be raised.

## See also