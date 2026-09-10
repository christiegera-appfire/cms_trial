# admShareFilter

## Description

Shares a filter. Share types may be 'project', 'projectRole', 'user', 'group', 'loggedin', 'global'.   
The value of the share must reflect either the user id, group id or project key, or an array, pipe separated, of project key and role id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admShareFilter(filterId, rights, sharePerm) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; shareFilter(filterId, rights, sharePerm);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filterId | int | Yes | The filter id |
| rights | int | Yes | The rights. 1 means share. There's not much documentation in Atlassian API about this |
| sharePerm | JSharePermission | Yes | The grantee |

## Return Type

**boolean**

## Example

```javascript
JFilter f = admGetFilterByName(name)[0];
    JSharePermission perm;
    perm.type="project";
    perm.object="TEST";
    
    admShareFilter(f.id, 1, perm);
    
    perm.type="group";
    perm.object="site-admins";
    admShareFilter(f.id, 1, perm);
```

Shares the filter with the project and the group

## See also