# fileInfo

## Description

Returns basic file information about a file such as the date it was created.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fileInfo(path) | **Package** | file |
| **Alias** |  | **Pkg Usage** | info(path) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path | String | Yes | File path to the file to get the information for. |

## Return Type

**String []**

Returns an array containing the information about the file.

## Examples

### Example 1

```javascript
string [] file = fileInfo("someFile.xlsx");
runnerLog("Path: " + file["absolutePath"]);
runnerLog("Created Date: " + parseDate("yyyy-MM-dd hh:mm:ss", file["created"]));
runnerLog("Created Date Long: " + formatNumber(file["createdLong"], "#####"));
runnerLog("Last Modified Date: " + parseDate("yyyy-MM-dd hh:mm:ss", file["lastModified"]));
runnerLog("Last Modified Long: " + formatNumber(file["lastModifiedLong"], "#####"));
 runnerLog("URI: " + file["uri"]);
runnerLog("Directory: " + file["isDirectory"]);
runnerLog("Symbolic Link: " + file["isSymbolic"]);
runnerLog("Parent Folder: " + file["parent"]);
runnerLog("Readable: " + file["canRead"]);
runnerLog("Writable: " + file["canWrite"]);
runnerLog("Executable: : " + file["canExecute"]);
```

```javascript
Path: C:\Program Files\Atlassian\Application Data\JIRA_versions\silprograms\someFile.xlsx
Created Date: 2020-10-13 13:05:49
Created Date Long: 1602608749593
Last Modified Date: 2020-10-13 13:07:50
Last Modified Long: 1602608870213
URI: /C:/Program Files/Atlassian/Application Data/JIRA_versions/silprograms/someFile.xlsx
Directory: false
Symbolic Link: false
Parent Folder: C:\Program Files\Atlassian\Application Data\JIRA_versions\silprograms
Readable: true
Writable: true
Executable: true
```

### Example 2

Get all the attachments for an issue that were created during the current day. Assume the issue has the following attachments:
Apple.jpg - created 2 weeks ago
Banana.jpg - 1 hour ago
Orange.jpg - created 1 week ago
Strawberry.jpg - 4 hours ago

```javascript
string [] attachmentsCreatedToday;
for(string a in attachments) {
    string [] file = fileInfo(getAttachmentPath(key, a));
    date created = parseDate("yyyy-MM-dd hh:mm:ss", file["created"]);
    if(created > startOfDay(currentDate())) {
        attachmentsCreatedToday += a;
    }
}
return attachmentsCreatedToday;
```

Results: Banana.jpg|Strawberry.jpg

1. It is recommended that you use forward slashes ( / ) for file paths.
2. If the file path contains a backslash replace it with two backslashes, otherwise you will get a syntax error.

## See also