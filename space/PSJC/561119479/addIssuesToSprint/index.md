# addIssuesToSprint

## Description

Associates multiple issues or tasks with a specific sprint, indicating that these tasks are part of the work to be completed during that sprint.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addIssuesToSprint(issue\_keys\_array, sprintId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue\_keys\_array | String [] | Yes | The issue keys |
| sprintId | integer | Yes | The sprint |

## Return Type

**Boolean**

Returns a boolean telling you if the issues were added in the sprint

## Example

```javascript
string [] issues = "TEST-1|TEST-2|TEST-3";
return addIssuesToSprint(issues, 12345);
```

Returns true if successful, false if otherwise.

## See also