# admSetProjectVersionReleaseDate

## Description

Set the release date for a version.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetProjectVersionReleaseDate(projectKey, versionName, releaseDate) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | setVersionRelease(projectKey, versionName, releaseDate) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |
| versionName | String | Yes | Version name. |
| releaseDate | Date | Yes | Release date. |

## Return Type

**string / boolean**

The return type doesn't have a meaning on server. On cloud it will return true if the release date is updated and false otherwise.

1. If projectKey or versionName is empty, an error will be raised.
2. If project or version does not exist, an error will be raised.
3. releaseDate must be a date after the start date, otherwise an error will be raised.

## See also