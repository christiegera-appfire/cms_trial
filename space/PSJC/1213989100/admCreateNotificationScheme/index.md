# admCreateNotificationScheme

## Description

Creates a new issue notification scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateNotificationScheme(newNotificationStruct) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createNotificationScheme(newNotificationStruct) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| newNotificationStruct | JIssueNotificationScheme | Yes | The structure of the notification scheme to be created. |

## Return Type

**string**

## Example

```javascript
JIssueNotificationSchemeNotificationDetail[] notificationDetails;
JIssueNotificationSchemeNotificationDetail notificationDetail; //https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-notification-schemes/#api-rest-api-3-notificationscheme-post
notificationDetail.notificationType = "Group";
notificationDetail.parameter = "site-admins";
notificationDetails = arrayAddElement(notificationDetails, notificationDetail);
JIssueNotificationSchemeEvent[] notificationEvents;
JIssueNotificationSchemeEvent notificationEvent;
notificationEvent.event = "1";
notificationEvent.notifications = notificationDetails;
notificationEvents = arrayAddElement(notificationEvents, notificationEvent);
JIssueNotificationScheme notification;
notification.name = "new notification";
notification.description = "new notification description";
notification.notificationSchemeEvents = notificationEvents;
return admCreateNotificationScheme(notification);
```

## See also