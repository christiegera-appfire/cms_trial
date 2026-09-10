# deleteSprint

## Description

Used to remove a specific sprint from a Scrum board. Deleting a sprint is typically done when a sprint is no longer relevant or needs to be replaced.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteSprint(sprintId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprintId | Integer | Yes | The sprint id |

## Return Type

**Boolean**

Returns true if the sprint is deleted.

## Example

```javascript
return deleteSprint(12345);
```

Returns true if successful, false if otherwise.

## See also