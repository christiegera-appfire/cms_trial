# getWorklogStartDate

## Description

Returns the start date of a worklog.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogStartDate(issue, worklog) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The issue key. |
| worklog | Number | Yes | Id of the selected worklog. |

## Return Type

**Date**

## Example

```javascript
print(getWorklogStartDate(key, 11201))
```

Prints the start date of the worklog with id = 11201, on the current issue.

## See also