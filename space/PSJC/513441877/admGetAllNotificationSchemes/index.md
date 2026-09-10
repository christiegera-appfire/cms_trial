# admGetAllNotificationSchemes

## Description

Retrieves a breakdown of events and notifications for all notification schemes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllNotificationSchemes(notificationSchemeName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | allNotificationSchemes(notificationSchemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| notificationSchemeName | string | Yes | The name of the notification scheme. |

## Return Type

[**JIssueNotificationScheme []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns all the notification schemes.

## Example

```javascript
JIssueNotificationScheme [] allNoteSchemes = admGetAllNotificationSchemes();
for(JIssueNotificationScheme jns in allNoteSchemes) {
    runnerLog("Id: " + jns.id);
    runnerLog("Name: " + jns.name);
}
```

## See also