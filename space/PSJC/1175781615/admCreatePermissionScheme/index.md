# admCreatePermissionScheme

## Description

Creates a new permission scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreatePermissionScheme(newPermissionStruct) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createPermissionScheme(newPermissionStruct) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| newPermissionStruct | JPermissionScheme | Yes | The structure of the scheme to be created. |

## Return Type

[**JPermissionScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JPermissionHolder holder; //https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permission-schemes/#api-rest-api-3-permissionscheme-get
// holder.parameter = "jira-software-users"; //groupName
holder.type = "group"; //type
holder.value = "be844d8e-13f1-43ea-b70b-bf690c23e3b2"; //groupId
JPermissionGrant[] grants;
JPermissionGrant grant;
grant.holder = holder;
grant.permission = "ADMINISTER_PROJECTS";
grants = arrayAddElement(grants, grant);
JPermissionScheme permission;
permission.name = "new scheme";
permission.description = "new scheme description";
permission.permissions = grants;
return admCreatePermissionScheme(permission);
```

## See also