# admReleaseProjectVersion

## Description

Rleases/unrelease a project version.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admReleaseProjectVersion(projectKey, versionName, release) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | releaseVersion(projectKey, versionName, release) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |
| versionName | String | Yes | Version name. |
| release | Boolean (true/false) | Yes | Flag for release(true) or unrelease(false). |

## Return Type

**string / boolean**

The return type doesn't have a meaning on server. On cloud it will return true if the version is release/unreleased and false otherwise.

1. If projectKey or versionName is empty, an error will be raised.
2. If project or version does not exist, an error will be raised.

## See also