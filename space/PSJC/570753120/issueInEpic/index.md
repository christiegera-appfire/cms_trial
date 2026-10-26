# issueInEpic

## Description

Checks whether a specific issue or task is associated with a particular epic, helping to determine the relationship between individual tasks and larger project goals.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueInEpic(boardId, epicId, issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | The board id |
| epicId | Integer | Yes | The epic id |
| issueKey | String | Yes | The key of the issue |

## Return Type

**Boolean**

True if the issue belongs to that epic, false otherwise

## Example

```javascript
return issueInEpic(12345, "TEST-123", "TEST-5");
```

## See also