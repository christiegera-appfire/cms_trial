# sprintCompleteDate

## Description

Retrieves the completion date of a specific sprint, indicating when the sprint's work was finished and reviewed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sprintCompleteDate(sprint id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprint id | Number | Yes | The sprint id |

## Return Type

**Date**

Returns the complete date of the sprint.

## Example

```javascript
date completeDate = sprintCompleteDate(5); // the complete date of the sprint with id 5
```

1. If there is no board with that name or id, an exception will be raised.
2. The user must have sufficient permissions to view the board.

## See also