# projectPM

## Description

Returns the user key of the project manager (project lead) of the selected project, if exists.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | projectPM(project) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Project key | String | Yes | Key of the selected project. |

## Return Type

**String**

The returned string represents the user key of the project lead.

## Example

```javascript
//Project key of the current project is PRJ
//User name of the project manager is JohnSmith
string PM;
PM = projectPM(project);
print("The project manager of " + project + " project is " + PM);
```

Result: The project manager of PRJ project is JohnSmith.

## See also