# admDeleteNotificationFromNotificationScheme

## Description

Deletes a notification from a notification scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeleteNotificationFromNotificationScheme(notificationSchemeId, notificationId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deleteNotificationFromNotificationScheme(notificationSchemeId, notificationId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| notificationSchemeId | integer | Yes | The id of the scheme from where the notification will be deleted. |
| notificationId | integer | Yes | The id of the notification that will be deleted. |

## Return Type

**boolean**

Returns true if the notification has been deleted.

## Example

### Example

```javascript
return admDeleteNotificationFromNotificationScheme(10005, 10197);
```

## See also