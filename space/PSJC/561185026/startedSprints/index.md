# startedSprints

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | startedSprints(board) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Description

Retrieves a list of sprints that are currently in progress, giving an overview of ongoing work periods.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| board | Integer | Yes | The board id |

## Return Type

**Integer []**

## Example

```javascript
int [] sprintIds = startedSprints("agileBoard");
// or
number [] sprintIds = startedSprints(2);
```

1. If there is no board with that id, an exception will be raised.
2. The user must have sufficient permissions to view the board.

## See also