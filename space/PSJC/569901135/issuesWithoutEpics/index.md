# issuesWithoutEpics

## Description

Retrieves a list of issues or tasks that are not associated with any epics, helping to identify work items that are not part of larger project goals.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issuesWithoutEpics(boardId [, jql]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | Board id |
| jql | String | No | JQL to further filter the returned issues. It is advisable to get only what you need. |

## Return Type

**String []**

Array of issue keys. All the issues in a backlog.

## Example

Returns all issues on a board without an epic that have an issue type of Story.

```javascript
string [] orphans = issuesWithoutEpics(12345, "type=Story");
return orphans;
```

## See also