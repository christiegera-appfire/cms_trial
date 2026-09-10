# usersInRole

## Description

Returns the users that corespond to a certain role on the specified project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | usersInRole(project, role) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Project key | String | Yes | Key of the selected project. |
| Role name | String | Yes | Name of the role that is verified. |

## Return Type

**String []**

Returns a list with the usernames of the users who have the given role on the specified project.

## Examples

```javascript
//The following users have the role developer in the project PRJ: dev1, dev2, dev3.
string role;
string[] userbyrole;
role = "developer";
userbyrole = usersInRole(project, role);
print ("The following users have the role " + role + " in the project" + project + ":");
print(userbyrole);
```

Result:The following users have the role developer in the project PRJ: dev1, dev2, dev3. Check the following row beginning with <StringPrintFunction> for the values.

## See also