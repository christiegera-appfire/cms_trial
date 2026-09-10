# getAttachmentFromEvent

## Description

Retrieves an attachment structure from the event. Useful when treating attachment events.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAttachmentFromEvent() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JAttachment**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
logPrint("INFO", "Result of listener: " + getAttachmentFromEvent());
```

Returns the JAttachment object, if any in the event.

## See also