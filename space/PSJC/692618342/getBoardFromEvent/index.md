# getBoardFromEvent

## Description

Retrieves a board structure from the event. Useful when treating sprint created/updated/deleted/configuration board events.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getBoardFromEvent() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JBoard**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
logPrint("INFO", "Result of listener: " + getBoardFromEvent());
```

Returns the JBoard, if any in the event.

## See also