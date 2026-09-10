# issueInBacklog

## Description

Checks whether a particular issue is currently in the backlog, which is a list of tasks awaiting prioritization and planning.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueInBacklog(boardId, issue\_key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | Board id |
| issue\_key | String | Yes | The issue key you want to check |

## Return Type

**Boolean**

True if it's in the backlog, false otherwise

## Example

```javascript
return issueInBacklog(12345, "TEST-123");
```

Returns true if issue exists in the backlog, false otherwise.

## See also