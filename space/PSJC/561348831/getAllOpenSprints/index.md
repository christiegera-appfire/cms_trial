# getAllOpenSprints

## Description

Retrieves a list of all open or active sprints within a project, offering an overview of ongoing sprint activities.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAllOpenSprints(boardId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | The board id |

## Return Type

**JSprint []**

Returns the future and active sprints structures.

## Example

```javascript
JSprint [] sprints = getAllOpenSprints(12345);
for(JSprint s in sprints) {
    runnerLog("Id: " + s.id);
    runnerLog("Name: " + s.name);
}
```

1. If there is no board with that name or id, an exception will be raised.
2. The user must have sufficient permissions to view the board.

## See also