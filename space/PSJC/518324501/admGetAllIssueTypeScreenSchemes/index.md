# admGetAllIssueTypeScreenSchemes

## Description

Returns all issue type schemes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllIssueTypeScreenSchemes() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | allIssueTypeScreenSchemes() |

## Return Type

[**JIssueTypeScreenScheme []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns all issue type schemes.

## Example

```javascript
JIssueTypeScreenScheme [] allItsSchemes = admGetAllIssueTypeScreenSchemes();
for(JIssueTypeScreenScheme itss in allItsSchemes) {
    runnerLog("Id: " + itss.id);
    runnerLog("Name: " + itss.name);
}
```

## See also