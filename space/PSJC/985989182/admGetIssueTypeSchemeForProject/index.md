# admGetIssueTypeSchemeForProject

## Description

Returns a specific issue type scheme, set on the specified project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetIssueTypeSchemeForProject(pkey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | issueTypeSchemeForProject(pkey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | string | Yes | Project key. |

## Return Type

[**JIssueTypeScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a specific issue type scheme.

## Example

```javascript
JIssueTypeScheme itScheme = admGetIssueTypeSchemeForProject("TT", 11000);
runnerLog("Id: " + itScheme.id);
runnerLog("Name: " + itScheme.name);
runnerLog("Description: " + itScheme.description );
```

## See also