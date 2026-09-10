# admGetNotificationScheme

## Description

Retrieves a breakdown of events and notifications for a notification scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetNotificationScheme(name, id) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | notificationScheme(name, id) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the notification scheme. |
| id | integer | Yes | The ID of the notification scheme. |

## Return Type

[**JIssueNotificationScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a notification scheme.

## Example

```javascript
JNotificationScheme noteScheme = admGetNotificationScheme("Default Notification Scheme", 11000);
runnerLog("Id: " + noteScheme.id);
runnerLog("Name: " + noteScheme.name);
runnerLog("Description: " + noteScheme.description );
```

## See also