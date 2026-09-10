# admRemovePrioritiesFromPriorityScheme

## Description

Removes the given priorities from the priority scheme, mapping the issues with deleted priorities

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admRemovePrioritiesFromPriorityScheme(schemeName, priorityIdsOrNames, priorityIdsMapping) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | removePrioritiesFromPriorityScheme(schemeName, priorityIdsOrNames, priorityIdsMapping) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeName | string | Yes | The name of the priority scheme from where the priorities should be removed |
| priorityIdsOrNames | string[] | Yes | The list of priorities to be removed |
| priorityIdsMapping | number [] | Yes | The mapping of priorities for issues being migrated into this priority scheme. Key is the old priority ID, value is the new priority ID (must exist in this priority scheme). |

## Return Type

**boolean**

Returns true if the priorities were removed, false otherwise.

## Example

### Example 1

Removes the priority named with ids 5 and 2 from "New priority scheme". The issues that have priority 5 will have priority 1 and the ones with 2 will be migrated to 3.

```javascript
admRemovePrioritiesFromPriorityScheme("test", {"5", "2"}, {"5", "1", "2", "3"});
```

## See also