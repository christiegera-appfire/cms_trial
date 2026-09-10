# sprintStartDate

## Description

Retrieves the start date of a specific sprint, marking the beginning of the time-boxed work period.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sprintStartDate(sprint id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprint id | Number | Yes | Sprint id |

## Return Type

**Date**

Returns the start date of the sprint.

## Example

```javascript
date startDate = sprintStartDate(5); // the start date of the sprint with id 5
```

1. If there is no sprint with that id, an empty result will be returned.
2. If there is no start date, an empty result will be returned.

## See also