# allGroups

## Description

Returns the list of group names that exist in the Jira environment.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | allGroups() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**String []**

The requested names of all groups.

## Example

```javascript
string[] groups = allGroups();
for(string gName in groups) {
    runnerLog(gName);
}
```

## See also