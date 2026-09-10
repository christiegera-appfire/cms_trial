# removeWorklogIncreaseEstimateBy

## Description

Removes the worklog and the Remaining time will be increased by the value of increaseBy.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeWorklogIncreaseEstimateBy(issue, worklog, increaseBy) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The issue key. |
| worklog | Number | Yes | Id of the selected worklog. |
| increaseBy | Interval | Yes | Interval to increase Remaining by. |

## Return Type

**None**

## Example

```javascript
removeWorklogIncreaseEstimateBy(key, 10000, "4h");
```

Removes the worklog with id = 10000 from the current issue, increasing the remaining time by 4 hours.

## See also