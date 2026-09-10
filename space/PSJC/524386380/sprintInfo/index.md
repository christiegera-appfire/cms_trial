# sprintInfo

## Description

Provides detailed information about a specific sprint.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sprintInfo(sprint\_id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprint id | Number | Yes | The sprint id |

## Return Type

**String []**

Returns name, startDate, endDate, and completeDate of the sprint.

## Example

```javascript
string [] info = sprintInfo(5);
string name = info["name"]; // the name of the sprint with id 5
```

If there is no sprint with such id, an empty string array will be returned.

## See also