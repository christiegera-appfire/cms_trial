# admSetProjectVersionStartDate

## Description

Set the start date for a version.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetProjectVersionStartDate(projectKey, versionName, startDate) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | setVersionStart(projectKey, versionName, startDate) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |
| versionName | String | Yes | Version name. |
| startDate | Date | Yes | Start date. |

## Return Type

**string / boolean**

The return type doesn't have a meaning on server. On cloud it will return true if the release date is updated and false otherwise.

1. If projectKey or versionName is empty, an error will be raised.
2. If project or version does not exist, an error will be raised.
3. startDate must be a date before the release date, otherwise an error will be raised.

## See also