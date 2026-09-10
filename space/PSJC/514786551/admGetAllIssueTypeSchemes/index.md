# admGetAllIssueTypeSchemes

## Description

Returns all issue type schemes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllIssueTypeSchemes() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | allIssueTypeSchemes() |

## Return Type

[**JIssueTypeScheme []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns all issue type schemes.

## Example

```javascript
JIssueTypeScheme [] allItSchemes = admGetAllIssueTypeSchemes();
for(JIssueTypeScheme its in allItSchemes) {
    runnerLog("Id: " + its.id);
    runnerLog("Name: " + its.name);
}
```

## See also