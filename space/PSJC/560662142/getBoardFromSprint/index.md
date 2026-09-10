# getBoardFromSprint

## Description

Retrieves the board associated with a specific sprint, allowing you to determine which board is managing the tasks for that sprint.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getBoardsFromSprint(sprintId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Sprint Id | Integer | Yes | The id of the sprint to retrieve boards for. |

## Return Type

**Integer**

## Example

```javascript
return getBoardFromSprint(101);
```

Result: Returns the id of the sprint.

## See also