# removeWorklogAdjustEstimate

## Description

Removes the worklog and the Remaining will be increased by the time from the worklog.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeWorklogAdjustEstimate(issue, worklog) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | Key of the selected issue. |
| worklog | Number | Yes | Id of the selected worklog. |

## Return Type

**None**

## Example

```javascript
removeWorklogAdjustEstimate(key, 10000);
```

Removes the worklog with id = 10000 from the current issue, recalculating the remaining time automatically.

## See also