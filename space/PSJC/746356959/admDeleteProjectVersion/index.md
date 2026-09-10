# admDeleteProjectVersion

## Description

Deletes a project version from a project. The version is also removed from any issues assigned to the version.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeleteProjectVersion(projectKey, versionName); | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deleteVersion(projectKey, versionName); |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Project Key | String | Yes | Project key of the project containing the version to be deleted. |
| Version Name | String | Yes | Name of the version to be deleted. |

## Return Type

**Boolean**

Returns "true" if operation succeeded.

## Example

```javascript
return admDeleteProjectVersion("TST", "Version 1.5.3.2");
```

Result: true/false

## See also