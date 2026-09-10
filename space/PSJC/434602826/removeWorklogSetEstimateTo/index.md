# removeWorklogSetEstimateTo

## Description

Removes the worklog and sets Remaining time to the value of setTo.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeWorklogSetEstimateTo(issue, worklog, setTo) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The issue key. |
| worklog | Number | Yes | Id of the selected worklog. |
| setTo | Interval | Yes | Interval to set the Remaining time with. |

## Return Type

**None**

## Example

```javascript
removeWorklogSetEstimateTo(key, 10000, "8h");
```

Removes the worklog with id = 10000 from the current issue, setting the remaining time to 8 hours.

## See also