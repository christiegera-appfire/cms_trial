# admCreateProject

[Unmapped macro: button-handy — no content to fall back on]

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateProject(key, name, description, projectType, url, category, defaultUser, assign\_to\_def\_user[,permissionScheme, issueSecurityScheme, notificationScheme, fieldConfigScheme, issueTypeScheme, issueTypeScreenScheme, workflowScheme]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createProject(key, name, description, projectType, url, category, defaultUser, assign\_to\_def\_user[,permissionScheme, issueSecurityScheme, notificationScheme, fieldConfigScheme, issueTypeScheme, issueTypeScreenScheme, workflowScheme]) |

## Description

Returns true if the project has been created.

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
| projectType | string | Yes | The project type. The value can be either "business", "service\_desk", or "software". This parameter is required. |
| fieldConfigScheme | string | No | The scheme ID or name. Leave blank if no scheme is available. |
| issueTypeScheme | string | No | The scheme ID or name. Leave blank if no scheme is available. |
| issueTypeScreenScheme | string | No | The scheme ID or name. Leave blank if no scheme is available. |
| workflowScheme | string | No | The scheme ID or name. Leave blank if no scheme is available. |

## Return Type

**Boolean**

Returns true if the project has been created.

## Example

```javascript
use "adm";
persistent int countCMP=0;
string keyprj = "CX"+ countCMP++;
string nameprj= "One very complex project" + countCMP;
boolean ret = createProject(keyprj, nameprj, "For fun", "software", null, null, currentUser(), false,
permissionScheme("Default Permission Scheme").id,
issueSecurityScheme("Simplified Issue Security Scheme").id,
notificationScheme("Default Notification Scheme").id,
null,
issueTypeScheme("Default Issue Type Scheme").id,
issueTypeScreenScheme("Default Issue Type Screen Scheme").id,
workflowScheme("classic").id);
```

## See also

[Unmapped macro: fc909b09-b512-4c31-a844-dd855b0e6aae/db1c8759-c7e5-4e80-9022-d19e47b0e2b0/static/macro — no content to fall back on]