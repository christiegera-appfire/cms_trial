# findDirectories

## Description

Searches for **directories** that match the given regex in the specified folder. The function only searches for directories, not files. Returns a list with **absolute** paths for directories that match the given regex. The regex match is done on the file name, not the full path. If the regex parameter is empty string, the function returns an empty result.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | findDirectories(directory, regex) | **Package** | file |
| **Alias** |  | **Pkg Usage** | findDirs(directory, regex) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| directory | String | Yes | Specifies the directory to search in. |
| regex | String | Yes | Specifies the file pattern to search for. |

## Return Type

**String []**

## Example

```javascript
findDirectories("C:/JIRA/plugins", "kepler.*");
```

Results: An array containing all absolute paths for folders starting with 'kepler' from the folder C:\JIRA\plugins.

1. It is recommended that you use forward slashes ( / ) for file paths.
2. If the regex contains a backslash replace it with two backslashes otherwise you will get a syntax error.

## See also