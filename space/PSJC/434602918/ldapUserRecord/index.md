# ldapUserRecord

## Description

Returns an array of the requested attribute. This is a LDAP search function. The second function syntax is more comfortable. Both get the LDAP record and shows the attribute of that user. Returned user must be unique, otherwise exception occurs.

Allowed attributes are (these are **case sensitive**):

- CN
- DN
- firstName
- lastName
- displayName
- title
- department
- division
- officeName (mapped on physicalDeliveryOfficeName attribute)
- company
- empID
- manager
- mail
- otherMailbox
- mobile
- homePhone
- workPhone
- userPrincipalName
- winPrincipalName

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | ldapUserRecord(attrib, ldapQuery) | **Package** | ldap |
| **Alias** | ldapUserRecord(attrib, cn, dn, memberof, email, ldapObjectClass) //deprecated | **Pkg Usage** | userRecord(attrib, ldapQuery) |

This syntax is deprecated and you should use the new alias name: [ldapUserAttr](/cms_trial/space/PSJC/434995660/ldapUserAttr/) instead.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| attrib | String | Yes | Attribute to be returned. |
| ldapQuery | String | Yes | Query, must return exactly one result. |

## Return Type

**String []**

The values of the specified attribute. If the attribute only has one value, the array will contain only one element, but will still be an array and not a single string.

## Examples

### Example

```javascript
ldapUserRecord("mobile", user, "", "", "", "user");
//gets the mobile attribute from LDAP user with specified CN
```

### OpenDS example

```javascript
string email = ldapUserRecord("mail", "(&(uid=user.1)(objectClass=inetOrgPerson))");
         string address = ldapUserRecord("postalAddress", "(&(uid=user.1)(objectClass=inetOrgPerson))");
```

LDAP must be configured. See [LDAP configuration](/cms_trial/space/PSJC/490995973/LDAP+configuration/) page.

Only Microsoft Active Directory is supported at this time, but it might work with other as well (tested with OpenDS). To provide support for other LDAP types [contact us.](https://appfire.atlassian.net/servicedesk/customer/portal/11)

## See also