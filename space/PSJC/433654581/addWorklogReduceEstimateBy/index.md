# addWorklogReduceEstimateBy

## Description

Adds worklog and the remaining time will be reduced by the value of reduceBY, but never below 0.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addWorklogReduceEstimateBy(issue, user, interval, startDate, comment, reduceBY) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | Key of the selected issue. |
| user | String | Yes | User name of the selected user. |
| interval | Interval | Yes | Interval of time worked. |
| startDate | Date | Yes | Start working date. |
| comment | String | Yes | Comment that will be posted on the worklog. |
| reduceBY | Interval | Yes | Interval to reduce Remaining by. |

## Return Type

**None**

## Example

```javascript
addWorklogReduceEstimateBy(key, currentUser(), "2h", currentDate(), "test worklog", "4h");
```

Adds an worklog of 2 hours for the current user on the current issue, reducing the remaining time by 4 hours.

## See also