# moveIssueToBacklog

## Description

Moves a single issue or task back to the backlog, indicating that it's no longer part of the active work items.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | moveIssueToBacklog(key, boardId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | String | Yes | The issue key you want to move |
| boardId | Integer | Yes | Board id |

## Return Type

**Boolean**

True if the move is ok

## Example

```javascript
return moveIssueToBacklog("TEST-1", 12345);
```

Returns true if successful, false if otherwise.

## See also