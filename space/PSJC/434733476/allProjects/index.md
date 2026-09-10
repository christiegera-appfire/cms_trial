# allProjects

## Description

Returns a string array with the keys of all the projects in Jira.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | allProjects() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**String []**

Returns a list of **keys** for all the projects in Jira.

## Example

```javascript
string [] projects = allProjects();
print(projects);
```

Results: prints a list with all the project keys in Jira. If we have 2 projects PRJ and TST, the logs will show PRJ|TST

## See also