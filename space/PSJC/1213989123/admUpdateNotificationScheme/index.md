# admUpdateNotificationScheme

## Description

Updates an existing notification scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateNotificationScheme(notificationSchemeId, name, description) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updateNotificationScheme(notificationSchemeId, name, description) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | integer | Yes | The id of the scheme to be updated. |
| name | string | Yes | The name that will be updated. |
| description | string | Yes | The description that will be updated. |

## Return Type

**boolean**

## Example

```javascript
return admUpdateNotificationScheme(10005, "updated notification scheme", "updated description");
```

## See also