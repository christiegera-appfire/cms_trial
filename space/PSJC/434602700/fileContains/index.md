# fileContains

## Description

Returns "true" if the file contains any string that matches the specified regex. If the regex contains a backslash replace it with two backslashes otherwise you will get a syntax error.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileContains(path\_to\_file, regex [, charset]) | **Package** | file |
| **Alias** |  | **Pkg Usage** | contains(path\_to\_file, regex [, charset]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_file | String | Yes | Specifies the file name. |
| regex | String | Yes | Specifies search string into the file path\_to\_file. |
| charset | String | No | The charset, optional. If you need to open a text file and the encoding is different, use a value that matches a valid charset name. |

## Return Type

**Boolean (true/false)**

## Example

```javascript
//This will match any "com.keplerrominfo.jira" occurence in myfile.txt.
fileContains("C:/myfile.txt","com\\.keplerrominfo.jira");
```

It is recommended that you use absolute file paths with forward slashes ( / ).

## See also