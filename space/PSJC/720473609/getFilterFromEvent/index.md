# getFilterFromEvent

## Description

Retrieves a filter structure from the event. Useful when treating filter events.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getFilterFromEvent() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JFilter**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
logPrint("INFO", "Result of listener: " + getFilterFromEvent());
```

Returns the JFilter object, if any in the event.

## See also