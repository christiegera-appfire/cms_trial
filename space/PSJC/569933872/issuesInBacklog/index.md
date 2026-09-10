# issuesInBacklog

## Description

Retrieves the issues or tasks located in the backlog, which is a list of work items awaiting prioritization and planning.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issuesInBacklog(boardId [, jql]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | Board id |
| jql | String | No | JQL to further filter the returned issues. It is advisable to get only what you need. |

## Return Type

**String []**

Array of issue keys. All the issues in a backlog.

## Examples

### Example 1

Gets all issues in the backlog.

```javascript
string [] issues = issuesInBacklog(12345);
for(string i in issues) {
     runnerLog(i);
}
```

### Example 2

Gets all issues in the backlog that are Bugs.

```javascript
string [] bugs = issuesInBacklog(12345, "type=Bug");
for(string b in bugs) {
     runnerLog(b);
}
```

## See also