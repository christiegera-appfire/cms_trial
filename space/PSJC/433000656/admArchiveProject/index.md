# admArchiveProject

## Description

Archives a project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admArchiveProject(projectKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | archiveProject(projectKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key of project to archive. |

## Return Type

**Boolean**

Returns 'true' if operation succeeded and 'false' otherwise.

## Example

```javascript
admArchiveProject("TSTPROJ");
```

Returns: true

## See also