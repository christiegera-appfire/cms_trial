# ldapUserList

## Description

Returns an array of the requested attributes for all users matching the query. This is an LDAP search function.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | ldapUserList(attributes, ldapQuery[, ldapName]) | **Package** | ldap |
| **Alias** |  | **Pkg Usage** | userList(attributes, ldapQuery[, ldapName]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| attributes | String [] | Yes | Attributes to be returned. |
| ldapQuery | String | Yes | Query. |
| ldapName | String | No | LDAP server name that you have configured. If missing, it directs the query to the default LDAP server. This parameter appears at version 4.0. |

## Return Type

**String []**

The values of the attributes for all users in multiples of N, where N is the number of requested attributes.  
The length of the returned array will be N x M. N = number of attributes requested, M = number of users matching the query. Therefore, element at index **i** is the value of the attribute at position **i%N** from the attributes array for the **(i/N)****th**user matching the query.

## Examples

```javascript
return ldapUserList({"cn", "uid"}, "objectClass=inetOrgPerson");
         //example return value: Aaron Atrc|user.3|Aarika Atpco|user.2|Aaren Atp|user.1|Aartjan Aalders|user.4|Aaccf Amar|user.0
         // contains cn,uid for the 5 users matching the filter: cn1,uid1,cn2,uid2,cn3,uid3...
```

Instead of exploiting the result as an array of strings, you may map it on some structure. Following code represents the above example:

```javascript
struct mystruct { 
         string cn;
         string uid;
     }
     mystruct [] arr = ldapUserList ( {"cn", "uid"}, "objectClass=inetOrgPerson");
     //now you can access it by:
     string x = arr[0].cn; //life is better, huh ?
```

LDAP must be configured. See [LDAP configuration](/cms_trial/space/PSJC/490995973/LDAP+configuration/) page.

Only Microsoft Active Directory is supported at this time, but it might work with other as well (tested with OpenDS). To provide support for other LDAP types [contact us.](https://appfire.atlassian.net/servicedesk/customer/portal/11)

## See also