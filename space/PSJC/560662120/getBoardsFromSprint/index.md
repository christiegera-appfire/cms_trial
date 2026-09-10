# getBoardsFromSprint

## Description

Retrieves the boards that are associated with a specific sprint.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getBoardsFromSprint(sprintId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Sprint Id | Integer | Yes | The id of the sprint to retrieve boards for. |

## Return Type

**Integer []**

## Example

```javascript
return getBoardsFromSprint(101);
```

Result: Returns an array of board names "Test Board 1|Test Board 2|Test Board 3".

## See also