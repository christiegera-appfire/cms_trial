# getAllBoards

## Description

Retrieves a list of all boards within a project or system, offering an overview of the available boards and their respective purposes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAllBoards() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JBoard []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns all the boards it can find.

## Example

```javascript
JBoard [] boards = getAllBoards();
for(JBoard b in boards) {
    runnerLog("Id: " + b.id); 
   runnerLog("Name: " + b.name);
}
```

## See also