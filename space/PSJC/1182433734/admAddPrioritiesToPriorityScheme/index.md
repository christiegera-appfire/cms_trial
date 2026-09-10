# admAddPrioritiesToPriorityScheme

## Description

Adds the given list of priorities to the given priority scheme

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddPrioritiesToPriorityScheme(schemeName, priorityIdsOrNames) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addPrioritiesToPriorityScheme(schemeName, priorityIdsOrNames) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeName | string | Yes | The name of the priority scheme |
| priorityIdsOrNames | string [] | Yes | The list of ids or names of the priorities to be added |

## Return Type

**boolean**

Returns true if the priorities were added, false otherwise.

## Examples

### Example 1

Adds priorities with ids 1 and 5 to the priority scheme named "Default priority scheme"

```javascript
admAddPrioritiesToPriorityScheme("Default priority scheme", {"1", "5"});
```

### Example 2

Adds priorities with names "High" and "Medium" to the priority scheme named "Default priority scheme"

```javascript
admAddPrioritiesToPriorityScheme("Default priority scheme", {"High", "Medium"});
```

## See also