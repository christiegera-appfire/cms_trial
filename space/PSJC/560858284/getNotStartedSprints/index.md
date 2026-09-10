# getNotStartedSprints

## Description

Retrieves information about sprints that have not yet started, helping to identify upcoming work periods.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getNotStartedSprints(boardId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | The board id |

## Return Type

[**JSprint []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the future sprints structures.

## Example

```javascript
JSprint [] sprints = getNotStartedSprints(12345);
for(JSprint s in sprints) {
    runnerLog("Id: " + s.id);
    runnerLog("Name: " + s.name);
}
```

1. If there is no board with that name or id, an exception will be raised.
2. The user must have sufficient permissions to view the board.

## See also