# updateWorklogSetEstimateTo

## Description

Updates the worklog and keeps the same Remaining time.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | updateWorklogSetEstimateTo(issue, worklog, interval, startDate, comment, setTo) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The issue key. |
| worklog | Number | Yes | Id of the selected worklog. |
| interval | Interval | Yes | Interval of time worked. |
| startDate | Date | Yes | Start working date. |
| comment | String | Yes | Comment that will be posted on the worklog. |
| setTo | Interval | Yes | Interval to set the Remaining time with. |

## Return Type

**None**

## Example

```javascript
updateWorklogSetEstimateTo(key, 10000, "2h", currentDate(), "test worklog", "8h");
```

Updates the worklog with id = 10000 from the current issue, setting the worked interval to 2 hours and setting the remaining time to 8 hours.

## See also