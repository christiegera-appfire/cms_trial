# projectMembers

## Description

Returns a list with all the user keys of the users who have a role in the specified project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | projectMembers(project) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| project key | String | Yes | Key of the project that is selected. |

## Return Type

**String []**

The return value is a list of user keys for the users who have a role on the specified project.

## Example

```javascript
//The current project key = PRJ1
//The users from the current project: Admin, Dev1, Dev2, Dev3, Test1, Test2, PM, BA1
print("The members of the project " + project + " are:");
print(projectMembers(project));
```

Result: Returns the following text: The members of the project PRJ1 are: Admin, Dev1, Dev2, Dev3, Test1, Test2, PM, BA1*.* Check the values on the next row beginning with <StringPrintFunction>.

## See also