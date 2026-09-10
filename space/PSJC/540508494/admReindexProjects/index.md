# admReindexProjects

## Description

Triggers a re-index of a Jira instance for the specified projects only.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admReindexProjects(projects) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | reindexProjects(projects) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projects | String | Yes | Array of project keys to be re-indexed. |

## Return Type

**boolean**

Returns 'true' if the re-index succeeds and 'false' if a certain exception appears.

## See also