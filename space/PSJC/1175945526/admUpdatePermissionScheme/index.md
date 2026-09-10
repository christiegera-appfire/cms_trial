# admUpdatePermissionScheme

## Description

Updates an existing permission scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdatePermissionScheme(schemeId, updPermissionStruct) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updatePermissionScheme(schemeId, updPermissionStruct) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | integer | Yes | The id of the scheme to be updated. |
| updPermissionStruct | JPermissionScheme | Yes | The updated structure of the scheme. |

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
permission.description = "updated scheme description";
permission.permissions = grants;
return admUpdatePermissionScheme(10011, permission);
```

## See also