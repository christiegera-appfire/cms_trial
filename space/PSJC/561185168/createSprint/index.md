# createSprint

## Description

Used to create a new sprint within a Scrum board. Sprints are time-boxed periods during which a team works on a specific set of work items to achieve project goals.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createSprint(boardId, sprintName [,goal [,startDate, endDate]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | The board id |
| sprintName | String | Yes | The sprint name. Must have some value |
| goal | String | No | The sprint goal |
| startDate | date | No | The sprint start date |
| endDate | date | No | The sprint end date |

## Return Type

**Integer**

Returns the id of the created sprint, or an invalid value if the sprint is not created.

## Example

```javascript
return createSprint(12345, "Sprint 17", "Get some work done", currentDate(), currentDate() + "2w");
```

## See also