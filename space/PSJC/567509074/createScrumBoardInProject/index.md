# createScrumBoardInProject

## Description

Creates a new Scrum board within a project based on a filter.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createScrumBoardInProject(name, filterId, project) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | Board name |
| filterId | Integer | Yes | Filter, make sure the JQL uses the Rank order otherwise you will not be able to rank the issues |
| project | String | Yes | Project key |

## Return Type

**Integer**

Gets the board id. Null if it cannot be created

## Example

Creates a new scrum board in the TEST project and returns the board id.

```javascript
int newBoard = createScrumBoardInProject("New scrum board", 12345, "TEST");
return newBoard;
```

## See also