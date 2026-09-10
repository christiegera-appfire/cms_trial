# ldapUserAttr

## Description

Returns an array of the requested attribute. This is an LDAP search function. It gets the LDAP record and shows the attribute of that user. Returned user must be unique otherwise exception occurs. You can retrieve any attribute defined in the scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | ldapUserAttr(attrib, ldapQuery[, ldapName]) | **Package** | ldap |
| **Alias** | ldapUserRecord(attrib, ldapQuery) //deprecated | **Pkg Usage** | userAttr(attrib, ldapQuery[, ldapName]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| attrib | String | Yes | Attribute to be returned. |
| ldapQuery | String | Yes | Query, must return exactly one result. |
| ldapName | String | No | Optional, stating with version 4.0, you can specify the LDAP server that must be searched. If missing, it's the default LDAP server. |

## Return Type

**String []**

The values of the specified attribute. If the attribute only has one value, the array will contain only one element, but will still be an array and not a single string.

## Example

### Open DS Example

```javascript
string email = ldapUserAttr("mail", "(&(uid=user.1)(objectClass=inetOrgPerson))");
string address = ldapUserAttr("postalAddress", "(&(uid=user.1)(objectClass=inetOrgPerson))");
```

LDAP must be configured. See [LDAP configuration](/cms_trial/space/PSJC/490995973/LDAP+configuration/) page.  
Only Microsoft Active Directory is supported at this time, but it might work with other as well (tested with OpenDS). To provide support for other LDAP types [contact us.](https://appfire.atlassian.net/servicedesk/customer/portal/11)

## See also