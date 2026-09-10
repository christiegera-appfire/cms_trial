# admUpdateProject

## Description

Returns true if the project is updated.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateProject(key, name, description, url, category, defaultUser, assign\_to\_def\_user[, permissionScheme, issueSecurityScheme, notificationScheme]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updateProject(key, name, description, url, category, defaultUser, assign\_to\_def\_user[, permissionScheme, issueSecurityScheme, notificationScheme]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | string | Yes | The project key. The value must be unique. |
| name | string | Yes | The project name. The value must be unique. |
| description | string | Yes | The project description. |
| url | string | Yes | The project URL. Leave blank if no URL is available. |
| category | string | Yes | The project category. Leave blank if no category is available. |
| defaultUser | string | Yes | The default project assignee. |
| assign\_to\_def\_user | boolean | Yes | Set to true to assign issues to the user by default. In this case, you must specify a user. |
| permissionScheme | string | No | The permission scheme ID or name. Leave blank if no permission scheme is available. |
| issueSecurityScheme | string | No | The issue security scheme ID or name. Leave blank if no issue security scheme is available. |
| notificationScheme | string | No | The notification scheme ID or name. Leave blank if no notification scheme is available. |

## Return Type

**Boolean**

Returns true if the project is updated.

## Example

```javascript
use "adm";
persistent int countCMP=0;
string keyprj = "CX"+ countCMP++;
string nameprj= "One very complex project" + countCMP;
boolean retUpd = updateProject(keyprj, nameprj, "another fun description", "https://goggle.com", null, currentUser(), true,
permissionScheme("Default Permission Scheme").id,
issueSecurityScheme("Simplified Issue Security Scheme").id,
notificationScheme("Default Notification Scheme").id);
```

## See also