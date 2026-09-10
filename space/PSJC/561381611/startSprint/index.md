# startSprint

## Description

Initiates a sprint within a Scrum board, marking the beginning of the sprint's time frame. This action is essential for tracking progress during the sprint.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | startSprint(sprintId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprintId | Integer | Yes | The sprint id |

## Return Type

**Boolean**

Returns true if the sprint is started.

## Example

```javascript
return startSprint(12345);
```

Returns true if successful, false if otherwise.

## See also