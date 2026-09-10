# addWorklogExistingEstimate

## Description

Adds worklog and keeps remaining time the same.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addWorklogExistingEstimate(issue, user, interval, startDate, comment) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | Key of the selected issue. |
| user | String | Yes | User name of the selected user. |
| interval | Interval | Yes | Interval of time worked. |
| startDate | Date | Yes | Start working date. |
| comment | String | Yes | Comment that will be posted on the worklog. |

## Return Type

**None**

## Example

```javascript
addWorklogExistingEstimate(key, currentUser(), "2h", currentDate(), "test worklog");
```

Adds an worklog of 2 hours for the current user on the current issue, keeping the old remaining time.

## See also