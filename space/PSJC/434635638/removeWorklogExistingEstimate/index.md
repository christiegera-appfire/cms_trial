# removeWorklogExistingEstimate

## Description

Removes the worklog and keeps Remaining time the same.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeWorklogExistingEstimate(issue, worklog) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The issue key. |
| worklog | Number | Yes | Id of the selected worklog. |

## Return Type

**None**

## Example

```javascript
removeWorklogExistingEstimate(key, 10000);
```

Removes the worklog with id = 10000 from the current issue, keeping the old remaining time.

## See also