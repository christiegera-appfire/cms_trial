# admCreatePriorityScheme

## Description

Creates a new priority scheme with the data provided in the parameters

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreatePriorityScheme(name, description, defaultPriorityId, priorityIds) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createPriorityScheme(name, description, defaultPriorityId, priorityIds) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the priority scheme. Must be unique |
| description | string | Yes | The description of the priority scheme. |
| defaultPriorityId | number | Yes | The id of the default priority for the priority scheme. |
| priorityIds | number [] | Yes | The ids of priorities in the scheme. |

## Return Type

**number**

Returns the id of the scheme created.

## Example

### Example 1

Creates a new priority scheme named "New priority scheme", with the default priority the one with id 1 and the priorities with ids 1, 2, 3

```javascript
admCreatePriorityScheme("New priority scheme", "new scheme description", 1, {1, 2, 3});
```

return true;

## See also