# closedSprints

## Description

Retrieves a list of sprints that have been completed and closed, offering a summary of past sprint data.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | closedSprints(board) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| board | Integer | Yes | The board id |

## Return Type

**Integer []**

Returns the closed sprints IDs.

## Example

```javascript
int [] sprintIds = closedSprints("agileBoard");
// or
number [] sprintIds = closedSprints(2);
```

1. If there is no board with that name or id, an exception will be raised.
2. The user must have sufficient permissions to view the board.

## See also