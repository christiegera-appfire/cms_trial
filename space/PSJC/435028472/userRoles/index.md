# userRoles

## Description

Returns the roles of the provided user in the project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | userRoles(project, user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| project key | String | Yes | Key of the selected project |
| user | String | Yes | The user name of the user that is verified. |

## Return Type

**String []**

Returns a list of roles the user associated with the given user has on the specified project.

## Examples

### Example 1

```javascript
//dev1 has the following roles in the project PRJ: developer, tester, business analyst.
string user;
string[] roles;
user = "dev1";
roles = userRoles(project, user);
print ("The user " + user + "has the following roles in the project" + project + ":");
print(roles);
```

Result: The user dev1 has the following roles in the project PRJ: developer, tester, business analyst. Check the values in log on the next row beginning with <StringPrintFunction>.

### Example 2

```javascript
//current user has the following roles in the project PRJ: developer, tester, business analyst.
string[] roles;
roles = userRoles(project, currentUser());
print ("The current user has the following roles in the project" + project + ":");
print(roles);
```

Result: The current user has the following roles in the project PRJ: developer, tester, business analyst. Check the values in log on the next row beginning with <StringPrintFunction>.

## See also