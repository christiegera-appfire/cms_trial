# findFiles

## Description

Searches for **files** that match the given regex in the specified folder. The function only searches for files, not directories. Returns a list with **absolute** paths for files that match the given regex. The regex match is done on the file name, not the full path. If the regex parameter is empty string, the function returns an empty result.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | findFiles(directory, regex) | **Package** | file |
| **Alias** |  | **Pkg Usage** | find(directory, regex) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| directory | String | Yes | Specifies the directory to search into. |
| regex | String | Yes | Specifies the file pattern to search for. |

## Return Type

**String []**

## Example

```javascript
findFiles("C:/JIRA/plugins", ".*\\.jar");
```

Results: An array containing all absolute paths for jar files from the folder C:\JIRA\plugins.

1. It is recommended that you use forward slashes ( / ) for file paths.
2. If the regex contains a backslash replace it with two backslashes otherwise you will get a syntax error.

## See also