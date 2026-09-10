# createKanbanBoardForUser

## Description

Creates a Kanban board customized for a specific user, typically allowing users to set up their own Kanban boards tailored to their preferences and work style.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createKanbanBoardForUser(name, filterId, user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | Board name |
| filterId | Integer | Yes | Filter id, mandatory |
| user | String | Yes | account id of the user for which you are creating the board |

## Return Type

**Integer**

Gets the board id. Null if it cannot be created

## Example

Creates a new kanban board for the user "joeUser".

```javascript
int newBoard = createKanbanBoardForUser("New board for Joe", 12345, "joeUser");
return newBoard;
```

## See also