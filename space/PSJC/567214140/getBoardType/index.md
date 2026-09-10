# getBoardType

## Description

Retrieves the type or category of a specific board, such as whether it's a Scrum board or a Kanban board, providing information about the board's methodology.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getBoardType(boardId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | Board id |

## Return Type

**String**

Gets the board type (scrum, kanban, simple)

## Example

```javascript
return getBoardType(12345);
```

## See also