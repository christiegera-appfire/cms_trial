# addIssueToSprint

## Description

Associates an issue or task with a specific sprint in a Scrum board, indicating that the issue is part of the work to be completed during that sprint.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addIssueToSprint(issue\_key, sprint\_id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue\_key | String | Yes | The issue key |
| sprint\_id | integer | Yes | The sprint id |

## Return Type

**Boolean**

'True' if the operation succeeded, 'false' otherwise.

## Example

```javascript
boolean result = addIssueToSprint("AGILE-3", 5);
```

1. If there is no issue with that issue key, an exception will be raised.
2. If there is no sprint with that sprint id, an exception will be raised.
3. The user must have enough permissions to perform this action.

## See also