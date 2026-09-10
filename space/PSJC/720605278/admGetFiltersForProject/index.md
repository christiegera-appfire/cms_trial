# admGetFiltersForProject

## Description

Gets all the filters matching a project in the share list.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetFiltersForProject(projectKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; filtersForProject(projectKey);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | The key of the project |

## Return Type

[**JFilter []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFilter [] filters = admGetFiltersForProject("TEST");
```

Gets all the filters for that project key

## See also