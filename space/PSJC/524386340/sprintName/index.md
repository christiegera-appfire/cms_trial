# sprintName

## Description

Retrieves the name or title of a specific sprint, which is a time-boxed period used in Agile project management for completing work within a specified timeframe.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sprintName(sprint\_id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprint id | Number | Yes | The Sprint id |

## Return Type

**String**

Returns the name of the sprint.

## Example

```javascript
string name = sprintName(5); // the name of the sprint with id 5
```

If there is no sprint with that id, an empty string will be returned.

## See also