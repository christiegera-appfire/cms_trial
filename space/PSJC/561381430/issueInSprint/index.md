# issueInSprint

## Description

Checks if a specific issue or task is associated with a particular sprint, helping to determine the relationship between individual tasks and sprint goals.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueInSprint(issue key, sprint id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | The issue key |
| sprint id | Integer | Yes | The sprint id |

## Return Type

**Boolean**

'True' if issue is in the sprint, 'false' otherwise.

## Example

```javascript
boolean result = issueInSprint("AGILE-3", 5);
```

1. If there is no issue with that issue key, an exception will be raised.
2. The user must have sufficient permissions to view the board.

## See also