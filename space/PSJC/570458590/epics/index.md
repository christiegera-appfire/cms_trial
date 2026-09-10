# epics

## Description

Retrieves a list of all the epics within a project or system, helping to manage and track high-level project goals and initiatives.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | epics(boardId) | **Package** |  |
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
JEpic [] epics = epics(12345);
for(JEpic e in epics) {
     runnerLog(e.name);
}
```

## See also