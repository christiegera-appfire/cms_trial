# getVersions

## Description

Returns the project versions (all).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getVersions(pkey) | **Package** | adm |
| **Alias** | admGetProjectVersions(pkey) //deprecated | **Pkg Usage** | getVersions(pkey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | String | Yes | Project key. |

## Return Type

**String []**

All the project versions, unsorted, as returned by the underlying Jira layer. The meaning that v2 comes after v1.3 is to be addressed in the script, not in this function.

## See also