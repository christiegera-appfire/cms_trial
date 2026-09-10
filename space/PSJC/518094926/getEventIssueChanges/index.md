# getEventIssueChanges

## Description

Retrieves a structure containing information about all the changes made for the specific event.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getEventIssueChanges() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JFieldChange**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFieldChange [] changes = getEventIssueChanges();
logPrint("ERROR", "Event Changes: " + changes);
```

## See also