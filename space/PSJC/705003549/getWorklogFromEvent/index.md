# getWorklogFromEvent

## Description

Retrieves a worklog structure from the event. Useful when treating worklog events.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogFromEvent() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JWorklog**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
logPrint("INFO", "Result of listener: " + getWorklogFromEvent());
```

Returns the JWorklog object, if any in the event.

## See also