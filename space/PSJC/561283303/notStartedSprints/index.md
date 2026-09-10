# notStartedSprints

## Description

Retrieves a list of sprints that have not yet started, helping to identify upcoming work periods that are yet to commence.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | notStartedSprints(board) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| board | Integer | Yes | The board id |

## Return Type

**Integer []**

Returns the future (not started) sprints IDs.

## Example

```javascript
int [] sprintIds = notStartedSprints("agileBoard");
// or
number [] sprintIds = notStartedSprints(2);
```

1. If there is no board with that name or id, an exception will be raised.
2. The user must have sufficient permissions to view the board.

## See also