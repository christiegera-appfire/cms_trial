# admCreatePermissionGrant

## Description

Creates a new permission grant.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreatePermissionGrant(schemeId, newPermissionGrantStruct) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createPermissionGrant(schemeId, newPermissionGrantStruct) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | integer | Yes | The id of the scheme where the grant will be added. |
| newPermissionGrant | JPermissionGrant | Yes | The structure of the permission grant to be created. |

## Return Type

[**JPermissionGrant**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

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
return admCreatePermissionGrant(10012, grant);
```

## See also