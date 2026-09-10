# issuesInBoard

## Description

Retrieves all the issues or tasks that are currently part of a specific board, offering an overview of the work being managed within that board.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issuesInBoard(boardId [, jql]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | Board id |
| jql | String | No | JQL to further filter the returned issues. It is advisable to get only what you need. |

## Return Type

**String []**

Array of issue keys. All the issues in a board.

## Examples

### Example 1

Gets all issues on the board.

```javascript
string [] issues = issuesInBoard(12345);
for(string i in issues) {
     runnerLog(i);
}
```

### Example 2

Gets all issues on the board that are Bugs.

```javascript
string [] bugs = issuesInBoard(12345, "type=Bug");
for(string b in bugs) {
     runnerLog(b);
}
```

## See also