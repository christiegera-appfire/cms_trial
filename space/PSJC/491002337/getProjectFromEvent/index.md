# getProjectFromEvent

## Description

Retrieves a structure containing information about a project that has been created or deleted.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getProjectFromEvent() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JProject**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
logPrint("INFO", "Result of listener: " + getProjectFromEvent());
```

The result is a structure containing project id, key, name, description, lead, url, avatar id, project category and type, and information about whether the project issues are unassigned by default.

## See also