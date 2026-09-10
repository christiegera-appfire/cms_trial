# projectsForBoard

## Description

Retrieves the projects associated with a specific board, providing information about which projects the board is linked to.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | projectsForBoard(boardId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | Board id |

## Return Type

**String []**

Gets the board projects keys

## Example

```javascript
string [] projects = projectsForBoard(boardId);
return projects;
```

## See also