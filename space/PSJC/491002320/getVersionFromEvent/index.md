# getVersionFromEvent

## Description

Retrieves a structure containing information about a version that has been archived, created, released, unarchived, unreleased, moved or merged.  
Due to some differences between Jira's server REST API and the REST API from cloud, this function will work slightly different here than it does on server. This happens because, in case of a version updated event, we cannot retrieve both of the information of the given version, before and after the changes being made.  
The function is a combination of the server functions for the version events (getVersionFromEvent / getOldVersionFromEvent).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getVersionFromEvent() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JVersion**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
logPrint("INFO", "Result of listener: " + getVersionFromEvent());
```

The result is a structure containing version id, name, description, project key of the version, start date and release dates, and information about whether the version is archieved or released.

## See also