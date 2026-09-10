# getVersion

## Description

Returns the project version.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getVersion(projectKey, versionName) | **Package** | adm |
| **Alias** | admGetProjectVersion(projectKey, versionName) //deprecated | **Pkg Usage** | getVersion(projectKey, versionName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |
| versionName | String | Yes | Version name. |

## Return Type

[**JVersion**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

All the properties of a version(id, name, description, projectKey, startDate, releaseDate, archived, released).

1. If projectKey or versionName is empty, an error will be raised.
2. If project or version does not exist, an error will be raised.

## See also