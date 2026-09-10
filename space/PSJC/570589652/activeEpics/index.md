# activeEpics

## Description

Retrieves a list of currently active epics, helping to identify high-level project goals and initiatives that are currently in progress.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | activeEpics(boardId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | The board id |

## Return Type

[**JEpic []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

The epic structures array

## Example

```javascript
JEpic [] epics = activeEpics(12345);
for(JEpic e in epics) {
     runnerLog(e.name);
}
```

## See also