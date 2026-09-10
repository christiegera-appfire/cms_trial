# admSetProjectNotificationScheme

## Description

Updates the notification scheme to the given one. Return true if success, false otherwise

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetProjectNotificationScheme(projectKey, schemeName) | **Package** | adm |
| **Alias** | setProjectNotificationScheme | **Pkg Usage** | setProjectNotifScheme(projectKey, schemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | The project key |
| schemeName | string | Yes | The name of the scheme to be set |

## Return Type

**Boolean (true/false)**

Returns true if the scheme was set and false otherwise.

## Example

```javascript
admSetProjectNotificationScheme("ITSD","Notification sch");
```

## See also