# sprintEndDate

## Description

Retrieves the end date of a specific sprint, which marks the conclusion of the time-boxed work period.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sprintEndDate(sprint id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprint id | Number | Yes | Sprint id |

## Return Type

**date**

## Example

```javascript
date endDate = sprintEndDate(5); // the end date of the sprint with id 5
```

1. If there is no sprint with that id, an exception will be raised.
2. The user must have sufficient permissions to view the board.

## See also