# closeSprint

## Description

Used to mark a sprint as completed or closed within a Scrum board, typically indicating that the work for that specific time frame has been finished and reviewed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | closeSprint(sprintId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprintId | Integer | Yes | The sprint id |

## Return Type

**Boolean**

Returns true if the sprint is marked as completed.

## Example

```javascript
return closeSprint(12345);
```

Returns true if successful, false if otherwise.

## See also