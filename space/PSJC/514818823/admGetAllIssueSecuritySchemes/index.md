# admGetAllIssueSecuritySchemes

## Description

Retrieves all security schemes for a specific issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllIssueSecuritySchemes() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | allIssueSecuritySchemes() |

## Return Type

[**JIssueSecurityScheme []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JIssueSecurityScheme [] allIsSchemes = admGetAllIssueSecuritySchemes();
for(JIssueSecurityScheme iss in allIsSchemes) {
    runnerLog("Id: " + iss.id);
    runnerLog("Name: " + iss.name);
}
```

## See also