# getSprintFromEvent

## Description

Retrieves a sprint structure from the event. Useful when treating sprint created/updated/deleted/started/closed event.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getSprintFromEvent() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JSprint**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
logPrint("INFO", "Result of listener: " + getSprintFromEvent());
```

Returns the JSprint, if any in the event.

## See also