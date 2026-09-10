# admUnArchiveProject

## Description

Restores a previously archived project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUnArchiveProject(projectKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | unarchiveProject(projectKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key of project to restore. |

## Return Type

**Boolean**

Returns 'true' if operation succeeded and 'false' otherwise.

## Example

```javascript
admUnArchiveProject("TSTPROJ");
```

Returns: true

## See also