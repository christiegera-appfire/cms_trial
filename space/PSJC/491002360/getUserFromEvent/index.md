# getUserFromEvent

## Description

Retrieves a structure containing information about an user that has been created or updated.  
The function is a combination of the server functions for the user events (getNewUserFromEvent / getOldUserFromEvent).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getUserFromEvent() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JUser**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
logPrint("INFO", "Result of listener: " + getUserFromEvent());
```

The result is a structure containing the user key, user name, the display name and the email of the user.

## See also