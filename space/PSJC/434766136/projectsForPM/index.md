# projectsForPM

## Description

Returns all the projects the selected user has the role of project manager (project lead) in.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | projectsForPM(user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| user name | String | Yes | User name of the user that is verified. |

## Return Type

**String []**

Returns a list of project keys the project lead is a specified user for.

## Examples

```javascript
//user "Admin" has the role of project manager in the following projects: PRJ3, PRJ5, PRJ6.
string projects = projectsForPM("Admin");
print("You have the role of project manager on the following projects: ");
print(projects);
```

Results: The following string is returned: You have the role of project manager on the following projects: PRJ3, PRJ5, PRJ6.

```javascript
projectsForPM(currentUser());
```

Results: Returns an array containing the keys of all the projects where the user has the role of project manager.

If there are no results to the invoking of the function the return value will be an empty array.

## See also