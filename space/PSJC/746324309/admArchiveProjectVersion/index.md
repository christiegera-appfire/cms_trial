# admArchiveProjectVersion

## Description

Archives/unarchives a project version.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admArchiveProjectVersion(projectKey, versionName, archive) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | archiveVersion(projectKey, versionName, archive) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |
| versionName | String | Yes | Version name. |
| archive | Boolean (true/false) | Yes | Flag for archive(true) or unarchive(false). |

## Return Type

**String / Boolean**

The return type doesn't have a meaning on server. On cloud it will return true if the version is archived/unarchived and false otherwise.

1. If projectKey or versionName is empty, an error will be raised.
2. If project or version does not exist, an error will be raised.

## See also