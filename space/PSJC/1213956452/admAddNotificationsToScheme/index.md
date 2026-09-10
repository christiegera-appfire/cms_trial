# admAddNotificationsToScheme

## Description

Adds the given list of notification to the given notification scheme

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddNotificationsToScheme(notificationSchemeId, notificationsToBeAdded) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addNotificationsToScheme(notificationSchemeId, notificationsToBeAdded) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| notificationSchemeId | integer | Yes | The id of the notification scheme |
| notificationsToBeAdded | JIssueNotificationSchemeEvent [] | Yes | The list of notifications to be added |

## Return Type

**boolean**

Returns true if the notification were added, false otherwise.

## Example

### Example

Adds notifications to the notification scheme with id "10005"

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
return admAddNotificationsToScheme(10005, notificationEvents);
```

## See also