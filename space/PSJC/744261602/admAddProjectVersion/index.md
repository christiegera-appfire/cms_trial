# admAddProjectVersion

## Description

Adds a version in the project

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddProjectVersion(pkey, versionName, versionDescription, releaseDate) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addVersion(pkey, versionName, versionDescription, releaseDate) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | String | Yes | Project key. |
| versionName | String | Yes | Version name. |
| versionDescription | String | Yes | Description. |
| releaseDate | Date | Yes | Release date. |

## Return Type

**Boolean (true/false)**

Returns 'true' if the version was added and 'false' otherwise.

It doesn't check if a version with the same name already exists. So far, Jira controller code allows the project version creation action.

## See also