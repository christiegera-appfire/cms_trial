# getIssueLinkFromEvent

## Description

Retrieves a structure containing information about a link that has been created or deleted.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getIssueLinkFromEvent() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JIssueLink**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JIssueLink link = getIssueLinkFromEvent();
logPrint("INFO", "Link ID: " + link.id);
logPrint("INFO", "Link Name: " + link.name);
logPrint("INFO", "Link Direction: " + link.direction);
logPrint("INFO", "Link Description: " + link.description);
logPrint("INFO", "Link Issue: " + link.issue);
logPrint("INFO", "Link Source: " + key);
```

Prints:
Link ID: 10001
Link Name: Cloners
Link Direction: 1
Link Description: clones
Link Issue: SIL-123
Link Source: SIL-456

## See also