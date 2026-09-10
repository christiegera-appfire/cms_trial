# admRemoveProjectsFromPriorityScheme

## Description

Removes the given projects from the priority scheme, mapping the issues with deleted priorities

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admRemoveProjectsFromPriorityScheme(schemeName, projectKeys, priorityIdsMapping) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | removeProjectsFromPriorityScheme(schemeName, projectKeys, priorityIdsMapping) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeName | string | Yes | The name of the priority scheme from where the priorities should be removed |
| projectKeys | string[] | Yes | The list of projects to be removed |
| priorityIdsMapping | number [] | Yes | The mapping of priorities for issues being migrated out of this priority scheme. Key is the old priority ID (must exist in this priority scheme), value is the new priority ID (must exist in the default priority scheme). Required for updating an existing priority scheme. Not used when creating a new priority scheme. |

## Return Type

**boolean**

Returns true if the projects were removed, false otherwise.

## Example

### Example 1

Removes the projects with keys "DEMO" and "ITSD" from "New priority scheme". The issues that have priority 3 will have priority 10001.

```javascript
admRemoveProjectsFromPriorityScheme( "New priority scheme", {"DEMO", "ITSD"}, {"3", "10001"});
```

## See also