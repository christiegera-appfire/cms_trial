# updateWorklogAdjustEstimate

## Description

Updates the worklog and the Remaining time will be adjusted with the value of interval, but never below 0.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | updateWorklogAdjustEstimate(issue, worklog, interval, startDate, comment) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The issue key. |
| worklog | Number | Yes | Id of the selected worklog. |
| interval | Interval | Yes | Interval of time worked. |
| startDate | Date | Yes | Start working date. |
| comment | String | Yes | Comment that will be posted on the worklog. |

## Return Type

**None**

## Example

```javascript
updateWorklogAdjustEstimate(key, 10000, "2h", currentDate(), "test worklog");
```

Updates the worklog with id = 10000 from the current issue, setting the worked interval to 2 hours and recalculating the remaining time automatically.

## See also