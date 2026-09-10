# issueTypesForProject

## Description

Retrieves the issue types for the project with the given key.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueTypesForProject(projectKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key |

## Return Type

**String[]**

The return value is a string array containing all the issue types available for the given project.

## Example

```javascript
return issueTypesForProject("TST");
```

Result: Improvement|Task|Sub-task|New Feature|Bug|Epic|Story|Symptom

## See also