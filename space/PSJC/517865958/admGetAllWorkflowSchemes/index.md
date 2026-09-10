# admGetAllWorkflowSchemes

## Description

Returns all workflow schemes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllWorkflowSchemes() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | allWorkflowSchemes() |

## Return Type

[**JWorkflowScheme []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns all workflow schemes.

## Example

```javascript
JWorkflowScheme [] allWorkflowSchemes = admGetAllWorkflowSchemes();
for(JWorkflowScheme jws in allWorkflowSchemes) {
    runnerLog("Id: " + jws.id);
    runnerLog("Name: " + jws.name);
}
```

## See also