# addWorklogSetEstimateTo

## Description

Adds worklog and sets remaining time to the value of setTo.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addWorklogSetEstimateTo(issue, user, interval, startDate, comment, setTo) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | Key of the selected issue. |
| user | String | Yes | User name of the selected user. |
| interval | Interval | Yes | Interval of time worked. |
| startDate | Date | Yes | Start working date. |
| comment | String | Yes | Comment that will be posted on the worklog. |
| setTo | Interval | Yes | Interval to set the remaining time with. |

## Return Type

**None**

## Example

```javascript
addWorklogSetEstimateTo(key, currentUser(), "2h", currentDate(), "test worklog", "8h");
```

Adds an worklog of 2 hours for the current user on the current issue, setting the remaining time to 8 hours.

## See also