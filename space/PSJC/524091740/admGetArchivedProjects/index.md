# admGetArchivedProjects

## Description

This function returns the list of archived projects.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetArchivedProjects() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | archivedProjects() |

## Return Type

**string []**

Returns and array of project keys.

## Example

```javascript
string [] archivedProjects = admGetArchivedProjects();
for(string ap in archivedProjects) {
	runnerLog(ap);
}
```

## See also