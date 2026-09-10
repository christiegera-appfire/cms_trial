# ldapUserStruct

## Description

Returns an array of JLdapUserStruct representing all users matched by the query.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | ldapUserStruct(ldapQuery[, ldapName]) | **Package** | ldap |
| **Alias** |  | **Pkg Usage** | userStruct(ldapQuery[, ldapName]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| ldapQuery | String | Yes | Query, must return exactly one result. |
| ldapName | String | No | Optional, starting with version 4.0, you can specify the LDAP server that must be searched. If missing, it's the default LDAP server. |

## Return Type

[**JLdapUserStruct []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Each element in the array represents a user. The attributes field of the JLdapUserStruct is also keyed by the attribute name for easy access to attributes. Each attribute is a JLdapUserAttribute. The "value" field of the attribute is a string array. If the attribute only has one value, the array will contain only one element, but will still be an array and not a single string.

## Example

### OpenDS Example

```javascript
JLdapUserStruct [] users = ldapUserStruct("objectClass=inetOrgPerson");
for(JLdapUserStruct u in users) {
    print(u.DN);
    for(JLdapUserAttribute attr in u.attributes) {
        print(attr.name + " = " + attr.value);
    }
    print("ID is : " + u.attributes["uid"].value);
}
```

LDAP must be configured. See [LDAP configuration](/cms_trial/space/PSJC/490995973/LDAP+configuration/) page.  
Only Microsoft Active Directory is supported at this time, but it might work with other as well (tested with OpenDS). To provide support for other LDAP types [contact us.](https://appfire.atlassian.net/servicedesk/customer/portal/11)

## See also