# getAllScrumBoards

## Description

Retrieves a list of all Scrum boards within a project or system. Scrum boards are used for managing work items in the context of Scrum methodology, which includes defined sprint cycles.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAllScrumBoards() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JBoard []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns all the boards it can find.

## Example

```javascript
JBoard [] boards = getAllScrumBoards();
for(JBoard b in boards) {
    runnerLog("Id: " + b.id); 
   runnerLog("Name: " + b.name);
}
```

## See also