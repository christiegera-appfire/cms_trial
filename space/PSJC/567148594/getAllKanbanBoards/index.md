# getAllKanbanBoards

## Description

Retrieves a list of all Kanban boards available in a project or system. Kanban boards are used for visualizing and managing work items in a Kanban methodology, typically without defined sprint cycles.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAllKanbanBoards() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JBoard []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns all the boards it can find.

## Example

```javascript
JBoard [] boards = getAllKanbanBoards();
for(JBoard b in boards) {
    runnerLog("Id: " + b.id); 
   runnerLog("Name: " + b.name);
}
```

## See also