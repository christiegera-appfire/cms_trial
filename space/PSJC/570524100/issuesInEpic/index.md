# issuesInEpic

## Description

Retrieves all the issues or tasks associated with a specific epic, offering an overview of the work items that contribute to the epic's objectives.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issuesInEpic(boardId, epicId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | The board id |
| epicId | Integer | Yes | The epic id |

## Return Type

**String []**

Issue belonging to that epic

## Example

```javascript
string [] issues = issuesInEpic(12345, "TEST-123");
return issues;
```

## See also