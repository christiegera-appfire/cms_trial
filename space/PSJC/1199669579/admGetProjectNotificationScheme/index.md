# admGetProjectNotificationScheme

## Description

Returns the name of the issue notification scheme name for the given project key or id

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetProjectNotificationScheme(projectKeyOrId) | **Package** | adm |
| **Alias** | getProjectNotificationScheme | **Pkg Usage** | projectNotifScheme(projectKeyOrId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKeyOrId | string | Yes | The key or the id of the project |

## Return Type

**string**

Returns the name of the issue notification scheme for the project.

## Example

```javascript
return admGetProjectNotificationScheme("TEST");
```

Default Notification Scheme

## See also