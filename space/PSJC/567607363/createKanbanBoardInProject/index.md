# createKanbanBoardInProject

## Description

Creates a new Kanban board within a project based on a filter.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createKanbanBoardInProject(name, filterId, project) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | Board name |
| filterId | Integer | Yes | Filter id, mandatory |
| project | String | Yes | Project key |

## Return Type

**Integer**

Gets the board id. Null if it cannot be created

## Example

Creates a new kanban board in the TEST project and returns the board id.

```javascript
int newBoard = createKanbanBoardInProject("New kanban board", 12345, "TEST");
return newBoard;
```

## See also