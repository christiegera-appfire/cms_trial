# admDeleteNotificationScheme

## Description

Deletes a notification scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeleteNotificationScheme(notificationSchemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deleteNotificationScheme(notificationSchemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| notificationSchemeId | integer | Yes | The id of the scheme that will be deleted. |

## Return Type

**boolean**

Returns true if the notification scheme has been deleted.

## Example

### Example

```javascript
return admDeleteNotificationScheme(10005);
```

## See also